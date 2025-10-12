# flet-svgicon

A lightweight custom control for [Flet](https://flet.dev/) that makes it easy to display and customize **SVG icons** directly from Python.  
Easily change **stroke color**, **fill color**, **size**, and **stroke width** of your SVGs in real time.

---

## ✨ Features
- 🎨 Customize **stroke color**, **fill color**, **size**, and **stroke width** from Python code
- ⚡ Simple API for quick integration into any Flet page
- 📁 Supports local SVG assets
- 🖥️ Works across platforms (desktop, web, mobile)

---
## 📸 Preview
![SVGIcon demo](assets/screenshot.png)

## Clone the repo and test this script:
```python
from flet_svg.controls import SVGIcon
import flet

folder_svg_script = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 21H4a2 2 0 0 1-2-2V5c0-1.1.9-2 2-2h5l2 3h9a2 2 0 0 1 2 2v2M19 15v6M16 18h6"/></svg>"""
check_svg_script = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>"""

def main(page:flet.Page):
    page.bgcolor = "#000000"
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.add(
        flet.Row([
            SVGIcon(
                svg_script=check_svg_script,
                stroke_color='#ffffff',
                size=50,stroke_width=1
            ),
            SVGIcon(
                svg_script=check_svg_script,
                stroke_color='#4fb4f7',
                size=50,stroke_width=2
            ),
            SVGIcon(
                svg_script=check_svg_script,
                stroke_color='#ffffff',
                size=50,stroke_width=3
            ),
            SVGIcon(
                svg_script=check_svg_script,
                stroke_color='#c77cd6',
                size=50,stroke_width=4
            ),
        ],alignment=flet.MainAxisAlignment.CENTER,spacing=20),
        flet.Row([
            SVGIcon(
                svg_script=folder_svg_script,
                stroke_color='#ffffff',
                size=50,stroke_width=1
            ),
            SVGIcon(
                svg_script=folder_svg_script,
                stroke_color="#a0f74f",
                size=50,stroke_width=2
            ),
            SVGIcon(
                svg_script=folder_svg_script,
                stroke_color='#ffffff',
                size=50,stroke_width=3
            ),
            SVGIcon(
                svg_script=folder_svg_script,
                stroke_color="#df2b8e",
                size=50,stroke_width=4
            ),
        ],alignment=flet.MainAxisAlignment.CENTER,spacing=20),
        
    )

flet.run(main,assets_dir='assets')
```