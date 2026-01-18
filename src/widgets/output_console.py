import tkinter as tk

from .output_analysis_result import AnalysisResultArea, FrequencyAnalysisResult
from .readonly_textbox import ReadOnlyTextBox


class OutputConsole(tk.Frame):
    """
    暗号の文字列結果や頻度分析結果を表示するウィジェット
    """

    def __init__(self, master: tk.Misc):
        """
        コンストラクタ

        Args:
            master (tk.Misc): 親ウィジェット
        """
        super().__init__(master)
        self.__cipher_console = ReadOnlyTextBox(self)
        self.__frequency_console = AnalysisResultArea(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.__cipher_console.grid(row=0, column=0, sticky="nsew")
        self.__frequency_console.grid(row=0, column=0, sticky="nsew")
        self.__toggle_console(self.__cipher_console)
    
    def __toggle_console(self, console: tk.Misc):
        """
        表示するコンソールを切り替える。

        Args:
            console (tk.Misc): 最前面に表示するコンソール
        """
        self.current_console = console
        console.tkraise()

    def set_output(self, result: str | FrequencyAnalysisResult):
        """
        出力内容に応じて適切なコンソールに表示する。

        `FrequencyAnalysisResult` の場合は分析結果用のコンソールに、  
        文字列の場合はテキストコンソールに切り替えて表示する。

        Args:
            result (str | FrequencyAnalysisResult): 表示する結果。
        """
        if isinstance(result, FrequencyAnalysisResult):
            self.__toggle_console(self.__frequency_console)
            self.__frequency_console.set_output(result)
        else:
            self.__toggle_console(self.__cipher_console)
            self.__cipher_console.set_text(result)
