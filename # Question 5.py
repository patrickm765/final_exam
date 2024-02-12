# Question 5

import tkinter as tk
from tkinter import filedialog
import os

class FileOpenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Opener App")

        # Create buttons
        self.button_f_txt = tk.Button(root, text="Open f.txt", command=self.open_f_txt)
        self.button_update1_png = tk.Button(root, text="Open Update1.png", command=self.open_update1_png)
        self.button_update2_png = tk.Button(root, text="Open Update2.png", command=self.open_update2_png)
        self.button_question3_py = tk.Button(root, text="Open #Question3.py", command=self.open_question3_py)
        self.button_question4_part1_py = tk.Button(root, text="Open #Question4 part1.py", command=self.open_question4_part1_py)

        # Grid buttons
        self.button_f_txt.grid(row=0, column=0, padx=10, pady=5)
        self.button_update1_png.grid(row=1, column=0, padx=10, pady=5)
        self.button_update2_png.grid(row=2, column=0, padx=10, pady=5)
        self.button_question3_py.grid(row=3, column=0, padx=10, pady=5)
        self.button_question4_part1_py.grid(row=4, column=0, padx=10, pady=5)

    def open_f_txt(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            os.system(f'start "" "{file_path}"')

    def open_update1_png(self):
        file_path = "Update1.png"
        os.system(f'start "" "{file_path}"')

    def open_update2_png(self):
        file_path = "Update2.png"
        os.system(f'start "" "{file_path}"')

    def open_question3_py(self):
        file_path = "#Question3.py"
        os.system(f'start "" "{file_path}"')

    def open_question4_part1_py(self):
        file_path = "#Question4 part1.py"
        os.system(f'start "" "{file_path}"')

# Create the Tkinter window
root = tk.Tk()
app = FileOpenerApp(root)
root.mainloop()