ci = ["苹果", "香蕉", "苹果", "橙子", "香蕉", "苹果", "西瓜", "橙子", "苹果"]
tjb = {}

for x in ci:
    if x in tjb:
        tjb[x] = tjb[x] + 1
    else:
        tjb[x] = 1
for k in tjb:
    print(k,tjb[k],"次")

zui = ""
zui_n = 0
for a in tjb:
    if tjb[a] > zui_n:
        zui = a
        zui_n = tjb[a]
print(f"出现最多：{zui},{zui_n}次")