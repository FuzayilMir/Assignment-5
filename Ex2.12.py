import numpy as np
import matplotlib.pyplot as plt



def dir_vec(P,Q):
  return P-Q



#Generate line points
def line_gen(P,Q):
  len =10
  dim = P.shape[0]
  x_PQ = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = P + lam_1[i]*(Q-P)
    x_PQ[:,i]= temp1.T
  return x_PQ

def tri_vert(p,q,r):
  a = (p**2 + r**2-q**2 )/(2*p)
  b = np.sqrt(r**2-a**2)
#Triangle vertices
  P = np.array([a,b]) 
  Q = np.array([0,0]) 
  R = np.array([p,0]) 
  return  P,Q,R


def line_dir_pt(m,P, dim):
  len = 10
  dim = P.shape[0]
  x_PQ = np.zeros((dim,len))
  lam_1 = np.linspace(0,10,len)
  for i in range(len):
    temp1 = P + lam_1[i]*m
    x_PQ[:,i]= temp1.T
  return x_PQ





#Triangle sides
p = 3.5
q = 4
r = 4

#Coordinates of P
a = (p**2 + r**2-q**2 )/(2*p)
b = np.sqrt(r**2-a**2)
print(a,b)
#Triangle vertices
P = np.array([a,b]) 
Q = np.array([0,0]) 
R = np.array([p,0]) 

#Generating all lines
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_PR = line_gen(P,R)

#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_PR[0,:],x_PR[1,:],label='$PR$')

plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'P')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 - 0.2), Q[1] * (1) , 'Q')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.03), R[1] * (1 - 0.1) , 'R')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

plt.axis('equal')
