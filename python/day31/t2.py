import os
with open("python/day31/rizhi.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    shu = 0
    jieguo = []
    for x in lines:
        if "错误" in x:
            jieguo.append(x)
            shu += 1
    print(f"共 {len(lines)} 行, 筛出 {shu} 行")

with open("python/day31/errors.txt", "w", encoding="utf-8") as f:
    for x in jieguo:
        f.write(x)