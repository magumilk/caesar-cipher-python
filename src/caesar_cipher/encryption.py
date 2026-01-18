from caesar_cipher.utils import shift_char, is_alpha

def encrypt(text: str, key: int) -> str:
    """シーザー暗号を用いて文字列を暗号化する.
    
    Args:
        text (str): 暗号化する文字列.
        key (int): シフト数.

    Returns:
        str: 暗号化された文字列.
    """
    ciphertext = ""
    for char in text:
        if is_alpha(char):
            ciphertext += shift_char(char.lower(), key)
            continue
        ciphertext += char
    return ciphertext