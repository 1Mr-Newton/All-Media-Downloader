from flet import *
h = 800;w=370
mc = '#43464c'


class CardRow(UserControl):
  def __init__(self,**kwargs):
    super().__init__(self)
    self.site1_name = kwargs.get('site1_name')
    self.site1_dls = kwargs.get('site1_dls')
    
    self.site2_name = kwargs.get('site2_name')
    self.site2_dls = kwargs.get('site2_dls')

    self.row = Row(
      alignment='spaceBetween',
      controls=[
        
      ]
    )

    if self.site1_name:self.row.controls.append(
       Stack(
          controls=[
            Card(
              height=225,width=140,
              elevation=25,
              top=5,left=5,opacity=0.3
            ),
            Container(
              padding=padding.only(left=15,right=15,top=20,bottom=20),
              height=235,width=150,
              bgcolor='#fbfbfb',
              border_radius=35,
              border=border.all(width=1,color='#cce6e6e6'),
              content=Column(
                alignment='spaceBetween',
                horizontal_alignment='center',
                controls=[
                  Stack(
                    controls=[
                      Card(
                        height=40,width=40,
                        elevation=8,
                        top=5,left=5,#opacity=0.3
                      ),
                      Container(
                        padding=5,
                        height=60,width=60,
                        bgcolor='white',
                        border_radius=35,
                        border=border.all(width=1,color='#cce6e6e6'),
                        alignment=alignment.center,
                        content=Container(
                          height=35,width=35,
                          border_radius=20,
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          content=Image(
                            src=f'assets/icons/{self.site1_name.lower()}.png',
                            fit=ImageFit.COVER,

                          )
                        )
                        
                        
                      ),
                    ]
                  ),
                
                  Text(
                    value=self.site1_name,
                    weight=FontWeight.BOLD,
                    color=mc,size=16,
                  ),
                  Column(
                    horizontal_alignment='center',
                    spacing=5,
                    controls=[
                      Text(
                        value='Total Download',
                        weight=FontWeight.W_500,
                        color=mc,size=14,
                      ),
                      Text(
                        value=self.site2_dls,
                        weight=FontWeight.BOLD,
                        color=mc,size=16,
                      ),
                    ]
                  )
                ]
              )
              
            ),
          ]
        )
)
    if self.site2_name:self.row.controls.append(
      Stack(
          controls=[
            Card(
              height=225,width=140,
              elevation=25,
              top=5,left=5,opacity=0.3
            ),
            Container(
              padding=padding.only(left=15,right=15,top=20,bottom=20),
              height=235,width=150,
              bgcolor='#fbfbfb',
              border_radius=35,
              border=border.all(width=1,color='#cce6e6e6'),
              content=Column(
                alignment='spaceBetween',
                horizontal_alignment='center',
                controls=[
                  Stack(
                    controls=[
                      Card(
                        height=40,width=40,
                        elevation=8,
                        top=5,left=5,#opacity=0.3
                      ),
                      Container(
                        padding=5,
                        height=60,width=60,
                        bgcolor='white',
                        border_radius=35,
                        border=border.all(width=1,color='#cce6e6e6'),
                        alignment=alignment.center,
                        content=Container(
                          height=35,width=35,
                          border_radius=20,
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          content=Image(
                            src=f'assets/icons/{self.site2_name.lower()}.png',
                            fit=ImageFit.COVER,

                          )
                        )
                        
                        
                      ),
                    ]
                  ),
                
                  Text(
                    value=self.site2_name,
                    weight=FontWeight.BOLD,
                    color=mc,size=16,
                  ),
                  Column(
                    horizontal_alignment='center',
                    spacing=5,
                    controls=[
                      Text(
                        value='Total Download',
                        weight=FontWeight.W_500,
                        color=mc,size=14,
                      ),
                      Text(
                        value=self.site1_dls,
                        weight=FontWeight.BOLD,
                        color=mc,size=16,
                      ),
                    ]
                  )
                ]
              )
              
            ),
          ]
        )



    )    

  def build(self):
    return self.row


class App(UserControl):
  def __init__(self,pg:Page,):
    self.pg = pg
    pg.window_height =h
    pg.window_width =w
    pg.bgcolor = colors.TRANSPARENT
    pg.window_bgcolor = colors.TRANSPARENT
    pg.window_title_bar_hidden =True
    pg.window_frameless = True
    pg.fonts = {
    "SF Pro Bold":"fonts/SFProText-Bold.ttf",
    "SF Pro Heavy":"fonts/SFProText-Heavy.ttf",
    "SF Pro HeavyItalic":"fonts/SFProText-HeavyItalic.ttf",
    "SF Pro Light":"fonts/SFProText-Light.ttf",
    "SF Pro Medium":"fonts/SFProText-Medium.ttf",
    "SF Pro Regular":"fonts/SFProText-Regular.ttf",
    "SF Pro Semibold":"fonts/SFProText-Semibold.ttf",
    "SF Pro SemiboldItalic":"fonts/SFProText-SemiboldItalic.ttf",
  }
    self.init_helper()
      
  def init_helper(self):

    self.card_row1 = CardRow(
      site1_name="Instagram",site1_dls="120",
      site2_name="TikTok",site2_dls="80"
    )
    self.card_row2 = CardRow(
      site1_name="YouTube",site1_dls="287",
      site2_name="Twitter",site2_dls="15"
    )
    
    self.card_row3 = CardRow(
      site1_name="Facebook",site1_dls="287",
      site2_name="SnapChat",site2_dls="15"
    )
    
    self.card_row4 = CardRow(
      site1_name="Reddit",site1_dls="287",
      site2_name="Pinterest",site2_dls="15"
    )
    
    self.base()

  def base(self):
    self.download_card_column = Column(
        height=h-150,
        scroll='auto',
        controls=[
          self.card_row1,
          self.card_row2,
          self.card_row3,
          self.card_row4,
          
        ]
      )
    
    self.pg.add(
      Container(
        animate_offset=self.animate_style,
        offset= transform.Offset(1,0),
        alignment=alignment.center,
        content=Text('Splash',size=30),
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        height=h,
        width=w,
        bgcolor='white',
        border_radius=40,
        content=Column(
          controls =[ 
            WindowDragArea(height=20,content=Container()),
            Container(
              padding=padding.only(top=20,left=25,right=25,bottom=5),
              content=Row(
                alignment='spaceBetween',
                controls=[
                  Container(
                    height=40,width=40,border_radius=25,bgcolor=mc,
                    content=Image(
                      src='assets/icons/menu.png',scale=0.3
                    ),
                  ),
                  Container(
                    content=Stack(
                      controls=[
                        Container(
                          height=10,width=150,bgcolor='#f9d966',margin=margin.only(bottom=20)
                        ),
                        Text(
                          left=5,
                          value='Category Download',
                          weight=FontWeight.W_600,
                          font_family='SF Pro Semibold',
                          color=mc,
                          size=14
                        )
                      ]
                    )
                  ),
                  Container(
                    content=Stack(
                      controls=[
                        Container(
                          margin=8,
                          content=Icon(
                            icons.NOTIFICATIONS_OUTLINED,
                            color=mc,
                            size=24,
                          ),
                        ),
                        Container(
                          alignment=alignment.center,
                          height=12,
                          width=12,
                          border_radius=8,
                          bgcolor='#22c993',
                          right=8,top=9,
                          padding=padding.only(bottom=1),
                          content=Text(
                            '2',
                            size=8
                          ),

                        )
                      ]
                    )
                  )
                ]
              )
            ),
            Container(
              padding=padding.only(top=25,left=20,right=20,bottom=0),
              content=self.download_card_column,
            )
          
          ]
        )

      )
   
   
    )

app(target=App, assets_dir='assets')