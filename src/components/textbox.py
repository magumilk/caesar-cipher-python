import tkinter as tk

class TextBox(tk.Frame):
    def __init__(self, master: tk.Misc, title: str | None = None):
        super().__init__(
            master,
        )
        self.__label = tk.Label(
            self,
            text=title,
            height=1,
        )
        self.__label.pack(side="top")
        self.__textbox = tk.Text(
            self,
        )
        self.__textbox.pack(side="top", fill="both", expand=True)
    
    def get_text(self) -> str:
        return self.__textbox.get("1.0", "end")