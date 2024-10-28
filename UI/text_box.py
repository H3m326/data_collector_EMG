import flet as ft


class Textbox(ft.Container):


    def __init__(self,title,width,height,hint_text,filter=None):
        super().__init__()

        self.bgcolor = ft.colors.TRANSPARENT
        self.main_color = ft.colors.WHITE
        
        self.border_radius = 15
        self.border = ft.border.all(2,self.main_color)
        self.blur = ft.Blur(10,10,ft.BlurTileMode.MIRROR)
        self.padding = ft.padding.only(10,5,10,10)

        self.text_field = ft.TextField(
            width = width,
            height = height,
            dense = True,
            border_color = self.main_color,
            border_width = 2,
            border_radius = self.border_radius,
            bgcolor = ft.colors.TRANSPARENT,
            hint_text = hint_text,
            hint_style = ft.TextStyle(color=self.main_color,size=20,weight=ft.FontWeight.W_400),
            text_align = ft.TextAlign.CENTER,
            text_style = ft.TextStyle(color=self.main_color,size=20,weight=ft.FontWeight.W_400),
            input_filter = filter,
        )

        self.content = ft.Column(
            alignment= ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.START,
            spacing = 0,
            controls = [ 
                ft.Text(title, size=20, color=self.main_color, weight=ft.FontWeight.W_700),
                self.text_field
            ]
        )