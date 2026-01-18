import tkinter as tk

class ReadOnlyTextBox(tk.Text):
    """
    読み取り専用のテキストボックスウィジェット
    """
    def __init__(self, master: tk.Misc):
        """
        コンストラクタ

        Args:
            master (tk.Misc): 親ウィジェット
        """
        super().__init__(master, state="disabled")
    
    def set_text(self, text: str):
        """
        テキストをテキストボックスに設定する

        Args:
            text (str): 設定するテキスト
        """
        self.configure(state="normal")
        self.delete("1.0", "end")
        self.insert("1.0", text)
        self.configure(state="disabled")