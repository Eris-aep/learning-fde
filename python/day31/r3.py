students = [
    {"姓名": "阿强", "分数": 95},
    {"姓名": "小美", "分数": 59},
    {"姓名": "大鹏", "分数": 72},
    {"姓名": "小雨", "分数": 88},
]


def dengji(fen,jige=60):
    if fen >= 90:
        return "优秀"
    elif fen >= jige:
        return "及格"
    else:
        return "不及格"


fenshu = []
for x in students:
    fenshu.append(x["分数"])
px = sorted(fenshu,reverse=True)

total = 0
for t in fenshu:
    total = total + t

for f in px:
    for s in students:
        if f == s["分数"]:
           print(f"{s['姓名']} {s['分数']} {dengji(s['分数'])}")
print("平均分", total / len(students))
print("最高分", px[0])

jgrs = 0
for tj in students:
    if dengji(tj["分数"]) == "不及格":
        pass
    else:
        jgrs += 1
print(f"及格人数 {jgrs}")