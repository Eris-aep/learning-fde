import os
import datetime

mulu = "python/reading/review_data2"
qz = datetime.datetime.now().strftime("%Y%m%d") + "_"

for name in os.listdir(mulu):
    old = mulu + "/" + name
    new = mulu + "/" + qz + name
    try:
        os.rename(old, new)
    except:
        pass
print("处理完成")
