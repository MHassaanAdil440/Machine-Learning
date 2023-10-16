#importing libraries
import numpy as np
import matplotlib.pyplot as plt

#initializing training set
#x_train is the input variable(size in square feet)
#y_train is the target(price in 1000s of dollars)
x_train = np.array([2.0,5.0,8.0])
y_train = np.array([300.0,500.0,750.0])
print(f"x_train: {x_train}")
print(f"y_train: {y_train}")

#plotting a scatter plot graph of the dataset
plt.scatter(x_train,y_train,c='r',marker='x')
plt.title('Housing Price')
plt.xlabel('Size(in sqrft)')
plt.ylabel('Price(in 1000s of dollars)')
plt.show()

w = 100
b = 0
print(f"w: {w}")
print(f"b: {b}")

#function to compute the prediction of the linear model
def Property_price_model(w,x,b):
    m = x.shape[0]
    y_hat = np.zeros(m)
    for i in range(m):
        y_hat[i] = w*x[i]+b
    return y_hat

y_hat = Property_price_model(w,x_train,b)
plt.plot(x_train,y_hat,c='b',label='Our Prediction')
plt.scatter(x_train,y_train,marker='x',c='r',label='Actual values')
plt.xlabel('Size(in sqrft)')
plt.ylabel('Price(in 1000s of dollars)')
plt.legend()
plt.show()