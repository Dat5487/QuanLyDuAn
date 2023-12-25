from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

class View_DanhSachDuAn:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\DanhSachDuAn\frame0")
    def __init__(self):
        self.root = Tk()
        self.root.title("Danh sách dự án")

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

        self.tree["columns"] = ("maduan", "tenduan","ngaybatdau","dukienhoanthanh")
        self.tree.column("maduan",width=0, stretch="no")
        self.tree.column("tenduan", width=425)
        self.tree.column("ngaybatdau", width=200)
        self.tree.column("dukienhoanthanh", width=200)
        self.tree.heading("tenduan", text="Tên dự án", anchor=CENTER)
        self.tree.heading("ngaybatdau", text="Ngày bắt đầu", anchor=CENTER)
        self.tree.heading("dukienhoanthanh", text="Thời gian hoàn thành", anchor=CENTER)

        self.tree.bind('<<TreeviewSelect>>', self.controller.on_select)
        self.tree['show'] = 'headings'
        self.tree.place(x=100,y=250,height=420)
        self.controller.update_treeview()

    def create_view(self,loaitaikhoan):
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

        image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            1103.0,
            165.0,
            image=image_image_3
        )

        button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        button_tiendo = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.view_quan_ly_tien_do,
            relief="flat"
        )
        button_tiendo.place(
            x=1021.0,
            y=368.0,
            width=177.0,
            height=45.0
        )

        button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        button_chitieu = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command = self.controller.view_quan_ly_chi_tieu,
            relief="flat"
        )
        button_chitieu.place(
            x=1021.0,
            y=304.0,
            width=181.0,
            height=47.0
        )

        button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        button_quanly = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.view_quan_ly_ho_so,
            relief="flat"
        )
        button_quanly.place(
            x=1021.0,
            y=239.0,
            width=177.0,
            height=48.0
        )

        button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        button_themduan = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.view_them_du_an_moi,
            relief="flat"
        )
        button_themduan.place(
            x=1021.0,
            y=143.0,
            width=177.0,
            height=48.0
        )
        button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.dang_xuat,
            relief="flat"
        )
        button_6.place(
            x=1021.0,
            y=590.0,
            width=177.0,
            height=45.0
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
            518.0,
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
            width=526.0,
            height=42.0
        )

        image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            515.0,
            76.0,
            image=image_image_5
        )
        button_quanly.configure(background="#FFFFFF")
        button_chitieu.configure(background="#FFFFFF")
        button_tiendo.configure(background="#FFFFFF")
        self.entry_timkiem.configure(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0
        )
        if loaitaikhoan == "Người xem":
            button_themduan.configure(state="disabled")
        self.entry_timkiem.bind('<KeyRelease>', self.controller.tim_kiem_du_an)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.resizable(False, False)
        self.root.mainloop()
