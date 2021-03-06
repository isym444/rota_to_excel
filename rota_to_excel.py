
import easyocr
from datetime import datetime, timedelta


import cv2
from matplotlib import pyplot as plt
import numpy as np
import csv

IMAGE_PATH = "abridged.png"
reader = easyocr.Reader(["en"], gpu=True)
result = reader.readtext(IMAGE_PATH)

# open the file in the write mode
with open('/Users/isym444/Desktop/rota_to_excel/test2.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    for a in result:
        print(a[1])
        writer.writerow([a[1]])
