import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 500)

def f(x):
    return 6.28 * x + 15 + 30.45 * np.sin(1.48 * x - 2.6)

y_true = np.array([26.7, 31.6, 34.4, 48.6, 48.7, 20.7, 71.7, 149.6, 86, 59.9, 66.2])

y_pred = []

for i in range(11):
    print(f(i), i)
    y_pred.append(f(i))

y_pred_arr = np.array(y_pred)

accuracy = np.mean(np.abs((y_true - y_pred_arr) / y_true)) * 100

percentageChange = ((f(20)-y_true[0])/y_true[0])*100 

plt.figure(figsize=(10, 6))
plt.text(-1, 150, f"Nøyaktighet: {accuracy}%")
plt.text(-1, 140, f"Endring mellom ({y_true[0]} and {f(20)}) = {percentageChange}%")
plt.plot(x, f(x), label=r'$F(x) = 6.28x + 15 + 30.45\sin(1.48x - 2.6)$', color='blue')
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], y_pred, 'ro')
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [26.7, 31.6, 34.4, 48.6, 48.7, 20.7, 71.7, 149.6, 86, 59.9, 66.2], 'go')
plt.plot([20], [f(20)], 'yo')
plt.title('Graph of $F(x) = 6.28x + 15 + 30.45\sin(1.48x - 2.6)$')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.show()