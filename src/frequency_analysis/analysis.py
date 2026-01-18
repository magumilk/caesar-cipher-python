from frequency_analysis.frequency_analysis_result import FrequencyAnalysisResult


# 英小文字のUnicodeコードポイントの範囲
__LOWER_ALPHA_STARTPOINT = 97
__LOWER_ALPHA_ENDPOINT = __LOWER_ALPHA_STARTPOINT + 26 - 1

def perform_frequency_analysis(text: str) -> FrequencyAnalysisResult:
    """与えられた文字列に対して頻度分析を行う.

    入力文字列から英小文字（a〜z）のみを抽出し,  
    各文字の出現回数をカウントする.  
    英小文字以外の文字（大文字、数字、記号など）は分析対象外とする.

    Args:
        text (str): 分析対象の文字列.

    Returns:
        FrequencyAnalysisResult: 元の文字列と、各英小文字の出現頻度を保持する分析結果オブジェクト
    """
    analyzed_text = ""
    char_frequency = __create_init_dict()
    for char in text:
        if __LOWER_ALPHA_STARTPOINT <= ord(char) <= __LOWER_ALPHA_ENDPOINT:
            analyzed_text += char
            char_frequency[char] += 1
    return FrequencyAnalysisResult(analyzed_text, char_frequency)

def __create_init_dict() -> dict[str, int]:
    """英小文字（a〜z）をキー、出現回数の初期値 0 を値とする辞書を生成する.  

    頻度分析において, すべての英小文字をあらかじめ  
    カウント対象として用意するための補助関数である.

    Returns:
        dict[str, int]: 英小文字（a〜z）をキー, 出現回数の初期値 0 を値とする辞書
    """
    init_dict = {}
    for char in range(__LOWER_ALPHA_STARTPOINT, __LOWER_ALPHA_ENDPOINT + 1):
        init_dict[chr(char)] = 0
    return init_dict