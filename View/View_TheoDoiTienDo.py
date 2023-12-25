from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

class View_TheoDoiTienDo:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\TheoDoiTienDo\frame0")
    def __init__(self):
        self.root = Tk()
        self.root.title("Theo dõi tiến độ")

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def create_controller(self, controller):
        self.controller = controller

    def destroy(self):
        self.root.update()
        self.root.destroy()
        
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Bạn chắc chắn muốn thoát chương trình ?"):
            self.root.destroy()
            
    def create_treeview(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('robota', 12)) # Modify the font of the body
        style.configure("Treeview.Heading", background="#3B71CA", foreground="white", font=('robota', 14))
        style.map("Treeview",background=[("selected","#9FA6B2")])
        style.map("Treeview.Heading",background=[("selected","#3B71CA")],foreground=[("selected","#white")])
        self.tree = ttk.Treeview(self.root)

        self.tree["columns"] = ("macongviec", "tencongviec","tiendotong","tiendohientai")
        self.tree.column("macongviec",width=0, stretch="no")
        self.tree.column("tencongviec", width=425)
        self.tree.column("tiendotong", width=200)
        self.tree.column("tiendohientai", width=200)
        self.tree.heading("tencongviec", text="Tên công việc", anchor=CENTER)
        self.tree.heading("tiendotong", text="Tiến độ tổng", anchor=CENTER)
        self.tree.heading("tiendohientai", text="Tiến độ hiện tại", anchor=CENTER)

        self.tree.bind('<<TreeviewSelect>>', self.controller.on_select)
        self.tree['show'] = 'headings'
        self.tree.place(x=100,y=250,height=420)
        self.controller.update_treeview()

    def create_view(self,loaitaikhoan = None):
        self.root.configure(bg = "#FFFFFF")
        window_height = 720
        window_width = 1280
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, 0))
        
        
        canvas = Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        self.create_treeview()
        image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            638.0,
            361.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            1103.0,
            401.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        button_quaylai = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.quay_lai_danh_sach_du_an,
            relief="flat"
        )
        button_quaylai.place(
            x=1021.0,
            y=388.0,
            width=177.0,
            height=45.0
        )

        image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            1103.0,
            165.0,
            image=image_image_3
        )

        button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        button_sodo = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.xay_dung_so_do,
            relief="flat"
        )
        button_sodo.place(
            x=1021.0,
            y=324.0,
            width=177.4276123046875,
            height=47.00007629394531
        )

        button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        button_xem = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.view_xem_cong_viec,
            relief="flat"
        )
        button_xem.place(
            x=1021.0,
            y=259.0,
            width=177.0,
            height=47.99998474121094
        )

        button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        button_them = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.view_them_cong_viec_moi,
            relief="flat"
        )
        button_them.place(
            x=1021.0,
            y=143.0,
            width=177.0,
            height=48.0
        )

        image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            515.0,
            466.0,
            image=image_image_4
        )

        entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            520.5,
            180.0,
            image=entry_image_1
        )
        self.entry_timkiem = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_timkiem.place(
            x=255.0,
            y=158.0,
            width=531.0,
            height=42.0
        )

        image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            515.0,
            76.0,
            image=image_image_5
        )
        if loaitaikhoan=="Người xem":
            button_them.configure(state="disabled")

        self.entry_timkiem.bind('<KeyRelease>', self.controller.tim_kiem_cong_viec)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.resizable(False, False)
        self.root.mainloop()
