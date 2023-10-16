import numpy as np
import matplotlib.pyplot as plt

# w = 0.5
b = 0

x = np.array([1,2,3])
y = np.array([1,2,3])

def line(w,x,b):
    m = x.shape[0]
    y_hat = np.zeros(m)
    for i in range(m):
        y_hat[i] = w*x[i]+b
    return y_hat

y_hat1 = line(1,x,b)
y_hat2 = line(0.5,x,b)
y_hat3 = line(0,x,b)
y_hat4 = line(-0.5,x,b)
# y_hat4 = line(,x,b)

plt.plot(x,y_hat1,label='Line 1', color='pink')
plt.plot(x,y_hat2,label='Line 2', color='purple') 
plt.plot(x,y_hat2,label='Line 3', color='yellow') 
plt.plot(x,y_hat3,label='Line 4', color='blue')
plt.scatter(x,y,marker='x',c='r', label='Actual value')
plt.title('My Graph')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()


