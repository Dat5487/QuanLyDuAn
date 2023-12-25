from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from View.View_DanhSachDuAn import View_DanhSachDuAn
from Model.HoSoModel import HoSoModel

from View.View_FormCongViec import View_FormCongViec
from View.View_TheoDoiTienDo import View_TheoDoiTienDo
import pandas as pd
import plotly.figure_factory as ff
import numpy as np


class CongViecController:
    macongviec = None
    maduan = None
    def __init__(self, model, viewDanhSachCongViec, maduan, loaitaikhoan):
        self.maduan = maduan
        self.loaitaikhoan = loaitaikhoan
        global globalLoaitaikhoan
        globalLoaitaikhoan = loaitaikhoan
        self.model = model
        self.viewDanhSachCongViec = viewDanhSachCongViec
        self.viewDanhSachCongViec.create_controller(self)
        self.viewDanhSachCongViec.create_view(loaitaikhoan)
        
        
    def display_result(self, result):
        messagebox.showinfo("Thông báo", result)
    
    def get_data(self):
        data = self.model.get_data_from_macongviec(self.macongviec)
        for item in data:
            macongviec = item[0]
            maduan = item[1]
            tencongviec = item[2]
            tiendotong = item[3]
            tiendohientai = item[4]
            mota = item[5]
            chitiet = item[6]
        data2 = [tencongviec, tiendotong, tiendohientai, mota, chitiet]
        return data2

    def get_selected_item(self):
        selected_item = self.viewDanhSachCongViec.tree.selection()
        if selected_item:
            return selected_item[0]
        return None
    
    def update_treeview(self):
        for item in self.viewDanhSachCongViec.tree.get_children():
            self.viewDanhSachCongViec.tree.delete(item)
        data = self.model.get_data_from_maduan(self.maduan)
        for item in data:
            self.viewDanhSachCongViec.tree.insert("", 0,values=(item[0], item[2], str(item[3]) + "%", str(item[4]) + "%", item[5], item[6]))

    def on_select(self, event):
        selected_items = self.viewDanhSachCongViec.tree.selection()
        if selected_items:
            selected_item = selected_items[0]
            values = self.viewDanhSachCongViec.tree.item(selected_item)['values']
            self.macongviec = values[0]

    def get_entry_value(self):
        tencongviec = self.viewFormCongViec.entry_tencongviec.get()
        tiendotong = self.viewFormCongViec.entry_tiendotong.get()
        tiendohientai = self.viewFormCongViec.entry_tiendohientai.get()
        mota = self.viewFormCongViec.textarea_mota.get("1.0",'end-1c')
        chitiet = self.viewFormCongViec.textarea_chitiet.get("1.0",'end-1c')
        tongtatcatiendo = self.model.get_tong_tien_do(self.maduan)
        if int(tongtatcatiendo) + int(tiendotong) > 100:
            self.display_result("Tổng tất cả tiến độ không được quá 100%")
            return False
        if tencongviec == "":
            self.display_result("Tên công việc không hợp lệ")
            return False
        if tiendotong == "":
            self.display_result("Tiến độ tổng không hợp lệ")
            return False
        if tiendohientai == "":
            tiendohientai = 0
        if int(tiendotong) < int(tiendohientai):
            self.display_result("Tiến độ tổng không thể nhỏ hơn tiến độ hiện tại")
            return False
        return [tencongviec, tiendotong, tiendohientai, mota, chitiet]

    def get_entry_value_suacongviec(self):
        tencongviec = self.viewFormCongViec.entry_tencongviec.get()
        tiendotong = self.viewFormCongViec.entry_tiendotong.get()
        tiendohientai = self.viewFormCongViec.entry_tiendohientai.get()
        mota = self.viewFormCongViec.textarea_mota.get("1.0",'end-1c')
        chitiet = self.viewFormCongViec.textarea_chitiet.get("1.0",'end-1c')
        tongtatcatiendo = self.model.get_tong_tien_do(self.maduan)
        tiendotongcu = self.model.get_tong_tien_do_cu(self.macongviec)
        if int(tongtatcatiendo) + int(tiendotong) - int(tiendotongcu) > 100:
            self.display_result("Tổng tất cả tiến độ không được quá 100%")
            return False
        if tencongviec == "":
            self.display_result("Tên công việc không hợp lệ")
            return False
        if tiendotong == "":
            self.display_result("Tiến độ tổng không hợp lệ")
            return False
        if tiendohientai == "":
            tiendohientai = 0
        if int(tiendotong) < int(tiendohientai):
            self.display_result("Tiến độ tổng không thể nhỏ hơn tiến độ hiện tại")
            return False
        return [tencongviec, tiendotong, tiendohientai, mota, chitiet]
    
    def view_them_cong_viec_moi(self):
        self.viewDanhSachCongViec.destroy()
        self.viewFormCongViec = View_FormCongViec()
        self.viewFormCongViec.create_controller(self)
        self.viewFormCongViec.create_view("themcongviec")

    def view_xem_cong_viec(self):
        if self.macongviec is None:
            self.display_result("Hãy chọn một công việc để quản lý")
            return
        else:
            data = self.get_data()
            self.viewDanhSachCongViec.destroy()
            self.viewFormCongViec = View_FormCongViec()
            self.viewFormCongViec.create_controller(self)
            self.viewFormCongViec.create_view("xemcongviec",data,self.loaitaikhoan)
            
        
    def them_cong_viec(self):
        input_values = self.get_entry_value()
        if input_values:
            tencongviec, tiendotong, tiendohientai, mota, chitiettiendo = input_values
            result = self.model.them_cong_viec(self.maduan, tencongviec, tiendotong, tiendohientai, mota, chitiettiendo)
            self.display_result("Thêm công việc mới thành công")
            self.clear()

    def view_sua_cong_viec(self):
        data = self.get_data()
        self.viewFormCongViec.destroy()
        self.viewFormCongViec = View_FormCongViec()
        self.viewFormCongViec.create_controller(self)
        self.viewFormCongViec.create_view("suacongviec",data)

    def sua_cong_viec(self):
        input_values = self.get_entry_value_suacongviec()
        if input_values:
            tencongviec, tiendotong, tiendohientai, mota, chitiettiendo = input_values
            result = self.model.sua_cong_viec(self.macongviec, tencongviec, tiendotong, tiendohientai, mota, chitiettiendo)
            self.display_result("Sửa công việc thành công")
            self.quay_lai_xem_cong_viec()

    def quay_lai_danh_sach_du_an(self):
        from Controller.HoSoController import HoSoController
        self.viewDanhSachCongViec.destroy()
        view =  View_DanhSachDuAn()
        model = HoSoModel()
        HoSoController(model,view,globalLoaitaikhoan)

    def quay_lai_theo_doi_tien_do(self):
        self.viewFormCongViec.destroy()
        self.viewDanhSachCongViec = View_TheoDoiTienDo()
        self.viewDanhSachCongViec.create_controller(self)
        self.viewDanhSachCongViec.create_view(self.loaitaikhoan)

    def quay_lai_xem_cong_viec(self):
        data = self.get_data()
        self.viewFormCongViec.destroy()
        self.viewFormCongViec = View_FormCongViec()
        self.viewFormCongViec.create_controller(self)
        self.viewFormCongViec.create_view("xemcongviec", data, self.loaitaikhoan)

    def xoa_cong_viec(self):
        result = self.model.xoa_cong_viec(self.macongviec)
        if result:
            self.display_result("Xóa công việc thành công")
            self.quay_lai_theo_doi_tien_do()

    def tim_kiem_cong_viec(self,event):
        search_text = self.viewDanhSachCongViec.entry_timkiem.get()
        for item in self.viewDanhSachCongViec.tree.get_children():
            self.viewDanhSachCongViec.tree.delete(item)
        if search_text:
            for item in self.model.tim_kiem_cong_viec(search_text,self.maduan):
                self.viewDanhSachCongViec.tree.insert("", 0,values=(item[0], item[2], str(item[3]) + "%", str(item[4]) + "%", item[5], item[6]))
        else:
            self.update_treeview()

    def clear(self):
        self.viewFormCongViec.entry_tencongviec.delete(0, END)
        self.viewFormCongViec.entry_tiendotong.delete(0, END)
        self.viewFormCongViec.entry_tiendohientai.delete(0, END)
        self.viewFormCongViec.textarea_mota.delete('1.0', END)
        self.viewFormCongViec.textarea_chitiet.delete('1.0', END)
        
    def xay_dung_so_do(self):
        data = self.model.get_data_from_maduan(self.maduan)
        if data == []:
            self.display_result("Chưa có dữ liệu để tạo sơ đồ")
            return False
        data = np.array(data)
        array = data[:, 2:-2] 
        first = True
        ketqua = []
        for congviec in array:
            if first:
                batdau = 0
                dukienketthuc = int(congviec[1])
                thucteketthuc = int(congviec[2])
                first = False
            else:
                batdau = dukienketthuc
                dukienketthuc = batdau + int(congviec[1])
                thucteketthuc = batdau + int(congviec[2])
            ketqua.append(dict(Task=congviec[0], Start=batdau, Finish=dukienketthuc, State="Dự kiến"))
            ketqua.append(dict(Task=congviec[0], Start=batdau, Finish=thucteketthuc, State="Thực tế"))

        ketqua.append(dict(Task="Tổng", Start=0, Finish=100, State="Tổng"))
        df = pd.DataFrame(ketqua)
        fig = ff.create_gantt(df, index_col = 'State',  bar_width = 0.4, show_colorbar=True)
        fig.update_layout(xaxis_type='linear', autosize=False, width=800, height=400)
        fig.show()

