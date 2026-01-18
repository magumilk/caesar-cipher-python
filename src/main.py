import tkinter as tk
from tkinter.font import nametofont

from caesar_cipher import encrypt, decrypt
from frequency_analysis import perform_frequency_analysis
from widgets import LabeledTextBox, OutputConsole, ShiftScale

def main():

    root = tk.Tk()
    root.state("zoomed")

    # フォントサイズの設定
    FONT_SIZE = 30
    nametofont("TkDefaultFont").configure(size=FONT_SIZE)
    nametofont("TkFixedFont").configure(size=FONT_SIZE)

    # 機能ごとに三つのエリアを定義し, 3:1:3の比率で配置
    input_area = tk.Frame(root)
    control_area = tk.Frame(root)
    output_area = OutputConsole(root)
    root.grid_rowconfigure(0, weight=3, uniform="main")
    root.grid_rowconfigure(1, weight=1, uniform="main")
    root.grid_rowconfigure(2, weight=3, uniform="main")
    root.grid_columnconfigure(0, weight=1)
    input_area.grid(row=0, column=0, sticky="nsew")
    control_area.grid(row=1, column=0, sticky="nsew")
    output_area.grid(row=2, column=0, sticky="nsew")

    # 入力エリアの定義
    # 入力テキストボックスとメモ用テキストボックスの横幅の比が3:2になるようにグリッドの重みを設定
    input_area.grid_columnconfigure(0, weight=3, uniform="input")
    input_area.grid_columnconfigure(1, weight=2, uniform="input")
    input_area.grid_rowconfigure(0, weight=1)
    # ウィジェットを生成して配置
    input_textbox = LabeledTextBox(input_area, "Input")
    memo = LabeledTextBox(input_area, "Memo")
    input_textbox.grid(row=0, column=0, sticky="nsew")
    memo.grid(row=0, column=1, sticky="nsew")

    # ボタンの関数の定義
    # 暗号化ボタンの押下処理
    def encrypt_button_handler():
        ciphertext = encrypt(input_textbox.get_text(), shift_scale.get_shift())
        output_area.set_output(ciphertext)
    # 復号化ボタンの押下処理
    def decrypt_button_handler():
        plaintext = decrypt(input_textbox.get_text(), shift_scale.get_shift())
        output_area.set_output(plaintext)
    # 頻度分析ボタンの押下処理
    def frequency_analysis_button_handler():
        output_area.set_output(perform_frequency_analysis(input_textbox.get_text()))

    # 操作エリアの定義
    # ウィジェットの生成
    shift_scale = ShiftScale(control_area)
    encrypt_button = tk.Button(control_area, text="暗号化", command=encrypt_button_handler)
    decrypt_button = tk.Button(control_area, text="復号化", command=decrypt_button_handler)
    frequency_analysis_button = tk.Button(control_area, text="頻度分析", command=frequency_analysis_button_handler)
    # グリッドで配置
    shift_scale.pack(side="left", fill="both", expand=True)
    encrypt_button.pack(side="left", fill="both", expand=True)
    decrypt_button.pack(side="left", fill="both", expand=True)
    frequency_analysis_button.pack(side="left", fill="both", expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()