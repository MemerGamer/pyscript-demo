import numpy as np #vektormuveletekhez szukseges csomag
import math as m
from js import document,alert

def Terfogat(A,B,C,D):
    vAB = getVect(A,B)
    vAC = getVect(A,C)
    vAD = getVect(A,D)
    
    ABxAC = np.cross(vAB,vAC)
    #print(ABxAC)
    nevezo = np.dot(ABxAC,vAD)
    V = nevezo / 6
    return V

def getVect(A,B):
    V = ()
    for i in range(len(A)):
        V = V + (B[i]-A[i],)
    return V

def convert(*ags, **kws):
    A = document.getElementById('coordinate1').value;
    B = document.getElementById('coordinate2').value;
    C = document.getElementById('coordinate3').value;
    D = document.getElementById('coordinate4').value;

    result = Terfogat(A,B,C,D)
    pyscript.write("result",result)