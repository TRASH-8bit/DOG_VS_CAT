import tkinter as tk
from tkinter.constants import Y
import tkinter.font as tkfont
import typing_extensions
import cv2
import easygui
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from numpy.core.fromnumeric import size
from scipy.ndimage.measurements import label

model = load_model('Dog_vs_cat_model.h5')

root = tk.Tk()

def upload():
    img = easygui.fileopenbox()
    orignal_img = cv2.imread(img)
    cv2.imshow("image", orignal_img)
    img = image.load_img(img,target_size=(150,150))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    result = model.predict(img)
    print(result[0])
    label_font = tkfont.Font(family="Lucida Grande",size=20)
    if result[0][0] == 0:
        label = tk.Label(root,text="IT'S A CAT", fg='black', font=label_font)
        label.place(x=200,y=100)
    else:
        label = tk.Label(root,text="IT'S A DOG", font=label_font)
        label.place(x=200,y=100)

cavas = tk.Canvas(width=400,height=400)
cavas.pack()

text = tk.Label(root, text="Upload a img of cat or dog and this software will identify the img as a cat or dog", bg='red', fg='black').pack()

upload_btn = tk.Button(root, text="Upload a image", bg='black', fg='white', command=upload)
upload_btn.place(x=200,y=300)

root.mainloop()