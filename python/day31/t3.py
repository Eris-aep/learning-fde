students = [
    {"姓名": "小明", "分数": 92},
    {"姓名": "小红", "分数": 78},
    {"姓名": "小刚", "分数": 55},
    {"姓名": "小丽", "分数": 88},
    {"姓名": "小华", "分数": 61},
]

# 1.
def dengji(fen, jige=60):
    if fen >= 90:
        return "优秀"
    elif fen >= jige:
        return "及格"
    else:
        return "不及格"
# 2.
fenshu = []
for s in students:
    fenshu.append(s["分数"])
pai = sorted(fenshu, reverse=True)

total = 0
for s in students:
    total = total + s["分数"]

for f in pai:
    for s in students:
        if s["分数"] ==f:
            print(s["姓名"],s["分数"],dengji(s["分数"]))
print("平均分：", total / len(students))
print("总分:", total)
dengji(55)
