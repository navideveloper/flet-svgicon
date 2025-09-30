import flet
from MyPack import SVGIcon

def main(page:flet.Page):
    page.bgcolor = "#000000"
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.add(
        flet.Row([
            SVGIcon(
                icon_path="./assets/check_icon.svg",
                stroke_color='#ffffff',
                size=50,stroke_width=1
            ),
            SVGIcon(
                icon_path="./assets/check_icon.svg",
                stroke_color='#4fb4f7',
                size=50,stroke_width=2
            ),
            SVGIcon(
                icon_path="./assets/check_icon.svg",
                stroke_color='#ffffff',
                size=50,stroke_width=3
            ),
            SVGIcon(
                icon_path="./assets/check_icon.svg",
                stroke_color='#c77cd6',
                size=50,stroke_width=4
            ),
        ],alignment=flet.MainAxisAlignment.CENTER,spacing=20),
        flet.Row([
            SVGIcon(
                icon_path="./assets/folder_icon.svg",
                stroke_color='#ffffff',
                size=50,stroke_width=1
            ),
            SVGIcon(
                icon_path="./assets/folder_icon.svg",
                stroke_color="#a0f74f",
                size=50,stroke_width=2
            ),
            SVGIcon(
                icon_path="./assets/folder_icon.svg",
                stroke_color='#ffffff',
                size=50,stroke_width=3
            ),
            SVGIcon(
                icon_path="./assets/folder_icon.svg",
                stroke_color="#df2b8e",
                size=50,stroke_width=4
            ),
        ],alignment=flet.MainAxisAlignment.CENTER,spacing=20),
        
    )

flet.run(main)