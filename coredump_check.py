import tkinter as tk
import argparse
import os.path
import time

COREDUMP_STR = 'coredump'

def IsCoredumpExist(line):
    if line.find(COREDUMP_STR) is not -1:
        return True;
    return False;

def CheckCoredump(filename, start_line):
    print(filename + ": " + str(start_line));
    last_line_idx = 0;
    with open(filename, 'r', encoding='ISO-8859-15') as log_file:
        for line in log_file:
            last_line_idx = last_line_idx+1;
            if last_line_idx < start_line:
                continue;
            if IsCoredumpExist(line):
                return True,last_line_idx
    return False,last_line_idx;

def ShowWindow(title, message):
    window = tk.Tk()
    window.title(title)
    window.geometry('300x100')

    label = tk.Label(window,
            text = message,
            width=300, height=100)
    label.pack()
    window.mainloop()

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='manual to this script') 
    parse.add_argument('--file_name', type=str, default=None)
    argv = parse.parse_args()
    filename = argv.file_name
    if not os.path.exists(filename):
        ShowWindow("Error", "file " + filename + " not exist!!")

    start_line = 0;

    while True:
        result,start_line = CheckCoredump(filename, start_line)
        if result is True:
            break;
        time.sleep(10)
   
    ShowWindow("Coredump Found", "in line " + str(start_line))
