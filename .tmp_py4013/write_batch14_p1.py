#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3526_range_xor_queries_with_subarray_reversals"] = r'''# LeetCode 3526 - Range XOR Queries with Subarray Reversals
# https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

from typing import List


class Solution:
    def getResults(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        a = nums[:]
        ans = []
        for q in queries:
            typ = q[0]
            if typ == 1:
                l, r = q[1], q[2]
                while l < r:
                    a[l], a[r] = a[r], a[l]
                    l += 1
                    r -= 1
            elif typ == 2:
                x = 0
                for i in range(q[1], q[2] + 1):
                    x ^= a[i]
                ans.append(x)
            else:
                a[q[1]] = q[2]
        return ans
'''

FILES["3527_find_the_most_common_response"] = r'''# LeetCode 3527 - Find the Most Common Response
# https://leetcode.com/problems/find-the-most-common-response/

from typing import List


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        cnt = {}
        for ws in responses:
            seen = set()
            for w in ws:
                if w not in seen:
                    seen.add(w)
                    cnt[w] = cnt.get(w, 0) + 1
        ans = responses[0][0]
        for w, v in cnt.items():
            if cnt[ans] < v or (cnt[ans] == v and w < ans):
                ans = w
        return ans
'''

FILES["3528_unit_conversion_i"] = r'''# LeetCode 3528 - Unit Conversion I
# https://leetcode.com/problems/unit-conversion-i/

from typing import List


class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        mod = 1000000007
        n = len(conversions) + 1
        g = [[] for _ in range(n)]
        for e in conversions:
            g[e[0]].append((e[1], e[2]))
        ans = [0] * n

        def dfs(s: int, mul: int) -> None:
            ans[s] = mul
            for to, w in g[s]:
                dfs(to, mul * w % mod)

        dfs(0, 1)
        return ans
'''

FILES["3529_count_cells_in_overlapping_horizontal_and_vertical_substrings"] = r'''# LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
# https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

from typing import List


class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        m, n = len(grid), len(grid[0])
        row = "".join(grid[i][j] for i in range(m) for j in range(n))
        col = "".join(grid[i][j] for j in range(n) for i in range(m))
        h_mark = [[False] * n for _ in range(m)]
        v_mark = [[False] * n for _ in range(m)]
        plen = len(pattern)
        for i in range(len(row) - plen + 1):
            if row[i : i + plen] == pattern:
                for t in range(plen):
                    pos = i + t
                    h_mark[pos // n][pos % n] = True
        for i in range(len(col) - plen + 1):
            if col[i : i + plen] == pattern:
                for t in range(plen):
                    pos = i + t
                    v_mark[pos % m][pos // m] = True
        ans = 0
        for i in range(m):
            for j in range(n):
                if h_mark[i][j] and v_mark[i][j]:
                    ans += 1
        return ans
'''

FILES["3530_maximum_profit_from_valid_topological_order_in_dag"] = r'''# LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
# https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

from typing import List


class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        def popcount(x: int) -> int:
            c = 0
            while x != 0:
                c += x & 1
                x >>= 1
            return c

        need = [0] * n
        dp = [-1] * (1 << n)
        dp[0] = 0
        for e in edges:
            need[e[1]] |= 1 << e[0]
        for mask in range(1 << n):
            if dp[mask] < 0:
                continue
            pos = popcount(mask) + 1
            for i in range(n):
                if ((mask >> i) & 1) != 0:
                    continue
                if (mask & need[i]) == need[i]:
                    nm = mask | (1 << i)
                    v = dp[mask] + score[i] * pos
                    if v > dp[nm]:
                        dp[nm] = v
        return dp[(1 << n) - 1]
'''

FILES["3531_count_covered_buildings"] = r'''# LeetCode 3531 - Count Covered Buildings
# https://leetcode.com/problems/count-covered-buildings/

from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        g1 = {}
        g2 = {}
        for b in buildings:
            g1.setdefault(b[0], []).append(b[1])
            g2.setdefault(b[1], []).append(b[0])
        for lst in g1.values():
            lst.sort()
        for lst in g2.values():
            lst.sort()
        ans = 0
        for b in buildings:
            x, y = b[0], b[1]
            l1, l2 = g1[x], g2[y]
            if l2[0] < x < l2[-1] and l1[0] < y < l1[-1]:
                ans += 1
        return ans
'''

FILES["3532_path_existence_queries_in_a_graph_i"] = r'''# LeetCode 3532 - Path Existence Queries in a Graph I
# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        g = [0] * n
        cnt = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                cnt += 1
            g[i] = cnt
        return [g[q[0]] == g[q[1]] for q in queries]
'''

FILES["3533_concatenated_divisibility"] = r'''# LeetCode 3533 - Concatenated Divisibility
# https://leetcode.com/problems/concatenated-divisibility/

from typing import List


class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        pows = [0] * n
        for i in range(n):
            p = 1
            num = nums[i]
            if num == 0:
                p = 10 % k
            else:
                x = num
                while x > 0:
                    p = p * 10 % k
                    x //= 10
            pows[i] = p
        memo = {}

        def dp(mask: int, mod: int) -> bool:
            if mask == (1 << n) - 1:
                return mod == 0
            key = (mask << 32) | mod
            if key in memo:
                return memo[key]
            for i in range(n):
                if ((mask >> i) & 1) == 0:
                    nm = (mod * pows[i] + nums[i]) % k
                    if dp(mask | (1 << i), nm):
                        memo[key] = True
                        return True
            memo[key] = False
            return False

        def reconstruct(mask: int, mod: int) -> List[int]:
            for i in range(n):
                if ((mask >> i) & 1) == 0:
                    nm = (mod * pows[i] + nums[i]) % k
                    if dp(mask | (1 << i), nm):
                        rest = reconstruct(mask | (1 << i), nm)
                        rest.insert(0, nums[i])
                        return rest
            return []

        if not dp(0, 0):
            return []
        return reconstruct(0, 0)
'''

FILES["3534_path_existence_queries_in_a_graph_ii"] = r'''# LeetCode 3534 - Path Existence Queries in a Graph II
# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:
        pairs = [[nums[i], i] for i in range(n)]
        pairs.sort(key=lambda x: x[0])
        m = 20
        f = [[0] * m for _ in range(n)]
        r = n - 1
        for l in range(n - 1, -1, -1):
            while pairs[r][0] - pairs[l][0] > maxDiff:
                r -= 1
            i, j = pairs[l][1], pairs[r][1]
            f[i][0] = j
            for k in range(1, m):
                f[i][k] = f[f[i][k - 1]][k - 1]
        ans = []
        for q in queries:
            i, j = q[0], q[1]
            if nums[i] > nums[j]:
                i, j = j, i
            if i == j:
                ans.append(0)
                continue
            if nums[i] == nums[j]:
                ans.append(1)
                continue
            d = 0
            for k in range(m - 1, -1, -1):
                if nums[f[i][k]] < nums[j]:
                    d |= 1 << k
                    i = f[i][k]
            if nums[f[i][0]] < nums[j]:
                ans.append(-1)
            else:
                ans.append(d + 1)
        return ans
'''

FILES["3535_unit_conversion_ii"] = r'''# LeetCode 3535 - Unit Conversion II
# https://leetcode.com/problems/unit-conversion-ii/

from typing import List


class Solution:
    def queryConversions(
        self, conversions: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        MOD = 1000000007

        def qpow(x: int, n: int) -> int:
            res = 1
            bx, bn = x, n
            while bn > 0:
                if bn & 1:
                    res = res * bx % MOD
                bx = bx * bx % MOD
                bn >>= 1
            return res

        n = len(conversions) + 1
        g = [[] for _ in range(n)]
        for e in conversions:
            g[e[0]].append((e[1], e[2]))
        res = [0] * n

        def dfs(s: int, mul: int) -> None:
            res[s] = mul
            for to, w in g[s]:
                dfs(to, mul * w % MOD)

        dfs(0, 1)
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            ans[i] = res[q[1]] * qpow(res[q[0]], MOD - 2) % MOD
        return ans
'''

FILES["3536_maximum_product_of_two_digits"] = r'''# LeetCode 3536 - Maximum Product of Two Digits
# https://leetcode.com/problems/maximum-product-of-two-digits/


class Solution:
    def maxProduct(self, n: int) -> int:
        a, b = 0, 0
        while n > 0:
            x = n % 10
            n //= 10
            if a < x:
                b = a
                a = x
            elif b < x:
                b = x
        return a * b
'''

FILES["3537_fill_a_special_grid"] = r'''# LeetCode 3537 - Fill a Special Grid
# https://leetcode.com/problems/fill-a-special-grid/

from typing import List


class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        m = 1 << n
        ans = [[0] * m for _ in range(m)]
        val = 0

        def dfs(x: int, y: int, k: int) -> None:
            nonlocal val
            if k == 1:
                ans[x][y] = val
                val += 1
                return
            h = k >> 1
            dfs(x, y, h)
            dfs(x + h, y, h)
            dfs(x + h, y - h, h)
            dfs(x, y - h, h)

        dfs(0, m - 1, m)
        return ans
'''

FILES["3538_merge_operations_for_minimum_travel_time"] = r'''# LeetCode 3538 - Merge Operations for Minimum Travel Time
# https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

from typing import List


class Solution:
    def minTravelTime(
        self, l: int, n: int, k: int, position: List[int], time: List[int]
    ) -> int:
        prefix = [0] * n
        prefix[0] = time[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + time[i]
        memo = {}
        INF = 10**18

        def dp(i: int, skips: int, last: int) -> int:
            if i == n - 1:
                return 0 if skips == 0 else INF
            key = (i, skips, last)
            if key in memo:
                return memo[key]
            rate = prefix[i]
            if last > 0:
                rate -= prefix[last - 1]
            res = INF
            end = n - 1
            if i + skips + 1 < end:
                end = i + skips + 1
            for j in range(i + 1, end + 1):
                cand = (position[j] - position[i]) * rate + dp(j, skips - (j - i - 1), i + 1)
                if cand < res:
                    res = cand
            memo[key] = res
            return res

        return dp(0, k, 0)
'''

FILES["3539_find_sum_of_array_product_of_magical_sequences"] = r'''# LeetCode 3539 - Find Sum of Array Product of Magical Sequences
# https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

from typing import List


class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        N, MOD = 31, 1000000007
        f = [0] * N
        g = [0] * N

        def qpow(a: int, kk: int) -> int:
            res = 1
            ba, bk = a, kk
            while bk > 0:
                if bk & 1:
                    res = res * ba % MOD
                ba = ba * ba % MOD
                bk >>= 1
            return res

        f[0] = g[0] = 1
        for i in range(1, N):
            f[i] = f[i - 1] * i % MOD
            g[i] = qpow(f[i], MOD - 2)

        def comb(mm: int, nn: int) -> int:
            if nn < 0 or nn > mm:
                return 0
            return f[mm] * g[nn] % MOD * g[mm - nn] % MOD

        n = len(nums)
        dp = [[[[-1] * N for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

        def dfs(i: int, j: int, kk: int, st: int) -> int:
            if kk < 0 or (i == n and j > 0):
                return 0
            if i == n:
                while st > 0:
                    kk -= st & 1
                    st >>= 1
                return 1 if kk == 0 else 0
            if dp[i][j][kk][st] != -1:
                return dp[i][j][kk][st]
            res = 0
            for t in range(j + 1):
                nt = t + st
                nk = kk - (nt & 1)
                p = qpow(nums[i], t)
                tmp = comb(j, t) * p % MOD * dfs(i + 1, j - t, nk, nt >> 1) % MOD
                res = (res + tmp) % MOD
            dp[i][j][kk][st] = res
            return res

        return dfs(0, m, k, 0)
'''

FILES["3540_minimum_time_to_visit_all_houses"] = r'''# LeetCode 3540 - Minimum Time to Visit All Houses
# https://leetcode.com/problems/minimum-time-to-visit-all-houses/

from typing import List


class Solution:
    def minTotalTime(
        self, forward: List[int], backward: List[int], queries: List[int]
    ) -> int:
        n = len(forward)
        sum_b = sum(backward)
        pf = [0] * (n + 1)
        pb = [0] * (n + 1)
        for i in range(n):
            pf[i + 1] = pf[i] + forward[i]
            pb[i + 1] = pb[i] + backward[i]
        ans = 0
        pos = 0
        for q in queries:
            r = 0
            if q < pos:
                r = pf[n]
            r += pf[q] - pf[pos]
            lft = 0
            if q > pos:
                lft = sum_b
            lft += pb[pos] - pb[q]
            ans += min(lft, r)
            pos = q
        return ans
'''

FILES["3541_find_most_frequent_vowel_and_consonant"] = r'''# LeetCode 3541 - Find Most Frequent Vowel and Consonant
# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/


class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        a = b = 0
        for i in range(26):
            c = chr(97 + i)
            if c in "aeiou":
                a = max(a, cnt[i])
            else:
                b = max(b, cnt[i])
        return a + b
'''

FILES["3542_minimum_operations_to_convert_all_elements_to_zero"] = r'''# LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stk = []
        ans = 0
        for x in nums:
            while stk and stk[-1] > x:
                ans += 1
                stk.pop()
            if x != 0 and (not stk or stk[-1] != x):
                stk.append(x)
        ans += len(stk)
        return ans
'''

FILES["3543_maximum_weighted_k_edge_path"] = r'''# LeetCode 3543 - Maximum Weighted K-Edge Path
# https://leetcode.com/problems/maximum-weighted-k-edge-path/

from typing import List


class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append((e[1], e[2]))
        dp = [[set() for _ in range(k + 1)] for _ in range(n)]
        for u in range(n):
            dp[u][0].add(0)
        for i in range(k):
            for u in range(n):
                for sm in dp[u][i]:
                    for to, w in graph[u]:
                        ns = sm + w
                        if ns < t:
                            dp[to][i + 1].add(ns)
        ans = -1
        for u in range(n):
            for sm in dp[u][k]:
                if sm > ans:
                    ans = sm
        return ans
'''

FILES["3544_subtree_inversion_sum"] = r'''# LeetCode 3544 - Subtree Inversion Sum
# https://leetcode.com/problems/subtree-inversion-sum/

from typing import List


class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        parent = [-1] * n
        memo = {}

        def dp(u: int, steps: int, inv: bool) -> int:
            key = (u, steps, inv)
            if key in memo:
                return memo[key]
            num = nums[u]
            if inv:
                num = -num
            neg_num = -num
            for v in graph[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                ns = steps + 1
                if ns > k:
                    ns = k
                num += dp(v, ns, inv)
                if steps == k:
                    neg_num += dp(v, 1, not inv)
            res = num
            if steps == k and neg_num > res:
                res = neg_num
            memo[key] = res
            return res

        return dp(0, k, False)
'''

FILES["3545_minimum_deletions_for_at_most_k_distinct_characters"] = r'''# LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
# https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        cnt.sort()
        ans = 0
        for i in range(26 - k):
            ans += cnt[i]
        return ans
'''

FILES["3546_equal_sum_grid_partition_i"] = r'''# LeetCode 3546 - Equal Sum Grid Partition I
# https://leetcode.com/problems/equal-sum-grid-partition-i/

from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        s = sum(x for row in grid for x in row)
        if s % 2 != 0:
            return False
        m, n = len(grid), len(grid[0])
        pre = 0
        for i in range(m):
            for x in grid[i]:
                pre += x
            if pre * 2 == s and i + 1 < m:
                return True
        pre = 0
        for j in range(n):
            for i in range(m):
                pre += grid[i][j]
            if pre * 2 == s and j + 1 < n:
                return True
        return False
'''

FILES["3547_maximum_sum_of_edge_values_in_a_graph"] = r'''# LeetCode 3547 - Maximum Sum of Edge Values in a Graph
# https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

from typing import List


def calc3547(left: int, right: int, is_cycle: bool) -> int:
    w0 = right
    w1 = right
    score = 0
    for value in range(right - 1, left - 1, -1):
        score += w0 * value
        w0 = w1
        w1 = value
    if is_cycle:
        score += w0 * w1
    return score


def get_comp(start: int, graph: List[List[int]], seen: List[bool]) -> List[int]:
    comp = [start]
    seen[start] = True
    i = 0
    while i < len(comp):
        for v in graph[comp[i]]:
            if not seen[v]:
                seen[v] = True
                comp.append(v)
        i += 1
    return comp


class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        seen = [False] * n
        cycle_sizes = []
        path_sizes = []
        for i in range(n):
            if seen[i]:
                continue
            comp = get_comp(i, graph, seen)
            all_deg2 = all(len(graph[u]) == 2 for u in comp)
            if all_deg2:
                cycle_sizes.append(len(comp))
            elif len(comp) > 1:
                path_sizes.append(len(comp))
        ans = 0
        cur_n = n
        for cs in cycle_sizes:
            ans += calc3547(cur_n - cs + 1, cur_n, True)
            cur_n -= cs
        path_sizes.sort(reverse=True)
        for ps in path_sizes:
            ans += calc3547(cur_n - ps + 1, cur_n, False)
            cur_n -= ps
        return ans
'''

FILES["3548_equal_sum_grid_partition_ii"] = r'''# LeetCode 3548 - Equal Sum Grid Partition II
# https://leetcode.com/problems/equal-sum-grid-partition-ii/

from typing import List


def rotate3548(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    t = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            t[j][i] = grid[i][j]
    return t


def check3548(g: List[List[int]]) -> bool:
    m, n = len(g), len(g[0])
    s1 = s2 = 0
    cnt1 = {}
    cnt2 = {}
    for row in g:
        for x in row:
            s2 += x
            cnt2[x] = cnt2.get(x, 0) + 1
    for i in range(m - 1):
        for x in g[i]:
            s1 += x
            s2 -= x
            cnt1[x] = cnt1.get(x, 0) + 1
            cnt2[x] = cnt2.get(x, 0) - 1
        if s1 == s2:
            return True
        if s1 < s2:
            diff = s2 - s1
            if cnt2.get(diff, 0) > 0:
                if (
                    (m - i - 1 > 1 and n > 1)
                    or (i == m - 2 and (g[i + 1][0] == diff or g[i + 1][n - 1] == diff))
                    or (n == 1 and (g[i + 1][0] == diff or g[m - 1][0] == diff))
                ):
                    return True
        else:
            diff = s1 - s2
            if cnt1.get(diff, 0) > 0:
                if (
                    (i + 1 > 1 and n > 1)
                    or (i == 0 and (g[0][0] == diff or g[0][n - 1] == diff))
                    or (n == 1 and (g[0][0] == diff or g[i][0] == diff))
                ):
                    return True
    return False


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        return check3548(grid) or check3548(rotate3548(grid))
'''

FILES["3549_multiply_two_polynomials"] = r'''# LeetCode 3549 - Multiply Two Polynomials
# https://leetcode.com/problems/multiply-two-polynomials/

import math
from typing import List


class Complex:
    def __init__(self, re: float, im: float) -> None:
        self.re = re
        self.im = im

    def mul(self, o: "Complex") -> "Complex":
        return Complex(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def add(self, o: "Complex") -> "Complex":
        return Complex(self.re + o.re, self.im + o.im)

    def sub(self, o: "Complex") -> "Complex":
        return Complex(self.re - o.re, self.im - o.im)

    def div(self, x: float) -> "Complex":
        return Complex(self.re / x, self.im / x)


def fft(a: List[Complex], invert: bool) -> None:
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while (j & bit) != 0:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while length <= n:
        angle = 2 * math.pi / length * (-1 if invert else 1)
        wlen = Complex(math.cos(angle), math.sin(angle))
        for i in range(0, n, length):
            w = Complex(1, 0)
            half = length >> 1
            for jj in range(half):
                u = a[i + jj]
                v = a[i + jj + half].mul(w)
                a[i + jj] = u.add(v)
                a[i + jj + half] = u.sub(v)
                w = w.mul(wlen)
        length <<= 1
    if invert:
        for i in range(n):
            a[i] = a[i].div(n)


class Solution:
    def multiply(self, poly1: List[int], poly2: List[int]) -> List[int]:
        if not poly1 or not poly2:
            return []
        m = len(poly1) + len(poly2) - 1
        n = 1
        while n < m:
            n <<= 1
        fa = [Complex(0, 0) for _ in range(n)]
        fb = [Complex(0, 0) for _ in range(n)]
        for i in range(n):
            fa[i] = Complex(poly1[i] if i < len(poly1) else 0, 0)
            fb[i] = Complex(poly2[i] if i < len(poly2) else 0, 0)
        fft(fa, False)
        fft(fb, False)
        for i in range(n):
            fa[i] = fa[i].mul(fb[i])
        fft(fa, True)
        return [int(round(fa[i].re)) for i in range(m)]
'''

FILES["3550_smallest_index_with_digit_sum_equal_to_index"] = r'''# LeetCode 3550 - Smallest Index With Digit Sum Equal to Index
# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            x, s = num, 0
            while x > 0:
                s += x % 10
                x //= 10
            if s == i:
                return i
        return -1
'''


def main() -> None:
    for folder, text in FILES.items():
        path = ROOT / folder / "solution.py"
        path.write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {folder}")
    print(f"done {len(FILES)}")


if __name__ == "__main__":
    main()
