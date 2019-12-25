import numpy as np
from PIL import Image
import hashlib
import os

# pic_dir = "/Users/free/Desktop/learn/13_play/photo_deduplication"
# bgpicPath = "/Users/free/Desktop/learn/13_play/photo_deduplication/xiaoying.png"
# bgpicPath1 = "/Users/free/Desktop/learn/13_play/photo_deduplication/xiaoying1.png"

# numpy
# pic_mask = np.array(Image.open(bgpicPath))
# pic_mask1 = np.array(Image.open(bgpicPath1))
# print((pic_mask==pic_mask1).all())
# print(pic_mask)
# print(pic_mask1)


# md5
# 用md5了，毕竟字符串比较短，而且是不可变类型，可以使用set去重
# file_txt = open(bgpicPath, 'rb').read()
# file_txt1 = open(bgpicPath1, 'rb').read()
# m = hashlib.md5(file_txt)
# m1 = hashlib.md5(file_txt1)
# print(m.hexdigest())
# print(m1.hexdigest())
# print(set([m.hexdigest(), m1.hexdigest()]))


def remove_repeat_pic(pic_abspath_list):
    '''
    删除重复照片
    @param：照片列表
    @return：
    '''
    mcode_li = []
    i = 0
    for pic_abspath in pic_abspath_list:
        mcode = make_md5(pic_abspath)
        if mcode not in mcode_li:
            mcode_li.append(mcode)
        else:
            os.remove(pic_abspath)
            i += 1
    print(f"删除重复图片完成！共删除{i}张图片")


def get_pic_abspath_list(*args):
    '''
    获取照片列表
    @param：文件夹
    @return：所有照片列表 所有文件夹列表
    '''
    pic_abspath_list = []
    dir_list = []
    for i in args:
        if os.path.isdir(i):
            dirpath = os.path.abspath(i)
            for root, dirs, names in os.walk(dirpath):
                dir_list.append(root)
                # dir_list += [*map(lambda x: os.path.join(root, x), dirs)]
                while ".DS_Store" in names[:]:
                    names.remove(".DS_Store")
                pic_abspath_list += [*map(lambda x: os.path.join(root, x), names)]
    return pic_abspath_list, dir_list


def make_md5(pic_path):
    '''
    md5编码
    @param：照片路径
    @return：照片md5编码
    '''
    pic_txt = open(pic_path, 'rb').read()
    m = hashlib.md5(pic_txt)
    mcode = m.hexdigest()
    return mcode


def remove_null_dir(dir_list):
    '''
    删除空文件夹
    @param：文件夹列表
    @return：
    '''
    for dir in dir_list:
        file_list = os.listdir(dir)
        while ".DS_Store" in file_list:
            file_list.remove(".DS_Store")
            os.remove(os.path.join(dir, ".DS_Store"))
        if not file_list:
            os.rmdir(dir)
            print('移除空目录: ' + dir)



if __name__ == '__main__':
    path = "./pic"
    path1 = "./pic1"
    pic_abspath_list, dir_list = get_pic_abspath_list(path, path1)
    print("图片文件夹列表：", dir_list)
    remove_repeat_pic(pic_abspath_list)
    print("删除重复图片后，文件夹为空的将被删除...")
    remove_null_dir(dir_list)
    print("Finished!")

