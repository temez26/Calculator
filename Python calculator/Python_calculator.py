import math
import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")

        self.expression = ""
        self.result = None
        self.memory = None

        self.create_ui()

    def create_ui(self):
        self.entry = tk.Entry(self.root, font=("Arial", 20))
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=0, sticky="nsew")

        button_texts = [
            ("7"), ("8"), ("9"),
            ("4"), ("5"), ("6"),
            ("1"), ("2"), ("3"), ("0"),
            ("+"), ("-"), ("*"), ("/"),
            ("^"), ("√"), ("="), ("M+"), ("MR"), ("C")
        ]

        for i, text in enumerate(button_texts):
            tk.Button(button_frame, text=text, command=lambda t=text: self.button_click(t), font=("Arial", 16), height=2, width=5).grid(row=i // 4, column=i % 4, sticky="nsew")

        # Configure row and column weights for resizing
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
            button_frame.grid_columnconfigure(i, weight=1)

        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)

        # Remove empty space in right corner
        self.root.grid_columnconfigure(4, weight=0)

        # Remove empty space in bottom corner
        self.root.grid_rowconfigure(2, weight=0)

    def button_click(self, char):
        if char.isdigit() or char == ".":
            self.expression += char
        elif char in "+-*/^":
            self.expression += " " + char + " "
        elif char == "=":
            try:
                self.result = eval(self.expression)
                self.expression = str(self.result)
            except Exception as e:
                self.expression = "Error"
        elif char == "√":
            try:
                self.result = math.sqrt(eval(self.expression))
                self.expression = str(self.result)
            except Exception as e:
                self.expression = "Error"
        elif char == "M+":
            self.memory = self.expression
            self.expression = ""
        elif char == "MR":
            if self.memory is not None:
                self.expression += self.memory
        elif char == "C":
            self.expression = ""

        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

def main():
    root = tk.Tk()
    calc = Calculator(root)
    root.geometry("400x500")  # Initial window size
    root.minsize(400, 500)  # Minimum window size
    root.mainloop()

if __name__ == "__main__":
    main()
