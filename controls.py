import flet
from . import functions

class SVGIcon(flet.Container):
    def __init__(self,
            svg_script:str,size:int=1,stroke_width:int=2,
            fill_color:str='#000000',stroke_color:str='#ffffff'
        ):
        super().__init__()
        self.size = size
        self.svg_script = svg_script
        self.fill_color = fill_color
        self.stroke_width = stroke_width
        self.stroke_color = stroke_color
        self.content = flet.Image(width=size,height=size)
    
    def did_mount(self):
        self.update_icon()
        return super().did_mount()

    def update_icon(self):
        content = functions.svg_to_base64(
            functions.color_svg(
                self.svg_script,
                self.fill_color,self.stroke_color,str(self.stroke_width),
            )
        )
        self.content.src_base64 = content
        self.update()

    def update(self):
        return super().update()