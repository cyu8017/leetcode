class Solution:
    def minMoves(self, nums, limit):
        n=len(nums);d=[0]*(2*limit+2)
        for i in range(n//2):
            a,b=nums[i],nums[-1-i];lo=min(a,b)+1;hi=max(a,b)+limit;s=a+b
            d[2]+=2;d[lo]-=1;d[s]-=1;d[s+1]+=1;d[hi+1]+=1
        ans=cur=10**9
        for s in range(2,2*limit+1):cur+=d[s] if cur!=10**9 else d[s]-10**9;ans=min(ans,cur)
        return ans
