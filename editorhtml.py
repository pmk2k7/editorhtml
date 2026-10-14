import os
import tkinter as tk
from tkinter import filedialog, messagebox
from subprocess import Popen
import webbrowser

def ensure_test_folder():
    """Ensure the test folder exists in the specified location."""
    test_folder = r"C:\xampp\htdocs\test"
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
    return test_folder

def save_and_preview():
    """Save the current code to a file and open it in a web browser."""
    code = editor.get("1.0", tk.END)
    file_type = selected_language.get()

    if not current_file.get():
        messagebox.showwarning("Warning", "Please save the file first.")
        return

    filename = current_file.get()
    save_path = os.path.join(ensure_test_folder(), filename)

    with open(save_path, "w", encoding="utf-8") as file:
        file.write(code)

    if file_type == "PHP":
        url = f"http://localhost/test/{filename}"
    else:
        url = f"file://{save_path}"

    webbrowser.open(url)

def open_file():
    """Open an existing HTML or PHP file from the test folder."""
    test_folder = ensure_test_folder()
    file_path = filedialog.askopenfilename(initialdir=test_folder, filetypes=[("All files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            editor.delete("1.0", tk.END)
            editor.insert("1.0", content)
            current_file.set(os.path.basename(file_path))

def save_file():
    """Save the current code to a file in the test folder."""
    test_folder = ensure_test_folder()
    file_path = filedialog.asksaveasfilename(initialdir=test_folder, defaultextension=".html", filetypes=[("HTML files", "*.html"), ("PHP files", "*.php"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(editor.get("1.0", tk.END))
        current_file.set(os.path.basename(file_path))

# Main Application Window
root = tk.Tk()
root.title("HTML/PHP Editor")
root.geometry("800x600")

# Current file name variable
current_file = tk.StringVar(value="")

# Language Selection
selected_language = tk.StringVar(value="HTML")

def change_file_type(event):
    """Change editor mode based on file type selection."""
    current = selected_language.get()
    label.config(text=f"Editor - {current}")

options = ["HTML", "PHP"]
lang_menu = tk.OptionMenu(root, selected_language, *options, command=change_file_type)
lang_menu.pack(anchor="w", padx=10, pady=5)

# Label and Text Area
label = tk.Label(root, text="Editor - HTML", font=("Arial", 14))
label.pack(anchor="w", padx=10)
editor = tk.Text(root, wrap=tk.WORD, font=("Consolas", 12))
editor.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(anchor="e", pady=10)

open_btn = tk.Button(btn_frame, text="Open", command=open_file)
open_btn.pack(side=tk.LEFT, padx=5)

save_btn = tk.Button(btn_frame, text="Save", command=save_file)
save_btn.pack(side=tk.LEFT, padx=5)

preview_btn = tk.Button(btn_frame, text="Preview", command=save_and_preview)
preview_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()
