import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import pathlib

LOG_PATH = pathlib.Path("demo_keystrokes.log")

def append_log(text):
    timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(f"{timestamp}    {text}\n")

def on_key(event):
    char = event.char
    keyname = event.keysym
    if char and char.isprintable():
        display = repr(char)
        append_log(f"CHAR {display}")
        live_view.insert(tk.END, f"{timestamp_prefix()} CHAR {display}\n")
    else:
        append_log(f"KEY {keyname}")
        live_view.insert(tk.END, f"{timestamp_prefix()} KEY {keyname}\n")
    live_view.see(tk.END)

def timestamp_prefix():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def clear_log():
    if LOG_PATH.exists():
        LOG_PATH.unlink()
    live_view.delete("1.0", tk.END)

root = tk.Tk()
root.title("Safe Keylogger Demo — Educational Only")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

label = tk.Label(frame, text="Type in the box below. This demo only logs input typed inside this window.")
label.pack(anchor="w")

input_box = scrolledtext.ScrolledText(frame, height=6, wrap="word")
input_box.pack(fill="both", expand=False, pady=(4,8))
input_box.insert(tk.END, "Focus here and type. This input is safe and local to the demo.\n")
input_box.focus_set()

input_box.bind("<Key>", on_key)

live_label = tk.Label(frame, text="Live log view (most recent at bottom):")
live_label.pack(anchor="w")

live_view = scrolledtext.ScrolledText(frame, height=10, state="normal", wrap="none")
live_view.pack(fill="both", expand=True)
live_view.insert(tk.END, "No entries yet.\n")

controls = tk.Frame(root, pady=6)
controls.pack(fill="x")
clear_btn = tk.Button(controls, text="Clear Log & Live View", command=clear_log)
clear_btn.pack(side="left", padx=(10,6))
info_lbl = tk.Label(controls, text="Log file: demo_keystrokes.log (created next to this script)")
info_lbl.pack(side="left", padx=8)

root.mainloop()
