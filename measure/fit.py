import numpy as np
import matplotlib.pyplot as plt

# 假设你有一些坐标数据
x = np.array([0, 50, 100, 150, 200, 250, 300])
y = np.array([1280, 1240, 1158, 1033, 855, 598, 189])

for i in range(len(y)):
    y[i] -= 1280
    y[i] = -y[i]

# 拟合一个二次多项式（可以改变拟合阶数）
coefficients = np.polyfit(x, y, 2)  
poly = np.poly1d(coefficients)

# 打印拟合的多项式解析式
print(f"拟合的二次多项式为: y = {coefficients[0]}x² + {coefficients[1]}x + {coefficients[2]}")

# 生成拟合曲线
x_fit = np.linspace(min(x), max(x), 100)
y_fit = poly(x_fit)

# 绘制结果
plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x_fit, y_fit, label='Fitted Curve', color='blue')
plt.legend()
plt.show()
