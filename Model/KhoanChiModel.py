import os
import pyodbc
import openpyxl
from tkinter import messagebox


class KhoanChiModel:
    maduan = None
    def __init__(self,):
        self.conn_str = (
            "Driver={SQL Server};"
            "Server=DESKTOP-IS4BEN5\SQLEXPRESS;"
            "Database=QuanLyDuAn;"
            "Trusted_Connection=yes"
        )
        try:
            self.conn = pyodbc.connect(self.conn_str)
            self.cursor = self.conn.cursor()
        except pyodbc.Error as e:
            self.exception("Lỗi Kết nối", f"Không thể kết nối đến cơ sở dữ liệu:\n{str(e)}")
            exit()
    
    def get_data_from_database(self,maduan):
        data = []
        for row in self.cursor.execute(f"SELECT * FROM KhoanChi WHERE maduan={maduan}"):
            data.append(row)
        return data
    
    def get_data_from_makhoanchi(self,makhoanchi):
        data = []
        for row in self.cursor.execute(f"SELECT * FROM KhoanChi WHERE makhoanchi={makhoanchi}"):
            data.append(row)
        return data
    
    def get_tong_ngan_sach(self,maduan):
        data = self.cursor.execute(f"SELECT tongngansach FROM HoSo WHERE maduan = {maduan}")
        result = data.fetchone()
        if result[0] == None:
            return 0
        return result[0]
    
    def get_ngan_sach_da_chi(self, maduan):
        data = self.cursor.execute(f"SELECT SUM(sotien) FROM KhoanChi WHERE maduan = {maduan}")
        result = data.fetchone()
        if result[0] == None:
            return 0
        return result[0]
    
    def them_khoan_chi(self,maduan, tenkhoanchi, noidung, thoigianthuchien, sotien):
        self.cursor.execute(f"INSERT INTO KhoanChi (maduan, tenkhoanchi, noidung, thoigianthuchien, sotien) VALUES ({maduan}, N'{tenkhoanchi}', N'{noidung}', N'{thoigianthuchien}', {sotien})")
        self.conn.commit()
        return True

    def xoa_khoan_chi(self,makhoanchi):
        confirm = messagebox.askyesno(title="Xác nhận", message="Bạn có chắc chắn muốn xóa không?")
        if confirm:
            self.cursor.execute(f"DELETE FROM KhoanChi WHERE makhoanchi='{makhoanchi}'")
            self.conn.commit()
            return True
        else:
            return False

    def tim_kiem_khoan_chi(self, search_text, maduan):
        try:
            data = []
            for item in self.cursor.execute(f"SELECT * FROM KhoanChi WHERE tenkhoanchi LIKE '%{search_text}%' AND maduan = {maduan}"):
                data.append(item)
            return data
        except pyodbc.Error as e:
            self.exception("Lỗi Truy vấn", f"Lỗi khi truy vấn cơ sở dữ liệu:\n{str(e)}")
            
    def get_ngan_sach_da_chi(self, maduan):
        data = self.cursor.execute(f"SELECT SUM(sotien) FROM KhoanChi WHERE maduan = {maduan}")
        result = data.fetchone()
        if result[0] == None:
            return 0
        return result[0]
    

