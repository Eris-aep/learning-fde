import os, sys, datetime


def yi_jia_guo(name):
    return name[:8].isdigit() and name[8:9] == "_"          # 从 day28/rename_tool.py 搬


def jia_qianzhui(wj):
    qz = datetime.datetime.now().strftime("%Y%m%d_")
    try:
        names = os.listdir(wj)
    except FileNotFoundError:
        print("目录不存在：",wj)
        return
    print("===进入预览模式==="); print()
    for name in names:
        if yi_jia_guo(name):
            print("已加过前缀，跳过：",name)
        else:
            print("将改名：",name,"->",qz + name)
    print()
    print("预览结束，确认执行吗？输 'y' 继续，其他键取消")
    User = input("请输入：")
    N, M, k = 0, 0, 0


    if User == "y":
        for name in names:
            if yi_jia_guo(name):
                print("已加过前缀，跳过：",name)
                M = M + 1
            else:
                try:
                    old = wj + "/" + name
                    new = wj + "/" + qz + name
                    os.rename(old,new)   
                    print(name,"->",qz + name)
                    N = N + 1
                except OSError:
                    print(f"{name} 改前缀失败，跳过这个文件继续处理下一个")
                    k = k + 1
        print("顶层：", os.listdir(wj))
        print(f"共改名 {N} 个，跳过 {M} 个, 失败{k}个")
    else:
        print("已取消，什么都没改")

          # 从 day28/rename_tool.py 的 main() 搬过来改


def fenlei(wj):
    try:
        names = os.listdir(wj)
    except FileNotFoundError:
        print(f"目录不存在：{wj}")
        return 
    
    skip, shi, move = 0,0,0
    print("===进入预览模式===")
    for x in names:
        files,hz = os.path.splitext(x)
        if hz == "":
            print("没有扩展名，跳过：", x)
        else:
            print(f"将移动： {x} -> {hz[1:]}/{x}")

    print()
    print("确认执行吗？输 y 继续，其他键取消");User = input("请输入:")
    if User == "y":
        for x in names:
            files,hz = os.path.splitext(x)
            if hz == "":
                print("没有扩展名，跳过：", x)
                skip = skip + 1
            else:
                try:
                    newpath = wj + "/" + hz[1:]
                    os.makedirs(newpath, exist_ok = True)
                    os.rename(wj + "/" + x, newpath + "/" + x )
                    print(f"已移动： {x} -> {hz[1:]}/{x}")
                    move = move + 1
                except OSError:
                    print(f"{x} 移动失败，跳过这个文件继续处理下一个")
                    shi = shi + 1
        print("顶层：", os.listdir(wj))
        print(f"共移动 {move} 个，跳过 {skip} 个，失败 {shi} 个")
    else:
        print("已取消，什么都没改")          # 从 day29/fenlei_tool.py 的 main() 搬过来改


def main():
    if len(sys.argv) < 3:           # 新写的：解析参数、分派
        print("用法：")
        print("     python wenjian_tool.py rename 目录   # 加日期前缀")
        print("     python wenjian_tool.py fenlei 目录   # 按扩展名分类")
        return
    moshi = sys.argv[1]; wj = sys.argv[2]
    if moshi not in ["rename","fenlei"]:
        print("不认识的模式： ", sys.argv[1])
        print("只支持 rename 和 fenlei")
        return   
    elif moshi == "rename":
        jia_qianzhui(wj)
        # print("现在目录里是：", os.listdir(sys.argv[2]))
    elif moshi == "fenlei":
        fenlei(wj)
        # print("现在顶层是：", os.listdir(sys.argv[2]))
main()
