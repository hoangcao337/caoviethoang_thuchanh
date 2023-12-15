import PySimpleGUI as sg
import cv2
import numpy as np

# Tạo giao diện GUI
layout = [
    [sg.Image(filename='', key='image')],
    [sg.Text('Kernel Size:'), sg.Slider((1, 10), 1, 1, orientation='h', size=(15, 15), key='slider')],
    [sg.Radio('Average', "RADIO1", default=True, key='average'), sg.Radio('Gaussian', "RADIO1", key='gaussian')],
    [sg.Button('Open'), sg.Button('Smooth'), sg.Button('Exit')]
]

window = sg.Window('Image Smoothing App', layout)

image = None

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Open':
        filename = sg.popup_get_file('Open an image', no_window=True)
        if filename:
            image = cv2.imread(filename)
            imgbytes = cv2.imencode('.png', image)[1].tobytes()
            window['image'].update(data=imgbytes)
    elif event == 'Smooth' and image is not None:
        kernel_size = int(values['slider']) * 2 + 1  # Đảm bảo kernel_size là số lẻ
        if values['average']:
            kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)
            image = cv2.filter2D(image, -1, kernel)
        elif values['gaussian']:
            image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
        imgbytes = cv2.imencode('.png', image)[1].tobytes()
        window['image'].update(data=imgbytes)

window.close()
