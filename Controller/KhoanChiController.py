from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from View.View_DanhSachDuAn import View_DanhSachDuAn
from View.View_FormKhoanChi import View_FormKhoanChi
from View.View_QuanLyNganSach import View_QuanLyNganSach
from View.View_CapNhatNganSach import View_CapNhatNganSach
from Model.NganSachModel import NganSachModel
from Model.HoSoModel import HoSoModel
from datetime import date

from datetime import datetime
import re

class KhoanChiController:
    maduan = None
    makhoanchi = None
    def __init__(self, model, viewQuanLyNganSach, maduan, loaitaikhoan):
        self.maduan = maduan
        self.loaitaikhoan = loaitaikhoan
        global globalLoaitaikhoan
        globalLoaitaikhoan = loaitaikhoan
        self.model = model
        self.viewQuanLyNganSach = viewQuanLyNganSach
        self.viewQuanLyNganSach.create_controller(self)
        data = self.thong_tin_ngan_sach()
        self.viewQuanLyNganSach.create_view(data[0],data[1],data[2],self.loaitaikhoan)
        
    def display_result(self, result):
        messagebox.showinfo("Thông báo", result)

    def get_selected_item(self):
        selected_item = self.viewQuanLyNganSach.tree.selection()
        if selected_item:
            return selected_item[0]
        return None
    
    def update_treeview(self):
        for item in self.viewQuanLyNganSach.tree.get_children():
            self.viewQuanLyNganSach.tree.delete(item)

        data = self.model.get_data_from_database(self.maduan)
        for item in data:
            sotien = self.format_currency(item[5])
            self.viewQuanLyNganSach.tree.insert("", 0,values=(item[0], item[2], sotien, item[4]))

    def on_select(self, event):
        selected_items = self.viewQuanLyNganSach.tree.selection()
        if selected_items:
            selected_item = selected_items[0]
            values = self.viewQuanLyNganSach.tree.item(selected_item)['values']
            self.makhoanchi = values[0]

    def view_them_chi_tieu_moi(self):
        self.viewQuanLyNganSach.destroy()
        self.viewThemKhoanChi = View_FormKhoanChi()
        self.viewThemKhoanChi.create_controller(self)
        self.viewThemKhoanChi.create_view("themkhoanchi",self.loaitaikhoan)
        
    def view_xem_khoan_chi(self):
        if self.makhoanchi is None:
            self.display_result("Hãy chọn một khoản chi để xem")
            return
        else:
            data = self.get_data()
            self.viewQuanLyNganSach.destroy()
            self.viewThemKhoanChi = View_FormKhoanChi()
            self.viewThemKhoanChi.create_controller(self)
            self.viewThemKhoanChi.create_view("xemkhoanchi",data)

    def view_cap_nhat_ngan_sach(self):
        from Controller.NganSachController import NganSachController
        self.viewQuanLyNganSach.destroy()
        view = View_CapNhatNganSach()
        model = NganSachModel()
        NganSachController(model,view,self.maduan,globalLoaitaikhoan)

    def get_entry_value_them_khoan_chi(self):
        tenkhoanchi = self.viewThemKhoanChi.entry_ten.get()
        sotien = self.viewThemKhoanChi.entry_sotien.get().replace(".", "")
        noidung = self.viewThemKhoanChi.textarea_noidung.get("1.0",'end-1c')
        if tenkhoanchi == "":
            self.display_result("Tên khoản chi không hợp lệ")
            return False
        try:
            int(sotien)
        except ValueError:
            self.display_result("Số tiền không hợp lệ")
            return False
        
        thoigianthuchien  = date.today()
        return [tenkhoanchi, noidung, thoigianthuchien, int(sotien)]
    
    def them_khoan_chi(self):
        input_values = self.get_entry_value_them_khoan_chi()
        if input_values:
            tenkhoanchi, noidung, thoigianthuchien, sotien = input_values
            if int(sotien) > self.ngan_sach_hien_tai:
                self.display_result("Khoản chi này vượt quá ngân sách")
            else:
                self.model.them_khoan_chi(self.maduan, tenkhoanchi, noidung, thoigianthuchien, sotien)
                self.display_result("Thêm khoản chi mới thành công")
                self.clear_khoan_chi()

    def clear_khoan_chi(self):
        self.viewThemKhoanChi.entry_ten.delete(0, END)
        self.viewThemKhoanChi.entry_sotien.delete(0, END)
        self.viewThemKhoanChi.textarea_noidung.delete('1.0', END)

    def get_data(self):
        data = self.model.get_data_from_makhoanchi(self.makhoanchi)
        for item in data:
            tenkhoanchi = item[2]
            noidung = item[3]
            sotien = self.format_currency(item[5])
        data2 = [tenkhoanchi, sotien, noidung]
        return data2

    def xoa_khoan_chi(self):
        if self.makhoanchi is None:
            self.display_result("Hãy chọn một khoản chi để xóa")
            return
        else:
            result = self.model.xoa_khoan_chi(self.makhoanchi)
            if result:
                self.display_result("Xóa khoản chi thành công")
                self.viewQuanLyNganSach.destroy()
                self.viewQuanLyNganSach = View_QuanLyNganSach()
                self.viewQuanLyNganSach.create_controller(self)
                self.thong_tin_ngan_sach()
                self.viewQuanLyNganSach.create_view(self.tong_ngan_sach_VND,self.ngan_sach_hien_tai_VND,self.ngan_sach_da_chi_VND,self.loaitaikhoan)

    def tim_kiem_khoan_chi(self,event):
        search_text = self.viewQuanLyNganSach.entry_timkiem.get()
        for item in self.viewQuanLyNganSach.tree.get_children():
            self.viewQuanLyNganSach.tree.delete(item)
        if search_text:
            for item in self.model.tim_kiem_khoan_chi(search_text,self.maduan):
                sotien = self.format_currency(item[5])
                self.viewQuanLyNganSach.tree.insert("", 0,values=(item[0], item[2], sotien, item[4]))
        else:
            self.update_treeview()

    def quay_lai_quan_ly_ngan_sach(self):
        self.viewThemKhoanChi.destroy()
        self.viewQuanLyNganSach = View_QuanLyNganSach()
        self.viewQuanLyNganSach.create_controller(self)
        self.thong_tin_ngan_sach()
        self.viewQuanLyNganSach.create_view(self.tong_ngan_sach_VND,self.ngan_sach_hien_tai_VND,self.ngan_sach_da_chi_VND,self.loaitaikhoan)

    
    def quay_lai_danh_sach_du_an(self):
        from Controller.HoSoController import HoSoController
        self.viewQuanLyNganSach.destroy()
        view = View_DanhSachDuAn()
        model = HoSoModel()
        HoSoController(model,view,globalLoaitaikhoan)

    def thong_tin_ngan_sach(self):
        self.tong_ngan_sach = self.model.get_tong_ngan_sach(self.maduan)
        self.ngan_sach_da_chi = self.model.get_ngan_sach_da_chi(self.maduan)
        self.ngan_sach_hien_tai = self.tong_ngan_sach - self.ngan_sach_da_chi
        self.tong_ngan_sach_VND = self.format_currency(self.tong_ngan_sach)
        self.ngan_sach_da_chi_VND = self.format_currency(self.ngan_sach_da_chi)
        self.ngan_sach_hien_tai_VND = self.format_currency(self.ngan_sach_hien_tai)
        return [self.tong_ngan_sach_VND,self.ngan_sach_hien_tai_VND,self.ngan_sach_da_chi_VND]

    def format_currency(self,number):
        number_str = str(number)
        decimal_part = ""
        
        if "." in number_str:
            number_str, decimal_part = number_str.split(".")
        
        formatted_number = ""
        while len(number_str) > 3:
            formatted_number = "." + number_str[-3:] + formatted_number
            number_str = number_str[:-3]
        
        formatted_number = number_str + formatted_number
        if decimal_part:
            formatted_number += "." + decimal_part
        
        return formatted_number + " VND"
