import numpy  # 科学计算
import sklearn  # 机器学习
import scipy
'''
Scipy是一个用于数学、科学、工程领域的常用软件包，
可以处理插值、积分、优化、图像处理、常微分方程
数值解的求解、信号处理等问题。它用于有效计算Numpy矩阵，
使Numpy和Scipy协同工作，高效解决问题。
'''
from sklearn.neighbors import KNeighborsClassifier  # KNN分类模型（近邻算法）
x_train = [[185, 80, 43], [170, 70, 41], [163, 45, 36],
           [165, 55, 39], [156, 41, 35]]  # 身高，体重，鞋子大小
y_train = ["男人", "男人", "女人", "男人", "女人"]

# 机器学习并训练数据，自己建立模型预测
knn = KNeighborsClassifier(2)  # 两个父类
knn.fit(x_train, y_train)  # 用已有数据，训练机器
print(knn.predict([[170, 85, 41], [175, 73, 40], [172, 42, 37]]))
