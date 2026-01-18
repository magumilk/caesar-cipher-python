import tkinter as tk
from PIL import ImageTk

from frequency_analysis import FrequencyAnalysisResult
from .uneditable_text import UneditableText

class AnalysisResultArea(tk.Frame):
    """
    分析結果を出力し, 表示するためのウィジェット
    """
    def __init__(self, master: tk.Misc):
        """
        コンストラクタ

        Args:
            master (tk.Misc): 親ウィジェット
        """
        super().__init__(master)
        self.__output_textbox = UneditableText(self)
        self.__graph = AnalysisResultGraph(self)
        self.grid_columnconfigure(0, weight=1, uniform="analysis")
        self.grid_columnconfigure(1, weight=1, uniform="analysis")
        self.grid_rowconfigure(0, weight=1, uniform="analysis")
        self.__output_textbox.grid(row=0, column=0, sticky="nsew")
        self.__graph.grid(row=0, column=1, sticky="nsew")
    
    def set_output(self, result: FrequencyAnalysisResult):
        """
        分析結果を出力する

        実際に出現頻度を数えた文字列を左側のテキストボックスに出力し,  
        出現頻度をグラフ化した画像を右側のウィジェットに出力する.

        Args:
            result (FrequencyAnalysisResult): 出力する分析結果
        """
        self.__output_textbox.set_text(result.analyzed_text)
        self.update_idletasks()
        size = (self.__graph.winfo_width(), self.__graph.winfo_height())
        self.__graph.set_graph(result.to_graph(size))


class AnalysisResultGraph(tk.Canvas):
    """
    分析結果のグラフを描画するウィジェット
    """

    def __init__(self, master: tk.Misc):
        """
        コンストラクタ

        Args:
            master (tk.Misc): 親ウィジェット
        """
        super().__init__(
            master,
        )
        self.__image_id: int | None = None
        self.__photo: ImageTk.PhotoImage | None = None
    
    def set_graph(self, graph: ImageTk.PhotoImage):
        """
        描画するグラフをセットする

        Args:
            graph (ImageTk.PhotoImage): 描画するグラフの画像
        """
        self.__photo = graph
        if self.__image_id is not None:
            self.delete(self.__image_id)
        self.__image_id = self.create_image(0, 0, anchor="nw", image=self.__photo)