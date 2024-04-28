"""
Example script for testing the Azure ttk theme
Author: rdbende
License: MIT license
Source: https://github.com/rdbende/ttk-widget-factory
"""

import tkinter as tk
from tkinter import ttk
import sv_ttk
import os
from datetime import datetime


# Function to get file data recursively
def get_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            subdir = os.path.relpath(root, directory)  # Gets the subdirectory path
            mod_time = os.path.getmtime(path)
            yield subdir, file, datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create value lists
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
        self.combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
        self.readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

        # Create control variables
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar(value=True)
        self.var_2 = tk.BooleanVar()
        self.var_3 = tk.IntVar(value=2)
        self.var_4 = tk.StringVar(value=self.option_menu_list[1])
        self.var_5 = tk.DoubleVar(value=75.0)

        # Create widgets :)
        self.setup_widgets()

    def setup_widgets(self):
        # Create a Frame for the Checkbuttons
        self.check_frame = ttk.LabelFrame(self, text="Checkbuttons", padding=(20, 10))
        self.check_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        # Checkbuttons
        self.check_1 = ttk.Checkbutton(
            self.check_frame, text="Unchecked", variable=self.var_0
        )
        self.check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.check_2 = ttk.Checkbutton(
            self.check_frame, text="Checked", variable=self.var_1
        )
        self.check_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        self.check_3 = ttk.Checkbutton(
            self.check_frame, text="Third state", variable=self.var_2
        )
        self.check_3.state(["alternate"])
        self.check_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

        self.check_4 = ttk.Checkbutton(
            self.check_frame, text="Disabled", state="disabled"
        )
        self.check_4.state(["disabled !alternate"])
        self.check_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

        # Separator
        self.separator = ttk.Separator(self)
        self.separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")

        # Create a Frame for the Radiobuttons
        self.radio_frame = ttk.LabelFrame(self, text="Radiobuttons", padding=(20, 10))
        self.radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

        # Radiobuttons
        self.radio_1 = ttk.Radiobutton(
            self.radio_frame, text="Unselected", variable=self.var_3, value=1
        )
        self.radio_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
        self.radio_2 = ttk.Radiobutton(
            self.radio_frame, text="Selected", variable=self.var_3, value=2
        )
        self.radio_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        self.radio_4 = ttk.Radiobutton(
            self.radio_frame, text="Disabled", state="disabled"
        )
        self.radio_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # Entry
        self.entry = ttk.Entry(self.widgets_frame)
        self.entry.insert(0, "Entry")
        self.entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

        # Spinbox
        self.spinbox = ttk.Spinbox(self.widgets_frame, from_=0, to=100, increment=0.1)
        self.spinbox.insert(0, "Spinbox")
        self.spinbox.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

        # Combobox
        self.combobox = ttk.Combobox(self.widgets_frame, values=self.combo_list)
        self.combobox.current(0)
        self.combobox.grid(row=2, column=0, padx=5, pady=10, sticky="ew")

        # Read-only combobox
        self.readonly_combo = ttk.Combobox(
            self.widgets_frame, state="readonly", values=self.readonly_combo_list
        )
        self.readonly_combo.current(0)
        self.readonly_combo.grid(row=3, column=0, padx=5, pady=10, sticky="ew")

        # Menu for the Menubutton
        self.menu = tk.Menu(self)
        self.menu.add_command(label="Menu item 1")
        self.menu.add_command(label="Menu item 2")
        self.menu.add_separator()
        self.menu.add_command(label="Menu item 3")
        self.menu.add_command(label="Menu item 4")

        # Menubutton
        self.menubutton = ttk.Menubutton(
            self.widgets_frame, text="Menubutton", menu=self.menu, direction="below"
        )
        self.menubutton.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

        # OptionMenu
        self.optionmenu = ttk.OptionMenu(
            self.widgets_frame, self.var_4, *self.option_menu_list
        )
        self.optionmenu.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

        # Button
        self.button = ttk.Button(self.widgets_frame, text="Button")
        self.button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

        # Accentbutton
        self.accentbutton = ttk.Button(
            self.widgets_frame, text="Accent button", style="Accent.TButton"
        )
        self.accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")

        # Togglebutton
        self.togglebutton = ttk.Checkbutton(
            self.widgets_frame, text="Toggle button", style="Toggle.TButton"
        )
        self.togglebutton.grid(row=8, column=0, padx=5, pady=10, sticky="nsew")

        # Switch
        self.switch = ttk.Checkbutton(
            self.widgets_frame, text="Switch", style="Switch.TCheckbutton"
        )
        self.switch.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")

        # Panedwindow
        self.paned = ttk.PanedWindow(self)
        self.paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

        # Pane #1
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=1)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.pane_1)
        self.scrollbar.pack(side="right", fill="y")

        # Treeview
        self.treeview = ttk.Treeview(self.pane_1, columns=("include", "subdir", "file", "modified"),
                            show="headings",  # Hide the tree column
                            selectmode="extended",  # Enable multiple selection
                            yscrollcommand=self.scrollbar.set)
        self.treeview.pack(fill=tk.BOTH, expand=True)
        # self.treeview = ttk.Treeview(
        #     self.pane_1,
        #     selectmode="browse",
        #     yscrollcommand=self.scrollbar.set,
        #     columns=(1, 2),
        #     height=10,
        # )
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)

        # Defining the columns
        self.treeview.heading('include', text='Include', anchor=tk.W)
        self.treeview.heading('subdir', text='Subdirectory', anchor=tk.W)
        self.treeview.heading('file', text='File Name', anchor=tk.W)
        self.treeview.heading('modified', text='Last Modified', anchor=tk.W)

        # Configuring column widths
        self.treeview.column('include', width=50, stretch=tk.NO, anchor=tk.CENTER)
        self.treeview.column('subdir', width=200, minwidth=150, stretch=tk.NO)
        self.treeview.column('file', width=200, minwidth=150, stretch=tk.NO)
        self.treeview.column('modified', width=150, minwidth=100, stretch=tk.NO)

        # Dictionary to store checkbox states
        checkbox_states = {}

        # Function to toggle inclusion check
        def toggle_include(event):
            region = self.treeview.identify_region(event.x, event.y)
            if region == "cell":
                col = self.treeview.identify_column(event.x)
                if col == "#1":  # The 'include' column
                    row_id = self.treeview.identify_row(event.y)
                    # Toggle the checkbox state
                    if row_id in checkbox_states and checkbox_states[row_id]:
                        self.treeview.set(row_id, 'include', '')  # Change to unchecked
                        checkbox_states[row_id] = False
                    else:
                        self.treeview.set(row_id, 'include', '✅')  # Change to checked
                        checkbox_states[row_id] = True
                print(checkbox_states)

        # Bind the left mouse button click to toggle_include function
        self.treeview.bind('<ButtonRelease-1>', toggle_include)  # Use ButtonRelease for more accurate detection

        # Inserting the data into the TreeView
        directory = "C:\\Users\\proje\\OneDrive\\Documents\\Guild Wars 2\\addons\\arcdps\\arcdps.cbtlogs\\1"  # Change this to your directory
        for subdir, file, modified in get_files(directory):
            oid = self.treeview.insert('', tk.END, values=('', subdir, file, modified))
            checkbox_states[oid] = False  # Initialize all checkboxes as unchecked

        # Notebook, pane #2
        self.pane_2 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_2, weight=3)

        # Notebook, pane #2
        self.notebook = ttk.Notebook(self.pane_2)
        self.notebook.pack(fill="both", expand=True)

        # Tab #1
        self.tab_1 = ttk.Frame(self.notebook)
        for index in [0, 1]:
            self.tab_1.columnconfigure(index=index, weight=1)
            self.tab_1.rowconfigure(index=index, weight=1)
        self.notebook.add(self.tab_1, text="Tab 1")

        # Scale
        self.scale = ttk.Scale(
            self.tab_1,
            from_=100,
            to=0,
            variable=self.var_5,
            command=lambda event: self.var_5.set(self.scale.get()),
        )
        self.scale.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

        # Progressbar
        self.progress = ttk.Progressbar(
            self.tab_1, value=0, variable=self.var_5, mode="determinate"
        )
        self.progress.grid(row=0, column=1, padx=(10, 20), pady=(20, 0), sticky="ew")

        # Label
        self.label = ttk.Label(
            self.tab_1,
            text="Azure theme for ttk",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label.grid(row=1, column=0, pady=10, columnspan=2)

        # Tab #2
        self.tab_2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_2, text="Tab 2")

        # Tab #3
        self.tab_3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_3, text="Tab 3")

        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Arc Top Stats AIO")

    # Simply set the theme
    sv_ttk.set_theme("dark")
    sv_ttk.use_dark_theme()

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    root.mainloop()
