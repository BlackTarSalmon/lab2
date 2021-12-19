def t1(i):
    i = str(i)
    return i == i[::-1]

def t2(l):
    d2 = []
    d3 = []
    d5=[]
    for i in l:
        if i%2 == 0:
            d2.append(i)
        if i%3 == 0:
            d3.append(i)
        if i%5 == 0:
            d5.append(i)
    return [d2,d3,d5]

def t3(i):
    o = 0
    if i < 0:
        end = -1
        i *= -1
    else:
        end = 1
    while i != 0:
        t = i%10
        o = o*10 + t
        i //= 10
    o *= end
    return o

def t4(x, a, n, step=0):
    #print(x)
    if n == step:
        return x
    else:
        step += 1
        x = ((n-1)*x + a/pow(x,(n-1)))/n
        return t4(x,a,n,step)

def t5(i):
    if i > 1:
        for x in range(2, int(i/2)+1):
            if i%x == 0:
                return False
    return True

print(t1(202))

x = t2([2,3,5,10,9,7,15])
for i in x:
    print(i)

print(t3(-223523501))
print(t4(2,34,5))
print(t5(7884))