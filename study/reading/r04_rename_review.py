# 文件：r04_rename_review.py
# 作用：给一个文件夹里的所有文件统一加前缀
import os

dz = "study/reading/review_data"
# dz = "study/reading/no_such_dir"

def yjg(name):
    return name[:3] == "new" and name[3:4] == "_"


def gai(wj, qz):
    n,m = 0, 0
    shi = 0
    try:
        G = os.listdir(wj)
    except FileNotFoundError:
        print("目录不存在：", dz)
        return 0
    print("===进入预览模式===")
    for x in G:
        if yjg(x):
            print("跳过：", x, "已添加前缀")
            n = n + 1
        else:
            print("将改名:",x,"->", qz + x)
    print("跳过", n,"次")
    print("预览结束，确认执行吗？输 'y' 继续，其他键取消")
    n,m = 0, 0
    User = input("请输入：")
    if User != "y":
        print("已取消，什么都没改")
    else:
        for x in G:
            if yjg(x):
                print("跳过：", x, "已添加前缀")
                n = n + 1
            else:
                old = wj + "/" + x
                new = wj + "/" + qz + x
                try:
                    os.rename(old,new)
                    print(f"{x} -> {qz}{x}")
                    m = m + 1
                except:
                    print(f"{x} 改名失败，跳过这个文件继续处理下一个")
                    shi = shi + 1
    print("共改名", m, "个，跳过", n, "个，失败", shi, "个")
    return m
print()


print("改了", gai(dz, "a/b"), "个")
