import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")

        self.expression = ""
        self.text_input = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display
        display_frame = tk.Frame(self.root)
        display_frame.pack(expand=True, fill="both")

        display = tk.Entry(display_frame, font=('arial', 20, 'bold'), textvariable=self.text_input, bd=30, insertwidth=4, width=14, borderwidth=4, justify="right")
        display.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(expand=True, fill="both")

        button_texts = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
            ("C", 5, 0), ("(", 5, 1), (")", 5, 2), ("CE", 5, 3)
        ]

        for (text, row, col) in button_texts:
            self.create_button(text, row, col, buttons_frame)

    def create_button(self, text, row, col, frame):
        button = tk.Button(frame, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, char):
        if char == "=":
            self.calculate_result()
        elif char == "C":
            self.clear_display()
        elif char == "CE":
            self.delete_last()
        else:
            self.append_to_expression(char)

    def append_to_expression(self, char):
        self.expression += str(char)
        self.text_input.set(self.expression)

    def calculate_result(self):
        try:
            result = str(eval(self.expression))
            self.text_input.set(result)
            self.expression = result
        except:
            self.text_input.set("Error")
            self.expression = ""

    def clear_display(self):
        self.expression = ""
        self.text_input.set("")

    def delete_last(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
