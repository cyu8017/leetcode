import heapq
class Solution:
    def isPossible(self, target):
        if len(target)==1: return target[0]==1
        total=sum(target); h=[-x for x in target]; heapq.heapify(h)
        while True:
            x=-heapq.heappop(h); rest=total-x
            if x==1 or rest==1: return True
            if rest==0 or x<=rest: return False
            prev=x%rest
            if prev==0: return False
            total=rest+prev; heapq.heappush(h,-prev)
