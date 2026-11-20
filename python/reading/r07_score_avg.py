def du(path):
    with open(path, "r", encoding="utf-8")as f:
        lines = f.readlines()
    return lines


def zongfen(path):
    total = 0
    n = 0
    try:
        for line in du(path):
            name, fen = line.strip().split(",")
            total = total + int(fen)
            n = n + 1
    except:
        pass
    return total / n


print(zongfen("python/reading/score_data/fenshu.txt"))
