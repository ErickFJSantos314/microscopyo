# 🔬 Microscó(py)o

Um visualizador interativo de lâminas histológicas digitais no formato SVS, desenvolvido em Python. (O nome é um trocadilho com a extensão de arquivo .py hehe)

## Descrição

Este projeto permite visualizar e navegar por lâminas histológicas digitais (arquivos SVS) de forma interativa, simulando a experiência de uso de um microscópio real. Ideal para estudos de patologia, histologia e análise de imagens médicas. 

> Este projeto é uma das etapas essenciais para um outro projeto de IA que estou fazendo, envolvendo lâminas histológicas. Como não tenho um microscópio físico, criei o MicroscoPYo para me ajudar com a navegação pelas lâminas

## Funcionalidades

- 🖼️ Visualização de lâminas SVS em alta resolução
- 🎮 Navegação intuitiva pela lâmina usando teclas WASD
- 🔍 Zoom in/out com múltiplos níveis de ampliação
- 📍 Indicador de posição e nível de zoom em tempo real
- 🖥️ Interface simples e responsiva com OpenCV

## 🎮 Controles

| Tecla | Ação |
|-------|------|
| `W` | Mover para cima |
| `S` | Mover para baixo |
| `A` | Mover para esquerda |
| `D` | Mover para direita |
| `E` | Zoom In (aumentar ampliação) |
| `Q` | Zoom Out (diminuir ampliação) |
| `X` | Sair do programa |

## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd "Microscopio virtual"
```

2. Crie um ambiente virtual:
```bash
python -m venv .venv
```

3. Ative o ambiente virtual:
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source .venv/bin/activate
     ```

4. Instale as dependências:
```bash
pip install openslide-python opencv-python numpy pillow openslide-bin
```

## 📂 Configuração

Antes de executar o programa, você precisa configurar o caminho da sua lâmina SVS:

1. Abra o arquivo `microscope.py`
2. Na linha 19, substitua `>seu caminho SVS aqui<` pelo caminho do seu arquivo SVS:
```python
caminho = (r'archives\sua-lamina.svs')
```

## ▶️ Como Usar

1. Certifique-se de que o ambiente virtual está ativado
2. Execute o programa:
```bash
python microscopyo.py
```
3. Use os controles para navegar pela lâmina
4. Pressione `X` para sair

## 🛠️ Tecnologias Utilizadas

- **OpenSlide**: Biblioteca para leitura de imagens histológicas
- **OpenCV**: Processamento e exibição de imagens
- **NumPy**: Manipulação de arrays e matrizes
- **Pillow (PIL)**: Processamento de imagens

## 📁 Estrutura do Projeto

```
Microscopio virtual/
├── microscope.py      # Código principal do microscópio virtual
├── archives/          # Diretório para armazenar lâminas SVS
├── .venv/            # Ambiente virtual (ignorado pelo git)
├── .gitignore        # Arquivos ignorados pelo git
└── README.md         # Este arquivo
```

## 📝 Notas

- O programa inicia a visualização no centro da lâmina
- A velocidade de movimentação se adapta automaticamente ao nível de zoom
- Resolução padrão da janela: 1024x768 pixels

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests


## 👨‍💻 Autor

Desenvolvido por Erick Francisco de Jesus Santos

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
