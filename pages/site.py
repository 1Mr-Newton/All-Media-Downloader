from flet import *
h = 800;w=370
mc = '#43464c'


class SitePage(UserControl):
  def __init__(self,):
    super().__init__()

  def build(self):
    return Container(
      content=Column(
        controls=[
          Container(
            content=Row(
              controls=[
                Icon(
                  icons.ARROW_BACK_OUTLINED,color=mc
                )
              ]
            )
          ),
          Container(),
        ]
      )
    )