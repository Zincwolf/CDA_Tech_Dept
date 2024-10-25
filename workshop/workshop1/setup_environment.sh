#!/bin/bash
conda env create -f ./environment.yml
source activate workshop1
echo "已成功创建环境"
read -p "按任意键继续..."