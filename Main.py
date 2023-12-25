from tkinter import Tk
from View.View_Login import View_Login
from Model.TaiKhoanModel import TaiKhoanModel
from Controller.TaiKhoanController import TaiKhoanController

if __name__ == "__main__":
    view = View_Login()
    model = TaiKhoanModel()
    controller = TaiKhoanController(model, view)


    