from ultralytics import YOLO
from tkinter import filedialog, Toplevel, Label
from PIL import Image, ImageTk
import cv2

# model = YOLO("yolov8n.pt")
#
# model.train(
#     data="/Users/trevorholm/PycharmProjects/senior-design-gui-prototype/CrosswalkDataset/data.yaml",  # Path to your YAML file
#     epochs=5,                     # Number of training epochs
#     imgsz=640,                     # Image size (pixels)
#     batch=16,                      # Batch size
#     workers=8                      # Number of workers for data loading
# )

model = YOLO("/Users/trevorholm/PycharmProjects/senior-design-gui-prototype/runs/detect/train4/weights/best.pt")

def detect_crosswalk(image_path):
    results = model(image_path)
    result_image = results[0].plot()
    return result_image

def load_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if not file_path:
        return

    detected_image = detect_crosswalk(file_path)

    image = cv2.cvtColor(detected_image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image_tk = ImageTk.PhotoImage(image)

    result_window = Toplevel()
    result_window.title("Crosswalk Detection Result")
    result_label = Label(result_window, image=image_tk)
    result_label.image = image_tk
    result_label.pack()