from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from View.View_DanhSachDuAn import View_DanhSachDuAn
from View.View_FormHoSoDuAn import View_FormHoSoDuAn
from View.View_QuanLyNganSach import View_QuanLyNganSach
from View.View_Login import View_Login

from Model.KhoanChiModel import KhoanChiModel
from Model.CongViecModel import CongViecModel
from Model.TaiKhoanModel import TaiKhoanModel

from Controller.KhoanChiController import KhoanChiController
from Controller.CongViecController import CongViecController
from View.View_TheoDoiTienDo import View_TheoDoiTienDo

from datetime import datetime
import re

class HoSoController:
    maduan = None
    loaitaikhoan = None
    def __init__(self, model, viewDanhSachDuAn, loaitaikhoan):
        self.loaitaikhoan = loaitaikhoan
        global globalLoaitaikhoan
        globalLoaitaikhoan = loaitaikhoan
        self.model = model
        self.viewDanhSachDuAn = viewDanhSachDuAn
        self.viewDanhSachDuAn.create_controller(self)
        self.viewDanhSachDuAn.create_view(loaitaikhoan)
        

    def display_result(self, result):
        messagebox.showinfo("Thông báo", result)
    
    def get_data(self):
        data = self.model.get_data_from_maduan(self.maduan)
        for item in data:
            maduan = item[0]
            tenduan = item[1]
            vitri = item[2]
            date_object = datetime.strptime(item[3], "%Y-%m-%d")
            ngaybatdau = date_object.strftime("%d/%m/%Y")
            date_object = datetime.strptime(item[4], "%Y-%m-%d")
            dukienhoanthanh = date_object.strftime("%d/%m/%Y")
            mota = item[5]
            tailieu = item[6]
        data2 = [maduan, tenduan, vitri, ngaybatdau, dukienhoanthanh, mota, tailieu]
        return data2

    def get_selected_item(self):
        selected_item = self.viewDanhSachDuAn.tree.selection()
        if selected_item:
            return selected_item[0]
        return None
    
    def update_treeview(self):
        for item in self.viewDanhSachDuAn.tree.get_children():
            self.viewDanhSachDuAn.tree.delete(item)

        data = self.model.get_data_from_database()
        for item in data:
            self.viewDanhSachDuAn.tree.insert("", 0,values=(item[0], item[1], item[3], item[4]))

    def on_select(self, event):
        selected_items = self.viewDanhSachDuAn.tree.selection()
        if selected_items:
            selected_item = selected_items[0]
            values = self.viewDanhSachDuAn.tree.item(selected_item)['values']
            self.maduan = values[0]
            global globalMaduan
            globalMaduan = values[0]

    def get_entry_value(self):
        tenduan = self.viewHoSoDuAn.textarea_ten.get("1.0",'end-1c')
        vitri = self.viewHoSoDuAn.textarea_vitri.get("1.0",'end-1c')
        mota = self.viewHoSoDuAn.textarea_mota.get("1.0",'end-1c')
        ngaybatdau = self.viewHoSoDuAn.entry_ngaybatdau.get()
        if tenduan == "":
            self.display_result("Tên dự án không hợp lệ")
            return False
        if vitri == "":
            self.display_result("Vị trí dự án không hợp lệ")
            return False
        if re.match(r"\d{2}/\d{2}/\d{4}", ngaybatdau):
            date_object = datetime.strptime(self.viewHoSoDuAn.entry_ngaybatdau.get(), "%d/%m/%Y")
            ngaybatdau = date_object.strftime("%Y%m%d")
        else:
            self.display_result("Thời gian bắt đầu không hợp lệ")
            return False

        ngayhoanthanh = self.viewHoSoDuAn.entry_ngayhoanthanh.get()
        if re.match(r"\d{2}/\d{2}/\d{4}", ngayhoanthanh):
            date_object = datetime.strptime(self.viewHoSoDuAn.entry_ngayhoanthanh.get(), "%d/%m/%Y")
            ngayhoanthanh = date_object.strftime("%Y%m%d")
        else:
            self.display_result("Thời gian hoàn thành không hợp lệ")
            return False

        tentep = self.viewHoSoDuAn.filename_label.cget("text")
        if not tenduan:
            return "Chưa nhập tên dự án"
        if not vitri:
            return "Chưa nhập vị trí"
        return [tenduan, vitri, ngaybatdau, ngayhoanthanh, mota, tentep]

    def view_them_du_an_moi(self):
        self.viewDanhSachDuAn.destroy()
        self.viewHoSoDuAn = View_FormHoSoDuAn()
        self.viewHoSoDuAn.create_controller(self)
        self.viewHoSoDuAn.create_view("themhoso",self.loaitaikhoan)

    def view_quan_ly_tien_do(self):
        if self.maduan is None:
            self.display_result("Hãy chọn một dự án để quản lý")
            return
        else:
            self.viewDanhSachDuAn.destroy()
            view = View_TheoDoiTienDo()
            model = CongViecModel()
            CongViecController(model,view,globalMaduan,globalLoaitaikhoan)

    def view_quan_ly_ho_so(self):
        if self.maduan is None:
            self.display_result("Hãy chọn một dự án để quản lý")
            return
        else:
            data = self.get_data()
            self.viewDanhSachDuAn.destroy()
            self.viewHoSoDuAn = View_FormHoSoDuAn()
            self.viewHoSoDuAn.create_controller(self)
            self.viewHoSoDuAn.create_view("quanlyhoso",self.loaitaikhoan,data)

    def view_quan_ly_chi_tieu(self):
        if self.maduan is None:
            self.display_result("Hãy chọn một dự án để quản lý")
            return
        else:
            self.viewDanhSachDuAn.destroy()
            model = KhoanChiModel()
            view = View_QuanLyNganSach()
            KhoanChiController(model, view, globalMaduan,globalLoaitaikhoan)
            

        
    def them_ho_so(self):
        input_values = self.get_entry_value()
        if input_values:
            tenduan, vitri, ngaybatdau, ngayhoanthanh, mota, tentep = input_values
            result = self.model.them_ho_so(tenduan, vitri, ngaybatdau, ngayhoanthanh, mota, tentep)
            self.display_result("Thêm hồ sơ mới thành công")
            self.clear()

    def quay_lai_danh_sach(self):
        self.viewHoSoDuAn.destroy()
        view = View_DanhSachDuAn()
        HoSoController(self.model, view ,globalLoaitaikhoan)

    def view_sua_ho_so(self):
        data = self.get_data()
        self.viewHoSoDuAn.destroy()
        self.viewHoSoDuAn = View_FormHoSoDuAn()
        self.viewHoSoDuAn.create_controller(self)
        self.viewHoSoDuAn.create_view("suahoso",self.loaitaikhoan,data)

    def sua_ho_so(self, maduan):
        input_values = self.get_entry_value()
        tenduan, vitri, ngaybatdau, ngayhoanthanh, mota, tentep = input_values
        result = self.model.sua_ho_so(maduan, tenduan, vitri, ngaybatdau, ngayhoanthanh, mota, tentep)
        self.display_result("Sửa hồ sơ thành công")
        self.thoat_sua_ho_so()

    def xoa_ho_so(self):
        result = self.model.xoa_ho_so(self.maduan)
        if result:
            self.display_result("Xóa hồ sơ thành công")
            self.quay_lai_danh_sach()

    def thoat_sua_ho_so(self):
        data = self.get_data()
        self.viewHoSoDuAn.destroy()
        self.viewHoSoDuAn = View_FormHoSoDuAn()
        self.viewHoSoDuAn.create_controller(self)
        self.viewHoSoDuAn.create_view("quanlyhoso",self.loaitaikhoan,data)

    def tim_kiem_du_an(self,event):
        search_text = self.viewDanhSachDuAn.entry_timkiem.get()
        for item in self.viewDanhSachDuAn.tree.get_children():
            self.viewDanhSachDuAn.tree.delete(item)
        if search_text:
            for item in self.model.tim_kiem_ho_so(search_text):
                self.viewDanhSachDuAn.tree.insert("", 0, values=(item[0], item[1], item[3], item[4]))
        else:
            self.update_treeview()

    def clear(self):
        self.viewHoSoDuAn.textarea_ten.delete('1.0', END)
        self.viewHoSoDuAn.textarea_vitri.delete('1.0', END)
        self.viewHoSoDuAn.textarea_mota.delete('1.0', END)
        self.viewHoSoDuAn.entry_ngaybatdau.delete(0, END)
        self.viewHoSoDuAn.entry_ngayhoanthanh.delete(0, END)
        self.viewHoSoDuAn.filename_label.config(text = "")

    def dang_xuat(self):
        confirm = messagebox.askyesno(title="Xác nhận", message="Bạn có chắc chắn muốn đăng xuất không?")
        if confirm:
            from Controller.TaiKhoanController import TaiKhoanController
            self.viewDanhSachDuAn.destroy()
            view =  View_Login()
            model = TaiKhoanModel()
            TaiKhoanController(model,view)

