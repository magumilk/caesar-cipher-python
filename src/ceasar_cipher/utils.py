__UPPER_ALPHA_STARTPOINT = 65
__UPPER_ALPHA_ENDPOINT = 90
__LOWER_ALPHA_STARTPOINT = 97
__LOWER_ALPHA_ENDPOINT = 122


def shift_char(char: str, shift: int) -> str:
    """指定の文字を `shift` だけずらす.  

    `char` で与えられた文字のUnicodeコードポイントに `shift` を加算した文字を返す.  
    与えられる文字は１文字だけを想定している.  

    Args:
        char (str): ずらすアルファベット.
        shift (int): ずらす量.

    Returns:
        str: ずらした文字
    """
    return chr(ord(char) + shift)


def is_lower_alpha(char: str) -> bool:
    """指定の文字が小文字アルファベットか判定する.
    
    Args:
        char (str): 判定する文字.

    Returns:
        bool: 小文字アルファベットかどうか
    """
    return __LOWER_ALPHA_STARTPOINT <= ord(char) <= __LOWER_ALPHA_ENDPOINT


def is_upper_alpha(char: str) -> bool:
    """指定の文字が大文字アルファベットか判定する.
    
    Args:
        char (str): 判定する文字.

    Returns:
        bool: 大文字アルファベットかどうか
    """
    return __UPPER_ALPHA_STARTPOINT <= ord(char) <= __UPPER_ALPHA_ENDPOINT


def is_alpha(char: str) -> bool:
    """指定の文字がアルファベットか判定する.
    
    Args:
        char (str): 判定する文字.

    Returns:
        bool: アルファベットかどうか
    """
    return is_lower_alpha(char) or is_upper_alpha(char)