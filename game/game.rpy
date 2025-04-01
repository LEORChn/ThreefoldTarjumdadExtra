
# 您只需要编辑以下信息即可轻松填写您的三相奇谈同人游戏基本信息。

init python:
    myGame = {
    'name'   : '    三相奇谈同人          ',
    'version': '    1.0                    ',
    'author' : '    {a=https://space.bilibili.com/3084436}疯狂小瑞瑞LEORChn{/a} ',
    'package': '                           ',
    'license': '    没有使用额外素材。     ',
    'textSpeed':    50                     ,
    # 上面是对话框每秒显示的字数，可以填0或正整数，如果是0则没有这个动画效果
    
}

define w = Character("无才帝")

label start:
  scene bg room
  show eileen happy
  menu:
    '...'
    '...':
      '......'
      w '您来了啊，老朋友，'
    '又见到你了，老朋友':
      w '！'
  w '有什么要问的吗？'
  play sound '分支出现.aac'
  menu:
    w '有什么要问的吗？'
    '...':
      play sound '分支选择.aac'
      '......'
    '又见到你了，老朋友':
      play sound '分支选择.aac'
      w '！'
      
  w "您已创建一个新的 Ren'Py 游戏。"
    
  w "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

  return
