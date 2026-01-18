from caesar_cipher.utils import shift_char, is_lower_alpha
from caesar_cipher.encryption import encrypt

def decrypt(text: str, key: int) -> str:
    """シーザー暗号を用いて文字列を復号する.
    
    Args:
        text (str): 復号する文字列.
        key (int): シフト数.

    Returns:
        str: 復号された文字列.
    """
    return encrypt(text, -key).upper()