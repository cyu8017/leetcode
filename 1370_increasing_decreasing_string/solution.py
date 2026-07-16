from collections import Counter
class Solution:
    def sortString(self, s):
        c=Counter(s); out=[]
        while len(out)<len(s):
            for seq in (range(26),range(25,-1,-1)):
                for i in seq:
                    ch=chr(97+i)
                    if c[ch]:out.append(ch);c[ch]-=1
        return ''.join(out)
