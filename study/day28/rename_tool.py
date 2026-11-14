import os,datetime
mulu = "study/day28/test_files"
# mulu = "study/day28/no_such_dir"
qz = datetime.datetime.now().strftime("%Y%m%d_")


def yjg(list):
    return list[:8].isdigit() and list[8:9] == "_"

def main():
    try:
        names = os.listdir(mulu)
    except FileNotFoundError:
        print("目录不存在：",mulu)
        return
    print("===进入预览模式==="); print()
    for name in names:
        if yjg(name):
            print("已加过前缀，跳过：",name)
        else:
            print("将改名：",name,"->",qz + name)
    print()
    print("预览结束，确认执行吗？输 'y' 继续，其他键取消")
    User = input("请输入：")
    N, M = 0, 0


    if User == "y":
        for name in names:
            if yjg(name):
                print("已加过前缀，跳过：",name)
                M = M + 1
            else:
                old = mulu + "/" + name
                new = mulu + "/" + qz + name
                os.rename(old,new)   
                print(name,"->",qz + name)
                N = N + 1
    else:
        print("已取消，什么都没改")


    print(f"共改名 {N} 个，跳过 {M} 个")
main()