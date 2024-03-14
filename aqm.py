#Complete Queen-Mclesky method with don't cares for 2,3,4 variables
def bin(n,nn):
    s=''
    for j in range(nn,-1,-1):
        c=int(n/2**j)
        if n>=2**j:
            n-=2**j
        s+=str(c)
    return s
def exp4(p,vb):
    expl=[]
    expos=[]
    l4=['A','B','C','D','(A^)','(B^)','(C^)','(D^)']
    l3=['A','B','C','(A^)','(B^)','(C^)']
    l2=['A','B','(A^)','(B^)']
    if vb==4:
        l=l4
    elif vb==3:
        l=l3
    else:
        l=l2
    l_2=[]
    for i in range(vb-1,-1,-1):
        l_2.append(2**i)
    for i in p:
        d_l=[]
        ll=i[0]
        b=bin(ll,vb-1)
        if len(i)==8:
            d_l.append(i[1]-i[0])
            d_l.append(i[2]-i[0])
            d_l.append(i[4]-i[0])
            for k in l_2:
                if k not in d_l:
                    break
            for i in range(len(l_2)):
                if k==l_2[i]:
                    break
            for sl in range(len(b)):
                b=list(b)
                if sl!=i:
                    b[sl]='_'
            for sl in range(len(b)):
                if b[sl]=='0':
                    expl.append(l[sl+vb])
                    expos.append(l[sl])
                elif b[sl]=='1':
                    expl.append(l[sl])
                    expos.append(l[sl+vb])
        elif len(i)==4:
            il=[]
            d_l.append(i[1]-i[0])
            d_l.append(i[2]-i[0])
            for k in l_2:
                if k not in d_l:
                    il.append(l_2.index(k))
            for sl in range(len(b)):
                b=list(b)
                if sl not in il:
                    b[sl]='_'
            ss=''
            pos_t=[]
            for sl in range(len(b)):
                if b[sl]=='0':
                    ss+=l[sl+vb]
                    pos_t.append(l[sl])
                elif b[sl]=='1':
                    ss+=l[sl]
                    pos_t.append(l[sl+vb])
            expos.append('+'.join(pos_t))
            expl.append(ss)
        elif len(i)==2:
            il=[]
            d_l.append(i[1]-i[0])
            for k in l_2:
                if k not in d_l:
                    il.append(l_2.index(k))
            for sl in range(len(b)):
                b=list(b)
                if sl not in il: 
                    b[sl]='_'
            ss=''
            pos_t=[]
            for sl in range(len(b)):
                if b[sl]=='0':
                    ss+=l[sl+vb]
                    pos_t.append(l[sl])
                elif b[sl]=='1':
                    ss+=l[sl]
                    pos_t.append(l[sl+vb])
            expos.append('+'.join(pos_t))
            expl.append(ss)
        else:
            ss=''
            pos_t=[]
            for sl in range(len(b)):
                if b[sl]=='0':
                    ss+=l[sl+vb]
                    pos_t.append(l[sl])
                elif b[sl]=='1':
                    ss+=l[sl]
                    pos_t.append(l[sl+vb])
            expos.append('+'.join(pos_t))
            expl.append(ss)
    laexp='+'.join(expl)
    lapos=')*('.join(expos)
    lapos+=')';lapos='('+lapos
    return [laexp,lapos]
def n_b(s):
    c=0
    for i in s:
        if i=='1':
            c+=1
    return c
v_b=int(input("Enter the number of variables:"))
mml=[]
d_c=[]
m_l=[]
while 1:
    n=int(input("Enter the minterms: "))
    if n<0 or n>2**v_b-1:
        break
    mml.append(n)
    m_l.append(n)
mml.sort()
mml=list(set(mml))
print("Don't Cares")
while 1:
    n=int(input("Enter the minterms: "))
    if n<0 or n>2**v_b-1:
        break
    if n in mml:
        print("Minterm already entered as Not don't care")
        print("Please use correct input")
        continue
    d_c.append(n)
    m_l.append(n)
m_l.sort()
m_l=list(set(m_l))
d_c=list(set(d_c))
pi=[]
ch2=[]
ch3=[]
ch=[]
pl=[]
ql=[]
ol=[]
l2=[8,4,2,1]
di={}
for h in range(5):
    di[h]=[]
pld={}
for h in range(4):
    pld[h]=[]
qld={}
for h in range(3):
    qld[h]=[]
old={}
for h in range(2):
    old[h]=[]
for i in m_l:
    b=bin(i,v_b-1)
    k=n_b(b)
    di[k].append(i)
if v_b>1:
    for i in range(v_b):
        for i1 in range(len(di[i+1])):
            for i2 in range(len(di[i])):
                b_c=di[i+1][i1]
                s_c=di[i][i2]
                if (b_c-s_c) in l2 and b_c>s_c:
                    if b_c not in ch:
                        ch2.append(b_c)
                    if s_c not in ch:
                        ch2.append(s_c)
                    t1=(s_c,b_c)
                    if t1 not in pl:
                        pl.append(t1)
                        pld[i].append(t1)
for num in m_l:
    if num not in ch2:
        t2=(num,)
        pi.append(t2)
if v_b>2:
    for i in range(v_b-1):
        for j1 in range(len(pld[i+1])):
            for j2 in range(len(pld[i])):
                g=pld[i+1][j1]
                e=pld[i][j2]
                if g[0]-e[0]==g[1]-e[1] and g[1]-e[1] in l2:
                    t=g+e
                    t=list(t)
                    t.sort()
                    t=tuple(t)
                    if g not in ch:
                        ch.append(g)
                    if e not in ch:
                        ch.append(e)
                    if t not in ql:
                        ql.append(t)
                        qld[i].append(t)
for num in pl:
    if num not in ch:
        pi.append(num)
if v_b>3:
    for i in range(v_b-2):
        for j1 in range(len(qld[i+1])):
            for j2 in range(len(qld[i])):
                g=qld[i+1][j1]
                e=qld[i][j2]
                if g[0]-e[0]==g[3]-e[3] and g[3]-e[3] in l2:
                    t=g+e
                    t=list(t)
                    t.sort()
                    t=tuple(t)
                    if g not in ch3:
                        ch3.append(g)
                    if e not in ch3:
                        ch3.append(e)
                    if t not in ol:
                        ol.append(t)
                        old[i].append(t)
                        pi.append(t)
for num in ql:
    if num not in ch3:
        pi.append(num)
print("Prime implicatns:",pi)
epi=[]
cpi={}
lpi=[]
mch=[]
for t in pi:
    for i in t:
        cpi[i]=cpi.get(i,0)+1
for k,v in cpi.items():
    if v==1 and k not in d_c:
        for t in pi:
            if k in t:
                epi.append(t)
                pi.remove(t)
for t in epi:
    for i in range(len(t)):
        if t[i] not in mch and t[i] not in d_c:
            mch.append(t[i])
mch.sort()
ech=[]
if mch!=mml:
    for i in mml:
        if i not in mch:
            ech.append(i)
chl=[]
if len(ech)!=0:
    for j in pi:
        e=0
        for i in ech:
            if i not in j:
                e=1
                break
        if(e==0):
            chl.append(j)
if len(chl)==1:
    epi.append(chl[0])
if len(chl)>1:
    ll=0
    for i in range(len(chl)):
        if(ll==0 or ll<len(chl[i])):
            ll=len(chl[i])
            t=chl[i]
    epi.append(t)
if len(ech)!=0 and len(chl)==0:
    for j in ech:
        for i in pi:
            if j in i:
                chl.append(i)
    chl=list(set(chl))
    while len(ech):
        t=(0,)
        i=ech[0]
        for j in chl:
            if i in j:
                if len(j)>len(t):
                    t=j
        for x in t:
            if x in ech:
                ech.remove(x)
        epi.append(t)
print("Essential prime implicants: ",epi)
le=exp4(epi,v_b)
print("SOP--->",le[0])
print("POS--->",le[1])