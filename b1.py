import numpy as np
import tkinter as tk
from tkinter import ttk


def giai_he_pt_tuyen_tinh(A, B):
    try:
        X = np.linalg.solve(A, B)
        return X
    except np.linalg.LinAlgError:
        return "Hệ phương trình không có nghiệm hoặc có vô số nghiệm."


def giai_button_click():
    try:
        A = np.array([[float(a_entries[i][j].get()) for j in range(n)] for i in range(m)])
        B = np.array([float(b_entries[i].get()) for i in range(m)])

        ket_qua = giai_he_pt_tuyen_tinh(A, B)

        if isinstance(ket_qua, str):
            result_label.config(text=ket_qua)
        else:
            result_label.config(text="Nghiệm của hệ phương trình là: " + ', '.join(map(str, ket_qua)))
    except ValueError:
        result_label.config(text="Nhập số hợp lệ cho ma trận và vector kết quả.")


def xoa_du_lieu():
    m_entry.delete(0, tk.END)
    n_entry.delete(0, tk.END)

    for i in range(m):
        for j in range(n):
            a_entries[i][j].delete(0, tk.END)
        b_entries[i].delete(0, tk.END)

    result_label.config(text="")


def quay_lai():
    m_entry.delete(0, tk.END)
    n_entry.delete(0, tk.END)

    for i in range(m):
        for j in range(n):
            a_entries[i][j].delete(0, tk.END)
            a_entries[i][j].insert(0, initial_values['A'][i][j])
        b_entries[i].delete(0, tk.END)
        b_entries[i].insert(0, initial_values['B'][i])

    result_label.config(text="")


# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Giải Hệ Phương Trình Tuyến Tính")

# Nhập số phương trình và ẩn
m_label = tk.Label(root, text="Số phương trình:")
m_label.grid(row=0, column=0, padx=10, pady=5, sticky="E")
m_entry = ttk.Entry(root)
m_entry.grid(row=0, column=1, padx=10, pady=5, sticky="W")

# Nhập số ẩn
n_label = tk.Label(root, text="Số ẩn:")
n_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")
n_entry = ttk.Entry(root)
n_entry.grid(row=1, column=1, padx=10, pady=5, sticky="W")

# Tạo nút và gán hàm khi nhấp vào
create_button = ttk.Button(root, text="Tạo Ma Trận", command=lambda: tao_ma_tran())
create_button.grid(row=2, column=0, columnspan=2, pady=10)

initial_values = {'A': None, 'B': None}  # Lưu trữ trạng thái ban đầu


def tao_ma_tran():
    global m, n, a_entries, b_entries, initial_values

    try:
        m = int(m_entry.get())
        n = int(n_entry.get())

        # Lưu trạng thái ban đầu
        initial_values['A'] = [[None] * n for _ in range(m)]
        initial_values['B'] = [None] * m
        for i in range(m):
            for j in range(n):
                initial_values['A'][i][j] = float(0)  # Giá trị mặc định là 0
            initial_values['B'][i] = float(0)

        # Tạo các ô nhập liệu cho ma trận A
        a_entries = [[None] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                entry = ttk.Entry(root, width=8)
                entry.grid(row=i + 3, column=j, padx=5, pady=5)
                a_entries[i][j] = entry
                a_entries[i][j].insert(0, initial_values['A'][i][j])  # Hiển thị giá trị mặc định

        # Tạo các ô nhập liệu cho vector kết quả B
        b_entries = [None] * m
        for i in range(m):
            entry = ttk.Entry(root, width=8)
            entry.grid(row=i + 3, column=n, padx=5, pady=5)
            b_entries[i] = entry
            b_entries[i].insert(0, initial_values['B'][i])  # Hiển thị giá trị mặc định

        # Tạo nút giải và gán hàm khi nhấp vào
        solve_button = ttk.Button(root, text="Giải Hệ Phương Trình", command=lambda: giai_button_click())
        solve_button.grid(row=m + 3, column=0, columnspan=n + 1, pady=10)

        # Tạo nhãn kết quả
        global result_label
        result_label = tk.Label(root, text="")
        result_label.grid(row=m + 4, column=0, columnspan=n + 1, pady=10)

        # Tạo nút xoá dữ liệu
        clear_button = ttk.Button(root, text="Xoá Dữ Liệu", command=lambda: xoa_du_lieu())
        clear_button.grid(row=m + 5, column=0, columnspan=n + 1, pady=10)

        # Tạo nút quay lại
        back_button = ttk.Button(root, text="Quay Lại", command=lambda: quay_lai())
        back_button.grid(row=m + 6, column=0, columnspan=n + 1, pady=10)

        # Tạo nút thoát
        exit_button = ttk.Button(root, text="Thoát", command=root.destroy)
        exit_button.grid(row=m + 7, column=0, columnspan=n + 1, pady=10)

    except ValueError:
        result_label.config(text="Nhập số hợp lệ cho số phương trình và số ẩn.")


# Chạy ứng dụng
root.mainloop()
