from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = 0
        for value in range(1, n + 1):
            total ^= value
        odd = 0
        for i in range(1, len(encoded), 2):
            odd ^= encoded[i]
        first = total ^ odd
        ans = [first]
        for value in encoded:
            ans.append(ans[-1] ^ value)
        return ans
