import tkinter
from tkinter import ttk
import abc
from Suvat import SUVAT
import webbrowser

class Menubar(ttk.Frame):
    """Builds a menu bar for the top of the main window"""
    def __init__(self, parent, *args, **kwargs):
        ''' Constructor'''
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_menubar()

    def on_exit(self):
        '''Exits program'''
        quit()

    def display_help(self):
        webbrowser.open("https://github.com/rustedorc/SUVAT")

    def display_about(self):
        webbrowser.open("https://github.com/rustedorc/SUVAT")

    def init_menubar(self):
        self.menubar = tkinter.Menu(self.root)
        self.menu_file = tkinter.Menu(self.menubar) # Creates a "File" menu
        self.menu_file.add_command(label='Exit', command=self.on_exit) # Adds an option to the menu
        self.menubar.add_cascade(menu=self.menu_file, label='File') # Adds File menu to the bar. Can also be used to create submenus.

        self.menu_help = tkinter.Menu(self.menubar) #Creates a "Help" menu
        self.menu_help.add_command(label='Help', command=self.display_help)
        self.menu_help.add_command(label='About', command=self.display_about)
        self.menubar.add_cascade(menu=self.menu_help, label='Help')

        self.root.config(menu=self.menubar)

class Window(ttk.Frame):
    """Abstract base class for a popup window"""
    __metaclass__ = abc.ABCMeta
    def __init__(self, parent):
        ''' Constructor '''
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.resizable(width=False, height=False) # Disallows window resizing
        self.validate_notempty = (self.register(self.notEmpty), '%P') # Creates Tcl wrapper for python function. %P = new contents of field after the edit.
        self.init_gui()

    @abc.abstractmethod # Must be overwriten by subclasses
    def init_gui(self):
        '''Initiates GUI of any popup window'''
        pass

    @abc.abstractmethod
    def do_something(self):
        '''Does something that all popup windows need to do'''
        pass

    def notEmpty(self, P):
        '''Validates Entry fields to ensure they aren't empty'''
        if P.strip():
            valid = True
        else:
            print("Error: Field must not be empty.") # Prints to console
            valid = False
        return valid

    def close_win(self):
        '''Closes window'''
        self.parent.destroy()

class SomethingWindow(Window):
    """ New popup window """
    def do_suvat(self) :
        pass


    def init_gui(self):
        self.parent.title("SUVAT Calculator")
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(4, weight=1)

        # Create Widgets

        self.label_title = ttk.Label(self.parent, text="Enter Values:")
        self.contentframe = ttk.Frame(self.parent, relief="sunken")

        #S
        self.label_S = ttk.Label(self.contentframe, text='Enter S')
        self.input_S = ttk.Entry(self.contentframe, width=30, validate='focusout', validatecommand=(self.validate_notempty))

        #U
        self.label_U = ttk.Label(self.contentframe, text='Enter U')
        self.input_U = ttk.Entry(self.contentframe, width=30, validate='focusout', validatecommand=(self.validate_notempty))

        #V
        self.label_V = ttk.Label(self.contentframe, text='Enter V')
        self.input_V = ttk.Entry(self.contentframe, width=30, validate='focusout', validatecommand=(self.validate_notempty))

        #A
        self.label_A = ttk.Label(self.contentframe, text='Enter A')
        self.input_A = ttk.Entry(self.contentframe, width=30, validate='focusout', validatecommand=(self.validate_notempty))

        #T
        self.label_test = ttk.Label(self.contentframe, text='Enter T')
        self.input_test = ttk.Entry(self.contentframe, width=30, validate='focusout', validatecommand=(self.validate_notempty))


        #input button
        self.btn_input = ttk.Button(self.parent, text="Enter", command=self.do_suvat())

        # Layout
        self.label_title.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.contentframe.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self.label_S.grid(row=0, column=0)
        self.input_S.grid(row=1, column=0, sticky='w')

        self.btn_input.grid(row=2, column=0, sticky='e')
        # Padding
        for child in self.parent.winfo_children():
            child.grid_configure(padx=10, pady=5)
        for child in self.contentframe.winfo_children():
            child.grid_configure(padx=5, pady=2)

    def do_something(self):
        '''Does something'''
        text = self.input_test.get().strip()
        if text:
            # Do things with text
            self.close_win()
        else:
            print("Error: But for real though, field must not be empty.")

class GUI(ttk.Frame):
    """Main GUI class"""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def openwindow(self):
        self.new_win = tkinter.Toplevel(self.root) # Set parent
        SomethingWindow(self.new_win)

    def init_gui(self):
        self.root.title('Test GUI')
        self.root.geometry("600x400")
        self.grid(column=0, row=0, sticky='nsew')
        self.grid_columnconfigure(0, weight=1) # Allows column to stretch upon resizing
        self.grid_rowconfigure(0, weight=1) # Same with row
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.option_add('*tearOff', 'FALSE') # Disables ability to tear menu bar into own window

        # Menu Bar
        self.menubar = Menubar(self.root)

        # Create Widgets
        self.btn = ttk.Button(self, text='Open Window', command=self.openwindow)

        # Layout using grid
        self.btn.grid(row=0, column=0, sticky='ew')

        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=5)



if __name__ == '__main__':
    root = tkinter.Tk()
    GUI(root)
    root.mainloop()
