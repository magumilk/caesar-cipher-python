from ceasar_cipher.utils import shift_char, is_lower_alpha

def descrypt(text: str, key: int) -> str:
    """シーザー暗号を用いて文字列を復号する.
    
    Args:
        text (str): 復号する文字列.
        key (int): シフト数.

    Returns:
        str: 復号された文字列.
    """
    plaintext = ""
    for char in text:
        if is_lower_alpha(char):
            plaintext += shift_char(char, -key).upper()
            continue
        plaintext += char
    return plaintext