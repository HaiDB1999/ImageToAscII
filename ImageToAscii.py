import cv2
import numpy as np
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from ImageToAscii import *
import time

replace = '................,,,,,,,,,,,,,,:::::::;;;;;;;;:::::::;;;;;;;;rrrrrrrrrrrrrrssssssssiiiiiiiiSSS555522222222XXXXXX33339999hhhhGGGG&&&&AAAAAAAAHHHHHHBBBBMMMMMM##################@@@@@@@@@@@@@@'
# replace = replace[::-1]
# print(replace)
np_replace = np.array(list(replace))

def join_ascii(image):
    num_line = image.shape[0]
    rs = ''
    for i in range(num_line):
        rs += ''.join(list(np_replace[image[i]])) + '\n'
    return rs

def ImageToAscii(path, width):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # resize
    print(path)
    # print(image)
    ratio = image.shape[0] / image.shape[1]
    new_width = width
    new_height = int(ratio*new_width/1.45)
    image = cv2.resize(image, (new_width, new_height))
    # print(image.shape)
    # # cv2.imshow('', image)
    # cv2.waitKey(5000)
    # cv2.destroyAllWindows()
    image = image/256*len(replace)
    image = image.astype(np.uint32)
    return join_ascii(image)

def GUI(texts):
    window = tk.Tk()
    window.title("My Love")
    window.geometry("900x1200")
    body = Frame(window, )
    body.pack()
    text= Text(body,  bg="#424242", fg="#FFFFFF",  height=900, font=("Times news roman", 1), width=600)
    list_text = texts.split('\n')
    for line in list_text:
        for word in line:
            text.insert(INSERT, word)
            text.pack()
            time.sleep(0.0001)
            window.update()
        text.insert(INSERT, '\n')
    window.mainloop()

if __name__ == "__main__":
    path = "/home/hai/Documents/Project/ImageToAscII/Images/MyLove.jpg"
    width = 220
    GUI(ImageToAscii(path, width))