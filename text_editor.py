import tkinter as tk
from tkinter import INSERT
from tkinter.filedialog import askopenfile, asksaveasfilename

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
        close_button = tk.Button(buttons_frame, text='Close', command=self._close_file)
        upper_button = tk.Button(buttons_frame, text='Upper Case', command=self._uppercase)
        lower_button = tk.Button(buttons_frame, text='Lower Case', command=self._lowercase)

        open_button.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        upper_button.grid(row=1, column=0, sticky='we', padx=5, pady=5)
        lower_button.grid(row=2, column=0, sticky='we', padx=5, pady=5)
        save_button.grid(row=3, column=0, sticky='we', padx=5, pady=5)
        save_as_button.grid(row=4, column=0, sticky='we', padx=5, pady=5)
        close_button.grid(row=5, column=0, sticky='we', padx=5, pady=5)

        buttons_frame.grid(row=0, column=0, sticky='ns')

        self.text_camp.grid(row=0, column=1, sticky='nswe')

    def _create_menu(self):
        app_menu = tk.Menu(self)
        self.config(menu=app_menu)

        file_menu = tk.Menu(app_menu, tearoff=False)
        app_menu.add_cascade(label='File', menu=file_menu)

        file_menu.add_command(label='New', command=self._close_file)
        file_menu.add_command(label='Open', command=self._open_file)
        file_menu.add_command(label='Save', command=self._save_file)
        file_menu.add_command(label='Save As...', command=self._save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.quit)

    def _open_file(self):
        self.file_open = askopenfile(mode='r+')
        # Delete text on the screen
        self.text_camp.delete(1.0, tk.END)
        # Review previous files
        if not self.file_open:
            return
        with open(self.file_open.name, 'r+') as self.file:
            text = self.file.read()
            self.text_camp.insert(1.0, text)
            self.title(f'*Text Editor - {self.file.name}')

    def _save_file(self):
        if self.file_open:
            with open(self.file_open.name, 'w') as self.file:
                text = self.text_camp.get(1.0, tk.END)
                self.file.write(text)
                self.title(f'Text Editor - {self.file.name}')
        else:
            self._save_as_file()

    def _save_as_file(self):
        self.file = asksaveasfilename(
            defaultextension='txt',
            filetypes=[('Text File', '*.txt'), ('All Files', '*,*')]
        )
        if not self.file:
            return
        with open(self.file, 'w') as self.file:
            text = self.text_camp.get(1.0, tk.END)
            self.file.write(text)
            self.title(f'Text Editor - {self.file.name}')
            self.file_open = self.file

    def _close_file(self):
        if self.file_open:
            self.text_camp.delete(1.0, tk.END)
            self.title('Text Editor by Steven Guamán - 2022')
            self.file_open = False
            self.file.close()
        else:
            self.text_camp.delete(1.0, tk.END)

    def _uppercase(self):
        text = self.text_camp.get(1.0, tk.END)
        self.text_camp.delete(1.0, tk.END)
        self.text_camp.insert(INSERT, text.upper())

    def _lowercase(self):
        text = self.text_camp.get(1.0, tk.END)
        self.text_camp.delete(1.0, tk.END)
        self.text_camp.insert(INSERT, text.lower())

if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()