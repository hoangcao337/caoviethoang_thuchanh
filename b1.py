import numpy as np
import tkinter as tk
from tkinter import ttk


def giai_he_pt_tuyen_tinh(A, B):
    try:
        X = np.linalg.solve(A, B)
        return X
    except np.linalg.LinAlgError:
        return "Hệ phương trình không có nghiệm hoặc có vô số nghiệm."


def giai_button_click(A_entries, B_entries, m, n, result_label):
    try:
        A = np.array([[float(A_entries[i][j].get()) for j in range(n)] for i in range(m)])
        B = np.array([float(B_entries[i].get()) for i in range(m)])

        ket_qua = giai_he_pt_tuyen_tinh(A, B)

        if isinstance(ket_qua, str):
            result_label.config(text=ket_qua)
        else:
            result_label.config(text="Nghiệm của hệ phương trình là: " + ', '.join(map(str, ket_qua)))
    except ValueError:
        result_label.config(text="Nhập số hợp lệ cho ma trận và vector kết quả.")


def xoa_du_lieu(A_entries, B_entries, result_label):
    for i in range(len(A_entries)):
        for j in range(len(A_entries[0])):
            A_entries[i][j].delete(0, tk.END)
        B_entries[i].delete(0, tk.END)

    result_label.config(text="")


def quay_lai(root):
    root.destroy()
    init_window()


def hien_thi_thong_bao(message):
    thong_bao = tk.Toplevel()
    thong_bao.title("Thông Báo")
    label = tk.Label(thong_bao, text=message)
    label.pack(padx=10, pady=10)
    button = ttk.Button(thong_bao, text="Đóng", command=thong_bao.destroy)
    button.pack(pady=10)


def tao_ma_tran(root, m, n):
    m_value = m.get()
    n_value = n.get()

    if not m_value or not n_value:
        hien_thi_thong_bao("Nhập số phương trình và số ẩn.")
        return

    try:
        m = int(m_value)
        n = int(n_value)

        # Kiểm tra xem số phương trình và số ẩn có được nhập không
        if m <= 0 or n <= 0:
            raise ValueError("Nhập số hợp lệ cho số phương trình và số ẩn.")

        # Tạo các ô nhập liệu cho ma trận A
        A_entries = [[None] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                entry = ttk.Entry(root, width=8)
                entry.grid(row=i + 3, column=j, padx=5, pady=5)
                A_entries[i][j] = entry

        # Tạo các ô nhập liệu cho vector kết quả B
        B_entries = [None] * m
        for i in range(m):
            entry = ttk.Entry(root, width=8)
            entry.grid(row=i + 3, column=n, padx=5, pady=5)
            B_entries[i] = entry

        # Tạo nút giải và gán hàm khi nhấp vào
        solve_button = ttk.Button(root, text="Giải Hệ Phương Trình",
                                  command=lambda: giai_button_click(A_entries, B_entries, m, n, result_label))
        solve_button.grid(row=m + 3, column=0, columnspan=n + 1, pady=10)

        # Tạo nhãn kết quả
        result_label = tk.Label(root, text="")
        result_label.grid(row=m + 4, column=0, columnspan=n + 1, pady=10)

        # Tạo nút xoá dữ liệu
        clear_button = ttk.Button(root, text="Xoá Dữ Liệu",
                                  command=lambda: xoa_du_lieu(A_entries, B_entries, result_label))
        clear_button.grid(row=m + 5, column=0, columnspan=n + 1, pady=10)

        # Tạo nút quay lại
        back_button = ttk.Button(root, text="Quay Lại", command=lambda: quay_lai(root))
        back_button.grid(row=m + 6, column=0, columnspan=n + 1, pady=10)

        # Tạo nút thoát
        exit_button = ttk.Button(root, text="Thoát", command=root.destroy)
        exit_button.grid(row=m + 7, column=0, columnspan=n + 1, pady=10)

    except ValueError as e:
        hien_thi_thong_bao(str(e))


def init_window():
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
    create_button = ttk.Button(root, text="Tạo Ma Trận", command=lambda: tao_ma_tran(root, m_entry, n_entry))
    create_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Chạy ứng dụng
    root.mainloop()


# Khởi tạo cửa sổ
init_window()
