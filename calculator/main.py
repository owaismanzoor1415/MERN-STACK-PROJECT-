import tkinter as tk

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = tk.StringVar()
        self.entry_value = ''

        self.entry = tk.Entry(master, width=17, bg='#fff',font=('Arial Bold', 28), textvariable=self.equation)
        self.entry.place(x=0, y=0)

        def add_hover(btn):
            original = btn.cget("bg")
            def on_enter(e): btn.config(bg="#d9d9d9")
            def on_leave(e): btn.config(bg=original)
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

        buttons = [
            ('(',0,50), (')',90,50), ('%',180,50),
            ('1',0,125), ('2',90,125), ('3',180,125),
            ('4',0,200), ('5',90,200), ('6',180,200),
            ('7',0,275), ('8',90,275), ('9',180,275),
            ('0',90,350), ('.',180,350),
            ('+',270,275), ('-',270,200),
            ('/',270,50),  ('x',270,125),
            ('=',270,350), ('C',0,350)
        ]

        for (txt, x, y) in buttons:
            if txt == '=':
                b = tk.Button(master, width=11, height=4, text='=', relief='flat', bg='gray',
                            command=lambda: self.solve())
            elif txt == 'C':
                b = tk.Button(master, width=11, height=4, text='C', relief='flat', bg='gray',
                            command=lambda: self.clear())
            elif txt == 'x':
                b = tk.Button(master, width=11, height=4, text='x', relief='flat', bg='white',
                            command=lambda: self.show('*'))
            else:
                b = tk.Button(master, width=11, height=4, text=txt, relief='flat', bg='white',
                            command=lambda v=txt: self.show(v))
            b.place(x=x, y=y)
            add_hover(b)
        master.bind("<Key>", self.key_input)
        master.bind("<Return>", lambda e: self.solve())
        master.bind("<BackSpace>", lambda e: self.backspace())

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def backspace(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)

    def key_input(self, event):
        ch = event.char
        if ch in "0123456789+-*/().%":
            self.show(ch)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")
            self.entry_value = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
