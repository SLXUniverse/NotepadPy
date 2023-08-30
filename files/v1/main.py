import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser


class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NotepadPy")

        # Create a Text widget for editing
        self.text_widget = tk.Text(self.root, undo=True)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        # Create a Menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Edit Menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_widget.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_widget.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)

        # Help Menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)

    def new_file(self):
        self.text_widget.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_widget.delete("1.0", tk.END)
                self.text_widget.insert("1.0", file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_widget.get("1.0", tk.END))

    def cut_text(self):
        self.text_widget.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_widget.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_widget.event_generate("<<Paste>>")

    def show_about(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("About NotepadPy")

        about_label = tk.Label(about_window, text="NotepadPy\nv1", font=("Helvetica", 16, "bold"))
        about_label.pack(pady=10)

        author_label = tk.Label(about_window, text="NotepadPy is free and open-source text. Based on Python and Tkinter.", font=("Helvetica", 12))
        author_label.pack()

        author_label = tk.Label(about_window, text="This application is created by\nSLX Universe", font=("Helvetica", 12))
        author_label.pack()

        open_source_button = tk.Button(about_window, text="Open Source", command=self.open_source)
        open_source_button.pack(pady=10)

        close_button = tk.Button(about_window, text="Close", command=about_window.destroy)
        close_button.pack()

    def open_source(self):
        webbrowser.open("https://github.com/SLXUniverse/NotepadPy")  # Replace with your actual link


if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
