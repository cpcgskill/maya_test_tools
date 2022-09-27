# maya_test_tools

maya 测试工具包

## 目录

- [快速开始](#快速开始)
    * [安装](#安装)
    * [使用](#使用)
- [版权说明](#版权说明)

## 快速开始

### 安装

注意下方的python是你的Python, 正常情况下可以直接通过python调用, 而Maya的python一般是C:\Program
Files\Autodesk\<Maya版本>\bin\mayapy.exe

```commandline
python -m pip install maya-test-tools
```

在windows下maya的安装例子

注意:

1. 请将Maya路径替换为自己的。
2. 请使用cmd

```commandline
"C:\Program Files\Autodesk\Maya2018\bin\mayapy.exe" -m pip install cpmel
```

### 使用

#### 打开文件

```python
from maya_test_tools import open_file

open_file('maya file path')
```

### 在命令行下询问是否用maya gui打开当前场景.

```python
from maya_test_tools import question_open_maya_gui

question_open_maya_gui()
```

## 版权说明

该项目签署了Apache-2.0 授权许可，详情请参阅 LICENSE




