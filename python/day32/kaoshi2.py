import os


def du(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()            


def suan(lines):
    mingzi = []
    zongfen = []                       
    for line in lines:                  
        line = line.strip()             
        if line == "":                  
            continue                 
        parts = line.split(",")        
        mingzi.append(parts[0])         
        zongfen.append(int(parts[1]) + int(parts[2]) + int(parts[3]))  
    return mingzi, zongfen              


def zui_gao(zongfen):                   
    best = 0                            
    for z in zongfen:                   
        if z > best:                    
            best = z
    return best


def pingjun(zongfen):
    total = 0
    for z in zongfen:
        total = total + z
    return total / len(zongfen)


def xie(path, mingzi, zongfen):
    best = zui_gao(zongfen)
    with open(path, "w", encoding="utf-8") as f:
        for i in range(len(mingzi)):
            f.write(mingzi[i] + " " + str(zongfen[i]) + "\n")
        f.write("最高分 " + str(best) + "\n")
        f.write("平均分 " + str(pingjun(zongfen)))


def main():
    lines = du("python/day32/chengji.txt")
    mingzi, zongfen = suan(lines)
    print("人数", len(mingzi))
    print("平均分", pingjun(zongfen))
    xie("python/day32/baogao.txt", mingzi, zongfen)


main()
