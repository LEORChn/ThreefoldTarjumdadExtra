init python:
    config.name = myGame['name'].strip()
    config.version = myGame['version'].strip() or "1.0"
    gui.about = _p("""
除了《三相奇谈》所有可能的素材以外，还使用了以下美术或声音素材：

%s
""")
    gui.aboutSanPy = _p("""
本程序使用基于 Ren'Py 引擎派生的 San'Py UI 制作，并使用了《三相奇谈》所有可能的美术和声音素材，如需详细了解，请{a=https://github.com/LEORChn/ThreefoldTarjumdadExtra}点击这里查看{/a}。

San'Py 作者：{a=https://space.bilibili.com/3084436}疯狂小瑞瑞LEORChn{/a}

San'Py 版本：v0.1
""")
