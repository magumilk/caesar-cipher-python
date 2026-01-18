import tkinter as tk
from PIL import ImageTk

from components.output_textbox import OutputConsole
from frequency_analysis import FrequencyAnalysisResult

class AnalysisResultArea(tk.Frame):
    def __init__(self, master: tk.Misc, textvariable: tk.StringVar | None = None):
        super().__init__(
            master,
        )
        self.__output_textbox = OutputConsole(
            self,
        )
        self.__output_textbox.pack(side="left", fill="both", expand=True)
        self.__graph = AnalysisResultGraph(self)
        self.__graph.pack(side="left", fill="both", expand=True)
    
    def set_output(self, result: FrequencyAnalysisResult):
        self.__output_textbox.set_text(result.analyzed_text)
        self.update_idletasks()
        size = (self.__graph.winfo_width(), self.__graph.winfo_height())
        self.__graph.set_graph(result.to_graph(size))


class AnalysisResultGraph(tk.Canvas):

    def __init__(self, master: tk.Misc):
        super().__init__(
            master,
        )
        self.__image_id: int | None = None
        self.__photo: ImageTk.PhotoImage | None = None
    
    def set_graph(self, graph: ImageTk.PhotoImage):
        self.__photo = graph
        if self.__image_id is not None:
            self.delete(self.__image_id)
        self.__image_id = self.create_image(0, 0, anchor="nw", image=self.__photo)