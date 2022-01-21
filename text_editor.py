import tkinter as tk

class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Text Editor by Steven Guamán - 2022')

        # Configuration min size window
        self.rowconfigure(0, minsize=600, weight=1)

        # Configuration min size second column
        self.columnconfigure(1, minsize=600, weight=1)

        # Text attrubute
        self.text_camp = tk.Text(self, wrap=tk.WORD)

        # File attribute
        self.file = None

        # Validate if file was opened before
        self.file_open = False


if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()