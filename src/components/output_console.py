import tkinter as tk

from .output_analysis_result import AnalysisResultArea, FrequencyAnalysisResult
from .uneditable_text import UneditableText

class OutputConsole(tk.Frame):
    def __init__(self, master: tk.Misc):
        super().__init__(master)
        self.__cipher_console = UneditableText(self)
        self.__frequency_console = AnalysisResultArea(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.__cipher_console.grid(row=0, column=0, sticky="nsew")
        self.__frequency_console.grid(row=0, column=0, sticky="nsew")
        self.__toggle_console(self.__cipher_console)
    
    def __toggle_console(self, console: tk.Misc):
        self.current_console = console
        console.tkraise()

    def set_output(self, result: str | FrequencyAnalysisResult):
        if isinstance(result, FrequencyAnalysisResult):
            self.__toggle_console(self.__frequency_console)
            self.__frequency_console.set_output(result)
        else:
            self.__toggle_console(self.__cipher_console)
            self.__cipher_console.set_text(result)