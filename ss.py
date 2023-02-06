import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row(
            [
                ft.ShaderMask(
                    ft.Container(
                      height=200,width=200,
                      bgcolor='black',
                    ),
                    blend_mode=ft.BlendMode.DST_OUT,
                    shader=ft.RadialGradient(
                        colors=[
                         ft.colors.TRANSPARENT,
                          ft.colors.BLACK,
                         ],
                        stops=[.02, 1],
                    ),
                    border_radius=100,
                ),
            ]
        )
    )

ft.app(target=main)