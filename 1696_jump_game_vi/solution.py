class Solution:
    def maxResult(self, nums, k):
        from collections import deque
        q=deque([(0,nums[0])])
        for i in range(1,len(nums)):
            while q[0][0]<i-k:q.popleft()
            score=nums[i]+q[0][1]
            while q and q[-1][1]<=score:q.pop()
            q.append((i,score))
        return q[-1][1]
