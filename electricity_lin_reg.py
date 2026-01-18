import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def cost(x,y,w,b):
    m=len(x)
    cost_t=0
    for i in range(m):
        f_x=w*x[i]+b
        cost_t+=(f_x-y[i])**2
    cost_t/=(2*m)
    return cost_t
def gradient(x,y,w,b):
    m=len(x)
    df=0
    dw=0
    for i in range(m):
        f_x=w*x[i]+b
        df+=f_x-y[i]
        dw+=(f_x-y[i])*x[i]
    df/=m
    dw/=m
    return df,dw
def final(x,y,w,b,alpha,iterations,df,dw):
    cost_final=[]
    for i in range(iterations):
        df,dw=gradient(x,y,w,b)
        w=w-alpha*dw
        b=b-alpha*df
        cost_final.append(cost(x,y,w,b))
        if i % 100 == 0:
           print(f"Iteration {i}: Cost={cost_final[-1]:.4f}, w={w:.4f}, b={b:.4f}")
    return w,b,cost_final

data=pd.read_csv('electricity_bill_data.csv')
x=data.iloc[:,0]
y=data.iloc[:,1]
plt.xlabel("Units consumed")
plt.ylabel("Price")
plt.title("ELECTRICITY BILL")
plt.scatter(x,y,marker="+")
# plt.show()
b=0
w=0
cost(x,y,w,b)
df,dw=gradient(x,y,w,b)
iterations=3000
alpha=0.000001
w_f,b_f,cost_f=final(x,y,w,b,alpha,iterations,df,dw)
y_f=w_f*x+b_f
plt.plot(x,y_f,color="red")
plt.legend(x,y)
plt.show()
# unit=int(input("Enter Units to see Price:"))
# y_f=w_f*unit+b_f
# print(f"Price of {unit} = {y_f}")
# from sklearn.metrics import  r2_score
# r2 = r2_score(y, y_f)
# print(f"R² Score: {r2:.4f}")

