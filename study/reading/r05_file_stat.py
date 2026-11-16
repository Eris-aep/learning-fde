# 文件：r05_file_stat.py
# 作用：统计一个文件夹里每种扩展名各有多少个文件，然后打印出来
import os

MULU = "study/reading/stat_data"


def tongji(mulu):
    # tj 用来装「扩展名 -> 个数」，一开始是空字典
    tj = {}
    for name in os.listdir(mulu):
        mingzi, hz = os.path.splitext(name)
        # 没有扩展名的（比如文件夹、README），跳过
        if hz == "":
            continue
        # 把这个扩展名的个数记进字典
        tj[hz] = tj.get(hz, 0) + 1
    return tj


def baogao(tj):
    print("扩展名统计：")
    for hz in tj:
        print(hz[1:], tj[hz], "个")


tj = tongji(MULU)
baogao(tj)
# 第一步：扩展名统计：  第二步：输入是通过os.listdir把指定路径下的所有东西都显示
# txt 1 个             ，通过os.path.splitext获取后缀+if判断是否属于文件而非文件夹
# jpg 1 个             ，最后统计每个后缀的个数。然后打印出来
# # md 1 个

# 第三步：              
# jpg2、md1、txt3       在17行，错在把值写死了，多少次都是1，
# 打印出：               导致无论有几个相同的后缀都是个数1       
# txt、jpg、md各1

# 第五步:                                   2.如果 MULU 是个不存在的目录，这个程序直接崩    
# tongji收被指定路径的所有子级                  必须要加保护，写法是：
# 返回一个收集了路径下所有后缀及个数的列表         try..except FileNotFoundError+print(返回字符串)