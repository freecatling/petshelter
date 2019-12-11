from PIL import Image
from PIL import ImageFont, ImageDraw

content = {
    "back_img": "paper.jpg",
    "01": {
        "ad": "惊喜总在风雨后",
        "head": "01.jpg"
    },
    "02": {
        "ad": "总相信有彩虹",
        "head": "02.jpg"
    },
    "03": {
        "ad": "命运就算曲折离奇",
        "head": "03.jpg"
    },
    "04": {
        "ad": "命运就算颠沛流离",
        "head": "04.jpg"
    },
    "05": {
        "ad": "命运恐吓着你",
        "head": "05.jpg"
    },
    "06": {
        "ad": "别流泪，伤心",
        "head": "06.jpg"
    },
    "07": {
        "ad": "我愿用医生永远陪伴你",
        "head": "07.jpg"
    },
    "08": {
        "ad": "啊啊啊啊啊啊",
        "head": "08.jpg"
    },
    "09": {
        "ad": "幸运如你",
        "head": "09.jpg"
    },
}

blank = Image.new("RGB", [300,900], "white")
blank.save("picture/backgroud.jpg")
backgroud = "picture/backgroud.jpg"
colorfulhhh = "picture/colorfulhhh.jpg"

def get_pic(head, adcount, mark):
    # bg 背景图
    bg = Image.open(backgroud)
    hh = Image.open(colorfulhhh)
    # head_img 表情图 缩放统一尺寸
    head_img = Image.open(f"picture/{head}").resize((150, 150), Image.ANTIALIAS)
    # 在背景图的75,200 坐标处贴上表情图
    bg.paste(head_img, (75, 100))
    # 在背景图的0,700 坐标处贴上哈哈哈图
    bg.paste(hh, (0, 700))
    draw = ImageDraw.Draw(bg)
    # 加字
    # 想要文字居中请自行计算位置，没有直接居中的功能
    ad_font = ImageFont.truetype("STHeiti Medium.ttc", 20)
    mark_font = ImageFont.truetype("STHeiti Medium.ttc", 100)
    # draw.text((125, 400), mark, font=mark_font, fill=(0, 0, 0))
    draw.text((125, 400), mark, font=mark_font, fill='black')
    draw.text((75, 250), adcount, font=ad_font, fill='black')
    bg.save(f'result/{mark}_new.jpg', 'jpeg')

# 提前定义好生成长图的函数 get_pic(head, adcount, mark)
for i in range(1, 10):
    head = content[f'0{i}']['head']
    adcount = content[f'0{i}']["ad"]
    get_pic(head, adcount, f"{i}")
print("九宫格图片生成完毕！")
