class Solution:
    def maxDiff(self, num):
        s = str(num)
        high = s
        for char in s:
            if char != "9":
                high = s.replace(char, "9")
                break
        low = s
        if s[0] != "1":
            low = s.replace(s[0], "1")
        else:
            for char in s[1:]:
                if char not in "01":
                    low = s.replace(char, "0")
                    break
        return int(high) - int(low)
