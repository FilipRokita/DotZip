#DotZip.py
#Filip Rokita
#www.filiprokita.com



#import
import zipfile
import tkinter as tk
from tkinter import filedialog



#def
def choose():
    global zipPath; zipPath = filedialog.askopenfilename(title='DotZip', initialdir='./', filetypes=[("zip", "*.zip")])
    global dotzip; dotzip = zipfile.ZipFile(zipPath, 'r')
    extractB['state'] = tk.NORMAL


def extract():
    dotzip.extractall(zipPath[:-4])



#main
root = tk.Tk()
root.title('DotZip')
root.geometry('300x100')
root.resizable(False, False)


chooseB = tk.Button(root, text='Choose File', command=choose, width=15); chooseB.pack()
extractB = tk.Button(root, text='Extract', state=tk.DISABLED, command=extract, width=15); extractB.pack()
authorL = tk.Label(root, text='www.filiprokita.com'); authorL.pack(pady=10)


root.mainloop()