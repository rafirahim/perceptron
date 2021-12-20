import numpy as np

def hardlim(w1,w2,x1,x2,b):
    a=w1*x1+w2*x2+b
    if a>0:
        return 1
    else:
        return 0

x=np.array([[0,0],[0,1],[1,0],[1,1]])

w1=np.random.random()
w2=np.random.random()
b=-0.5

print(" Initial weights:")
print(" W1 : ",w1)
print(" W2 : ",w2)
y_predict=np.array([0,1,1,1])
y=[0,0,0,0]

for j in range(2):
    for i in range (len(x)):
        y[i]=hardlim(w1,w2,x[i][0],x[i][1],b)
        error=y_predict[i]-y[i]
        w1=w1+0.1*error*x[i][0]
        w2=w2+0.1*error*x[i][1]
print(" Initial output:")
print(" Y =",y)


print(" Final weights:")

print(" W1 =",w1)
print(" W2 =",w2)
