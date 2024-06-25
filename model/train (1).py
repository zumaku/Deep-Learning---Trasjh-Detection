# -*- coding: utf-8 -*-
"""train.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lidc58vVIauj0LSqrctuPBGoJiY9uaXW

# Langkah 1: Persiapan Pelatihan
"""

# Install YOLO
!pip install ultralytics

from google.colab import drive
drive.mount('/content/drive')

dataset_path = '/content/drive/MyDrive/deep_learning/dataset'

!cp -r $dataset_path /content

"""# Langkah 2: Melatih Model"""

# Lakukan training YOLOv5
from ultralytics import YOLO

# Muat model YOLOv5
model = YOLO('yolov5s.pt')  # Menggunakan pre-trained weights YOLOv5 small

# Melatih model dengan dataset yang ada di /content/dataset
results = model.train(data='/content/dataset/data.yaml', epochs=10, batch=16, name='yolov5_results', imgsz=640)

"""# Langkah 3: Mengevaluasi Model"""

import matplotlib.pyplot as plt
import cv2
import os

# Path ke direktori hasil pelatihan
results_dir = '/content/runs/detect/yolov5_results2/'

# Menampilkan grafik hasil pelatihan
results_img = os.path.join(results_dir, 'results.png')
img = cv2.imread(results_img)
plt.figure(figsize=(10, 10))
plt.imshow(img)
plt.axis('off')
plt.show()

"""# Langkah 4: Mengetes Model"""

# Path ke model yang sudah dilatih
model_path = '/content/runs/detect/yolov5_results2/weights/best.pt'  # Update this based on your directory

# Muat model yang sudah dilatih
model = YOLO(model_path)

# Path ke folder yang berisi gambar
image_folder = '/content/drive/MyDrive/deep_learning/'

# Daftar nama file gambar
image_files = ['tes_image.jpg', 'tes_image2.jpg', 'tes_image3.jpg']  # Sesuaikan dengan nama gambar Anda

# Lakukan prediksi untuk setiap gambar dalam folder
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)

    # Lakukan prediksi
    results = model(image_path)

    # Menampilkan hasil prediksi
    for result in results:
        # Convert image to RGB (default is BGR)
        img = result.plot()
        plt.figure(figsize=(10, 10))
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title(image_file)
        plt.axis('off')
        plt.show()