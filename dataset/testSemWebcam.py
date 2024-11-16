from ultralytics import YOLO
import cv2
from collections import defaultdict
import numpy as np

# Carregar o modelo YOLO
model = YOLO("runs/detect/train/weights/best.pt")

# Caminho da imagem
image_path = "C:/temp/ws-pycharm/Extensao/pythonProject/dataset/train/Oil Spill in Water_31.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Erro ao carregar a imagem. Verifique o caminho.")
else:
    # Inicializa as variáveis de rastreamento
    track_history = defaultdict(lambda: [])
    deixar_rastro = True

    # Realiza a detecção
    results = model(img)  # Não rastreamos aqui, apenas detecção

    # Acessa o primeiro (e único) resultado
    result = results[0]

    # Visualizar os resultados na imagem
    for box in result.boxes.xyxy.cpu().numpy():
        x1, y1, x2, y2 = map(int, box[:4])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = "com mancha"  # Substitua pelo label do objeto, se disponível
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    if result.boxes is not None and len(result.boxes) > 0:
        print("Detecções encontradas:")
        for box in result.boxes.xyxy.cpu().numpy():
            print(box)
    else:
        print("Nenhuma detecção encontrada.")


    if deixar_rastro:
        try:
            # Obter as caixas delimitadoras e IDs de rastreamento
            boxes = result.boxes.xywh.cpu()
            track_ids = result.boxes.id
            if track_ids is not None:
                track_ids = track_ids.int().cpu().tolist()
            else:
                track_ids = [None] * len(boxes)

            # Plotar os rastros
            for box, track_id in zip(boxes, track_ids):
                x, y, w, h = box
                track = track_history[track_id]
                track.append((float(x), float(y)))  # Adiciona o ponto central (x, y)
                if len(track) > 30:  # Limita o rastro a 30 pontos
                    track.pop(0)

                # Desenha as linhas do rastreamento
                if len(track) > 1:  # Apenas desenha se houver mais de um ponto
                    points = np.array(track).astype(np.int32).reshape((-1, 1, 2))
                    cv2.polylines(img, [points], isClosed=False, color=(230, 0, 0), thickness=5)
        except Exception as e:
            print(f"Erro ao desenhar rastros: {e}")
            import traceback
            traceback.print_exc()

    # Exibir detalhes do resultado
    print(result)  # Mostra um resumo do resultado
    print(result.boxes.xyxy.cpu().numpy())  # Coordenadas das caixas

    # Exibe a imagem processada
    cv2.imshow("Resultado", img)
    cv2.imwrite("C:/temp/resultado.jpg", img)  # Salva no diretório especificado
    cv2.waitKey(0)
    cv2.destroyAllWindows()
