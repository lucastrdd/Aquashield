from ultralytics import YOLO
import cv2
from collections import defaultdict
import numpy as np

# Carregar o modelo YOLO treinado
model = YOLO("runs/detect/train/weights/best.pt")

# INSIRA AQUI O PATH DA IMAGEM QUE QUER RATREAR
image_path = "data/dataset/test/test1.png"
img = cv2.imread(image_path)

if img is None:
    print("Erro ao carregar a imagem. Verifique o caminho.")
else:
    # Inicializa as variáveis de rastreamento
    track_history = defaultdict(lambda: [])

    # Realiza a detecção
    results = model(img)  # Não rastrea aqui, apenas detecta

    # Acessa o primeiro (e único) resultado
    result = results[0]

    # Desenhar os resultados na imagem
    for box in result.boxes.xyxy.cpu().numpy():
        x1, y1, x2, y2 = map(int, box[:4])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = "Mancha" 
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Debug com print
    if result.boxes is not None and len(result.boxes) > 0:
        print("Detecções encontradas:")
        for box in result.boxes.xyxy.cpu().numpy():
            print(box)
    else:
        print("Nenhuma detecção encontrada.")

    # Exibe a imagem processada
    cv2.imshow("Resultado", img)
    cv2.imwrite("C:/temp/resultado.jpg", img)  # Salva no diretório especificado
    cv2.waitKey(0)
    cv2.destroyAllWindows()
