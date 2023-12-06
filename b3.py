import numpy as np
from matplotlib import pyplot as plt
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox, OptionMenu
from mpl_toolkits.mplot3d import Axes3D

class GeometryApp:
    def __init__(self, master):
        self.master = master
        master.title("Ứng dụng hỗ trợ học tập môn Hình học")

        self.label = Label(master, text="Chào mừng đến với ứng dụng hỗ trợ học tập môn Hình học!")
        self.label.pack()

        self.shapes = ["Hình vuông", "Hình chữ nhật", "Hình tròn"]
        self.shape_var = StringVar(master)
        self.shape_var.set(self.shapes[0])  # default value
        self.shape_menu = OptionMenu(master, self.shape_var, *self.shapes)
        self.shape_menu.pack()

        self.draw_button = Button(master, text="Vẽ và tính toán", command=self.draw_and_calculate)
        self.draw_button.pack()

    def draw_and_calculate(self):
        shape = self.shape_var.get()
        if shape == "Hình vuông":
            self.square_side = StringVar()
            self.square_entry = Entry(self.master, textvariable=self.square_side)
            self.square_entry.pack()
            self.square_button = Button(self.master, text="Vẽ và tính hình vuông", command=self.draw_and_calculate_square)
            self.square_button.pack()
        elif shape == "Hình chữ nhật":
            self.rectangle_length = StringVar()
            self.rectangle_width = StringVar()
            self.rectangle_length_entry = Entry(self.master, textvariable=self.rectangle_length)
            self.rectangle_length_entry.pack()
            self.rectangle_width_entry = Entry(self.master, textvariable=self.rectangle_width)
            self.rectangle_width_entry.pack()
            self.rectangle_button = Button(self.master, text="Vẽ và tính hình chữ nhật", command=self.draw_and_calculate_rectangle)
            self.rectangle_button.pack()
        elif shape == "Hình tròn":
            self.circle_radius = StringVar()
            self.circle_entry = Entry(self.master, textvariable=self.circle_radius)
            self.circle_entry.pack()
            self.circle_button = Button(self.master, text="Vẽ và tính hình tròn", command=self.draw_and_calculate_circle)
            self.circle_button.pack()

    def draw_and_calculate_square(self):
        side = self.square_side.get()
        if not side.isdigit():
            messagebox.showinfo("Thông báo", "Mời nhập lại")
            return
        side = int(side)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = y = np.linspace(0, side, 2)
        X, Y = np.meshgrid(x, y)
        Z = np.zeros_like(X)
        ax.plot_surface(X, Y, Z)
        plt.show()
        area = side ** 2
        perimeter = 4 * side
        messagebox.showinfo("Kết quả", f"Diện tích hình vuông: {area}\nChu vi hình vuông: {perimeter}")

    def draw_and_calculate_rectangle(self):
        length = self.rectangle_length.get()
        width = self.rectangle_width.get()
        if not length.isdigit() or not width.isdigit():
            messagebox.showinfo("Thông báo", "Mời nhập lại")
            return
        length = int(length)
        width = int(width)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = np.linspace(0, length, 2)
        y = np.linspace(0, width, 2)
        X, Y = np.meshgrid(x, y)
        Z = np.zeros_like(X)
        ax.plot_surface(X, Y, Z)
        plt.show()
        area = length * width
        perimeter = 2 * (length + width)
        messagebox.showinfo("Kết quả", f"Diện tích hình chữ nhật: {area}\nChu vi hình chữ nhật: {perimeter}")

    def draw_and_calculate_circle(self):
        import math
        radius = self.circle_radius.get()
        if not radius.isdigit():
            messagebox.showinfo("Thông báo", "Mời nhập lại")
            return
        radius = int(radius)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        phi = np.linspace(0, 2 * np.pi, 100)
        rho = np.linspace(0, radius, 100)
        phi, rho = np.meshgrid(phi, rho)
        X = rho * np.cos(phi)
        Y = rho * np.sin(phi)
        Z = np.zeros_like(X)
        ax.plot_surface(X, Y, Z)
        plt.show()
        area = math.pi * (radius ** 2)
        circumference = 2 * math.pi * radius
        messagebox.showinfo("Kết quả", f"Diện tích hình tròn: {area}\nChu vi hình tròn: {circumference}")

root = Tk()
my_gui = GeometryApp(root)
root.mainloop()
