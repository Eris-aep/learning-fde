import os
def tongji(mingzi):
    tj = {}
    for x in mingzi:
        hz = x.split(".")[-1]
        tj[hz] = tj.get(hz, 0) + 1
    return tj


shuju = ["a.txt", "b.txt", "c.md", "README"]
print(tongji(shuju))