# 批量文件工具

一句话简介：
一个命令搞定批量改名前缀和按类型归档

## 解决什么问题

手工改名易错、不可逆；文件夹里各种格式混在一起

## 怎么用	

正规格式：在powershell中输入以下：

```
cd 你的存放wenjian_tool.py的路径
python wenjian_tool.py 模式 要执行该模式的路径
```

例子如下：
例子1：
```
PS E:\网页\学习Python> python study/day30/wenjian_tool.py
用法：
     python wenjian_tool.py rename 目录   # 加日期前缀
     python wenjian_tool.py fenlei 目录   # 按扩展名分类
PS E:\网页\学习Python>
```

例子2：
```
PS E:\网页\学习Python>  python study/day30/wenjian_tool.py rename study/day30/test_rename
===进入预览模式===

将改名： a.txt -> 20261117_a.txt
将改名： b.txt -> 20261117_b.txt
将改名： c.md -> 20261117_c.md

预览结束，确认执行吗？输 'y' 继续，其他键取消
请输入：y
a.txt -> 20261117_a.txt
b.txt -> 20261117_b.txt
c.md -> 20261117_c.md
顶层： ['20261117_a.txt', '20261117_b.txt', '20261117_c.md']
共改名 3 个，跳过 0 个, 失败0个
PS E:\网页\学习Python>
```

例子3：
```
PS E:\网页\学习Python>  python study/day30/wenjian_tool.py fenlei study/day30/test_fenlei
===进入预览模式===
将移动： 作文.txt -> txt/作文.txt
没有扩展名，跳过： 归档
将移动： 数据.txt -> txt/数据.txt
将移动： 照片.jpg -> jpg/照片.jpg
将移动： 笔记.md -> md/笔记.md

确认执行吗？输 y 继续，其他键取消
请输入:y
已移动： 作文.txt -> txt/作文.txt
没有扩展名，跳过： 归档
已移动： 数据.txt -> txt/数据.txt
已移动： 照片.jpg -> jpg/照片.jpg
已移动： 笔记.md -> md/笔记.md
顶层： ['jpg', 'md', 'txt', '归档']
共移动 4 个，跳过 1 个，失败 0 个
PS E:\网页\学习Python>
```

错误示范：
```
cd 你的存放wenjian_tool.py的路径
python wenjian_tool.py      （此条错误缺少参数）
python wenjian_tool.py aaaa 要执行该模式的路径      (没有叫aaaa的模式，模式错误)
```

## 安全设计	

1.可以事先预览后确认
2.可重复跑（幂等）
3.对小白萌新友好：目录不存在、模式不存在等等直接给中文提示，不给报错代码。单文件失败，中文显示且不中断程序允许

## 运行环境	

Python 3，无第三方库

## 已知限制	

只处理给定目录的第一层，不进子文件夹
前缀内容是固定值
