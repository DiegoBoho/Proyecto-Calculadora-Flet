import flet as ft
operadores = ["+","-","*","/", "%","**","//","(",")","."]

def botones(i, page,label):

    def click(e):
        if label.value == "0":
            label.value = str(i)
        else:
            label.value +=  str(i)
        page.update()

    return ft.ElevatedButton(text=str(i), on_click=click)

def calcular(page,label):
    def click(e):
        label.value = str(eval(label.value))
        page.update()

    return ft.ElevatedButton(text="=", on_click=click)

def borrar(page,label):
    def click(e):
        label.value = "0"
        page.update()

    return ft.ElevatedButton(text="C", on_click=click)

def operaciones(page,label,operador):
    def click(e):
        label.value += operador
        page.update()

    return ft.ElevatedButton(text=operador, on_click=click)

def main(page: ft.Page):
    page.title = "Calculadora"
    page.window_width = 400
    page.window_height = 400
    page.window_min_width = 400
    page.window_min_height = 400
    page.window_max_width = 400
    page.window_max_height = 400
    page.window_resizable = False
    page.update()
    label = ft.Text("0", size=30, color="blue")
    crearBotones = [botones(i, page,label) for i in range(0, 10)]
    botonesOperadores = [operaciones(page,label,operador) for operador in operadores]
    label2 = ft.Text("Calculadora", size=30, color="red")
    page.add(
        ft.Column(
            controls=[
                label2,
                label,
                ft.Row(
                    controls=crearBotones+[borrar(page,label)],
                    alignment=ft.MainAxisAlignment.CENTER,
                    wrap=True,
                    spacing=5
                ),
                ft.Row(
                    controls=[
                        calcular(page,label)
                    ] + botonesOperadores,
                alignment=ft.MainAxisAlignment.CENTER,
                wrap=True,
                spacing=10
                ),
     
            ]))
ft.app(target=main)