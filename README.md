# Python 学习仓库（FDE 路线）

每天一个 `dayXX` 目录，记录 Python 基础的练习与阶段作品；`study/reading/` 放读代码、审代码的练习素材。

## 目录结构

- `study/day01` ~ `study/day30` —— 每日练习（语法、循环、函数、文件、异常、模块）
- `study/reading/` —— 读代码 / 审代码练习
- `study/day30/wenjian_tool.py` —— 阶段作品：批量文件工具

## 阶段作品：批量文件工具

一个命令搞定「批量加日期前缀」和「按扩展名归档」：

```
python study/day30/wenjian_tool.py rename 目标目录   # 加日期前缀
python study/day30/wenjian_tool.py fenlei 目标目录   # 按扩展名分类
python study/day30/wenjian_tool.py                   # 不带参数，显示用法
```

安全设计：

- 先预览、输 `y` 才执行，可随时取消
- 可重复运行（幂等），不会叠加第二层前缀
- 目录不存在时给中文提示，不抛 Traceback
- 单个文件失败只跳过它，不中断整批

详细用法与示例输出见 [study/day30/README.md](study/day30/README.md)。

## 运行环境

Python 3，无需安装任何第三方库。
