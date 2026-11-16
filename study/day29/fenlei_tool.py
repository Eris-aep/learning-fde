mulu = "study/day29/test_files"
# mulu = "study/day29/no_such_dir"
import os

def main():

    try:
        names = os.listdir(mulu)
    except FileNotFoundError:
        print(f"目录不存在：{mulu}")
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
                    newpath = mulu + "/" + hz[1:]
                    os.makedirs(newpath, exist_ok = True)
                    os.rename(mulu + "/" + x, newpath + "/" + x )
                    print(f"已移动： {x} -> {hz[1:]}/{x}")
                    move = move + 1
                except:
                    print(f"{x} 移动失败，跳过这个文件继续处理下一个")
                    shi = shi + 1
        print("顶层：", os.listdir(mulu))
        print(f"共移动 {move} 个，跳过 {skip} 个，失败 {shi} 个")
    else:
        print("已取消，什么都没改")
main()