class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9 + 7
        ends0 = ends1 = 0
        has0 = False
        for ch in binary:
            if ch == "0":
                has0 = True
                ends0 = (ends0 + ends1) % MOD
            else:
                ends1 = (ends0 + ends1 + 1) % MOD
        return (ends0 + ends1 + (1 if has0 else 0)) % MOD
