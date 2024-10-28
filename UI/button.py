import flet as ft


class Button(ft.Container):


    def __init__(self,height,width,title,title_size,icon_name,icon_size,onclick=None):
        super().__init__()

        self.main_color = ft.colors.WHITE

        self.height = height
        self.width = width
        self.border_radius = 20
        self.bgcolor = ft.colors.TRANSPARENT
        self.border = ft.border.all(3,self.main_color)
        self.blur = ft.Blur(10,10,ft.BlurTileMode.MIRROR)
        self.padding = 0
        self.ink = True
        self.on_click = onclick

        self.content = ft.Row(
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            spacing = 10,
            controls = [ 
                ft.Icon(icon_name, self.main_color, icon_size),
                ft.Text(title, size=title_size, color=self.main_color, weight=ft.FontWeight.W_600),
            ]
        )