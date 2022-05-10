from ast import excepthandler
from numpy import cross, dot

from js import document,alert
     
def get_vector(A,B):
    V = ()
    for i in range(len(A)):
        V = V + (B[i]-A[i],)
    return V

def calculate_volume(A,B,C,D):
    try:
        vAB, vAC, vAD = get_vector(A,B), get_vector(A,C), get_vector(A,D)   
        ABxAC = cross(vAB,vAC)
        return (dot(ABxAC,vAD) / 6)
    except:
        raise Exception("Invalid Data")
    
def convert(*ags, **kws):
    
    try:
        A = document.getElementById('coordinate1').value;
        B = document.getElementById('coordinate2').value;
        C = document.getElementById('coordinate3').value;
        D = document.getElementById('coordinate4').value;
    
    
        result=abs(calculate_volume(eval(A),eval(B),eval(C),eval(D)))
        pyscript.write("result",result)    
    except:
        pyscript.write("result","Invalid INPUT")    