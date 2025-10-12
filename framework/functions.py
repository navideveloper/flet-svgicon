import base64
import re,os

def color_svg(svg_text: str, fill_color: str = None, stroke_color: str = None, stroke_width: str = None) -> str:
    if fill_color:
        svg_text = re.sub(r'fill="[^"]*"', f'fill="{fill_color}"', svg_text)
        svg_text = re.sub(
            r'(<(?:path|rect|circle|polygon|ellipse|line|polyline)\b(?![^>]*fill=))',
            r'\1 fill="' + fill_color + '"',
            svg_text
        )

    if stroke_color:
        svg_text = re.sub(r'stroke="[^"]*"', f'stroke="{stroke_color}"', svg_text)
        svg_text = re.sub(
            r'(<(?:path|rect|circle|polygon|ellipse|line|polyline)\b(?![^>]*stroke=))',
            r'\1 stroke="' + stroke_color + '"',
            svg_text
        )

    if stroke_width:
        svg_text = re.sub(r'stroke-width="[^"]*"', f'stroke-width="{stroke_width}"', svg_text)
        svg_text = re.sub(
            r'(<(?:path|rect|circle|polygon|ellipse|line|polyline)\b(?![^>]*stroke-width=))',
            r'\1 stroke-width="' + stroke_width + '"',
            svg_text
        )

    return svg_text

def svg_to_base64(svg_text: str) -> str:
    return base64.b64encode(svg_text.encode("utf-8")).decode()
