import json
import math

def load_journal(name):
    f=open(name)
    jdata=f.read()
    data=json.loads(jdata)
    f.close()

    return data

def compute_phi(name,event):
    data=load_journal(name)

    n11=n00=n10=n01=n1_=n0_=n_1=n_0=0

    for i in data:
        if event in i['events']:
            if(i['squirrel']==True):
                n11+=1
            else:
                n10+=1
        else:
            if(i['squirrel']==True):
                n01+=1
            else:
                n00+=1

    n1_=n11+n10
    n0_=n00+n01
    n_1=n01+n11
    n_0=n00+n10

    phi=((n11*n00)-(n10*n01))/math.sqrt(n1_*n0_*n_1*n_0)
    return phi

def compute_correlations(name):
    data=load_journal(name)
    d={}

    for i in data:
        for j in i['events']:
            if j not in d:
                d[j]=compute_phi(name,j)

    return d

def diagnose(name):
    d=compute_correlations(name)

    a=min(d,key=d.get)
    b=max(d,key=d.get)
    
    return b,a