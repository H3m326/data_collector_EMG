import flet as ft

class PopUp(ft.AlertDialog):

    def __init__(self,name,size,width,height):
        super().__init__()

        self.bgcolor = ft.colors.TRANSPARENT
        self.content_padding = 0
        self.title_padding = 0
        self.icon_padding = 0
        self.inset_padding = 0
        self.action_button_padding = 0
        self.actions_padding = 0
        self.modal = True

        self.name = ft.Text(value=name, weight=ft.FontWeight.BOLD, size=size, color=ft.colors.BLACK)
        
        self.content = ft.Container(
            bgcolor = ft.colors.WHITE,
            border = ft.border.all(8,ft.colors.PURPLE),
            border_radius = 30,
            padding = 0,
            width = width,
            height = height,
            alignment = ft.alignment.center,
            content = self.name
        )

    def show(self,value):
        self.name.value = value
        self.name.update()
        
                            