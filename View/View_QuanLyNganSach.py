from pathlib import Path
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox

class View_QuanLyNganSach:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\QuanLyNganSach\frame0")

    def __init__(self):
        self.root = Tk()
        self.root.title("Quản lý ngân sách")

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def destroy(self):
        self.root.update()
        self.root.destroy()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Bạn chắc chắn muốn thoát chương trình ?"):
            self.root.destroy()

    def create_controller(self, controller):
        self.controller = controller

    def create_treeview(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('robota', 12)) # Modify the font of the body
        style.configure("Treeview.Heading", background="#3B71CA", foreground="white", font=('robota', 14))
        style.map("Treeview",background=[("selected","#9FA6B2")])
        style.map("Treeview.Heading",background=[("selected","#3B71CA")],foreground=[("selected","#white")])
        self.tree = ttk.Treeview(self.root)
        
        self.tree["columns"] = ("makhoanchi", "tenkhoanchi","sotien","thoigianthuchien")
        self.tree.column("makhoanchi",width=0, stretch="no")
        self.tree.column("tenkhoanchi", width=400)
        self.tree.column("sotien", width=180)
        self.tree.column("thoigianthuchien", width=200)
        self.tree.heading("tenkhoanchi", text="Tên khoản chi", anchor=CENTER)
        self.tree.heading("sotien", text="Số tiền", anchor=CENTER)
        self.tree.heading("thoigianthuchien", text="Thời gian thực hiện", anchor=CENTER)

        self.tree.bind('<<TreeviewSelect>>', self.controller.on_select)
        self.tree['show'] = 'headings'
        self.tree.place(x=100,y=360,height=320)
        self.controller.update_treeview()

    def create_view(self, tong_ngan_sach=0, ngan_sach_hien_tai=0 ,ngan_sach_da_chi=0,loaitaikhoan = None):

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
            1066.0,
            468.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_quaylai = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.quay_lai_danh_sach_du_an,
            relief="flat"
        )
        self.button_quaylai.place(
            x=978.0,
            y=543.0,
            width=177.0,
            height=45.0
        )

        button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_them = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.view_them_chi_tieu_moi,
            relief="flat"
        )
        self.button_them.place(
            x=978.0,
            y=338.0,
            width=177.0,
            height=48.0
        )

        button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_thayDoiNganSach = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.view_cap_nhat_ngan_sach,
            relief="flat"
        )
        self.button_thayDoiNganSach.place(
            x=978.0,
            y=468.0,
            width=177.0,
            height=56.0
        )

        button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.button_xoa = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.xoa_khoan_chi,
            relief="flat"
        )
        self.button_xoa.place(
            x=978.0,
            y=404.0,
            width=177.0,
            height=45.0
        )

        image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            489.0,
            468.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            627.0,
            169.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            259.0,
            169.0,
            image=image_image_5
        )

        image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(
            994.0,
            169.0,
            image=image_image_6
        )

        image_image_7 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        image_7 = canvas.create_image(
            639.0,
            72.0,
            image=image_image_7
        )

        self.custom_font = font.Font(family="Roboto", size=20, weight="bold")
        self.tongNganSach = Label(self.root, text=tong_ngan_sach,background="#E2C21A",fg="#F5F5F5",font=self.custom_font)
        self.tongNganSach.place(x=103,y=159)
        self.nganSachHienTai = Label(self.root, text=ngan_sach_hien_tai,background="#18DF50",fg="#F5F5F5",font=self.custom_font)
        self.nganSachHienTai.place(x=480,y=159)
        self.nganSachDaChi = Label(self.root, text=ngan_sach_da_chi,background="#DBAAAA",fg="#F5F5F5",font=self.custom_font)
        self.nganSachDaChi.place(x=840,y=159)

        button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        self.button_xem = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.view_xem_khoan_chi,
            relief="flat"
        )
        self.button_xem.place(
            x=978.0,
            y=278.0,
            width=177.0,
            height=48.0
        )
        entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            482.0,
            318.0,
            image=entry_image_1
        )
        self.entry_timkiem = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_timkiem.place(
            x=203.0,
            y=298.0,
            width=558.0,
            height=38.0
        )
        
        self.entry_timkiem.configure(bd=0,bg="#F4F4F4",fg="#000716",highlightthickness=0)
        self.button_quaylai.configure(background="#F5F5F5")
        self.button_xem.configure(background="#F5F5F5")
        self.tongNganSach.configure(background="#E2C21A",fg="#F5F5F5")
        self.nganSachHienTai.configure(background="#18DF50",fg="#F5F5F5")
        self.nganSachDaChi.configure(background="#DBAAAA",fg="#F5F5F5")
        if loaitaikhoan == "Người xem":
            self.button_them.configure(state="disabled")
            self.button_thayDoiNganSach.configure(state="disabled")
            self.button_xoa.configure(state="disabled")

        self.entry_timkiem.bind('<KeyRelease>', self.controller.tim_kiem_khoan_chi)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.resizable(False, False)
        self.root.mainloop()