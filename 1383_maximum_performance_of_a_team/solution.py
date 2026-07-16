import heapq
class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        h=[];total=ans=0
        for e,s in sorted(zip(efficiency,speed),reverse=True):
            heapq.heappush(h,s);total+=s
            if len(h)>k:total-=heapq.heappop(h)
            ans=max(ans,total*e)
        return ans%1_000_000_007
