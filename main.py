import json,os,urllib.request
E=os.environ["MAKEFUN_ENV_URL"]
def P(p,b):
 r=urllib.request.Request(E+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 with urllib.request.urlopen(r) as x:return json.load(x)
V=(0,100,320,330,500,900,0)
N=(-33,-31,-18,-14,14,18,31,33);K=(-17,-16,-15,-1,1,15,16,17)
O={2:N,6:K,3:(-17,-15,15,17),4:(-16,-1,1,16),5:K}
H="abcdefgh"
def F(f):
 p=f.split();b=[0]*128;i=112
 for ch in p[0]:
  if ch=="/":i-=24
  elif ch.isdigit():i+=int(ch)
  elif ch.isalpha():
   v="PNBRQKpnbrqk".index(ch);b[i]=v+1 if v<6 else 5-v;i+=1
 s=1 if p[1]=="w" else -1;e=-1
 if p[3]!="-":e=ord(p[3][0])-97+(int(p[3][1])-1)*16
 return b,s,p[2],e
def A(b,q,s):
 d=-16*s
 for o in (d-1,d+1):
  j=q+o
  if not j&136 and b[j]==s:return 1
 for o in N:
  j=q+o
  if not j&136 and b[j]==s*2:return 1
 for o in K:
  j=q+o;n=1
  while not j&136:
   v=b[j]
   if v:
    if v==s*6 and n==1:return 1
    if v==s*5:return 1
    if v==s*3 and abs(o) in(15,17):return 1
    if v==s*4 and abs(o) not in(15,17):return 1
    break
   j+=o;n+=1
 return 0
def k(b,s):
 for i,v in enumerate(b):
  if v==s*6:return i
def G(b,s,e,c):
 m=[];R=7*(s>0);S=6-5*(s>0)
 for i,p in enumerate(b):
  if not p or (p>0)!=(s>0):continue
  t=abs(p)
  if t==1:
   d=16*s;j=i+d
   if not j&136 and b[j]==0:
    if j>>4==R:m.append((i,j,5))
    else:
     m.append((i,j,0))
     if i>>4==S:
      x=i+2*d
      if b[x]==0:m.append((i,x,0))
   for o in (d-1,d+1):
    j=i+o
    if j&136:continue
    if b[j] and (b[j]>0)!=(s>0):m.append((i,j,5 if j>>4==R else 0))
    elif j==e:m.append((i,j,0))
  else:
   for o in O[t]:
    j=i+o
    while not j&136:
     v=b[j]
     if v==0:m.append((i,j,0))
     elif (v>0)!=(s>0):m.append((i,j,0));break
     else:break
     if t in(2,6):break
     j+=o
 q=k(b,s)
 for d in (1,-1):
  ch="K" if d>0 else "Q"
  if s<0:ch=ch.lower()
  if ch not in c:continue
  tg=q+2*d;rk=q+3*d if d>0 else q-4
  em=range(q+1,q+3) if d>0 else range(q-3,q)
  if b[rk]!=(4 if s>0 else -4):continue
  if any(b[x] for x in em):continue
  if A(b,q,-s) or A(b,q+d,-s) or A(b,tg,-s):continue
  m.append((q,tg,0))
 o=[]
 for x in m:
  y=b[:];D_(b,x)
  if not A(b,k(b,s),-s):o.append(x)
  b[:]=y
 return o
def D_(b,m):
 f,t,q=m;p=b[f];w=b[t]
 b[t]=p if not q else (q if p>0 else -q);b[f]=0
 if abs(p)==1 and w==0 and abs((t&7)-(f&7))==1:b[t-16*(1 if p>0 else -1)]=0
 if abs(p)==6 and abs(t-f)==2:
  a,b2=(f+1,f+3) if t>f else (f-1,f-4);b[a]=b[b2];b[b2]=0
def W(b):
 s=0;w=0;z=0
 for i,p in enumerate(b):
  if not p:continue
  t=abs(p);v=V[t];r=i>>4;f=i&7
  if p<0:r=7-r
  g=6-abs(3-f)-abs(3-r)
  if t==1:v+=r*10+(6 if 2<=f<=5 else 0)
  elif t==2:v+=g*3
  elif t==3:
   v+=g*2;w+=p>0;z+=p<0
  elif t==5:v+=g
  s+=v if p>0 else -v
 return s+28*(w>1)-28*(z>1)
D=[0];L=9999
class T(Exception):pass
def M(b,m):
 f,t,q=m;v=b[t]
 return (V[abs(v)]*10-V[abs(b[f])] if v else 0)+(900 if q else 0)
def Q(b,s,a,y,e,c):
 h=A(b,k(b,s),-s);v=W(b) if s>0 else -W(b)
 if not h:
  if v>=y:return y
  if v>a:a=v
 m=G(b,s,e,c);m.sort(key=lambda x:-M(b,x))
 for x in m:
  if not h and M(b,x)==0:continue
  z=b[:];D_(b,x);v=-Q(b,-s,-y,-a,e,c);b[:]=z
  if v>=y:return y
  if v>a:a=v
 if not m:return -99999 if h else 0
 return a
def S(b,s,d,a,y,e,c,p):
 D[0]+=1
 if D[0]>L:raise T
 if d==0:return Q(b,s,a,y,e,c)
 m=G(b,s,e,c)
 if not m:return -99999+p if A(b,k(b,s),-s) else 0
 m.sort(key=lambda x:-M(b,x))
 for x in m:
  z=b[:];D_(b,x);v=-S(b,-s,d-1,-y,-a,e,c,p+1);b[:]=z
  if v>=y:return y
  if v>a:a=v
 return a
def u(m):
 f,t,q=m
 return H[f&7]+str((f>>4)+1)+H[t&7]+str((t>>4)+1)+("q" if q else "")
def C(b,s,e,c,l):
 B=None
 for d in range(1,9):
  D[0]=0
  try:
   m=G(b,s,e,c)
   if not m:return l[0]
   m.sort(key=lambda x:-M(b,x));x0=None;w=-10**9
   for x in m:
    y=b[:];D_(b,x);n=-S(b,-s,d-1,-10**9,-w,e,c,1);b[:]=y
    if n>w:w=n;x0=x
   B=x0
  except T:break
 if B is None:return l[0]
 z=u(B)
 return z if z in l else l[0]
while True:
 g=P("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  b,s,c,e=F(g["fen"]);g=P("/move",{"game":g["game"],"move":C(b,s,e,c,g["legal_moves"])})
