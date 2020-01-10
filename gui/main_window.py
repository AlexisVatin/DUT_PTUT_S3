import tkinter as tk
from logic.bot import Bot


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = 'Bot'

        # List name
        self.name_list = tk.Listbox()
        self.name_list.insert(1, 'Test')

        # Start Bot
        self.btn_run_bot = tk.Button(self, text="Run bot", command=self.run_bot)

        # Add / Delete name
        self.frame_btn = tk.Frame(self)
        self.btn_add_name = tk.Button(self.frame_btn, text="Add name", command=self.add_name_to_list)
        self.btn_remove_name = tk.Button(self.frame_btn, text="Delete selected name", command=self.remove_name_from_list)


        self.frame_name = tk.Frame(self)
        self.label_name = tk.Label(self.frame_name, text="Name of influencer")
        self.input_name = tk.Entry(self.frame_name, text="Get")

        # Input num loop
        self.frame_num_loop = tk.Frame(self)
        self.label_num_loop = tk.Label(self.frame_num_loop, text="Number of Loop")
        self.input_num_loop = tk.Spinbox(self.frame_num_loop, from_=1, to=10)

        # Close
        self.btn_quit = tk.Button(self, text="Quit", command=self.destroy)

        # Place element on main window
        self.btn_run_bot.pack()
        self.name_list.pack()

        self.btn_add_name.grid(row=0, column=0)
        self.btn_remove_name.grid(row=0, column=1)
        self.frame_btn.pack()

        self.label_name.grid(row=0, column=0)
        self.input_name.grid(row=0, column=1)
        self.frame_name.pack()

        self.label_num_loop.grid(row=0, column=0)
        self.input_num_loop.grid(row=0, column=1)
        self.frame_num_loop.pack()

        self.btn_quit.pack()


    def add_name_to_list(self):
        if self.input_name.get():
            self.name_list.insert(0, self.input_name.get())

    def remove_name_from_list(self):
        selected = self.name_list.curselection()
        for index in reversed(selected):
            self.name_list.delete(index)

    def run_bot(self):
        list_name = reversed(self.name_list.get(0, self.name_list.size()))
        bot = Bot(list_name, "drivers\chromedriver.exe")
        bot.execute()
 
