class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows={}
        for r,c in reservedSeats:
            if 2<=c<=9:rows[r]=rows.get(r,0)|(1<<(c-2))
        ans=2*(n-len(rows))
        for m in rows.values():
            left=m&0b00001111==0;right=m&0b11110000==0;middle=m&0b00111100==0
            ans+=2 if left and right else int(left or right or middle)
        return ans
