
import pandas as pd
import os
from tkinter import Tk
from app import AplikasiSiswa

if __name__ == "__main__":
    root = Tk()
    app = AplikasiSiswa(root)
    app.frame_login.pack(fill="both", expand=True)
    root.mainloop()
