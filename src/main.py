import tkinter as tk
from typing import Literal

from caesar_cipher import encrypt, decrypt
from frequency_analysis import perform_frequency_analysis
from components import TextBox, OutputConsole, AnalysisResultArea, ShiftScale

def main():

    root = tk.Tk()
    root.state("zoomed")

    input_area = tk.Frame(root)
    config_area = tk.Frame(root)
    output_area = tk.Frame(root)

    input_textbox = TextBox(input_area, "Input")
    memo = TextBox(input_area, "Memo")
    input_textbox.grid(row=0, column=0, columnspan=7, sticky="nsew")
    memo.grid(row=0, column=8, sticky="nsew")

    output_textbox = OutputConsole(output_area)
    analysis_result_area = AnalysisResultArea(output_area)
    output_textbox.pack(side="left", fill="both", expand=True)
    is_analysis_result_area_display: bool = True

    def toggle_output_console(display: Literal["CIPHER", "ANALYSIS"]):
        if display == "CIPHER":
            output_textbox.pack(side="left", fill="both", expand=True)
        else:
            analysis_result_area.pack(side="left", fill="both", expand=True)
        nonlocal is_analysis_result_area_display
        is_analysis_result_area_display = (display == "ANALYSIS")

    def encrypt_button_handler():
        ciphertext = encrypt(input_textbox.get_text(), shift_scale.get_shift())
        output_textbox.set_text(ciphertext)
        print(ciphertext)
        toggle_output_console("CIPHER")
    
    def decrypt_button_handler():
        plaintext = decrypt(input_textbox.get_text(), shift_scale.get_shift())
        output_textbox.set_text(plaintext)
        toggle_output_console("CIPHER")
    
    def frequency_analysis_button_handler():
        analysis_result_area.set_output(perform_frequency_analysis(input_textbox.get_text()))
        toggle_output_console("ANALYSIS")

    shift_scale = ShiftScale(config_area)
    encrypt_button = tk.Button(config_area, text="暗号化", command=encrypt_button_handler)
    decrypt_button = tk.Button(config_area, text="復号化", command=decrypt_button_handler)
    frequency_analysis_button = tk.Button(config_area, text="頻度分析", command=frequency_analysis_button_handler)
    shift_scale.pack(side="left", fill="both", expand=True)
    encrypt_button.pack(side="left", fill="both", expand=True)
    decrypt_button.pack(side="left", fill="both", expand=True)
    frequency_analysis_button.pack(side="left", fill="both", expand=True)

    input_area.pack(side="top", fill="both", expand=True)
    config_area.pack(side="top", fill="both", expand=True)
    output_area.pack(side="top", fill="both", expand=True)


    root.mainloop()

if __name__ == "__main__":
    main()