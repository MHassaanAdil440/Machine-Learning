import numpy as np

def Property_price_model(w,x,b):
    m = x.shape[0]
    y_hat = np.zeros(m)
    for i in range(m):
        y_hat[i] = w*x[i]+b
    return y_hat

def cost_function(y_hat, y):
    m = y_hat.shape[0]
    single_cost = np.zeros(m)
    for i in range(m):
        single_cost[i] = (y_hat[i] - y[i])**2
    cost_sum = np.sum(single_cost)
    cost = (1/(2*m))*cost_sum
    return cost
