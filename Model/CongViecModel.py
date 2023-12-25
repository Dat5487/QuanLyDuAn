import os
import pyodbc
import openpyxl
from tkinter import messagebox


class CongViecModel:
    maduan = None
    def __init__(self):
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

    
    def get_data_from_maduan(self,maduan):
        data = []
        for row in  self.cursor.execute(f"SELECT * FROM CongViec WHERE maduan={maduan}"):
            data.append(row)
        return data
    
    def get_data_from_macongviec(self,macongviec):
        data = []
        for row in self.cursor.execute(f"SELECT * FROM CongViec WHERE macongviec={macongviec}"):
            data.append(row)
        return data
    
    def get_tong_tien_do_cu(self,macongviec):
        data = self.cursor.execute(f"SELECT tiendotong FROM CongViec WHERE macongviec={macongviec}")
        result = data.fetchone()
        if result[0] == None:
            return 0
        return result[0]
    
    def them_cong_viec(self, maduan, tencongviec, tiendotong, tiendohientai, mota, chitiettiendo):
        self.cursor.execute(f"INSERT INTO CongViec (maduan, tencongviec, tiendotong, tiendohientai, mota, chitiettiendo) VALUES ({maduan}, N'{tencongviec}', {tiendotong}, {tiendohientai}, N'{mota}', N'{chitiettiendo}')")
        self.conn.commit()
        return True
    
    def get_tong_tien_do(self, maduan):
        data = self.cursor.execute(f"SELECT SUM(tiendotong) FROM CongViec WHERE maduan = {maduan}")
        result = data.fetchone()
        if result[0] == None:
            return 0
        return result[0]
    
    def sua_cong_viec(self, macongviec, tencongviec, tiendotong, tiendohientai, mota, chitiettiendo):
        self.cursor.execute(f"UPDATE CongViec SET tencongviec=N'{tencongviec}', tiendotong={tiendotong}, tiendohientai={tiendohientai}, mota=N'{mota}', chitiettiendo=N'{chitiettiendo}' WHERE macongviec={macongviec}")
        self.conn.commit()
        return True

    def xoa_cong_viec(self,macongviec):
        confirm = messagebox.askyesno(title="Xác nhận", message="Bạn có chắc chắn muốn xóa không?")
        if confirm:
            self.cursor.execute(f"DELETE FROM CongViec WHERE macongviec={macongviec}")
            self.conn.commit()
            return True
        else:
            return False

    def tim_kiem_cong_viec(self, search_text, maduan):
        try:
            data = []
            for item in self.cursor.execute(f"SELECT * FROM CongViec WHERE tencongviec LIKE '%{search_text}%' AND  maduan={maduan}"):
                data.append(item)
            return data
        except pyodbc.Error as e:
            self.exception("Lỗi Truy vấn", f"Lỗi khi truy vấn cơ sở dữ liệu:\n{str(e)}")

    

