from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class View_Login:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\Login\frame0")
    def __init__(self):
        self.root = Tk()
        self.root.title("Đăng nhập tài khoản")

        
    def create_controller(self, controller):
        self.controller = controller

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def destroy(self):
        self.root.destroy()
        
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Bạn chắc chắn muốn thoát chương trình ?"):
            self.root.destroy()

    def create_view(self):
        self.root.configure(bg = "#DBD1F7")
        window_height = 720
        window_width = 1280
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, 0))

 
        canvas = Canvas(
            self.root,
            bg = "#DBD1F7",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file= self.relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            610.0,
            355.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file= self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.check_account,
            relief="flat"
        )
        button_1.place(
            x=800.0,
            y=528.0,
            width=402.0,
            height=52.0
        )

        entry_image_1 = PhotoImage(
            file= self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            997.7889709472656,
            469.8666687011719,
            image=entry_image_1
        )
        self.entry_matkhau = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0, show="*"
        )
        self.entry_matkhau.place(
            x=810.0,
            y=443.0,
            width=375.57794189453125,
            height=51.73333740234375
        )

        entry_image_2 = PhotoImage(
            file= self.relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            998.2110290527344,
            352.8666687011719,
            image=entry_image_2
        )
        self.entry_tendangnhap = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_tendangnhap.place(
            x=810.4220581054688,
            y=326.0,
            width=375.57794189453125,
            height=51.73333740234375
        )

        image_image_2 = PhotoImage(
            file= self.relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            329.0,
            349.0,
            image=image_image_2
        )
        self.root.bind('<Return>', self.controller.check_account)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.resizable(False, False)
        self.root.mainloop()