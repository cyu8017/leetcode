class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''.join(str(ord(c) - 96) for c in s)
        for _ in range(k):
            num = str(sum(int(d) for d in num))
        return int(num)
