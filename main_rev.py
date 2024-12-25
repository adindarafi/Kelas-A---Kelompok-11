import pandas as pd
import os
import tkinter as tk
from tkinter import Tk
from app_rev import AplikasiSiswa

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiSiswa(root)
    app.frame_login.pack(fill="both", expand=True)
    root.mainloop()