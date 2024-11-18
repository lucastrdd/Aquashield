# Detecção de Mancha de Óleo na Água com YOLO  

Projeto criado junto ao projeto de extensão Logical Space da Universidade Estadual da Paraíba (UEPB), que utiliza o modelo **YOLO (You Only Look Once)** para detectar manchas de óleo na água. O objetivo é criar uma solução eficiente e rápida para identificar áreas afetadas por vazamentos de óleo, ajudando na preservação ambiental e na resposta a desastres.  

## 📋 Visão Geral  

A detecção de manchas de óleo é feita com base em imagens fornecidas por drones, satélites ou fotografias aéreas. O YOLO foi escolhido devido à sua simplicidade de implementação, alta precisão e desempenho em tarefas de detecção de objetos.

## 🛠️ Funcionalidades  

- Detecção de manchas de óleo em tempo real.  
- Suporte para imagens e vídeos.   
- Otimização para hardware limitado (GPU/CPU).  

## 📂 Estrutura do Projeto  

```plaintext
detecao-manchas-oleo/
├── data/
│   ├── test/            # Imagens de teste
│   ├── train/           # Imagens de treinamento
│   ├── validation/      # Imagens de validação
├── runs/
│   ├── detect/          # Resultados das detecções
│   ├── train/           # Resultados do treinamento
│       ├── weights/     # Pesos do modelo treinado
│           ├── best.pt  # Melhor modelo treinado
|           ├── last.pt # Ultimo modelo treinado (não necessariamente o melhor)
├── scripts/
│   ├── deteccaoImagem.py # Script de detecção em imagens
│   ├── deteccaoWebcam.py # Script de detecção em tempo real via webcam
│   ├── treino.py         # Script de treinamento
├── utils/
│   ├── imgDownloader.py  # Script para download de imagens
├── [yolov10n.pt](http://_vscodecontentref_/0)           # Modelo YOLO não treinado
├── [config.yaml](http://_vscodecontentref_/1)           # Configuração do modelo e treinamento
├── [README.md](http://_vscodecontentref_/2)             # Documentação do projeto
```

## 🚀 Como Usar  

### Pré-requisitos  

- Python 3.8+
- Instalar as dependências do projeto:
  ```sh
  pip install -r requirements.txt
  ```

### Treinamento do Modelo  

Para treinar o modelo, execute o script [`scripts/treino.py`](scripts/treino.py ):
```sh
python 

treino.py


```

### Detecção em Imagens  

Para detectar manchas de óleo em uma imagem, execute o script [`scripts/deteccaoImagem.py`](scripts/deteccaoImagem.py ):
```sh
python 

deteccaoImagem.py


```

### Detecção em Tempo Real  

Para detectar manchas de óleo em tempo real usando a webcam, execute o script [`scripts/deteccaoWebcam.py`](scripts/deteccaoWebcam.py ):
```sh
python 

deteccaoWebcam.py


```

## 📄 Licença  

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENSE para mais detalhes.
