import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [ 1, 4, 9, 16, 25]
plt.style.use('seaborn')
fig, ax = plt.subplots()  #subplots()方法可以在一张图片中绘制一个或多个图表
ax.plot(input_value, squares, linewidth=3)  #尝试根据给出的数据制定图表

#设置图表标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

#设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)
#汉字字体
plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']

plt.show()  #打开Matplotlib的绘图显示器
