import os
import datetime

mulu = "study/day28/test_files"
qian = datetime.datetime.now().strftime("%Y%m%d") + "_"
print("前缀是：", qian)
print()
print("=== 预览模式：只显示要改什么，一个文件都不动 ===")
for name in os.listdir(mulu):
    if name[:len(qian)] == qian:
        print("已加过前缀，跳过：", name)
    else:
        print("将改名：", name, "->", qian + name)
