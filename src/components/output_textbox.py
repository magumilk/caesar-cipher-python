import tkinter as tk

class OutputConsole(tk.Text):
    def __init__(self, master: tk.Misc):
        super().__init__(
            master,
            state="disabled",
        )
    
    def set_text(self, text: str):
        self.configure(state="normal")
        self.delete("1.0", "end")
        self.insert("1.0", text)
        self.configure(state="disabled")