import flet as ft
import time

from UI.text_box import Textbox
from UI.button import Button
from UI.drop_down_ports import DropDownPorts
from UI.drop_down import DropDown
from UI.pop_up import PopUp


class MainContent(ft.Row):

    def __init__(self,page:ft.Page):
        super().__init__()

        self.page = page
        self.page.on_keyboard_event = self.keyboard

        self.alignment = ft.MainAxisAlignment.START
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.spacing = 30

        self.txf_n_muestras = Textbox("Numero de muestras:",300,40,"int",ft.NumbersOnlyInputFilter())
        self.txf_n_mediciones = Textbox("Numero de mediciones:",300,40,"int",ft.NumbersOnlyInputFilter())
        self.txf_nombre_archivos = Textbox("Nombre de archivos:",300,40,"any")

        self.dd_port = DropDownPorts("Puerto",300,40)
        self.dd_baud_rate = DropDown("Baud rate",300,40,[300,600,1200,2400,4800,9600,14400,19200,28800,38400,57600,115200])

        self.btn_start = Button(50,300,"Iniciar",23,ft.icons.PLAY_ARROW,30,self.on_click_start)
        self.btn_save = Button(50,300,"Guardar",23,ft.icons.DOWNLOAD_ROUNDED,30,self.on_click_download)

        self.pop_up = PopUp("HOLA",180,800,600)

        self.started = False

        self.graphs_column = ft.Column(
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            spacing = 30,
            controls=[
                ft.Container(height=1),
            ]
        )
        

        self.controls = [
            ft.Container(height=1),
            
            ft.Column(
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                spacing = 35,
                controls=[
                    ft.Container(height=1),
                    self.txf_n_muestras,
                    self.txf_n_mediciones,
                    self.txf_nombre_archivos,
                    self.dd_port,
                    self.dd_baud_rate,
                    self.btn_start,
                    self.btn_save
                ]
            ),
            self.graphs_column   
        ]
    
   
    def start(self,e):
        self.started = True
        print("Starting ...")


    def cancel(self,e):
        self.started = False
        print("Cancelling ...")


    def on_click_download(self,e):
        print("Saving ...")


    def keyboard(self,e:ft.KeyboardEvent):

        if e.key == "Escape":
            self.cancel(e)

        if e.key == "Enter":
            self.start()


def main(page:ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.resizable = False
    page.window.width = 1350
    page.window.height = 780
    page.padding = 0
    page.spacing = 0

    page.add(
        ft.Stack([
            ft.Container(ft.Image(src="assets/background.jpg", fit=ft.ImageFit.FIT_HEIGHT)),
            ft.Container(width=1800, height=900, bgcolor="#70000000"),
            MainContent(page)
        ])

    )


if __name__ == '__main__':
    ft.app(target=main)