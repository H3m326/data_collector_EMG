import flet as ft
import serial.tools.list_ports


class DropDownPorts(ft.Container):


    def __init__(self,title,width,height):
        super().__init__()

        self.bgcolor = ft.colors.TRANSPARENT
        self.main_color = ft.colors.WHITE
        
        self.border_radius = 15
        self.blur = ft.Blur(10,10,ft.BlurTileMode.MIRROR)
        self.padding = ft.padding.only(0,5,0,0)

        self.no_ports = False

        self.on_hover = self.get_ports

        self.drop_down = ft.Dropdown(
            width = width,
            height = height,
            border_color = self.main_color,
            border_width = 2,
            border_radius = self.border_radius,
            dense = True,
            icon_size = 34,
            icon_enabled_color = ft.colors.WHITE,
            icon_disabled_color = ft.colors.WHITE,
            text_style = ft.TextStyle(18, color=ft.colors.BLACK, weight=ft.FontWeight.W_500),
            label = title,
            label_style = ft.TextStyle(18, color=ft.colors.WHITE, weight=ft.FontWeight.W_500),
            on_blur = self.get_ports,
            options=[
                ft.dropdown.Option("No ports found")
            ],
        )

        self.content = self.drop_down

    def get_ports(self,e):

        ports = serial.tools.list_ports.comports()

        if ports:
            self.drop_down.options = [ ft.dropdown.Option(f"{port.device}") for port in ports]
            self.drop_down.update()
            return
            
        self.drop_down.options = [ ft.dropdown.Option("No ports found") ]
        self.drop_down.update()
            

        

        
