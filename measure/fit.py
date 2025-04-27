import numpy as np
import matplotlib.pyplot as plt

result = []
with open('measure/data.csv', 'r') as f:
    for line in f:
        a, b = map(float, line.strip().split(','))
        result.append([a, b])

x, y = [], []
for cnt in result:
    x.append(cnt[0])
    y.append(cnt[1])

# print("x数组:", x)
# print("y数组:", y)

# 拟合一个二次多项式（可以改变拟合阶数）
mi = 8
coefficients = np.polyfit(x, y, mi)
poly = np.poly1d(coefficients)

expr = ""
for i, coef in enumerate(coefficients):
    power = mi - i
    if power == 0:
        expr += f"{coef:.6f}"
    elif power == 1:
        expr += f"{coef:.6f}x + "
    else:
        expr += f"{coef:.6f}x^{power} + "
expr = expr.rstrip(" + ")
print(f"拟合的多项式为: {expr}")

# 打印拟合的多项式解析式
# print(f"拟合的二次多项式为: y = {coefficients[0]}x² + {coefficients[1]}x + {coefficients[2]}")
# print(f"拟合的一次多项式为: y = {coefficients[0]}x + {coefficients[1]}")

# 生成拟合曲线
x_fit = np.linspace(min(x), max(x), 100)
y_fit = poly(x_fit)

# 绘制结果
plt.scatter(x, y, color='red', label='Data')
plt.plot(x_fit, y_fit, label='Fit', color='blue')

plt.legend()
plt.show()
