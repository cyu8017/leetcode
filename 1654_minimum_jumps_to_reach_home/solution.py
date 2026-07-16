class Solution:
    def minimumJumps(self, forbidden, a, b, x):
        from collections import deque
        bad=set(forbidden); limit=max([x]+forbidden)+a+b
        q=deque([(0,0,False)]); seen={(0,False)}
        while q:
            p,d,back=q.popleft()
            if p==x:return d
            for np,nb in ((p+a,False),(p-b,True)):
                if np>=0 and np<=limit and np not in bad and (np,nb) not in seen and not(back and nb):
                    seen.add((np,nb)); q.append((np,d+1,nb))
        return -1
