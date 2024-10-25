# 关于Github中`pull request`的操作指南

## `pull request`介绍

不过多赘述，详情请见[github官方文档](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

简而言之，大多把它翻译成“拉取请求”（不是很认可，这个翻译很糟糕，但是也没找到什么更恰当的，不如就直接用英语），简称`pr`，是用于请求（仓库所有者或有权限的）将你的`修改`提交至上级仓库或`main`分支之中的。

## 简述标准合作流程（以CDA_Tech_Dept为例）

1. 将仓库`fork`到自己的主页，选择仅`main`分支；
   - 直接点击`Fork`按钮；
2. 将此项目`clone`到本地，进行操作；
   - 在本地新建文件夹，使用下面的命令

   ```git
   git clone https://github.com/usrname/repositoryname
   ```

3. 新建一个分支用于修改，将`main`中内容完整复制仅新的分支，假设命名为`new-feature-branch`;
    - 使用下述命令：

    ```git
    git fetch origin
    git checkout main
    git pull origin main
    git checkout -b new-feature-branch
    git push origin new-feature-branch
    ```

4. 完成后，提交修改至`new-feature-branch`

    ```git
    git add .
    git commit -m "你的提交信息"
    git push origin new-feature-branch
    ```

5. 在Github中点击出现的绿色`Compare&pull request`，选择原仓库的`main`分支进行比对，随后可以`create new pull request`；
6. 完成上步后，原仓库在所有者或拥有修改权限者可以选择直接将你的pr合并至`main`还是先新建分支合并至分支后查看修改再与`main`进行`merge`操作；
7. 至此，一次完整的`pr`操作即完成了。

注：上述代码仅供示例参考，根据实际情况会有所不同。有疑问可自行搜索`CSDN`、`知乎`，或者询问`ChatGPT`、`Copilot`等，也可邮件询问[Alan Zhou](mailto:zhoualan1@icloud.com)。

## 说明与注意事项

由于github比较算法的限制，只允许提交`“修改”`，即在原基础上进行修改而非随意的增加文件，所以你的`pr`流程必须保证是在原项目的基础上也就是说你的提交必须是`全部原内容`+`修改`，单独新建一个分支而不复制main中内容，或是单独push一个文件是不可以进行pr操作的，比较算法将显示nothing to compare并不允许你进行pr操作，反映在界面中便是点击`Compare&pull request`后不会出现`create new pull request`按钮，而是直接重定向回`code`栏，这个过程不会出现任何与无法`pr`的原因相关提示（官方文档作者真应该千刀万剐（bushi））。

----
——By Alan Zhou  
允许成员进行恰当的编辑与补充，允许分享