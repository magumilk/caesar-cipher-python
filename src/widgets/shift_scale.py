import tkinter as tk

class ShiftScale(tk.Frame):
    """
    シフト数を設定するスケールウィジェット
    """
    __LABEL_TEXT = "シフト数"
    def __init__(self, master: tk.Misc):
        """
        コンストラクタ

        Args:
            master (tk.Misc): 親ウィジェット
        """
        super().__init__(master)
        self.__scale_var = tk.IntVar(value=0)
        self.__label = tk.Label(
            self,
            text=self.__LABEL_TEXT,
            width=len(self.__LABEL_TEXT)*2,
            height=1,
        )
        self.__label.pack(side="top", fill="both", expand=True)
        self.__scale = tk.Scale(
            self,
            from_=0,
            to=ord("z") - ord("a"),
            resolution=1,
            variable=self.__scale_var,
            orient="horizontal",
        )
        self.__scale.pack(side="top", fill="both", expand=True)
    
    def get_shift(self) -> int:
        """
        シフト数を取得する

        Returns:
            int: シフト数
        """
        return self.__scale_var.get()