class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        def score(s: str) -> int:
            # Alice maximizes, Bob minimizes; '?' contribute +9/2 expected to Alice advantage
            q = s.count('?')
            dig = sum(int(c) for c in s if c != '?')
            return dig * 2 + q * 9
        return score(num[:half]) != score(num[half:])
