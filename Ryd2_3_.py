f = open("Test.txt", "r")
data = f.read()
x = len(data)
i =0
fo = open("Output.txt",'a')
p= False
c=False
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
    fo.write('  '+'"Answer"'+': "')
while(c==False):
    prq()
    while(i<x and p==False):
        if(data[i]=='\n' and data[i+1]=='(' and data[i+2]=='a' and data[i+3]==')'):
            p=True
            i+=1
            break
        else:
            fo.write(data[i])
        i+=1  
    fo.write('",'+'\n')
    pra()
    while(i<x):
        if(data[i]=='\n'):
            i=i+1
            break
        else:
            fo.write(data[i])
        i+=1
    fo.write('",'+'\n')
    prb()
    while(i<x):
        if(data[i]=='\n'):
            i=i+1
            break
        else:
            fo.write(data[i])
        i+=1
    fo.write('",'+'\n')
    prc()
    while(i<x):
        if(data[i]=='\n'):
            i=i+1
            break
        else:
            fo.write(data[i])
        i+=1
    fo.write('",'+'\n')
    prd()
    while(i<x):
        if(data[i]=='\n'):
            i=i+1
            break
        else:
            fo.write(data[i])
        i+=1
    fo.write('",'+'\n')
    pran()
    while(i<x):
        if(data[i]=='\n'):
            i=i+1
            break
        else:
            fo.write(data[i])
        i+=1
    fo.write('"'+'\n'+' },')
    if(i<x):
        i=i+1  
        p= False  
    else:
        c=True
fo.write(']')
fo.close()
f.close()