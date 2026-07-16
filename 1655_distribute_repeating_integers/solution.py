class Solution:
    def canDistribute(self, nums, quantity):
        from collections import Counter
        cnt=list(Counter(nums).values()); quantity.sort(reverse=True); m=len(quantity)
        sums=[0]*(1<<m)
        for mask in range(1,1<<m):
            bit=mask&-mask; sums[mask]=sums[mask^bit]+quantity[bit.bit_length()-1]
        dp={0}
        for c in cnt:
            nxt=set(dp)
            for mask in dp:
                left=((1<<m)-1)^mask; sub=left
                while sub:
                    if sums[sub]<=c:nxt.add(mask|sub)
                    sub=(sub-1)&left
            dp=nxt
        return (1<<m)-1 in dp
