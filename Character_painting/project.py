#coding=utf-8
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def painting(txt, img_path, fontsize=9, new_img=None):
    font = ImageFont.truetype("Hiragino.ttc", fontsize)  # 字体 字大小
    img = Image.open(img_path)
    width, height = img.size
    newImg = Image.new("RGBA", (width, height), (10, 10, 10))  #背景色rgb，偏黑显示好一些
    x = 0
    for i in range(0, height, fontsize):  # 需要与字体大小一致 range(stop) range(start, stop[, step])
        for j in range(0, width, fontsize):  # 需要与字体大小一致
            color = img.getpixel((j, i))  # 函数功能，该函数检索指定坐标点的像素的RGB颜色值
            draw = ImageDraw.Draw(newImg)
            draw.text((j, i), txt[x % len(txt):x % len(txt)+1], fill=(color[0], color[1], color[2]), font=font)
            x += 1
    newImg = newImg.convert("RGB")
    if new_img:
        new_path = f"result/{new_img}.jpg"
    else:
        org_pic_name = (img_path.split("/"))[-1].split(".")[0]
        new_path = f"result/{org_pic_name}_new.jpg"
    newImg.save(new_path, "JPEG")
    return new_path

if __name__ == '__main__':
    print("字符画填充：\n")
    pics = os.listdir("picture")
    try:
        pics.remove(".DS_Store")
    except:
        pass
    for i in range(len(pics)):
        img_path = os.path.join("picture", pics[i])
        pics[i] = img_path
        print(f'{i}  {img_path}')
    img_no = input("请输入原图序号（无输入直接enter，将使用默认值）：")
    txt = input("请输入填充内容（无输入直接enter，将使用默认值）：")
    fontsize = input("请输入填充字体大小,整数（无输入直接enter，将使用默认值）：")
    new_img = input("请输入新图片名称（无输入直接enter，将使用默认值）：")
    img_no = img_no if img_no else 0
    txt = txt if txt else "000000"
    fontsize = int(fontsize) if fontsize else 9
    new_img = new_img if new_img else None
    img_path = pics[int(img_no)]
    new_path = painting(txt, img_path, fontsize, new_img)
    pwd = os.path.dirname(os.path.abspath("__file__"))
    print("新图片生成:", os.path.join(pwd, new_path))

