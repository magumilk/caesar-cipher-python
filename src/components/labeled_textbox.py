import tkinter as tk

class LabeledTextBox(tk.Frame):
    """
    ラベル付きテキストボックスウィジェット
    """
    def __init__(self, master: tk.Misc, title: str | None = None):
        """
        コンストラクタ

        Args:
            master (tk.Misc): 親ウィジェット
            title (str, optional): ラベルのテキスト. 省略時は `None`.
        """
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
        """
        テキストボックスに記述された文字列を取得する

        Returns:
            str: 取得した文字列
        """
        return self.__textbox.get("1.0", "end")