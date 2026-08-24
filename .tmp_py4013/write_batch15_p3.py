#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["3687_library_late_fee_calculator"] = r'''# LeetCode 3687 - Library Late Fee Calculator
# https://leetcode.com/problems/library-late-fee-calculator/

from typing import List


class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        def fee(x: int) -> int:
            if x == 1:
                return 1
            if x > 5:
                return 3 * x
            return 2 * x

        return sum(fee(x) for x in daysLate)
'''

FILES["3688_bitwise_or_of_even_numbers_in_an_array"] = r'''# LeetCode 3688 - Bitwise OR of Even Numbers in an Array
# https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if x % 2 == 0:
                ans |= x
        return ans
'''

FILES["3689_maximum_total_subarray_value_i"] = r'''# LeetCode 3689 - Maximum Total Subarray Value I
# https://leetcode.com/problems/maximum-total-subarray-value-i/

from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))
'''

FILES["3690_split_and_merge_array_transformation"] = r'''# LeetCode 3690 - Split and Merge Array Transformation
# https://leetcode.com/problems/split-and-merge-array-transformation/

from typing import List, Tuple


class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        def to_arr(nums: List[int]) -> Tuple[int, ...]:
            t = [0] * 6
            for i in range(n):
                t[i] = nums[i]
            return tuple(t)

        start = to_arr(nums1)
        target = to_arr(nums2)
        vis = {start}
        q = [start]
        ans = 0
        while True:
            nq = []
            for cur in q:
                if cur == target:
                    return ans
                for l in range(n):
                    for r in range(l, n):
                        remain = list(cur[:l]) + list(cur[r + 1 : n])
                        sub = list(cur[l : r + 1])
                        for pos in range(len(remain) + 1):
                            nxt_slice = remain[:pos] + sub + remain[pos:]
                            nxt = to_arr(nxt_slice)
                            if nxt not in vis:
                                vis.add(nxt)
                                nq.append(nxt)
            q = nq
            ans += 1
'''

FILES["3691_maximum_total_subarray_value_ii"] = r'''# LeetCode 3691 - Maximum Total Subarray Value II
# https://leetcode.com/problems/maximum-total-subarray-value-ii/

from typing import List
import heapq


class SparseTableRMQ:
    def __init__(self, data: List[int]) -> None:
        self.n = len(data)
        max_log = 0
        while (1 << max_log) <= self.n:
            max_log += 1
        max_log += 1
        self.f_max = [[0] * max_log for _ in range(self.n)]
        self.f_min = [[0] * max_log for _ in range(self.n)]
        self.lg = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.lg[i] = self.lg[i >> 1] + 1
        for i in range(self.n):
            self.f_max[i][0] = data[i]
            self.f_min[i][0] = data[i]
        for j in range(1, max_log):
            for i in range(self.n - (1 << j) + 1):
                self.f_max[i][j] = max(self.f_max[i][j - 1], self.f_max[i + (1 << (j - 1))][j - 1])
                self.f_min[i][j] = min(self.f_min[i][j - 1], self.f_min[i + (1 << (j - 1))][j - 1])

    def query_max(self, l: int, r: int) -> int:
        k = self.lg[r - l + 1]
        return max(self.f_max[l][k], self.f_max[r - (1 << k) + 1][k])

    def query_min(self, l: int, r: int) -> int:
        k = self.lg[r - l + 1]
        return min(self.f_min[l][k], self.f_min[r - (1 << k) + 1][k])


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = SparseTableRMQ(nums)
        pq = []
        for l in range(n):
            val = st.query_max(l, n - 1) - st.query_min(l, n - 1)
            heapq.heappush(pq, (-val, l, n - 1))
        ans = 0
        for _ in range(k):
            val, l, r = heapq.heappop(pq)
            val = -val
            ans += val
            if r > l:
                next_val = st.query_max(l, r - 1) - st.query_min(l, r - 1)
                heapq.heappush(pq, (-next_val, l, r - 1))
        return ans
'''

FILES["3692_majority_frequency_characters"] = r'''# LeetCode 3692 - Majority Frequency Characters
# https://leetcode.com/problems/majority-frequency-characters/


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        f = {}
        for i in range(26):
            if cnt[i] > 0:
                f[cnt[i]] = f.get(cnt[i], "") + chr(97 + i)
        mx = 0
        mv = 0
        ans = ""
        for v, cs in f.items():
            if len(cs) > mx or (len(cs) == mx and v > mv):
                mx = len(cs)
                mv = v
                ans = cs
        return ans
'''

FILES["3693_climbing_stairs_ii"] = r'''# LeetCode 3693 - Climbing Stairs II
# https://leetcode.com/problems/climbing-stairs-ii/

from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        inf = 10**9
        f = [inf] * (n + 1)
        f[0] = 0
        for i in range(1, n + 1):
            x = costs[i - 1]
            for j in range(max(0, i - 3), i):
                f[i] = min(f[i], f[j] + x + (i - j) * (i - j))
        return f[n]
'''

FILES["3694_distinct_points_reachable_after_substring_removal"] = r'''# LeetCode 3694 - Distinct Points Reachable After Substring Removal
# https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/


class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)
        f = [0] * (n + 1)
        g = [0] * (n + 1)
        x = y = 0
        for i in range(1, n + 1):
            c = s[i - 1]
            if c == "U":
                y += 1
            elif c == "D":
                y -= 1
            elif c == "L":
                x -= 1
            else:
                x += 1
            f[i] = x
            g[i] = y
        st = set()
        for i in range(k, n + 1):
            a = f[n] - (f[i] - f[i - k])
            b = g[n] - (g[i] - g[i - k])
            st.add((a, b))
        return len(st)
'''

FILES["3695_maximize_alternating_sum_using_swaps"] = r'''# LeetCode 3695 - Maximize Alternating Sum Using Swaps
# https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for a, b in swaps:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
        comp_vals = {}
        comp_idx = {}
        for i in range(n):
            r = find(i)
            comp_vals.setdefault(r, []).append(nums[i])
            comp_idx.setdefault(r, []).append(i)
        arr = [0] * n
        for r, vals in comp_vals.items():
            idxs = comp_idx[r]
            vals.sort(reverse=True)
            even = sorted(i for i in idxs if i % 2 == 0)
            odd = sorted(i for i in idxs if i % 2 == 1)
            ei = 0
            for v in vals:
                if ei < len(even):
                    arr[even[ei]] = v
                else:
                    arr[odd[ei - len(even)]] = v
                ei += 1
        ans = 0
        for i in range(n):
            if i % 2 == 0:
                ans += arr[i]
            else:
                ans -= arr[i]
        return ans
'''

FILES["3696_maximum_distance_between_unequal_words_in_array_i"] = r'''# LeetCode 3696 - Maximum Distance Between Unequal Words in Array I
# https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-i/

from typing import List


class Solution:
    def maxDistance(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            if words[i] != words[0]:
                ans = max(ans, i + 1)
            if words[i] != words[n - 1]:
                ans = max(ans, n - i)
        return ans
'''

FILES["3697_compute_decimal_representation"] = r'''# LeetCode 3697 - Compute Decimal Representation
# https://leetcode.com/problems/compute-decimal-representation/

from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []
        p = 1
        while n > 0:
            v = n % 10
            n //= 10
            if v != 0:
                ans.append(p * v)
            p *= 10
        ans.reverse()
        return ans
'''

FILES["3698_split_array_with_minimum_difference"] = r'''# LeetCode 3698 - Split Array With Minimum Difference
# https://leetcode.com/problems/split-array-with-minimum-difference/

from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0] * n
        f = [True] * n
        g = [True] * n
        s[0] = nums[0]
        for i in range(1, n):
            s[i] = s[i - 1] + nums[i]
            f[i] = f[i - 1]
            if nums[i] <= nums[i - 1]:
                f[i] = False
        for i in range(n - 2, -1, -1):
            g[i] = g[i + 1]
            if nums[i] <= nums[i + 1]:
                g[i] = False
        inf = 10**18
        ans = inf
        for i in range(n - 1):
            if f[i] and g[i + 1]:
                s1, s2 = s[i], s[n - 1] - s[i]
                ans = min(ans, abs(s1 - s2))
        return ans if ans < inf else -1
'''

FILES["3699_number_of_zigzag_arrays_i"] = r'''# LeetCode 3699 - Number of ZigZag Arrays I
# https://leetcode.com/problems/number-of-zigzag-arrays-i/


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l + 1
        if n == 1:
            return m % MOD
        up = [1] * m
        down = [1] * m
        for _ in range(2, n + 1):
            pref_down = [0] * (m + 1)
            for j in range(m):
                pref_down[j + 1] = (pref_down[j] + down[j]) % MOD
            nup = [pref_down[j] for j in range(m)]
            suf_up = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                suf_up[j] = (suf_up[j + 1] + up[j]) % MOD
            ndown = [suf_up[j + 1] for j in range(m)]
            up, down = nup, ndown
        ans = 0
        for j in range(m):
            ans = (ans + up[j]) % MOD
            ans = (ans + down[j]) % MOD
        return ans
'''

FILES["3700_number_of_zigzag_arrays_ii"] = r'''# LeetCode 3700 - Number of ZigZag Arrays II
# https://leetcode.com/problems/number-of-zigzag-arrays-ii/


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l + 1
        if n == 1:
            return m % MOD
        up = [1] * m
        down = [1] * m
        for _ in range(2, n + 1):
            pref = [0] * (m + 1)
            for j in range(m):
                pref[j + 1] = (pref[j] + down[j]) % MOD
            nup = [pref[j] for j in range(m)]
            suf = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                suf[j] = (suf[j + 1] + up[j]) % MOD
            ndown = [suf[j + 1] for j in range(m)]
            up, down = nup, ndown
        ans = 0
        for j in range(m):
            ans = (ans + up[j]) % MOD
            ans = (ans + down[j]) % MOD
        return ans
'''

FILES["3701_compute_alternating_sum"] = r'''# LeetCode 3701 - Compute Alternating Sum
# https://leetcode.com/problems/compute-alternating-sum/

from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans = 0
        for i, x in enumerate(nums):
            if i % 2 == 0:
                ans += x
            else:
                ans -= x
        return ans
'''

FILES["3702_longest_subsequence_with_non_zero_bitwise_xor"] = r'''# LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
# https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xorv = 0
        cnt0 = 0
        for x in nums:
            xorv ^= x
            if x == 0:
                cnt0 += 1
        n = len(nums)
        if xorv != 0:
            return n
        if cnt0 == n:
            return 0
        return n - 1
'''

FILES["3703_remove_k_balanced_substrings"] = r'''# LeetCode 3703 - Remove K-Balanced Substrings
# https://leetcode.com/problems/remove-k-balanced-substrings/


class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stk = []
        for c in s:
            if stk and stk[-1][0] == c:
                stk[-1][1] += 1
            else:
                stk.append([c, 1])
            if c == ")" and len(stk) > 1:
                top = stk[-1]
                prev = stk[-2]
                if top[1] == k and prev[1] >= k:
                    stk.pop()
                    prev[1] -= k
                    if prev[1] == 0:
                        stk.pop()
        return "".join(p[0] * p[1] for p in stk)
'''

FILES["3704_count_no_zero_pairs_that_sum_to_n"] = r'''# LeetCode 3704 - Count No-Zero Pairs That Sum to N
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
'''

FILES["3706_maximum_distance_between_unequal_words_in_array_ii"] = r'''# LeetCode 3706 - Maximum Distance Between Unequal Words in Array II
# https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/

from typing import List


class Solution:
    def maxDistance(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            if words[i] != words[0]:
                ans = max(ans, i + 1)
            if words[i] != words[n - 1]:
                ans = max(ans, n - i)
        return ans
'''

FILES["3707_equal_score_substrings"] = r'''# LeetCode 3707 - Equal Score Substrings
# https://leetcode.com/problems/equal-score-substrings/


class Solution:
    def scoreBalance(self, s: str) -> bool:
        l = 0
        r = 0
        for c in s:
            r += (ord(c) - 97) + 1
        for i in range(len(s) - 1):
            x = (ord(s[i]) - 97) + 1
            l += x
            r -= x
            if l == r:
                return True
        return False
'''

FILES["3708_longest_fibonacci_subarray"] = r'''# LeetCode 3708 - Longest Fibonacci Subarray
# https://leetcode.com/problems/longest-fibonacci-subarray/

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        f = 2
        ans = f
        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1] + nums[i - 2]:
                f += 1
                ans = max(ans, f)
            else:
                f = 2
        return ans
'''

FILES["3709_design_exam_scores_tracker"] = r'''# LeetCode 3709 - Design Exam Scores Tracker
# https://leetcode.com/problems/design-exam-scores-tracker/

import bisect


class ExamTracker:
    def __init__(self) -> None:
        self.times = [0]
        self.pre = [0]

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.pre.append(self.pre[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        l = bisect.bisect_left(self.times, startTime) - 1
        r = bisect.bisect_left(self.times, endTime + 1) - 1
        return self.pre[r] - self.pre[l]
'''

FILES["3710_maximum_partition_factor"] = r'''# LeetCode 3710 - Maximum Partition Factor
# https://leetcode.com/problems/maximum-partition-factor/

from typing import List


class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 2:
            return 0

        def dist(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        def ok(d: int) -> bool:
            g = [[] for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if dist(i, j) < d:
                        g[i].append(j)
                        g[j].append(i)
            color = [-1] * n
            for i in range(n):
                if color[i] != -1:
                    continue
                q = [i]
                color[i] = 0
                while q:
                    u = q.pop(0)
                    for v in g[u]:
                        if color[v] == -1:
                            color[v] = color[u] ^ 1
                            q.append(v)
                        elif color[v] == color[u]:
                            return False
            return True

        lo, hi = 0, 0
        for i in range(n):
            for j in range(i + 1, n):
                hi = max(hi, dist(i, j))
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
'''

FILES["3711_maximum_transactions_without_negative_balance"] = r'''# LeetCode 3711 - Maximum Transactions Without Negative Balance
# https://leetcode.com/problems/maximum-transactions-without-negative-balance/

from typing import List
import heapq


class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        tm = {}
        ans = len(transactions)
        s = 0
        heap = []

        for x in transactions:
            s += x
            tm[x] = tm.get(x, 0) + 1
            heapq.heappush(heap, x)
            while s < 0:
                while heap and tm.get(heap[0], 0) == 0:
                    heapq.heappop(heap)
                y = heap[0]
                s -= y
                ans -= 1
                c = tm[y]
                if c == 1:
                    del tm[y]
                    heapq.heappop(heap)
                else:
                    tm[y] = c - 1
                    heapq.heappop(heap)
        return ans
'''


def main():
    written = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.py"
        if not path.parent.exists():
            print("MISSING FOLDER", folder)
            continue
        path.write_text(content, encoding="utf-8", newline="\n")
        written += 1
    print("wrote", written)


if __name__ == "__main__":
    main()
