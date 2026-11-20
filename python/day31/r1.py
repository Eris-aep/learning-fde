shuiguo = ["苹果", "梨", "苹果", "香蕉", "梨", "苹果", "西瓜"]
tj = {}

for s in shuiguo:
    if s in tj:
        tj[s] = tj[s] + 1
    else:
        tj[s] = 1
for k in tj:
    print(k,tj[k],"次")
zui = ""
zui_n = 0
for a in tj:
    if tj[a] > zui_n:
        zui = a
        zui_n = tj[a]
print("出现最多：",zui,zui_n,"次")
print("不同的词有", len(tj),"种")