class Solution:
    def minimumDeviation(self, nums):
        import heapq
        h=[];mn=10**20
        for x in nums:
            if x%2:x*=2
            mn=min(mn,x);heapq.heappush(h,-x)
        ans=10**20
        while True:
            x=-heapq.heappop(h);ans=min(ans,x-mn)
            if x%2:return ans
            x//=2;mn=min(mn,x);heapq.heappush(h,-x)
