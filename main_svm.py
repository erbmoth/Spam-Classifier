# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import scipy.io as sp_io
import matplotlib.pyplot as plt
from sklearn import svm



data=sp_io.loadmat("ex6data2.mat")
X=np.zeros((51,3))
Y=np.zeros((51,))
x=data['X']
Y=data['y']
k=(Y==1)
plt.scatter(x[k[:,0],0],x[k[:,0],1],marker='+',color='black')
k=(Y==0)
plt.scatter(x[k[:,0],0],x[k[:,0],1],marker='o',color='yellow',)

sigma=0.2

clf=svm.SVC(kernel='rbf',C=1000,gamma=4)
clf.fit(x,Y)

x1_min,x1_max=x[:,0].min(),x[:,0].max()
x2_min,x2_max=x[:,1].min(),x[:,1].max()
h=0.02
xx1,xx2=np.meshgrid(np.arange(x1_min,x1_max,h),np.arange(x2_min,x2_max,h))


Z=clf.predict(np.c_[xx1.ravel(),xx2.ravel()])


Z = Z.reshape(xx1.shape)
plt.contour(xx1, xx2, Z, cmap=plt.cm.Paired)
plt.show()

pred=clf.predict(x)

print("accuracy="+str(np.mean(pred==Y.ravel())*100))








