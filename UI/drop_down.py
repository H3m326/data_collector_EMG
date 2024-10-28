import flet as ft

class DropDown(ft.Container):


    def __init__(self,title,width,height,values):
        super().__init__()

        self.bgcolor = ft.colors.TRANSPARENT
        self.main_color = ft.colors.WHITE
        
        self.border_radius = 15
        self.blur = ft.Blur(10,10,ft.BlurTileMode.MIRROR)
        self.padding = ft.padding.only(0,5,0,0)

        self.no_ports = False

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
            options = [ft.dropdown.Option(f"{value}") for value in values]
        )

        self.content = self.drop_down
