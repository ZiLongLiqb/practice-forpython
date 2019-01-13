import numpy as np 
import matplotlib.pyplot as plt 
import random

dot=np.array([[0,0],[1,0],[1/2,np.sqrt(3)/2]])
l=list()
for item in dot:
	l.append(item)
now=[1/2,0]
p=np.random.rand(1,10000)
def get_random(k):
	if k<1/3:
		return 0
	elif k>=1/3 and k<2/3:
		return 1
	else:
		return 2
for k in p[0]:
	l.append(now)
	pra=get_random(k)
	new_dot=(dot[pra]+now)/2
	now=new_dot
plt.figure()
x=[]
y=[]
for k in l:
	x.append(k[0])
	y.append(k[1])
plt.scatter(x,y,s=0.5)
ax=plt.gca()
ax.set_aspect(1)
plt.show()
