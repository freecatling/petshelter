import os
import re
import json
import jieba
import collections
import wordcloud
import numpy as np
import PIL

# 将微信聊天记录中的中文词语进行词频统计，并将其生成自定义的云词图
PRO_PATH = os.path.dirname(os.path.abspath(__file__))
CUSSTOPWORDS = ["不是", "就是", "还是","这么", "怎么", "这个", "不能",
                "什么", "没有", "那个", "那么", "一个", "红包", "恭喜发财",
                "大吉大利", "微信", "领取", "红包"]


# 1 读取数据　整理中文词汇
def getChineseStr(chatPath):
    """
    读取数据　整理中文词汇
    @param: chatPath 要制作云词图的数据
    @return: chineseStr 提取出的中文字符串
    """
    dpath = os.path.join(PRO_PATH, chatPath)
    with open(dpath, "r")as f:
        content = f.read()

    content_dic = json.loads(content.lstrip('var data = '))
    message = content_dic["message"]
    ourchatstr = ""
    for info in message:
        if not info["m_nsContent"].startswith("image"):
            ourchatstr += info["m_nsContent"]+" "
    chineseStr = re.findall(r'[\u4e00-\u9fa5]+', ourchatstr)

    return chineseStr


# 2 jieba分词　统计词频
def splitWord(dataStr):
    """
    jieba分词　统计词频
    @param: dataStr 要进行分词的字符串
    @return: allwordslist 分词后的列表
    """
    allwordslist = jieba.lcut("".join(dataStr))
    for word in allwordslist[:]:
        if len(word) == 1:
            try:
                allwordslist.remove(word)
            except:
                pass

    countli = collections.Counter(allwordslist)
    # list1 = sorted(countli.items(), key=lambda x: x[1], reverse=True)
    print(len(countli))
    print(countli)
    return allwordslist


# 3 用个性化图片做背景　生成云词图
def genWordCloud(allwordslist, bgpicPath, newPicPath, maxWords):
    """
    用个性化图片做背景　生成云词图
    @param: allwordslist 分词后的列表
            bgpicPath 背景图路径
            newPicPath 生成图片路径
            maxWords 最大填充词量
    @return:
    """
    txt = " ".join(allwordslist)
    pic_mask = np.array(PIL.Image.open(bgpicPath))
    w = wordcloud.WordCloud(
        font_path='font/Hiragino.ttc',
        width=1000,
        height=800,
        margin=2,
        background_color='white',
        mask=pic_mask,
        max_words=maxWords,
        max_font_size=60,
        stopwords=set(CUSSTOPWORDS),
        # color_func=wordcloud.ImageColorGenerator(pic_mask),
        scale=1.5
    )
    w = w.generate(txt)  # 设置的stopwords才管用
    # w = w.fit_words(dict(countli))  # 直接用词频统计的dict方式，但是这种方式下，设置stopwords不生效
    w.to_file(newPicPath)


if __name__ == '__main__':
    # 用户输入 准备数据
    print("有爱的词图：\n")
    pics = os.listdir("pic")
    data = os.listdir("data")
    try:
        pics.remove(".DS_Store")
        data.remove(".DS_Store")
    except:
        pass
    for i in range(len(pics)):
        img_path = os.path.join("pic", pics[i])
        pics[i] = img_path
        print(f'{i}  {img_path}')
    img_no = input("请输入背景图序号（无输入直接enter，将使用默认值 0）：")
    for i in range(len(data)):
        dataPath = os.path.join("data", data[i])
        data[i] = dataPath
        print(f'{i}  {dataPath}')
    chat_no = input("请输入选择的聊天记录（无输入直接enter，将使用默认值 0）：")
    maxWords = input("请输入最多填充词量,整数（无输入直接enter，将使用默认值 200）：")
    newPicName = input("请输入新图片名称（无输入直接enter，将使用默认值）：")
    img_no = img_no if img_no else 0
    chat_no = chat_no if chat_no else 0
    maxWords = int(maxWords) if maxWords else 200
    bgpicPath = pics[int(img_no)]
    chatPath = data[int(chat_no)]
    if not newPicName:
        newPicName = "{}_{}_{}.jpg".format(os.path.split(chatPath)[1].split(".")[0],
                                           os.path.split(bgpicPath)[1].split(".")[0], maxWords)
    newPicPath = f'resultpic/{newPicName}'
    # 调用函数
    chineseStr = getChineseStr(chatPath)
    allwordslist = splitWord(chineseStr)
    genWordCloud(allwordslist, bgpicPath, newPicPath, maxWords)
    print("词云图片生成:", os.path.join(PRO_PATH, newPicPath))






