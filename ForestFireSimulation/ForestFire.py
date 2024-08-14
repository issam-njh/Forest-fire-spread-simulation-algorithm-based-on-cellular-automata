import matplotlib.pyplot as plt
from copy import deepcopy



def neighborE(i,j,n,Tab):
    if(i==(n-1)): 
        d=0
    else: 
        d=(Tab[i+1][j] - Tab[i][j])/8
    return d


def neighborW(i,j,n,Tab):
    if(i==0):
        g=0 
    else:
        g=(Tab[i-1][j] - Tab[i][j])/8
    return g 


def neighborN(i,j,m,Tab):
    if(j==0):
        h=0
    else:
        h=(Tab[i][j-1] - Tab[i][j])/8
    return h


def neighborS(i,j,m,Tab):
    if(j==m-1):
        b=0
    else:
        b=(Tab[i][j+1] - Tab[i][j])/8
    return b

def neighboring(i,j,n,m,Tab,d,p):
    
    S= neighborE(i,j,n,Tab)
    N= neighborW(i,j,n,Tab)
    W=neighborN(i,j,m,Tab)
    E=neighborS(i,j,m,Tab)
    
    (E,W,N,S)=windInfluence(d,p,E,W,S,N)
    
    
    return( E + W + N + S)
    
    
        

def isOnFire(T):
    n=len(T[0][:])
    m=len(T[:][0])
    Tab = [[0 for x in range(m)] for y in range(n)]
    for i in range(n):
        for j in range(m):
            if T[i][j]>=250:
                Tab[i][j]=1
    return(Tab)

def burningCell(T1,T2):
    
    n=len(T1[0][:])
    m=len(T1[:][0])
    for i in range(n):
        for j in range(m):
            if T2[i][j]==1 and T1[i][j]<600:
                T1[i][j]+=20
    return(T1)
    
    
def windInfluence(d,p,E,W,S,N):
    p=p/60
    if d == "S":
        S=S-S*p
        N=N+N*p
    elif d == "N":
        N=N-N*p
        S=S+S*p
    elif d == "E":
        E=E-E*p
        W=W+W*p
    elif d == "W":
        W=W-W*p
        E=E+E*p
    
    return (E,W,N,S)
    
    

def automateCellulaire(T,d,p):
    n=len(T[0][:])
    m=len(T[:][0])
    Tab= deepcopy(T)
    Tfire = isOnFire(T)
    for i in range(n):
        for j in range(m):
            if Tfire[i][j]==0:
                Tab[i][j]=T[i][j]+neighboring(i,j,n,m,T,d,p)
    
    Tab = burningCell(Tab , Tfire)
    return(Tab)
    
def fireSpread(T,x,d,p):
    Tab= automateCellulaire(T,d,p)
    for i in range(x//20):
        for j in range(20):
            Tab= automateCellulaire(Tab,d,p)   
        plt.matshow(Tab)
        plt.colorbar()
        plt.show()

        
              









