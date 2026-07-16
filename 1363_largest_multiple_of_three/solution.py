class Solution:
    def largestMultipleOfThree(self, digits):
        cnt=[0]*10
        for d in digits:cnt[d]+=1
        rem=sum(digits)%3
        def remove(r,k):
            for d in range(r,10,3):
                while cnt[d] and k:cnt[d]-=1;k-=1
                if not k:return True
            return False
        if rem and not remove(rem,1):remove(3-rem,2)
        s=''.join(str(d)*cnt[d] for d in range(9,-1,-1))
        return '0' if s and s[0]=='0' else s
