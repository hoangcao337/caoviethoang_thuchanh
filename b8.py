import cv2
import numpy as np
from tkinter import filedialog
from tkinter import *
from PIL import Image
from PIL import ImageTk

def select_image(panelA=None, panelB=None):
    # Mở cửa sổ chọn tệp để người dùng chọn ảnh
    path = filedialog.askopenfilename()

    if len(path) > 0:
        # Đọc ảnh và chuyển đổi sang ảnh xám
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Tách biên ảnh
        edges = cv2.Canny(gray, 50, 150)

        # Chuyển đổi ảnh sang định dạng PIL và sau đó sang định dạng ImageTk
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        edges = Image.fromarray(edges)
        edges = ImageTk.PhotoImage(edges)

        # Nếu các khung ảnh đang tồn tại, hãy xóa chúng
        if panelA is not None or panelB is not None:
            panelA.destroy()
            panelB.destroy()

        # Tạo hai khung ảnh trên cửa sổ GUI và hiển thị ảnh và ảnh tách biên
        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side="left", padx=10, pady=10)

        panelB = Label(image=edges)
        panelB.image = edges
        panelB.pack(side="right", padx=10, pady=10)

# Khởi tạo cửa sổ Tkinter và nút chọn ảnh
root = Tk()
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

# Khởi tạo hai khung ảnh
panelA = None
panelB = None

# Bắt đầu vòng lặp chính của cửa sổ Tkinter
root.mainloop()
