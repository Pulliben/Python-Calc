import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root =root
        self.root.title("Calculator")

        # Create the entry widget for displaying the input/output
        self.entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=4, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Create buttons and place them in the grid
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+','ac','(',')'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            if button == '=':
                tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), bd=8, bg='red',fg='blue' , command=self.evaluate).grid(
                    row=row_val, column=col_val)
            elif button=='ac':
                tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), bd=8, command=self.clear).grid(
                    row=row_val, column=col_val)
            else:
                tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), bd=8,
                          command=lambda b=button: self.on_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_click(self, char):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current_text + char)

    def evaluate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def clear(self):
        self.entry.delete(0,tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

    


