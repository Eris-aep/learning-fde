with open("python/day31/rizhi.txt", "r", encoding="utf-8")as f:
    lines = f.readlines()
    jieguo = []
    U_true = []
    for x in lines:
        if "错误" in x:
            jieguo.append(x)
        else:
            U_true.append(x)
    print(f"共 {len(lines)} 行，错误 {len(jieguo)} 行，正常 {len(U_true)} 行")

with open("python/day31/errors.txt", "w", encoding="utf-8")as f:
    for x in jieguo:
        f.write(x)

with open("python/day31/ok.txt", "w", encoding="utf-8")as f:
    for x in U_true:
        f.write(x)