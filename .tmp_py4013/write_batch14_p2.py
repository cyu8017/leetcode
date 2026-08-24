#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3551_minimum_swaps_to_sort_by_digit_sum"] = r'''# LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
# https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

from typing import List


def f3551(x: int) -> int:
    s = 0
    while x != 0:
        s += x % 10
        x //= 10
    return s


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [[f3551(nums[i]), nums[i]] for i in range(n)]
        arr.sort(key=lambda x: (x[0], x[1]))
        d = {arr[i][1]: i for i in range(n)}
        vis = [False] * n
        ans = n
        for i in range(n):
            if not vis[i]:
                ans -= 1
                j = i
                while not vis[j]:
                    vis[j] = True
                    j = d[nums[j]]
        return ans
'''

FILES["3552_grid_teleportation_traversal"] = r'''# LeetCode 3552 - Grid Teleportation Traversal
# https://leetcode.com/problems/grid-teleportation-traversal/

from collections import deque
from typing import List


class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        g = {}
        for i in range(m):
            for j in range(n):
                c = matrix[i][j]
                if c.isalpha():
                    g.setdefault(c, []).append((i, j))
        dirs = [-1, 0, 1, 0, -1]
        INF = 1 << 30
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        q = deque([(0, 0)])
        while q:
            i, j = q.popleft()
            d = dist[i][j]
            if i == m - 1 and j == n - 1:
                return d
            c = matrix[i][j]
            if c in g:
                for x, y in g[c]:
                    if d < dist[x][y]:
                        dist[x][y] = d
                        q.appendleft((x, y))
                del g[c]
            for idx in range(4):
                x, y = i + dirs[idx], j + dirs[idx + 1]
                if 0 <= x < m and 0 <= y < n and matrix[x][y] != "#" and d + 1 < dist[x][y]:
                    dist[x][y] = d + 1
                    q.append((x, y))
        return -1
'''

FILES["3553_minimum_weighted_subgraph_with_the_required_paths_ii"] = r'''# LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

from typing import List


class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        LOG = 17
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        parent = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        dist = [0] * n

        def dfs(u: int, p: int) -> None:
            parent[0][u] = p
            for to, w in g[u]:
                if to == p:
                    continue
                depth[to] = depth[u] + 1
                dist[to] = dist[u] + w
                dfs(to, u)

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != -1 and depth[parent[k][u]] >= depth[v]:
                    u = parent[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        def path(u: int, v: int) -> int:
            a = lca(u, v)
            return dist[u] + dist[v] - 2 * dist[a]

        dfs(0, -1)
        for k in range(1, LOG):
            for v in range(n):
                if parent[k - 1][v] != -1:
                    parent[k][v] = parent[k - 1][parent[k - 1][v]]
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            a, b, c = q[0], q[1], q[2]
            ans[i] = (path(a, b) + path(b, c) + path(a, c)) // 2
        return ans
'''

FILES["3555_smallest_subarray_to_sort_in_every_sliding_window"] = r'''# LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
# https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

from typing import List


def f3555(nums: List[int], i: int, j: int, inf: int) -> int:
    mi, mx = inf, -inf
    l, r = -1, -1
    for p in range(i, j + 1):
        if nums[p] < mx:
            r = p
        else:
            mx = nums[p]
        q = j - p + i
        if nums[q] > mi:
            l = q
        else:
            mi = nums[q]
    if r == -1:
        return 0
    return r - l + 1


class Solution:
    def minSubarraySort(self, nums: List[int], k: int) -> List[int]:
        inf = 1 << 30
        n = len(nums)
        return [f3555(nums, i, i + k - 1, inf) for i in range(n - k + 1)]
'''

FILES["3556_sum_of_largest_prime_substrings"] = r'''# LeetCode 3556 - Sum of Largest Prime Substrings
# https://leetcode.com/problems/sum-of-largest-prime-substrings/

import math


def is_prime3556(x: int) -> bool:
    if x < 2:
        return False
    sqrt_x = int(math.sqrt(x))
    for i in range(2, sqrt_x + 1):
        if x % i == 0:
            return False
    return True


class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        st = set()
        n = len(s)
        for i in range(n):
            x = 0
            for j in range(i, n):
                x = x * 10 + (ord(s[j]) - 48)
                if is_prime3556(x):
                    st.add(x)
        nums = sorted(st)
        ans = 0
        i = len(nums) - 1
        while i >= 0 and len(nums) - i <= 3:
            ans += nums[i]
            i -= 1
        return ans
'''

FILES["3557_find_maximum_number_of_non_intersecting_substrings"] = r'''# LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
# https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/


class Solution:
    def maxSubstrings(self, word: str) -> int:
        ans = 0
        first = {}
        for i, c in enumerate(word):
            if c not in first:
                first[c] = i
            elif i - first[c] + 1 >= 4:
                ans += 1
                first.clear()
        return ans
'''

FILES["3558_number_of_ways_to_assign_edge_weights_i"] = r'''# LeetCode 3558 - Number of Ways to Assign Edge Weights I
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 1000000007
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        def dfs(i: int, fa: int) -> int:
            res = 0
            for j in g[i]:
                if j != fa:
                    res = max(res, dfs(j, i) + 1)
            return res

        def pow2(exp: int) -> int:
            a, res = 2, 1
            while exp > 0:
                if exp & 1:
                    res = res * a % mod
                a = a * a % mod
                exp >>= 1
            return res

        return pow2(dfs(1, 0) - 1)
'''

FILES["3559_number_of_ways_to_assign_edge_weights_ii"] = r'''# LeetCode 3559 - Number of Ways to Assign Edge Weights II
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

from typing import List


class Solution:
    def assignEdgeWeights(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        MOD, LOG = 1000000007, 17
        n = len(edges) + 1
        depth = [0] * (n + 1)
        graph = [[] for _ in range(n + 1)]
        parent = [[-1] * (n + 1) for _ in range(LOG)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        def dfs(u: int, p: int) -> None:
            parent[0][u] = p
            for v in graph[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != -1 and depth[parent[k][u]] >= depth[v]:
                    u = parent[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        def mod_pow(exp: int) -> int:
            base, res = 2, 1
            while exp > 0:
                if exp & 1:
                    res = res * base % MOD
                base = base * base % MOD
                exp >>= 1
            return res

        dfs(1, -1)
        for k in range(1, LOG):
            for v in range(1, n + 1):
                if parent[k - 1][v] != -1:
                    parent[k][v] = parent[k - 1][parent[k - 1][v]]
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            u, v = q[0], q[1]
            if u == v:
                ans[i] = 0
                continue
            a = lca(u, v)
            d = depth[u] + depth[v] - 2 * depth[a]
            ans[i] = mod_pow(d - 1)
        return ans
'''

FILES["3560_find_minimum_log_transportation_cost"] = r'''# LeetCode 3560 - Find Minimum Log Transportation Cost
# https://leetcode.com/problems/find-minimum-log-transportation-cost/


class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        x = max(n, m)
        if x <= k:
            return 0
        return k * (x - k)
'''

FILES["3561_resulting_string_after_adjacent_removals"] = r'''# LeetCode 3561 - Resulting String After Adjacent Removals
# https://leetcode.com/problems/resulting-string-after-adjacent-removals/


def is_contiguous(a: str, b: str) -> bool:
    x = abs(ord(a) - ord(b))
    return x == 1 or x == 25


class Solution:
    def resultingString(self, s: str) -> str:
        stk = []
        for c in s:
            if stk and is_contiguous(stk[-1], c):
                stk.pop()
            else:
                stk.append(c)
        return "".join(stk)
'''

FILES["3562_maximum_profit_from_trading_stocks_with_discounts"] = r'''# LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

from typing import List


class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:
        g = [[] for _ in range(n + 1)]
        for e in hierarchy:
            g[e[0]].append(e[1])

        def dfs(u: int) -> List[List[int]]:
            nxt = [[0, 0] for _ in range(budget + 1)]
            for v in g[u]:
                fv = dfs(v)
                for j in range(budget, -1, -1):
                    for jv in range(j + 1):
                        for pre in range(2):
                            nxt[j][pre] = max(nxt[j][pre], nxt[j - jv][pre] + fv[jv][pre])
            f = [[0, 0] for _ in range(budget + 1)]
            price = future[u - 1]
            for j in range(budget + 1):
                for pre in range(2):
                    cost = present[u - 1] // (pre + 1)
                    if j >= cost:
                        buy_profit = nxt[j - cost][1] + (price - cost)
                        f[j][pre] = max(nxt[j][0], buy_profit)
                    else:
                        f[j][pre] = nxt[j][0]
            return f

        return dfs(1)[budget][0]
'''

FILES["3563_lexicographically_smallest_string_after_adjacent_removals"] = r'''# LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
# https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/


def is_consec3563(a: str, b: str) -> bool:
    d = abs(ord(a) - ord(b))
    return d == 1 or d == 25


class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)
        dp = [[""] * (n + 1) for _ in range(n + 1)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length
                min_str = s[i] + dp[i + 1][j]
                for k in range(i + 1, j):
                    if is_consec3563(s[i], s[k]) and dp[i + 1][k] == "":
                        cand = dp[k + 1][j]
                        if cand < min_str:
                            min_str = cand
                dp[i][j] = min_str
        return dp[0][n]
'''

FILES["3565_sequential_grid_path_cover"] = r'''# LeetCode 3565 - Sequential Grid Path Cover
# https://leetcode.com/problems/sequential-grid-path-cover/

from typing import List


class Solution:
    def findPath(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        dirs = [-1, 0, 1, 0, -1]
        st = 0
        path = []

        def f(i: int, j: int) -> int:
            return i * n + j

        def dfs(i: int, j: int, v: int) -> bool:
            nonlocal st
            path.append([i, j])
            if len(path) == m * n:
                return True
            idx = f(i, j)
            st |= 1 << idx
            if grid[i][j] == v:
                v += 1
            for t in range(4):
                x, y = i + dirs[t], j + dirs[t + 1]
                if 0 <= x < m and 0 <= y < n:
                    idx2 = f(x, y)
                    if ((st >> idx2) & 1) == 0 and (grid[x][y] == 0 or grid[x][y] == v):
                        if dfs(x, y, v):
                            return True
            path.pop()
            st ^= 1 << idx
            return False

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or grid[i][j] == 1:
                    if dfs(i, j, 1):
                        return path
                    path.clear()
                    st = 0
        return []
'''

FILES["3566_partition_array_into_two_equal_product_subsets"] = r'''# LeetCode 3566 - Partition Array into Two Equal Product Subsets
# https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

from typing import List


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        for i in range(1 << n):
            x = y = 1
            for j in range(n):
                if ((i >> j) & 1) != 0:
                    x *= nums[j]
                else:
                    y *= nums[j]
                if x > target or y > target:
                    break
            if x == target and y == target:
                return True
        return False
'''

FILES["3567_minimum_absolute_difference_in_sliding_submatrix"] = r'''# LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                nums = [grid[x][y] for x in range(i, i + k) for y in range(j, j + k)]
                nums.sort()
                d = 2147483647
                for t in range(1, len(nums)):
                    if nums[t] != nums[t - 1]:
                        d = min(d, abs(nums[t] - nums[t - 1]))
                if d != 2147483647:
                    ans[i][j] = d
        return ans
'''

FILES["3568_minimum_moves_to_clean_the_classroom"] = r'''# LeetCode 3568 - Minimum Moves to Clean the Classroom
# https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        d = [[0] * n for _ in range(m)]
        x = y = cnt = 0
        for i in range(m):
            for j in range(n):
                c = classroom[i][j]
                if c == "S":
                    x, y = i, j
                elif c == "L":
                    d[i][j] = cnt
                    cnt += 1
        if cnt == 0:
            return 0
        vis = [[[[False] * (1 << cnt) for _ in range(energy + 1)] for _ in range(n)] for _ in range(m)]
        q = [[x, y, energy, (1 << cnt) - 1]]
        vis[x][y][energy][(1 << cnt) - 1] = True
        dirs = [-1, 0, 1, 0, -1]
        ans = 0
        while q:
            t = q
            q = []
            for s in t:
                i, j, cur_energy, mask = s
                if mask == 0:
                    return ans
                if cur_energy <= 0:
                    continue
                for kk in range(4):
                    nx, ny = i + dirs[kk], j + dirs[kk + 1]
                    if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != "X":
                        nxt_energy = energy if classroom[nx][ny] == "R" else cur_energy - 1
                        nxt_mask = mask
                        if classroom[nx][ny] == "L":
                            nxt_mask &= ~(1 << d[nx][ny])
                        if not vis[nx][ny][nxt_energy][nxt_mask]:
                            vis[nx][ny][nxt_energy][nxt_mask] = True
                            q.append([nx, ny, nxt_energy, nxt_mask])
            ans += 1
        return -1
'''

FILES["3569_maximize_count_of_distinct_primes_after_split"] = r'''# LeetCode 3569 - Maximize Count of Distinct Primes After Split
# https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

from typing import List


class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        mx = max(nums)
        for q in queries:
            mx = max(mx, q[1])
        is_p = [False] * (mx + 1)
        for i in range(2, mx + 1):
            is_p[i] = True
        i = 2
        while i * i <= mx:
            if is_p[i]:
                for j in range(i * i, mx + 1, i):
                    is_p[j] = False
            i += 1
        ans = [0] * len(queries)
        for qi, q in enumerate(queries):
            nums[q[0]] = q[1]
            best = 0
            left = {}
            right = {}
            for v in nums:
                if v <= mx and is_p[v]:
                    right[v] = right.get(v, 0) + 1
            for i in range(len(nums) - 1):
                v = nums[i]
                if v <= mx and is_p[v]:
                    left[v] = left.get(v, 0) + 1
                    c = right[v] - 1
                    if c == 0:
                        del right[v]
                    else:
                        right[v] = c
                best = max(best, len(left) + len(right))
            ans[qi] = best
        return ans
'''

FILES["3571_find_the_shortest_superstring_ii"] = r'''# LeetCode 3571 - Find the Shortest Superstring II
# https://leetcode.com/problems/find-the-shortest-superstring-ii/


class Solution:
    def shortestSuperstring(self, s1: str, s2: str) -> str:
        if len(s1) > len(s2):
            return self.shortestSuperstring(s2, s1)
        m = len(s1)
        if s1 in s2:
            return s2
        for i in range(m):
            if s2.startswith(s1[i:]):
                return s1[:i] + s2
            length = m - i
            if len(s2) >= length and s2[-length:] == s1[:length]:
                return s2 + s1[m - i :]
        return s1 + s2
'''

FILES["3572_maximize_ysum_by_picking_a_triplet_of_distinct_xvalues"] = r'''# LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
# https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

from typing import List


class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        arr = [[x[i], y[i]] for i in range(n)]
        arr.sort(key=lambda p: -p[1])
        ans = 0
        vis = set()
        for a, b in arr:
            if a not in vis:
                vis.add(a)
                ans += b
                if len(vis) == 3:
                    return ans
        return -1
'''

FILES["3573_best_time_to_buy_and_sell_stock_v"] = r'''# LeetCode 3573 - Best Time to Buy and Sell Stock V
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        f = [[[0, 0, 0] for _ in range(k + 1)] for _ in range(n)]
        for j in range(1, k + 1):
            f[0][j][1] = -prices[0]
            f[0][j][2] = prices[0]
        for i in range(1, n):
            for j in range(1, k + 1):
                f[i][j][0] = max(
                    f[i - 1][j][0],
                    max(f[i - 1][j][1] + prices[i], f[i - 1][j][2] - prices[i]),
                )
                f[i][j][1] = max(f[i - 1][j][1], f[i - 1][j - 1][0] - prices[i])
                f[i][j][2] = max(f[i - 1][j][2], f[i - 1][j - 1][0] + prices[i])
        return f[n - 1][k][0]
'''

FILES["3574_maximize_subarray_gcd_score"] = r'''# LeetCode 3574 - Maximize Subarray GCD Score
# https://leetcode.com/problems/maximize-subarray-gcd-score/

from typing import List


def gcd3574(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * n
        for i in range(n):
            x = nums[i]
            while x % 2 == 0:
                cnt[i] += 1
                x //= 2
        ans = 0
        for l in range(n):
            g = 0
            mi = 2147483647
            t = 0
            for r in range(l, n):
                g = gcd3574(g, nums[r])
                if cnt[r] < mi:
                    mi = cnt[r]
                    t = 1
                elif cnt[r] == mi:
                    t += 1
                score = g * (r - l + 1)
                if t <= k:
                    score *= 2
                ans = max(ans, score)
        return ans
'''

FILES["3575_maximum_good_subtree_score"] = r'''# LeetCode 3575 - Maximum Good Subtree Score
# https://leetcode.com/problems/maximum-good-subtree-score/

from typing import Dict, List, Tuple


class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        MOD = 1000000007
        n = len(vals)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[par[i]].append(i)
        ans = 0

        def digit_mask(x: int) -> Tuple[int, int, int]:
            v = x
            mask = 0
            if x == 0:
                return (1, 1, 0)
            while x > 0:
                d = x % 10
                if (mask & (1 << d)) != 0:
                    return (0, 0, 0)
                mask |= 1 << d
                x //= 10
            return (mask, 1, v)

        def dfs(u: int) -> Dict[int, int]:
            nonlocal ans
            dp = {0: 0}
            dm = digit_mask(vals[u])
            if dm[1] == 1:
                dp[dm[0]] = dm[2]
            for c in g[u]:
                child = dfs(c)
                ndp = {}
                for k1, v1 in dp.items():
                    for k2, v2 in child.items():
                        if (k1 & k2) == 0:
                            nm = k1 | k2
                            ndp[nm] = max(ndp.get(nm, 0), v1 + v2)
                for k, v in dp.items():
                    ndp[k] = max(ndp.get(k, 0), v)
                for k, v in child.items():
                    ndp[k] = max(ndp.get(k, 0), v)
                dp = ndp
            best = 0
            for s in dp.values():
                best = max(best, s)
            ans = (ans + best) % MOD
            return dp

        dfs(0)
        return ans
'''


def main() -> None:
    for folder, text in FILES.items():
        path = ROOT / folder / "solution.py"
        path.write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {folder}")
    print(f"done {len(FILES)}")


if __name__ == "__main__":
    main()
