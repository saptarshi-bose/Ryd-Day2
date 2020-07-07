f = open("Test1.txt", "r")
data = f.read()
x = len(data)
print(x)
i =0
fo = open("Output.txt",'a')
q = False
o = False
p= False
r = False
s= False
t=False
c=False
ans = 2991
cans=1
fo.write('[')
def prq():
    fo.write('\n'+' {'+'\n'+'  '+'"Question"'+': "')
def pra():
    fo.write('  '+'"Option_A"'+': "')
def prb():
    fo.write('  '+'"Option_B"'+': "')
def prc():
    fo.write('  '+'"Option_C"'+': "')
def prd():
    fo.write('  '+'"Option_D"'+': "')
def pran():
    fo.write('   '+'"Answer"'+': "'+data[ans])
while(c==False):
    prq()
    while(i<x-1 and q ==False):
        if(data[i]=='A' and data[i+1]=='.'):
            q=True
            break
        elif(q!=True):
            fo.write(data[i])
            i+=1
    fo.write('",')
    pra()
    while(i<x-1 and o ==False):
        if(data[i]=='B' and data[i+1]=='.'):
            o=True
            break
        elif(o!=True):
            fo.write(data[i])
            i+=1
    fo.write('",')
    prb()
    while(i<x-1 and p ==False):
        if(data[i]=='C'and data[i+1]=='.' ):
            p=True
            break
        elif(p!=True):
            fo.write(data[i])
            i+=1
    fo.write('",')
    prc()
    while(i<x-1 and r ==False):
        if(data[i]=='D' and data[i+1]=='.'):
            r=True
            break
        elif(r!=True):
            fo.write(data[i])
            i+=1
    fo.write('",')
    prd()
    while(i<x-1 and s ==False):
        if(data[i]=='\n'):
            s=True
            break
        elif(s!=True):
            fo.write(data[i])
            i+=1
    fo.write('",')
    i+=2
    fo.write('\n')
    pran()
    cans+=1
    if(cans<10):
        ans=ans+5
    else:
        ans=ans+6
    fo.write('"'+'\n'+'  },'+'\n')
    if(i<x):
        i=i+2
        q = False
        o = False
        p= False
        r = False
        s= False
        t=False
       
    else:
        c=True
fo.write(']')
fo.close()
