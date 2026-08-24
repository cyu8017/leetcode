# LeetCode 3704 - Count No-Zero Pairs That Sum to N
# https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/


class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        s = str(n)
        m = len(s)
        digits = [0] * (m + 1)
        for i in range(m):
            digits[i] = ord(s[m - 1 - i]) - 48
        dp = [[[0, 0] for _ in range(2)] for _ in range(2)]
        dp[0][1][1] = 1
        for pos in range(m + 1):
            ndp = [[[0, 0] for _ in range(2)] for _ in range(2)]
            target = digits[pos]
            for carry in range(2):
                for alive_a in range(2):
                    for alive_b in range(2):
                        ways = dp[carry][alive_a][alive_b]
                        if ways == 0:
                            continue
                        A = []
                        if alive_a == 1:
                            for d in range(1, 10):
                                A.append((d, 1))
                            if pos > 0:
                                A.append((0, 0))
                        else:
                            A.append((0, 0))
                        B = []
                        if alive_b == 1:
                            for d in range(1, 10):
                                B.append((d, 1))
                            if pos > 0:
                                B.append((0, 0))
                        else:
                            B.append((0, 0))
                        for da, na in A:
                            for db, nb in B:
                                sm = da + db + carry
                                if sm % 10 != target:
                                    continue
                                ncarry = sm // 10
                                ndp[ncarry][na][nb] += ways
            dp = ndp
        return dp[0][0][0]
