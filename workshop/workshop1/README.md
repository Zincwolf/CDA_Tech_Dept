# CDA行业探索组Workshop1（存档）

## 基本信息

- 主题：玩转量化术语：Python实战指南
- 2024/10/23，13:30 ~ 15:30
- 东中院4-201
- Tutor：Zane Wu， [Zincwolf@outlook.com](mailto:Zincwolf@outlook.com)
- TA：Yu Wang， [wangyv123@sjtu.edu.cn](mailto:wangyv123@sjtu.edu.cn)

## 活动议程

1. 介绍与开场（13:30 - 13:45）
2. 量化术语概述（13:45 - 14:15）
3. Python实战演示（14:15 - 15:30）

## 所需准备

- 个人笔记本电脑
- 安装好[anaconda]([https://](https://www.anaconda.com/))，[vscode](https://code.visualstudio.com/)

## 环境配置

### 手动配置

创建环境并安装必要的Python库，命令如下：

<button onclick="copyToClipboard()">一键复制</button>

<script> function copyToClipboard() { const text = `conda create -n workshop1 python=3.10 conda activate workshop1 pip install numpy pandas openpyxl`; navigator.clipboard.writeText(text).then(() => { alert('已复制到剪贴板'); }).catch(err => { console.error('复制失败', err); }); } </script>

```bash
    conda create -n workshop1 python=3.10
    conda activate workshop1
    pip install numpy pandas openpyxl
```

### 通过脚本配置

在安装好anaconda的前提下，可通过下述命令直接创建虚拟环境：

<button onclick="copyToClipboard()">一键复制</button>

<script> function copyToClipboard() { const text = `conda env create -f environment.yml conda activate workshop1`; navigator.clipboard.writeText(text).then(() => { alert('已复制到剪贴板'); }).catch(err => { console.error('复制失败', err); }); } </script>

```bash
    conda env create -f environment.yml
    conda activate workshop1
```

或者，点击以下链接下载并运行批处理文件（适用于 Windows 用户）或 Shell 脚本（适用于 Mac 用户）来自动配置环境：

1. <a href="./setup_environment.bat" download>下载并运行批处理文件（Windows）</a>

2. <a href="./setup_environment.sh" download>下载并运行Shell脚本（Mac）</a>

## 参考资料

- [Python工具入门：VSCode和Anaconda+v1.0(1)_纯图版](./references/Python工具入门：VSCode和Anaconda+v1.0(1)_纯图版.pdf)
- [Anaconda安装-超详细版(2023) -  CSDN App](https://blog.csdn.net/weixin_43412762/article/details/129599741?sharetype=blogdetail&shareId=129599741&sharerefer=APP&sharesource=2301_81346728&sharefrom=link)
- [vscode安装+配置+使用+调试【保姆级教程】 -  CSDN App](https://blog.csdn.net/weixin_60915103/article/details/131617196?sharetype=blogdetail&shareId=131617196&sharerefer=APP&sharesource=2301_81346728&sharefrom=link)
- [CDA1配置环境1](./references/CDA1配置环境1.pdf)
- [wksp1课件（pdf）](./references/wksp1.pdf)

## 文件说明

- [`data`](./data)文件夹中包含本次workshop所需的数据文件;
- [`notebook`](./notebook)文件夹中[`cda_lab1.ipynb`](./notebook/cda_lab1.ipynb)为本次workshop主要使用的代码及课程任务,[`python_101.ipynb`](./notebook/python_101.ipynb)则是一些`python`基础入门语法和数据结构，以供需要的同学自学；
- [`references`](./references)文件夹包含本次workshop所需的部分参考资料;
- `environment.yml`,`setup_environment.bat`以及`setup_environment.sh`均为使用[使用脚本配置环境](#通过脚本配置)所需.

## 补充

- 创建环境
  - 使用本存档的同学以[本文档中为准](#手动配置);
  - jupyter notebook选择内核时若没有找到创建好的环境, 可以创建本地文件夹并通过code打开后重新选择内核,原因在于vscode必须在确定的项目文件夹中方可创建环境;
  - 若需在vscode中编写并运行py脚本(即`.py`文件), 可通过按下`Crtl`+`Shift`+`P`，找到`Python: 选择解释器(Python: Select Interpreter)`点击并选择创建好的虚拟环境;
- 修正:自由流通比例 = 样本总股本 / 自由流通量 修改为 自由流通量 / 样本总股本;
- 如果追求更高的速度，可以考虑学习汇编语言.

<details>
<summary>来自部长的惊喜链接大礼包！</summary>

- [量化金融岗位介绍](https://sme.cuhk.edu.cn/article/2112)
- [量化金融求职准备](https://sme.cuhk.edu.cn/article/2119)
- [Quant Firm Guide](https://www.thewallstreetquants.com/firm-list)
- [中证1000指数 (000852)](https://www.csindex.com.cn/#/indices/family/detail?indexCode=000852)
- [3小时快学期权（第二版）](https://book.douban.com/subject/35076061/)
- [华尔街见闻：高频量化交易手续费或提升9倍至1元，将挤压部分高频策略空间](https://wallstreetcn.com/articles/3721499#)
- [Figgie](https://www.figgie.com)
- [BigQuant](https://bigquant.com/wiki/doc/5a695bqm44cb5by55ocn44cb5rex5bqm44cb6zug5lit5bqm77ya5bi46keb6auy6akr5zug5a2q5yk5oyh5qch6yc76l6r-zmH0YGSf6P)

</details>
