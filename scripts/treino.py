from ultralytics import YOLO

# para marcar as imagens
# https://www.makesense.ai/

def main():
    # Carrega o modelo
    model = YOLO("yolov10n.pt") 

    # Usa o modelo
    model.train(data="config.yaml", epochs=300, device=0)  # Se vc não estiver usando GPU, apague a flag device
    metrics = model.val()


if __name__ == '__main__':
    # freeze_support()
    main()