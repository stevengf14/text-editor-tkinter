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

        self._create_components()
        self._create_menu()

    def _create_components(self):
        buttons_frame = tk.Frame(self, relief=tk.RAISED, bd=2)
        open_button = tk.Button(buttons_frame, text='Open', command=self._open_file)
        save_button = tk.Button(buttons_frame, text='Save', command=self._save_file)
        save_as_button = tk.Button(buttons_frame, text='Save As...', command=self._save_as_file)

        open_button.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        save_button.grid(row=1, column=0, sticky='we', padx=5, pady=5)
        save_as_button.grid(row=2, column=0, sticky='we', padx=5, pady=5)

        buttons_frame.grid(row=0, column=0, sticky='ns')

        self.text_camp.grid(row=0, column=1, sticky='nswe')

    def _create_menu(self):
        app_menu = tk.Menu(self)
        self.config(menu=app_menu)

        file_menu = tk.Menu(app_menu, tearoff=False)
        app_menu.add_cascade(label='File', menu=file_menu)

        file_menu.add_command(label='Open', command=self._open_file)
        file_menu.add_command(label='Save', command=self._save_file)
        file_menu.add_command(label='Save As...', command=self._save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.quit)

    def _open_file(self):
        pass

    def _save_file(self):
        pass

    def _save_as_file(self):
        pass

if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()