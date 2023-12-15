import cv2
import numpy as np
from tkinter import filedialog, Label, Button, Tk
from PIL import Image, ImageTk

def enhance_image(image_path):
    # Đọc ảnh
    img = cv2.imread(image_path, 1)

    # Tăng cường ảnh
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    # Cân bằng histogram của kênh Y
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

    # Chuyển đổi lại ảnh YUV thành BGR
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    return img_output

def select_image():
    # Mở hộp thoại chọn file
    filename = filedialog.askopenfilename()

    # Tăng cường ảnh
    enhanced_img = enhance_image(filename)

    # Chuyển đổi ảnh từ OpenCV sang PhotoImage để hiển thị
    enhanced_img = cv2.cvtColor(enhanced_img, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(enhanced_img)
    imgtk = ImageTk.PhotoImage(image=im_pil)

    # Hiển thị ảnh
    panel.imgtk = imgtk
    panel.config(image=imgtk)

# Tạo cửa sổ Tkinter
root = Tk()
panel = Label(root)
panel.pack(side="bottom", fill="both", expand="yes")

# Tạo nút chọn ảnh
btn = Button(root, text="Chọn ảnh", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes")

# Bắt đầu vòng lặp chính của Tkinter
root.mainloop()
