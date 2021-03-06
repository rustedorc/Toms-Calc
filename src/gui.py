import tkinter
from tkinter import ttk
import abc
from Suvat import SUVAT
import webbrowser
import time
from threading import Thread

questions = None
S_var = None
U_var = None
V_var = None
A_var = None
T_var = None

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

class SuvatWindow(Window):
    """ New popup window """
    def button_press(self) :
        self.S_temp = self.input_S.get()
        self.U_temp = self.input_U.get()
        self.V_temp = self.input_V.get()
        self.A_temp = self.input_A.get()
        self.T_temp = self.input_T.get()

        self.temp_dic = {
        'S' : self.S_temp,
        'U' : self.U_temp,
        'V' : self.V_temp,
        'A' : self.A_temp,
        'T' : self.T_temp,
        }

        key_copy = tuple(self.temp_dic.keys())
        for k in key_copy :
            try:
                self.temp_dic[k] = float(self.temp_dic[k])
            except ValueError :
                self.temp_dic[k] = None

        num_S = self.temp_dic.get("S")
        num_U = self.temp_dic.get("U")
        num_V = self.temp_dic.get("V")
        num_A = self.temp_dic.get("A")
        num_T = self.temp_dic.get("T")
        global questions
        questions = SUVAT(S=num_S,U=num_U,V=num_V,A=num_A,T=num_T)
        questions.Find()

        global S_var
        S_var = questions.S

        global U_var
        U_var = questions.U

        global V_var
        V_var = questions.V

        global A_var
        A_var = questions.A

        global T_var
        T_var = questions.T

        self.input_S.destroy()
        self.input_U.destroy()
        self.input_V.destroy()
        self.input_A.destroy()
        self.input_T.destroy()
        self.label_S.destroy()
        self.label_U.destroy()
        self.label_V.destroy()
        self.label_A.destroy()
        self.label_T.destroy()

        self.label_title = ttk.Label(self.parent, text="SUVAT Values:")

        self.input_S = ttk.Label(self.contentframe, text=f"S is: {round(S_var,2)}") #validatecommand=(self.validate_notempty)
        self.input_U = ttk.Label(self.contentframe, text=f"U is: {round(U_var,2)}")
        self.input_V = ttk.Label(self.contentframe, text=f"V is: {round(V_var,2)}")
        self.input_A = ttk.Label(self.contentframe, text=f"A is: {round(A_var,2)}")
        self.input_T = ttk.Label(self.contentframe, text=f"T is: {round(T_var,2)}")
        self.input_S.grid(row=1, column=0, sticky='w')
        self.input_U.grid(row=3, column=0, sticky='w')
        self.input_V.grid(row=5, column=0, sticky='w')
        self.input_A.grid(row=7, column=0, sticky='w')
        self.input_T.grid(row=9, column=0, sticky='w')

        self.label_title.grid(row=0, column=0, columnspan=2, sticky='nsew')

        for child in self.parent.winfo_children():
            child.grid_configure(padx=10, pady=5)
        for child in self.contentframe.winfo_children():
            child.grid_configure(padx=5, pady=2)

        self.btn_input.destroy()
        self.btn_input = ttk.Button(self, text='Close', command=self.close)
        self.btn_input.grid(row=2, column=0, sticky='e')

    def close(self) :
        self.parent.quit()

    def init_gui(self):
        self.parent.title("SUVAT Calculator")
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(4, weight=1)
        self.parent.geometry("300x400")

        # Create Widgets

        self.label_title = ttk.Label(self.parent, text="Enter Values:")
        self.contentframe = ttk.Frame(self.parent, relief="sunken")

        #S
        self.S_var = tkinter.StringVar()
        self.label_S = ttk.Label(self.contentframe, text='Enter S')
        self.input_S = ttk.Entry(self.contentframe, width=30, validate='focusout', textvariable=self.S_var) #validatecommand=(self.validate_notempty)

        #U
        self.U_var = tkinter.StringVar()
        self.label_U = ttk.Label(self.contentframe, text='Enter U')
        self.input_U = ttk.Entry(self.contentframe, width=30, validate='focusout',textvariable=self.U_var) #validatecommand=(self.validate_notempty)

        #V
        self.V_var = tkinter.StringVar()
        self.label_V = ttk.Label(self.contentframe, text='Enter V')
        self.input_V = ttk.Entry(self.contentframe, width=30, validate='focusout',textvariable=self.V_var) #validatecommand=(self.validate_notempty)

        #A
        self.A_var = tkinter.StringVar()
        self.label_A = ttk.Label(self.contentframe, text='Enter A')
        self.input_A = ttk.Entry(self.contentframe, width=30, validate='focusout',textvariable=self.A_var) #validatecommand=(self.validate_notempty)

        #T
        self.T_var = tkinter.StringVar()
        self.label_T = ttk.Label(self.contentframe, text='Enter T')
        self.input_T = ttk.Entry(self.contentframe, width=30, validate='focusout',textvariable=self.T_var) #validatecommand=(self.validate_notempty)


        #input button
        self.btn_input = ttk.Button(self.parent, text="Enter", command=self.button_press)

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

class GUI(ttk.Frame):
    """Main GUI class"""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
        self.instance = kwargs.get("instance")


    def openwindow(self):
        self.new_win = tkinter.Toplevel(self.root) # Set parent
        SuvatWindow(self.new_win)

    def init_gui(self):

        self.root.title('Toms Calculator')
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
        self.btn = ttk.Button(self, text='SUVAT Calc', command=self.openwindow)
        # Layout using grid
        self.btn.grid(row=0, column=0, sticky='ew')
        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=5)
