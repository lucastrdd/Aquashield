from ultralytics import YOLO

# para marcar as imagens
# https://www.makesense.ai/

def main():
    # Load a model
    model = YOLO("yolov10n.pt") 

    # Use the model
    model.train(data="dataset/oil.yaml", epochs=30, device=0)  # Se vc não estiver usando GPU, apague a flag device
    metrics = model.val()


if __name__ == '__main__':
    # freeze_support()
    main()