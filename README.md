# Python / Web 学习仓库（FDE 路线）

按**阶段**组织：`python/` 是阶段 1（Python 基础，Day 2–Day 32），`web/` 是阶段 2（Web 开发，2026-11 起）。

## 目录结构

- `python/dayXX/` —— 阶段 1 每日练习：语法、循环、函数、文件读写、异常处理、模块、命令行工具
- `python/reading/` —— 读代码 / 审代码练习（r01–r08，含测试数据）
- `python/review/` —— 语法巩固轮
- `web/` —— 阶段 2 内容（第 1 天起新增）

## 阶段作品：批量文件工具

一个命令搞定「批量加日期前缀」和「按扩展名归档」：

```
cd python/day30
python wenjian_tool.py                              # 不带参数，显示用法
python wenjian_tool.py rename 目标目录              # 加日期前缀
python wenjian_tool.py fenlei 目标目录              # 按扩展名分类
```

安全设计：

- 先预览、输 `y` 才执行，可随时取消
- 可重复运行（幂等），不会叠加第二层前缀
- 目录不存在时给中文提示，不抛 Traceback
- 单个文件失败只跳过它，不中断整批

详细用法与示例输出见 [python/day30/README.md](python/day30/README.md)。

## 运行环境

Python 3，无需安装任何第三方库。
