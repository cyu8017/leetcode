#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["3877_minimum_removals_to_achieve_target_xor"] = r'''# LeetCode 3877 - Minimum Removals To Achieve Target Xor
# https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

from typing import List


class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        mx = 0
        for x in nums:
            mx = max(mx, x)
        m = 0
        if mx > 0:
            u = mx
            while u != 0:
                m += 1
                u >>= 1
        if (1 << m) <= target:
            return -1
        n = len(nums)
        N = 1 << m
        NEG = float("-inf")
        f = [[NEG] * N for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            x = nums[i - 1]
            for j in range(N):
                f[i][j] = f[i - 1][j]
                if f[i - 1][j ^ x] != NEG:
                    f[i][j] = max(f[i][j], f[i - 1][j ^ x] + 1)
        if f[n][target] < 0:
            return -1
        return n - int(f[n][target])
'''

FILES["3878_count_good_subarrays"] = r'''# LeetCode 3878 - Count Good Subarrays
# https://leetcode.com/problems/count-good-subarrays/

from typing import List


class Solution:
    def countGoodSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        l = [-1] * n
        stk: List[int] = []
        for i in range(n):
            x = nums[i]
            while stk and nums[stk[-1]] < x and (nums[stk[-1]] | x) == x:
                stk.pop()
            if stk:
                l[i] = stk[-1]
            stk.append(i)
        r = [n] * n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and (nums[stk[-1]] | nums[i]) == nums[i]:
                stk.pop()
            if stk:
                r[i] = stk[-1]
            stk.append(i)
        ans = 0
        for i in range(n):
            ans += (i - l[i]) * (r[i] - i)
        return ans
'''

FILES["3879_maximum_distinct_path_sum_in_a_binary_tree"] = r'''# LeetCode 3879 - Maximum Distinct Path Sum In A Binary Tree
# https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSum(self, root: Optional[TreeNode]) -> int:
        g: Dict[TreeNode, List[Optional[TreeNode]]] = {}
        vis: Dict[int, bool] = {}

        def dfs(node: Optional[TreeNode], p: Optional[TreeNode]) -> None:
            if not node:
                return
            g[node] = [p, node.left, node.right]
            dfs(node.left, node)
            dfs(node.right, node)

        def dfs2(node: Optional[TreeNode]) -> int:
            if not node or vis.get(node.val) is True:
                return 0
            vis[node.val] = True
            res = node.val
            best = 0
            for nxt in g[node]:
                best = max(best, dfs2(nxt))
            vis[node.val] = False
            return res + best

        g.clear()
        vis.clear()
        dfs(root, None)
        ans = float("-inf")
        for node in g:
            ans = max(ans, dfs2(node))
            vis.clear()
        return int(ans)
'''

FILES["3880_minimum_absolute_difference_between_two_values"] = r'''# LeetCode 3880 - Minimum Absolute Difference Between Two Values
# https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

from typing import List


class Solution:
    def minAbsoluteDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        last = [-ans, -ans, -ans]
        for i in range(n):
            x = nums[i]
            if x != 0:
                ans = min(ans, i - last[3 - x])
                last[x] = i
        if ans > n:
            return -1
        return ans
'''

FILES["3881_direction_assignments_with_exactly_k_visible_people"] = r'''# LeetCode 3881 - Direction Assignments With Exactly K Visible People
# https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

from typing import List, Optional

N3881 = 100001
MOD3881 = 1000000007
fact3881: Optional[List[int]] = None
invFact3881: Optional[List[int]] = None
ready3881 = False


def qmi3881(a: int, k: int, p: int) -> int:
    res = 1
    A = a
    K = k
    P = p
    while K != 0:
        if (K & 1) != 0:
            res = res * A % P
        K >>= 1
        A = A * A % P
    return res


def init3881() -> None:
    global fact3881, invFact3881, ready3881
    if ready3881:
        return
    fact3881 = [0] * N3881
    invFact3881 = [0] * N3881
    fact3881[0] = invFact3881[0] = 1
    for i in range(1, N3881):
        fact3881[i] = fact3881[i - 1] * i % MOD3881
        invFact3881[i] = qmi3881(fact3881[i], MOD3881 - 2, MOD3881)
    ready3881 = True


def comb3881(n: int, k: int) -> int:
    return fact3881[n] * invFact3881[k] % MOD3881 * invFact3881[n - k] % MOD3881


class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        init3881()
        l = pos
        r = n - pos - 1
        ans = 0
        for a in range(min(k, l) + 1):
            b = k - a
            if b <= r:
                ans = (ans + 2 * comb3881(l, a) % MOD3881 * comb3881(r, b) % MOD3881) % MOD3881
        return ans
'''

FILES["3882_minimum_xor_path_in_a_grid"] = r'''# LeetCode 3882 - Minimum XOR Path in a Grid
# https://leetcode.com/problems/minimum-xor-path-in-a-grid/

from typing import List


class Solution:
    def minXor(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[False] * 1024 for _ in range(cols)]
        for row in range(rows):
            left = [False] * 1024
            for col in range(cols):
                nxt = [False] * 1024
                value = grid[row][col]
                if row == 0 and col == 0:
                    nxt[value] = True
                else:
                    for xorv in range(1024):
                        if dp[col][xorv] or left[xorv]:
                            nxt[xorv ^ value] = True
                dp[col] = nxt
                left = nxt
        for xorv in range(1024):
            if dp[cols - 1][xorv]:
                return xorv
        return -1
'''

FILES["3883_count_non_decreasing_arrays_with_given_digit_sums"] = r'''# LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
# https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

from typing import List


class Solution:
    def countNonDecreasingArrays(self, digitSum: List[int]) -> int:
        mod = 1000000007
        groups: List[List[int]] = [[] for _ in range(51)]
        for x in range(5001):
            s = 0
            y = x
            while y > 0:
                s += y % 10
                y //= 10
            groups[s].append(x)
        prev_vals = groups[digitSum[0]]
        dp = [1] * len(prev_vals)
        for pos in range(1, len(digitSum)):
            cur_vals = groups[digitSum[pos]]
            nxt = [0] * len(cur_vals)
            j = 0
            prefix = 0
            for i in range(len(cur_vals)):
                x = cur_vals[i]
                while j < len(prev_vals) and prev_vals[j] <= x:
                    prefix += dp[j]
                    if prefix >= mod:
                        prefix -= mod
                    j += 1
                nxt[i] = prefix
            prev_vals = cur_vals
            dp = nxt
        ans = 0
        for x in dp:
            ans += x
            if ans >= mod:
                ans -= mod
        return ans
'''

FILES["3884_first_matching_character_from_both_ends"] = r'''# LeetCode 3884 - First Matching Character From Both Ends
# https://leetcode.com/problems/first-matching-character-from-both-ends/


class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        for i in range(n // 2 + 1):
            if s[i] == s[n - i - 1]:
                return i
        return -1
'''

FILES["3885_design_event_manager"] = r'''# LeetCode 3885 - Design Event Manager
# https://leetcode.com/problems/design-event-manager/

from typing import Dict, List


class EventManager:
    def __init__(self, events: List[List[int]]):
        self.sl: List[List[int]] = []
        self.d: Dict[int, int] = {}
        for e in events:
            event_id, priority = e[0], e[1]
            self.sl.append([-priority, event_id])
            self.d[event_id] = priority
        self._sort()

    def _sort(self) -> None:
        self.sl.sort(key=lambda a: (a[0], a[1]))

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        old = self.d[eventId]
        self.sl = [x for x in self.sl if not (x[0] == -old and x[1] == eventId)]
        self.sl.append([-newPriority, eventId])
        self.d[eventId] = newPriority
        self._sort()

    def pollHighest(self) -> int:
        if not self.sl:
            return -1
        top = self.sl.pop(0)
        event_id = top[1]
        del self.d[event_id]
        return event_id
'''

FILES["3886_sum_of_sortable_integers"] = r'''# LeetCode 3886 - Sum of Sortable Integers
# https://leetcode.com/problems/sum-of-sortable-integers/

from typing import List


class Solution:
    def sumOfSortableIntegers(self, nums: List[int]) -> int:
        def rotation_matches(block: List[int], target: List[int]) -> bool:
            k = len(block)
            prefix = [0] * k
            for i in range(1, k):
                j = prefix[i - 1]
                while j > 0 and target[i] != target[j]:
                    j = prefix[j - 1]
                if target[i] == target[j]:
                    j += 1
                prefix[i] = j
            matched = 0
            for i in range(2 * k - 1):
                x = block[i % k]
                while matched > 0 and x != target[matched]:
                    matched = prefix[matched - 1]
                if x == target[matched]:
                    matched += 1
                if matched == k:
                    return True
            return False

        n = len(nums)
        sorted_nums = sorted(nums)
        divisors: List[int] = []
        d = 1
        while d * d <= n:
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
            d += 1
        answer = 0
        for k in divisors:
            ok = True
            for start in range(0, n, k):
                block = nums[start : start + k]
                target = sorted_nums[start : start + k]
                if not rotation_matches(block, target):
                    ok = False
                    break
            if ok:
                answer += k
        return answer
'''

FILES["3887_incremental_even_weighted_cycle_queries"] = r'''# LeetCode 3887 - Incremental Even-Weighted Cycle Queries
# https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

from typing import List, Tuple


class Solution:
    def countValidEdges(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n
        parity = [0] * n

        def find(x: int) -> Tuple[int, int]:
            if parent[x] == x:
                return (x, 0)
            res = find(parent[x])
            root, p = res[0], res[1]
            parity[x] ^= p
            parent[x] = root
            return (root, parity[x])

        ans = 0
        for e in edges:
            fu = find(e[0])
            fv = find(e[1])
            ru, pu = fu[0], fu[1]
            rv, pv = fv[0], fv[1]
            if ru == rv:
                if (pu ^ pv) == e[2]:
                    ans += 1
                continue
            if size[ru] < size[rv]:
                ru, rv = rv, ru
                pu, pv = pv, pu
            parent[rv] = ru
            parity[rv] = pu ^ pv ^ e[2]
            size[ru] += size[rv]
            ans += 1
        return ans
'''

FILES["3888_minimum_operations_to_make_all_grid_elements_equal"] = r'''# LeetCode 3888 - Minimum Operations To Make All Grid Elements Equal
# https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        max_val = grid[0][0]
        for row in grid:
            for x in row:
                max_val = max(max_val, x)

        def check(target: int) -> int:
            diff = [[0] * (n + 2) for _ in range(m + 2)]
            total_ops = 0
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
                    cur_val = grid[i - 1][j - 1] + diff[i][j]
                    if cur_val > target:
                        return -1
                    if cur_val < target:
                        if i + k - 1 > m or j + k - 1 > n:
                            return -1
                        needed = target - cur_val
                        total_ops += needed
                        diff[i][j] += needed
                        diff[i + k][j] -= needed
                        diff[i][j + k] -= needed
                        diff[i + k][j + k] += needed
            return total_ops

        for t in range(max_val, max_val + 2):
            res = check(t)
            if res != -1:
                return res
        return -1
'''

FILES["3889_mirror_frequency_distance"] = r'''# LeetCode 3889 - Mirror Frequency Distance
# https://leetcode.com/problems/mirror-frequency-distance/

from typing import Dict


class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq: Dict[str, int] = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        ans = 0
        vis: Dict[str, bool] = {}
        for c, v in freq.items():
            if "a" <= c <= "z":
                m = chr(97 + 25 - (ord(c) - 97))
            else:
                m = chr(48 + (9 - (ord(c) - 48)))
            if vis.get(m) is True:
                continue
            vis[c] = True
            mv = freq.get(m, 0)
            ans += abs(v - mv)
        return ans
'''

FILES["3890_integers_with_multiple_sum_of_two_cubes"] = r'''# LeetCode 3890 - Integers With Multiple Sum Of Two Cubes
# https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

from typing import Dict, List, Optional

GOOD3890: Optional[List[int]] = None


def init3890() -> None:
    global GOOD3890
    if GOOD3890 is not None:
        return
    LIMIT = 1000000000
    cnt: Dict[int, int] = {}
    cubes = [0] * 1001
    for i in range(1001):
        cubes[i] = i * i * i
    for a in range(1, 1001):
        for b in range(a, 1001):
            x = cubes[a] + cubes[b]
            if x > LIMIT:
                break
            cnt[x] = cnt.get(x, 0) + 1
    GOOD3890 = []
    for k, v in cnt.items():
        if v > 1:
            GOOD3890.append(k)
    GOOD3890.sort()


class Solution:
    def findGoodIntegers(self, n: int) -> List[int]:
        init3890()
        lo = 0
        hi = len(GOOD3890)
        while lo < hi:
            mid = (lo + hi) // 2
            if GOOD3890[mid] <= n:
                lo = mid + 1
            else:
                hi = mid
        return GOOD3890[:lo]
'''

FILES["3891_minimum_increase_to_maximize_special_indices"] = r'''# LeetCode 3891 - Minimum Increase To Maximize Special Indices
# https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

from typing import List


class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[-1, -1] for _ in range(n)]

        def dfs(i: int, j: int) -> int:
            if i >= n - 1:
                return 0
            if f[i][j] != -1:
                return f[i][j]
            cost = max(0, max(nums[i - 1], nums[i + 1]) + 1 - nums[i])
            ans = cost + dfs(i + 2, j)
            if j > 0:
                ans = min(ans, dfs(i + 1, 0))
            f[i][j] = ans
            return ans

        return dfs(1, (n & 1) ^ 1)
'''

FILES["3892_minimum_operations_to_achieve_at_least_k_peaks"] = r'''# LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
# https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

from typing import List

INF3892 = (1 << 53) // 4


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return 0
        if k > n // 2:
            return -1
        cost = [0] * n
        for i in range(n):
            left = nums[(i + n - 1) % n]
            right = nums[(i + 1) % n]
            need = max(left, right)
            if need >= nums[i]:
                cost[i] = need - nums[i] + 1

        def line(left: int, right: int, choose: int) -> int:
            if choose == 0:
                return 0
            if left > right or choose > (right - left + 2) // 2:
                return INF3892
            prev2 = [INF3892] * (choose + 1)
            prev1 = [INF3892] * (choose + 1)
            prev2[0] = prev1[0] = 0
            for i in range(left, right + 1):
                current = prev1[:]
                for j in range(1, choose + 1):
                    if prev2[j - 1] != INF3892 and prev2[j - 1] + cost[i] < current[j]:
                        current[j] = prev2[j - 1] + cost[i]
                prev2 = prev1
                prev1 = current
            return prev1[choose]

        answer = line(1, n - 1, k)
        with_first = line(2, n - 2, k - 1)
        if with_first != INF3892:
            with_first += cost[0]
            answer = min(answer, with_first)
        if answer == INF3892:
            return -1
        return answer
'''

FILES["3893_maximum_team_size_with_overlapping_intervals"] = r'''# LeetCode 3893 - Maximum Team Size With Overlapping Intervals
# https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

from typing import List


class Solution:
    def maximumTeamSize(self, startTime: List[int], endTime: List[int]) -> int:
        def upper_bound(a: List[int], x: int) -> int:
            lo = 0
            hi = len(a)
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        n = len(startTime)
        st = sorted(startTime)
        en = sorted(endTime)
        ans = 0
        for t in range(n):
            l = startTime[t]
            r = endTime[t]
            i = upper_bound(en, l - 1)
            j = upper_bound(st, r)
            ans = max(ans, j - i)
        return ans
'''

FILES["3894_traffic_signal_color"] = r'''# LeetCode 3894 - Traffic Signal Color
# https://leetcode.com/problems/traffic-signal-color/


class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer == 0:
            return "Green"
        if timer == 30:
            return "Orange"
        if timer > 30 and timer <= 90:
            return "Red"
        return "Invalid"
'''

FILES["3895_count_digit_appearances"] = r'''# LeetCode 3895 - Count Digit Appearances
# https://leetcode.com/problems/count-digit-appearances/

from typing import List


class Solution:
    def countDigitOccurrences(self, nums: List[int], digit: int) -> int:
        ans = 0
        for num in nums:
            x = num
            while x > 0:
                if x % 10 == digit:
                    ans += 1
                x //= 10
        return ans
'''

FILES["3896_minimum_operations_to_transform_array_into_alternating_prime"] = r'''# LeetCode 3896 - Minimum Operations To Transform Array Into Alternating Prime
# https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

from typing import List, Optional

MX3896 = 200000
isPrime3896: Optional[List[bool]] = None
primes3896: Optional[List[int]] = None


def init3896() -> None:
    global isPrime3896, primes3896
    if isPrime3896 is not None:
        return
    isPrime3896 = [True] * (MX3896 + 1)
    isPrime3896[0] = isPrime3896[1] = False
    i = 2
    while i * i <= MX3896:
        if isPrime3896[i]:
            j = i * i
            while j <= MX3896:
                isPrime3896[j] = False
                j += i
        i += 1
    primes3896 = []
    for i in range(2, MX3896 + 1):
        if isPrime3896[i]:
            primes3896.append(i)


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        init3896()
        ans = 0
        for i in range(len(nums)):
            x = nums[i]
            if i % 2 == 0:
                lo = 0
                hi = len(primes3896)
                while lo < hi:
                    mid = (lo + hi) >> 1
                    if primes3896[mid] < x:
                        lo = mid + 1
                    else:
                        hi = mid
                ans += primes3896[lo] - x
            elif isPrime3896[x]:
                ans += 2 if x == 2 else 1
        return ans
'''

FILES["3897_maximum_value_of_concatenated_binary_segments"] = r'''# LeetCode 3897 - Maximum Value Of Concatenated Binary Segments
# https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

from typing import List

MOD3897 = 1000000007


def group3897(p: List[int]) -> int:
    if p[1] == 0:
        return 0
    if p[0] > 0:
        return 1
    return 2


class Solution:
    def maxValue(self, nums1: List[int], nums0: List[int]) -> int:
        n = len(nums1)
        pairs = [[nums1[i], nums0[i]] for i in range(n)]
        b = 0
        for i in range(n):
            b += nums1[i] + nums0[i]
        pairs.sort(key=lambda a: (
            group3897(a),
            -a[0] if group3897(a) == 0 else (-a[0] if group3897(a) == 1 else a[1]),
            a[1] if group3897(a) == 1 else 0,
        ))
        p = [0] * b
        p[0] = 1
        for i in range(1, b):
            p[i] = (2 * p[i - 1]) % MOD3897
        ans = 0
        b -= 1
        for pr in pairs:
            cnt1, cnt0 = pr[0], pr[1]
            while cnt1 > 0:
                ans = (ans + p[b]) % MOD3897
                b -= 1
                cnt1 -= 1
            b -= cnt0
        return ans
'''

FILES["3898_find_the_degree_of_each_vertex"] = r'''# LeetCode 3898 - Find The Degree Of Each Vertex
# https://leetcode.com/problems/find-the-degree-of-each-vertex/

from typing import List


class Solution:
    def findDegrees(self, matrix: List[List[int]]) -> List[int]:
        ans = [0] * len(matrix)
        for i in range(len(matrix)):
            for x in matrix[i]:
                ans[i] += x
        return ans
'''

FILES["3899_angles_of_a_triangle"] = r'''# LeetCode 3899 - Angles Of A Triangle
# https://leetcode.com/problems/angles-of-a-triangle/

import math
from typing import List


class Solution:
    def internalAngles(self, sides: List[float]) -> List[float]:
        sides = sorted(sides)
        a, b, c = sides[0], sides[1], sides[2]
        if a + b <= c:
            return []
        pi = math.acos(-1.0)
        A = math.acos((b * b + c * c - a * a) / (2.0 * b * c)) * 180.0 / pi
        B = math.acos((a * a + c * c - b * b) / (2.0 * a * c)) * 180.0 / pi
        C = 180.0 - A - B
        return [A, B, C]
'''

FILES["3900_longest_balanced_substring_after_one_swap"] = r'''# LeetCode 3900 - Longest Balanced Substring After One Swap
# https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

from typing import Dict, List


class Solution:
    def longestBalanced(self, s: str) -> int:
        cnt0 = 0
        for c in s:
            if c == "0":
                cnt0 += 1
        cnt1 = len(s) - cnt0
        pos: Dict[int, List[int]] = {}
        pos[0] = [-1]
        ans = 0
        pre = 0
        for i in range(len(s)):
            if s[i] == "1":
                pre += 1
            else:
                pre -= 1
            if pre not in pos:
                pos[pre] = []
            pos[pre].append(i)
            ans = max(ans, i - pos[pre][0])
            if pre - 2 in pos:
                p = pos[pre - 2]
                if (i - p[0] - 2) // 2 < cnt0:
                    ans = max(ans, i - p[0])
                elif len(p) > 1:
                    ans = max(ans, i - p[1])
            if pre + 2 in pos:
                p = pos[pre + 2]
                if (i - p[0] - 2) // 2 < cnt1:
                    ans = max(ans, i - p[0])
                elif len(p) > 1:
                    ans = max(ans, i - p[1])
        return ans
'''

FILES["3901_good_subsequence_queries"] = r'''# LeetCode 3901 - Good Subsequence Queries
# https://leetcode.com/problems/good-subsequence-queries/

from typing import List


def gcd3901(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


class SegmentTree3901:
    def __init__(self, n: int):
        self.tr = [{"l": 0, "r": 0, "g": 0} for _ in range(n << 2)]
        self.build(1, 1, n)

    def build(self, u: int, l: int, r: int) -> None:
        self.tr[u]["l"] = l
        self.tr[u]["r"] = r
        self.tr[u]["g"] = 0
        if l == r:
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)

    def pushup(self, u: int) -> None:
        self.tr[u]["g"] = gcd3901(self.tr[u << 1]["g"], self.tr[u << 1 | 1]["g"])

    def modify(self, u: int, x: int, v: int) -> None:
        if self.tr[u]["l"] == self.tr[u]["r"]:
            self.tr[u]["g"] = v
            return
        mid = (self.tr[u]["l"] + self.tr[u]["r"]) >> 1
        if x <= mid:
            self.modify(u << 1, x, v)
        else:
            self.modify(u << 1 | 1, x, v)
        self.pushup(u)

    def query(self, u: int, l: int, r: int) -> int:
        if l > r:
            return 0
        if self.tr[u]["l"] >= l and self.tr[u]["r"] <= r:
            return self.tr[u]["g"]
        mid = (self.tr[u]["l"] + self.tr[u]["r"]) >> 1
        if r <= mid:
            return self.query(u << 1, l, r)
        if l > mid:
            return self.query(u << 1 | 1, l, r)
        return gcd3901(self.query(u << 1, l, mid), self.query(u << 1 | 1, mid + 1, r))


class Solution:
    def countGoodSubseq(self, nums: List[int], p: int, queries: List[List[int]]) -> int:
        n = len(nums)
        tree = SegmentTree3901(n)
        cnt = 0
        for i in range(n):
            if nums[i] % p == 0:
                tree.modify(1, i + 1, nums[i])
                cnt += 1
        ans = 0
        for q in queries:
            idx, val = q[0], q[1]
            if nums[idx] % p == 0:
                tree.modify(1, idx + 1, 0)
                cnt -= 1
            if val % p == 0:
                tree.modify(1, idx + 1, val)
                cnt += 1
            nums[idx] = val
            if tree.tr[1]["g"] != p:
                continue
            if cnt < n or n > 6:
                ans += 1
                continue
            for i in range(1, n + 1):
                left_g = tree.query(1, 1, i - 1)
                right_g = tree.query(1, i + 1, n)
                if gcd3901(left_g, right_g) == p:
                    ans += 1
                    break
        return ans
'''

FILES["3902_zigzag_level_sum_of_binary_tree"] = r'''# LeetCode 3902 - Zigzag Level Sum Of Binary Tree
# https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelSum(self, root: Optional[TreeNode]) -> List[int]:
        ans: List[int] = []
        q = [root]
        left = True
        while q:
            nq = []
            for node in q:
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            m = len(q)
            s = 0
            for i in range(m):
                node = q[i] if left else q[m - i - 1]
                child = node.left if left else node.right
                if not child:
                    break
                s += node.val
            ans.append(s)
            left = not left
            q = nq
        return ans
'''

FILES["3903_smallest_stable_index_i"] = r'''# LeetCode 3903 - Smallest Stable Index I
# https://leetcode.com/problems/smallest-stable-index-i/

from typing import List


class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])
        left = 0
        for i in range(n):
            left = max(left, nums[i])
            if left - right[i] <= k:
                return i
        return -1
'''

FILES["3904_smallest_stable_index_ii"] = r'''# LeetCode 3904 - Smallest Stable Index II
# https://leetcode.com/problems/smallest-stable-index-ii/

from typing import List


class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])
        left = 0
        for i in range(n):
            left = max(left, nums[i])
            if left - right[i] <= k:
                return i
        return -1
'''

FILES["3905_multi_source_flood_fill"] = r'''# LeetCode 3905 - Multi Source Flood Fill
# https://leetcode.com/problems/multi-source-flood-fill/

from typing import Dict, List


class Solution:
    def colorGrid(self, n: int, m: int, sources: List[List[int]]) -> List[List[int]]:
        ans = [[0] * m for _ in range(n)]
        q = [s[:] for s in sources]
        dirs = [-1, 0, 1, 0, -1]
        for s in q:
            ans[s[0]][s[1]] = s[2]
        while q:
            vis: Dict[int, int] = {}
            for curr in q:
                r, c, color = curr[0], curr[1], curr[2]
                for i in range(4):
                    x = r + dirs[i]
                    y = c + dirs[i + 1]
                    if 0 <= x < n and 0 <= y < m and ans[x][y] == 0:
                        key = (x << 32) | (y & 0xFFFFFFFF)
                        if key not in vis or color > vis[key]:
                            vis[key] = color
            q = []
            for key, color in vis.items():
                x = key >> 32
                y = key & 0xFFFFFFFF
                ans[x][y] = color
                q.append([x, y, color])
        return ans
'''

FILES["3906_count_good_integers_on_a_grid_path"] = r'''# LeetCode 3906 - Count Good Integers On A Grid Path
# https://leetcode.com/problems/count-good-integers-on-a-grid-path/

from typing import List


class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        key = [False] * 16
        row = 0
        col = 0
        key[0] = True
        for c in directions:
            if c == "D":
                row += 1
            else:
                col += 1
            key[row * 4 + col] = True
        s = ""
        f: List[List[int]] = []

        def dfs(pos: int, last: int, lim: bool) -> int:
            if pos == 16:
                return 1
            if not lim and f[pos][last] != -1:
                return f[pos][last]
            res = 0
            start = last if key[pos] else 0
            end = ord(s[pos]) - 48 if lim else 9
            for i in range(start, end + 1):
                next_last = i if key[pos] else last
                res += dfs(pos + 1, next_last, lim and (i == end))
            if not lim:
                f[pos][last] = res
            return res

        def calc(x: int) -> int:
            nonlocal s, f
            if x < 0:
                return 0
            t = str(x)
            s = "0" * (16 - len(t)) + t
            f = [[-1] * 10 for _ in range(16)]
            return dfs(0, 0, True)

        return calc(r) - calc(l - 1)
'''


def main() -> None:
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.py"
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"wrote {folder}")
    print(f"done {len(FILES)}")


if __name__ == "__main__":
    main()
