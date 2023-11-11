import tkinter as tk
from tkinter import simpledialog
from sympy import Symbol, integrate, diff, solve, Eq

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Phần mềm hỗ trợ học tập Giải tích")

        # Tạo các widget
        self.label = tk.Label(master, text="Chọn loại phép toán:")
        self.label.pack()

        # Dropdown menu cho loại phép toán
        self.operations = ["Tích phân", "Đạo hàm", "Giải phương trình", "Tích phân xác định", "Giải hệ phương trình tuyến tính"]
        self.operation_var = tk.StringVar(master)
        self.operation_var.set(self.operations[0])  # Mặc định là tích phân

        self.operation_menu = tk.OptionMenu(master, self.operation_var, *self.operations)
        self.operation_menu.pack()

        self.label = tk.Label(master, text="Nhập biểu thức:")
        self.label.pack()

        self.expression_entry = tk.Entry(master)
        self.expression_entry.pack()

        self.calculate_button = tk.Button(master, text="Tính kết quả", command=self.calculate_result)
        self.calculate_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate_result(self):
        operation = self.operation_var.get()
        expression_str = self.expression_entry.get()

        try:
            x = Symbol('x')
            y = Symbol('y')  # Thêm dòng này để định nghĩa biến y
            if operation == "Tích phân":
                result = integrate(expression_str, x)
            elif operation == "Đạo hàm":
                result = diff(expression_str, x)
            elif operation == "Giải phương trình":
                result = solve(expression_str, x)
            elif operation == "Tích phân xác định":
                a = simpledialog.askfloat("Nhập giá trị", "Nhập giá trị thấp nhất của phạm vi tích phân:")
                b = simpledialog.askfloat("Nhập giá trị", "Nhập giá trị cao nhất của phạm vi tích phân:")
                result = integrate(expression_str, (x, a, b))
            elif operation == "Giải hệ phương trình tuyến tính":
                eq1_str = simpledialog.askstring("Nhập phương trình", "Nhập phương trình thứ nhất:")
                eq2_str = simpledialog.askstring("Nhập phương trình", "Nhập phương trình thứ hai:")
                eq1 = Eq(eval(eq1_str), 0)
                eq2 = Eq(eval(eq2_str), 0)
                result = solve((eq1, eq2), (x, y))  # Đặt biến y trong solve
            else:
                result = "Lựa chọn không hợp lệ"

            self.result_label.config(text=f"Kết quả {operation}: {result}")
        except Exception as e:
            self.result_label.config(text=f"Lỗi: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
