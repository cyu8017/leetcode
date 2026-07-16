# LeetCode 0936 - Stamping the Sequence
# https://leetcode.com/problems/stamping-the-sequence/

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        n, m = len(target), len(stamp)
        done = [False] * n
        ans: list[int] = []

        changed = True
        while changed:
            changed = False
            for i in range(n - m, -1, -1):
                ok = all(done[i + j] or target[i + j] == stamp[j] for j in range(m))
                if ok and any(not done[i + j] for j in range(m)):
                    for j in range(m):
                        done[i + j] = True
                    ans.append(i)
                    changed = True
                    break
        return ans[::-1] if all(done) else []
