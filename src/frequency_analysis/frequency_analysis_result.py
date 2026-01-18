from io import BytesIO

from matplotlib import pyplot as plt
from PIL import ImageTk, Image

class FrequencyAnalysisResult:
    """頻度分析の結果を保持するクラス

    Attributes:
        analyzed_text: 分析対象として抽出された文字列（英小文字のみ等）
        char_frequency: 文字をキー, 出現回数を値とする辞書
    """
    def __init__(self, analyzed_text: str, char_frequency: dict[str, int]):
        """コンストラクタ

        Args:
            analyzed_text: 分析対象として扱った文字列
            char_frequency: 文字をキー、出現回数を値とする辞書
        """
        self.__analyzed_text = analyzed_text
        self.__char_frequency = char_frequency
    
    def to_graph(self) -> ImageTk.PhotoImage:
        """文字の出現頻度を棒グラフ化し、Tkinter 用画像として返す。

        `matplotlib` で棒グラフを生成し, PNG としてメモリ上に保存した後,  
        `PIL.Image` で読み込んで `ImageTk.PhotoImage` に変換して返す.

        Returns:
            Tkinter 上で表示できる棒グラフ画像（`ImageTk.PhotoImage`）"""
        x = range(len(self.__char_frequency))
        y = self.__char_frequency.values()

        fig, ax = plt.subplots()
        ax.bar(x, y, tick_label=self.__char_frequency.keys())

        ofs = BytesIO()
        fig.savefig(ofs, format="png")
        plt.close()
        ofs.seek(0)  # ファイルの先頭に移動

        return ImageTk.PhotoImage(Image.open(ofs))

    @property
    def analyzed_text(self) -> str:
        """分析対象として抽出された文字列"""
        return self.__analyzed_text
    
    @property
    def char_frequency(self) -> dict[str, int]:
        """文字の出現頻度辞書"""
        return self.__char_frequency.copy()
    
    def __repr__(self):
        return f"FrequencyAnalysisResult(analyzed_text={self.__analyzed_text}, char_frequency={self.__char_frequency})"