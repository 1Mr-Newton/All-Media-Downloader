from flet import *
from pytube import YouTube
h = 800;w=370
mc = '#43464c'
pc = '#30a6a6'

class WindowDrag(UserControl):
  def __init__(self):
    super().__init__()
  def build(self):
    return Container(
      content=WindowDragArea(height=20,content=Container()),
    )

class CardRow(UserControl):
  def __init__(self,func=None,**kwargs):
    super().__init__(self)
    self.func = func
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
              on_click=self.func,
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
              on_click=self.func,
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
    self.animate_style = animation.Animation(200,AnimationCurve.DECELERATE)

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

  def switch_page(self,e:TapEvent,site):
    print('Switching to',site)
    for page in self.switch_control:
      self.switch_control[page].offset.x = 1
      self.switch_control[page].update()
    self.switch_control[site].offset.x = 0
    self.switch_control[site].update()

  def fetch_video_details(self,e:TapEvent):
    url = self.url_input.value
    if url != '':
      self.pg.splash = ProgressBar()
      self.pg.update()
      yt = YouTube(url)
      print(yt.streams)
      self.pg.splash = None
      self.pg.update()
      

  def base(self):
    self.url_input =TextField(
      # keyboard_type=KeyboardType.DATETIME,
      content_padding=Padding(left=5, top=3, right=5, bottom=3),
      expand=True,
      color=mc,
      border_color=None,
      border=InputBorder.NONE,
      hint_text='Paste link here...',
      hint_style=TextStyle(
        color='#686868',

      ),
      
    )

    
    
    self.download_card_column = Column(
        height=h-210,
        scroll='auto',
        controls=[
          self.card_row1,
          self.card_row2,
          self.card_row3,
          self.card_row4,
          
        ]
      )
    
    self.splash_screen = Container(
        animate_offset=self.animate_style,
        offset= transform.Offset(1,0),
        alignment=alignment.center,
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        height=h,
        width=w,
        bgcolor='white',
        border_radius=40,
        content=Column(
          controls =[ 
            WindowDrag(),
            Stack(
              controls=[
                Container(
                  padding=padding.only(top=20,left=25,right=25,bottom=5),
                  content=Column(
                    height=h,
                    width=w,
                    controls=[
                      Row(
                        controls=[
                          Text(
                            'Very fast and 100% free',
                            color='#666c73',
                            font_family='SF Pro Semibold',

                          )
                        ]
                      ),
                      Row(
                        controls=[
                          Text(
                            'Supports',
                            color='black',
                            font_family='SF Pro Semibold',
                            size=35,

                          )
                        ]
                      ),
                      Row(
                        # alignment='center',
                        controls=[
                          Container(
                            content=Stack(
                              controls=[
                                Container(
                                  height=20,width=150,bgcolor='#f9d966',margin=margin.only(bottom=50)
                                ),
                                Text(
                                  left=5,
                                  top=-10,
                                  value='multiple',
                                  weight=FontWeight.W_400,
                                  # font_family='SF Pro Regular',
                                  color=mc,
                                  size=36
                                ),
                              ]
                            )
                          ),
                          Text(
                            
                            value='Sites',
                            weight=FontWeight.W_500,
                            font_family='SF Pro Heavy',
                            color='black',
                            size=35
                          )


                        ]
                      ),

                      Container(
                        content=Text(
                          value='All Media Downloader is the easiest application to download videos from Facebook, Instagram, Twitter, TikTok and other sites.',
                          color=mc,size=13,weight=FontWeight.W_600,
                        ),
                      ),
                      


                ]
              )
            
            ),
                
                Container(
                  bottom=100,
                  # width=250,
                  content=Image(
                    src='assets/icons/sp.png'
                  )
                ),
                Container(
                  on_click=lambda e: self.switch_page(e,'home'),
                  alignment=alignment.center,
                  top=260,
                  left=20,
                  height=55,
                  width=150,
                  bgcolor=pc,
                  border_radius=26,
                  content=Row(
                    alignment='center',
                    controls=[
                      Text(
                        'Get Start'
                      ),
                      Container(
                        height=25,
                        width=25,
                        # padding=,
                        alignment=alignment.center,
                        bgcolor='yellow',
                        border_radius=25,
                        content=Icon(
                          icons.ARROW_FORWARD_IOS_OUTLINED,
                          color=mc,
                          size=15,
                        ),
                      )
                    ]
                  )
                )
              ]
            ),
            
            
          ]
        )

      )


    self.home_screen = Container(
        animate_offset=self.animate_style,
        offset= transform.Offset(0,0),
        alignment=alignment.center,
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        # expand=True,
        height=h,
        width=w,
        bgcolor='white',
        border_radius=40,
        content=Stack(
          controls=[
            Column(
              controls =[ 
                WindowDrag(),
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
                              value='All Media Downloader',
                              weight=FontWeight.W_600,
                              font_family='SF Pro Semibold',
                              color=mc,
                              size=13
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
                Row(
                  alignment='center',
                  controls=[
                    Container(
                      height=60,
                      content=Row(
                          width=w-60,
                          alignment='spaceBetween',
                          controls=[
                            Container(
                              border=border.all(width=1,color='#cce6e6e6'),
                              height=50,
                              width=240,
                              bgcolor='white',
                              border_radius=25,
                              content=Row(
                                spacing=0,
                                controls=[
                                  Container(
                                    padding=padding.only(left=20,right=12,top=5,bottom=5),
                                    content=Icon(
                                      icons.LINK_OUTLINED,
                                      color=mc,
                                      size=20,
                                      rotate=-0.5
                                    ),
                                  ),
                                  

                                  self.url_input,
                                  

                                ]
                              )
                            ),
                            Container(
                              on_click= self.fetch_video_details,
                              height=50,
                              width=50,
                              bgcolor=pc,
                              border_radius=25,
                              content=Icon(
                                icons.DOWNLOAD_OUTLINED
                              )
                              
                            ),
                          ]
                        )
                    ),

                  ]
                ),
                Container(
                  padding=padding.only(top=25,left=20,right=20,bottom=0),
                  content=self.download_card_column,
                )
              
              ]
            ),
            Container(
              padding=padding.only(top=20,bottom=20,right=20,left=20),
              height=400,bgcolor='white',bottom=0,width=w,
              content=Column(
                horizontal_alignment='center',
                controls=[
                  Container(height=20),
                  Text(
                    value='Video Found',
                    font_family="SF Pro Semibold",
                    color='black',
                    size=14,
                  ),
                  Divider(height=0.5,thickness=0.5),
                  Container(
                    content=Row(
                      height=100,
                      controls=[
                        Container(
                          height=80,
                          width=120,
                          bgcolor='red',
                          border_radius=20,
                        ),
                        Column(
                          spacing=0,
                          alignment='center',
                          controls=[
                            Text('Video Title',color='black'),
                            Text('Some description here',color='black')
                          ]
                        )
                      ]
                    ),
                  ),
                  Divider(height=0.2,thickness=0.2,),
                  Container(
                    # bgcolor='black',
                    height=100,width=300,
                    content=Column(
                      controls=[
                        Row(
                          alignment='spaceBetween',
                          controls=[
                            Text(
                              value='1080P',color='black',
                              font_family='SF Pro Semibold',
                            ),
                            Row(
                              controls=[
                                Text(
                                  value='Size: 9.5MB',
                                  font_family='SF Pro Medium',
                                  color='black',
                                ),
                                RadioGroup(
                                  content=Radio(),
                                )
                              ]
                            )
                          ]
                        ),
                      ]
                      # height=1
                    )
                  ),

                  Divider(height=0.2,thickness=0.2,),

                  Row(
                    alignment='center',
                    controls=[
                      Container(
                        alignment=alignment.center,
                        height=45,width=130,
                        border=border.all(width=1.3,color='black'),
                        border_radius=25,
                        content=Text(
                          value='Cancel',color='black',size=12,font_family='SF Pro Semibold'
                        )
                      ),
                      Container(
                        alignment=alignment.center,
                        height=45,width=130,
                        bgcolor=pc,
                        border_radius=25,
                        content=Text(
                          value='Download',color='white',size=12,font_family='SF Pro Semibold'
                        )
                      ),
                    ]
                  )
                  
                ]
              )
            ),
            Container(
              width=40,
              height=40,
              border=border.all(width=12,color='black'),
              bgcolor='white',
              bottom=380,
              border_radius=20,
              left=150,
              alignment=alignment.center,
              # padding=padding.only(bottom=3),
              content=Icon(
                icons.CLOSE,color='black',size=12
              )
            ),
          ]
        )
      )

    self.site_screen = Container(
      animate_offset=self.animate_style,
      alignment=alignment.center,
      height=h,width=w,bgcolor='white',
      offset= transform.Offset(1,0),
      content=Column(
        controls=[
          WindowDrag(),
          Container(
            padding=padding.only(left=20,right=20,top=20),
            content=Row(
              alignment='spaceBetween',
              controls=[
                Icon(
                  icons.ARROW_BACK_OUTLINED,
                  color=mc,
                ),
                Text(
                  value='Instagram',color=mc,
                  font_family='SF Pro Semibold'
                ),
                Icon(
                  icons.SHARE_OUTLINED,
                  color=mc,
                ),
              ]
            )
          ),
          Stack(
            expand=True,
            controls=[
              Container(
                padding=20,
                expand=True,
                content=Column(
                  scroll = 'auto',
                  horizontal_alignment='center',
                  controls=[
                    Container(
                      content=Column(
                        controls=[
                          Container(
                            clip_behavior=ClipBehavior.ANTI_ALIAS,
                            height=100,
                            # bgcolor='blue',
                            content=Row(
                              controls=[
                                Container(
                                  # height=90,
                                  # expand=True,
                                  width=120,
                                  border_radius=15,
                                  image_src='assets/images/1.png',
                                  image_fit=ImageFit.COVER,
                                ),
                                Container(
                                  expand=True,
                                  # bgcolor='orange',
                                  content=Column(
                                  spacing=2,
                                  alignment='center',
                                  controls=[
                                    Text(
                                      value='Title of video',
                                      font_family='SF Pro Semibold',
                                      color=mc,
                                      no_wrap=True
                                    ),
                                    Text(
                                      value='Description of video',
                                      font_family='SF Pro Regular',
                                      color=mc,
                                      no_wrap=True,
                                      size=12
                                    ),
                                    
                                    Container(
                                      # bgcolor='brown',
                                      margin=margin.only(top=5),
                                      height=30,
                                      # width=170,
                                      content=Row(
                                        alignment='spaceBetween',
                                        vertical_alignment='center',
                                        
                                        controls=[
                                          Column(
                                            # alignment='spaceBetween',
                                            controls=[
                                              Row(
                                                alignment='end',
                                                controls=[
                                                  Text(
                                                    value='4.5 / 8.9 MB',
                                                    color=mc,
                                                    size=10,
                                                    font_family='SF Pro Medium'
                                                  )
                                                ]
                                              ),
                                              Container(
                                                width=100,height=2,bgcolor='#1a888888',border_radius=5,
                                                padding=padding.only(right=100/2),
                                                content=Container(expand=True,bgcolor=pc)
                                              )
                                            ]
                                          ),
                                          Container(
                                            height=25,width=25,border_radius=25,
                                            content=Icon(
                                              icons.PAUSE_CIRCLE_OUTLINE,color=mc
                                            )
                                          ),
                                          Container(
                                            height=25,width=25,border_radius=25,
                                            content=Image(
                                              src='assets/icons/menu_popup.png',scale=0.6,color=mc
                                            )
                                          ),
                                          
                                        ]
                                      )
                                    )
                                  ]
                                )
                              
                                )
                              
                              ]
                            )
                          ),
                          Divider(
                            height=0.2,thickness=.2
                          )
                        ]
                      )
                    )

                  ]
                )
              ),
              Stack(
                width=w-20,height=120,bottom=0,
                controls=[
                  
                  Container(
                    border_radius=35,
                    gradient=LinearGradient(
                        colors=[
                         colors.TRANSPARENT,
                          colors.BLACK,
                         ],
                        stops=[.02, 1],
                        begin=alignment.top_center,
                        end=alignment.bottom_center,
                    ),
                    
                    opacity=0.5,
                  ),
                  Container(
                    padding=padding.only(left=20,right=20,top=20,bottom=20),
                    height=235,width=w-20,
                    bgcolor='#fbfbfb',
                    border_radius=35,
                    margin=margin.only(top=20),
                    content=Row(
                      controls=[
                        # Container(height=30,width=30,bgcolor='red'),
                        
                        Container(
                          alignment=alignment.center,
                          height=45,
                          expand=True,
                          bgcolor=pc,
                          border_radius=30,
                          content=Text(
                            'Open Folder'
                          )
                        ),
                      ]
                    )
                    
                  ),
                ]
              ),

            ]
          )

        ]
      )
    )
    
    self.switch_control = {
      'splash':self.splash_screen,
      'home':self.home_screen,
      'site':self.site_screen,
    }


    self.pg.add(
      Container(
        # padding=20,
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        height=h,width=w,
        bgcolor='white',
        border_radius=40,
        content=Stack(
          controls=[
      
            self.splash_screen,
            self.home_screen,
            self.site_screen,
            # Container(
            #   height=500,bgcolor='black',bottom=100
            # )
          ]
        )
      ),
      Row(
        alignment='center',
        controls=[
          Container(
          height=50,width=100,bgcolor='purple',
          on_click=lambda e: self.switch_page(e,'splash'),
        ),
        Container(
          height=50,width=100,bgcolor='purple',
          on_click=lambda e: self.switch_page(e,'home'),
        ),
        Container(
          height=50,width=100,bgcolor='purple',
          on_click=lambda e: self.switch_page(e,'site'),
        )
        ]
      )
    )

app(target=App, assets_dir='assets')