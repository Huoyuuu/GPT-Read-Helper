# 辅助使用[Claude v2.0](https://claude.ai)阅读GitHub项目

[English](./README.md) | 中文文档

## 使用示例：

### [chatgpt-mirai-qq-bot Project](https://github.com/lss233/chatgpt-mirai-qq-bot/)
<img src="https://s2.loli.net/2023/07/15/lpe954kwRimj3Gt.png" width="500">
### [teenytinycompiler Project](https://github.com/AZHenley/teenytinycompiler)
<img src="https://s2.loli.net/2023/07/15/dhRoe64iSgkP29W.png" width="500">

## 使用方法：
1. 下载项目源代码到本地。
2. 使用Combiner脚本将源代码整合到名为 `output.txt` 的单个文件中。
3. 将 `output.txt` 文件提供给Claude v2.0进行分析和输出。

## 参考提示：
这是一个GitHub项目的代码整合示例，它以目录结构开头，然后是每个代码文件的具体内容。
我希望您能辅助我理解项目。请阅读代码，先给出总体概述，再总结出50个具体细致的要点，以帮助我理解源代码。每个要点的格式应为：序号 + 表情符号 + 中文描述。

## TODO：
- [ ] 改为通过爬虫提取网站源码，不用将项目下载到本地。
- [ ] 集成为油猴脚本/浏览器插件。
- [ ] 将服务部署在指定服务器上，通过输入GitHub项目链接来使用。

## Combiner脚本说明：
```Python
项目描述：

名称：Combiner.py
描述：该脚本用于自动提取项目下所有文本文件并将内容整合输出到output.txt中。
作者：火雨
日期：23.7.14

使用方法：
将Combiner.py文件放在项目根目录下，在命令行中执行`python Combiner.py`。运行结果将保存在output.txt文件中。

output.txt格式：
1. tree /f生成的树形图
--------
2. 文件1名字及具体内容
--------
3. 文件2名字及具体内容
等等等等

参考提示：
这是一个GitHub项目的代码整合示例，它以目录结构开头，然后是每个代码文件的具体内容。
我希望您能辅助我理解项目。请阅读代码，先给出总体概述，再总结出50个具体细致的要点，以帮助我理解源代码。每个要点的格式应为：序号 + 表情符号 + 中文描述。

注意：
- 在运行时，请确保已正确配置Python环境。
- 脚本将自动提取项目根目录下的所有文本文件，不包括Combiner.py文件本身。
- 对于非文本类文件，将会忽略编码异常UnicodeDecodeError并跳过处理。
