def cost(w,b,x,y):
    m=len(x)
    total=0
    for i in range(m):
        f_X=w*x[i]+b
        total+=(f_X-y[i])**2
    total/=(2*m)
    return total
def gradient(w,b,x,y):
    df=0
    dw=0
    m=len(x)
    for i in range(m):
        f_x=w*x[i]+b
        df+=f_x-y[i]
        dw+=(f_x-y[i])*x[i]
    df/=m
    dw/=m
    return df,dw
def final_loop(w,x,y,b,dj,dw,iteration,alpha):
    cost_history=[]
    for i in range(iteration):
        dj,dw=gradient(w,b,x,y)
        w=w-alpha*dw
        b=b-alpha*dj
        cost_history.append(cost(w,b,x,y))
        if i % 100 == 0:  # print every 100 iterations
            print(f"Iteration {i}: Cost={cost_history[-1]:.4f}, w={w:.4f}, b={b:.4f}")
    return w,b,cost_history
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('student_scores.csv')
x=data.iloc[:,0]
y=data.iloc[:,1]
plt.scatter(x,y,color="blue",marker="*")
plt.xlabel("student study hours")
plt.ylabel("Student scores")
plt.title("Study Hours vs Score")
# plt.show()
b=0
w=0
# cost_i=cost(w,b,x,y)
# print(cost_i)
dj,dw=gradient(w,b,x,y)
iteration=1500
alpha=0.01
w_f,b_f,cost_history=final_loop(w,x,y,b,dj,dw,iteration,alpha)
y_predict=w_f*x+b_f
plt.plot(x,y_predict,color="red")
study_hours = 7
predicted_score = w_f * study_hours + b_f
print(f"Predicted score for {study_hours} study hours: {predicted_score:.2f}")
plt.show()




