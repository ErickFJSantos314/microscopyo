# IMPORTAÇÕES

import os
import sys
if hasattr(os, 'add_dll_directory'):
    import openslide_bin
    dll_path = os.path.dirname(openslide_bin.__file__)
    os.add_dll_directory(dll_path)
import openslide
from openslide import OpenSlide
from openslide.deepzoom import DeepZoomGenerator
from PIL import Image
import cv2
import numpy as np

# CAPTURA DE LAMINA

caminho = (r'archives\>seu caminho SVS aqui<') # preencha aqui com o caminho do seu arquivo svs
slide = OpenSlide(caminho)

# VARIAVEIS DE ESTADO

largura_total, altura_total = slide.dimensions
posicao_X = largura_total // 2
posicao_Y = altura_total // 2
nivel_atual = 1
tamanho_tela = (1024, 768)

# LOOP DE FUNCIONAMENTO

while True:
    imagem_PIL = slide.read_region((posicao_X, posicao_Y), nivel_atual, tamanho_tela)
    matriz_bruta = np.array(imagem_PIL)
    imagem_openCV = cv2.cvtColor(matriz_bruta, cv2.COLOR_RGBA2BGR)
    Texto = f"X: {posicao_X} Y: {posicao_Y} Zoom: {nivel_atual}"
    cv2.putText(imagem_openCV, Texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow("microscopyo", imagem_openCV)

    tecla = cv2.waitKey(1) & 0xFF
    
    # MOVIMENTAÇÃO PELA LÂMIINA

    passo = 500 * (2 ** nivel_atual)

    if tecla == ord('d'): posicao_X += passo
    if tecla == ord('a'): posicao_X -= passo
    if tecla == ord('s'): posicao_Y += passo
    if tecla == ord('w'): posicao_Y -= passo

    # ZOOM IN E ZOOM OUT

    if tecla == ord('e'):
        if nivel_atual > 0:
            nivel_atual -= 1
            print(f"Zoom In: Nível {nivel_atual}")
            
    if tecla == ord('q'):
        if nivel_atual < (slide.level_count - 1):
            nivel_atual += 1
            print(f"Zoom Out: Nível {nivel_atual}")

    # LIMITES

    posicao_X = max(0, min(posicao_X, largura_total - tamanho_tela[0]))
    posicao_Y = max(0, min(posicao_Y, altura_total - tamanho_tela[1]))

    # FECHAMENTO

    if tecla == ord('x'):
        break

cv2.destroyAllWindows()