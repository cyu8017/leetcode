MOD = 1000000007
class Fancy:
    def __init__(self):
        self.n=0; self.size=1<<17
        self.tree=[0]*(2*self.size); self.mul=[1]*(2*self.size); self.add=[0]*(2*self.size)
    def _apply(self,p,m,a):
        self.tree[p]=(self.tree[p]*m+a)%MOD
        self.mul[p]=self.mul[p]*m%MOD; self.add[p]=(self.add[p]*m+a)%MOD
    def _push(self,p):
        if self.mul[p]!=1 or self.add[p]:
            self._apply(2*p,self.mul[p],self.add[p]); self._apply(2*p+1,self.mul[p],self.add[p])
            self.mul[p]=1; self.add[p]=0
    def _update(self,p,l,r,ql,qr,m,a):
        if ql<=l and r<=qr: self._apply(p,m,a); return
        self._push(p); mid=(l+r)//2
        if ql<=mid: self._update(2*p,l,mid,ql,qr,m,a)
        if qr>mid: self._update(2*p+1,mid+1,r,ql,qr,m,a)
    def _get(self,p,l,r,i):
        if l==r: return self.tree[p]
        self._push(p); mid=(l+r)//2
        return self._get(2*p,l,mid,i) if i<=mid else self._get(2*p+1,mid+1,r,i)
    def append(self,val):
        self._update(1,0,self.size-1,self.n,self.n,0,val%MOD); self.n+=1
    def addAll(self,inc):
        if self.n: self._update(1,0,self.size-1,0,self.n-1,1,inc%MOD)
    def multAll(self,m):
        if self.n: self._update(1,0,self.size-1,0,self.n-1,m%MOD,0)
    def getIndex(self,idx):
        return self._get(1,0,self.size-1,idx) if idx<self.n else -1
