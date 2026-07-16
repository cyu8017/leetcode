class Solution:
    def minimumIncompatibility(self, nums, k):
        from functools import lru_cache
        n=len(nums);size=n//k;full=(1<<n)-1;groups={}
        for mask in range(1<<n):
            if mask.bit_count()!=size:continue
            vals=[nums[i] for i in range(n) if mask>>i&1]
            if len(set(vals))==size:groups[mask]=max(vals)-min(vals)
        @lru_cache(None)
        def dp(mask):
            if mask==full:return 0
            first=next(i for i in range(n) if not(mask>>i&1));best=10**9
            for g,c in groups.items():
                if g>>first&1 and not g&mask:best=min(best,c+dp(mask|g))
            return best
        ans=dp(0);return -1 if ans>=10**9 else ans
