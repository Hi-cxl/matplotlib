#在windows系统中安装matplotlib
#1.下载matplotlib安装程序
#2.将.whl的文件复制到你的项目文件夹，打开命令窗口，切换到项目文件夹，使用pip安装
#3.python -m pip install --user matplotlib-3.0.3-cp37-cp37m-manylinux1_x86_64.whl
#测试matplotlib，输入python，输入import matplotlib 如果没有出现任何错误消息，就说明你的系统安装了matplotlib


#导入模块pyplot，并给它指定别名plt
import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares= [1,4,9,16,25]
plt.plot(input_values, squares, linewidth=5)

#设置图标标题，并给出坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

#plt.show()打开matplotlib查看器，并显示绘制的图形
plt.show()