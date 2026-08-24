#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3362_zero_array_transformation_iii"] = r'''# LeetCode 3362 - Zero Array Transformation III
# https://leetcode.com/problems/zero-array-transformation-iii/

from typing import List


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda a: a[0])
        h = []
        n = len(nums)
        diff = [0] * (n + 1)
        j = 0
        used = 0
        cur = 0
        for i in range(n):
            cur += diff[i]
            while j < len(queries) and queries[j][0] == i:
                h.append(queries[j][1])
                j += 1
            while cur < nums[i]:
                if not h:
                    return -1
                h.sort(reverse=True)
                if h[0] < i:
                    return -1
                r = h.pop(0)
                cur += 1
                diff[r + 1] -= 1
                used += 1
        return len(queries) - used
'''

FILES["3363_find_the_maximum_number_of_fruits_collected"] = r'''# LeetCode 3363 - Find the Maximum Number of Fruits Collected
# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = 0
        for i in range(n):
            ans += fruits[i][i]
            fruits[i][i] = 0
        neg = -(1 << 30)
        dp2 = [[neg] * n for _ in range(n)]
        dp3 = [[neg] * n for _ in range(n)]
        dp2[0][n - 1] = fruits[0][n - 1]
        for i in range(n):
            for j in range(n):
                if dp2[i][j] == neg:
                    continue
                for dj in (-1, 0, 1):
                    ni, nj = i + 1, j + dj
                    if ni < n and 0 <= nj < n and nj > ni:
                        v = dp2[i][j] + fruits[ni][nj]
                        if v > dp2[ni][nj]:
                            dp2[ni][nj] = v
        dp3[n - 1][0] = fruits[n - 1][0]
        for j in range(n):
            for i in range(n):
                if dp3[i][j] == neg:
                    continue
                for di in (-1, 0, 1):
                    ni, nj = i + di, j + 1
                    if 0 <= ni < n and nj < n and ni > nj:
                        v = dp3[i][j] + fruits[ni][nj]
                        if v > dp3[ni][nj]:
                            dp3[ni][nj] = v
        ans += dp2[n - 1][n - 1] + dp3[n - 1][n - 1]
        return ans
'''

FILES["3364_minimum_positive_sum_subarray"] = r'''# LeetCode 3364 - Minimum Positive Sum Subarray
# https://leetcode.com/problems/minimum-positive-sum-subarray/

from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        ans = 2147483647
        found = False
        for i in range(n):
            length = l
            while length <= r and i + length <= n:
                s = pref[i + length] - pref[i]
                if s > 0 and s < ans:
                    ans = s
                    found = True
                length += 1
        return ans if found else -1
'''

FILES["3365_rearrange_k_substrings_to_form_target_string"] = r'''# LeetCode 3365 - Rearrange K Substrings to Form Target String
# https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        sz = n // k
        cnt = {}
        for i in range(0, n, sz):
            a = s[i : i + sz]
            b = t[i : i + sz]
            cnt[a] = cnt.get(a, 0) + 1
            cnt[b] = cnt.get(b, 0) - 1
        return all(v == 0 for v in cnt.values())
'''

FILES["3366_minimum_array_sum"] = r'''# LeetCode 3366 - Minimum Array Sum
# https://leetcode.com/problems/minimum-array-sum/

from typing import List


def tryCand(ndp: List[List[float]], base: float, na: int, nb: int, v: int) -> None:
    if base + v < ndp[na][nb]:
        ndp[na][nb] = base + v


class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        inf = 1e18
        dp = [[inf] * (op2 + 1) for _ in range(op1 + 1)]
        dp[0][0] = 0
        for x in nums:
            ndp = [[inf] * (op2 + 1) for _ in range(op1 + 1)]
            for a in range(op1 + 1):
                for b in range(op2 + 1):
                    if dp[a][b] == inf:
                        continue
                    tryCand(ndp, dp[a][b], a, b, x)
                    if a < op1:
                        tryCand(ndp, dp[a][b], a + 1, b, (x + 1) // 2)
                    if b < op2 and x >= k:
                        tryCand(ndp, dp[a][b], a, b + 1, x - k)
                    if a < op1 and b < op2:
                        v1 = (x + 1) // 2
                        if v1 >= k:
                            tryCand(ndp, dp[a][b], a + 1, b + 1, v1 - k)
                        if x >= k:
                            tryCand(ndp, dp[a][b], a + 1, b + 1, (x - k + 1) // 2)
            dp = ndp
        ans = inf
        for a in range(op1 + 1):
            for b in range(op2 + 1):
                if dp[a][b] < ans:
                    ans = dp[a][b]
        return int(ans)
'''

FILES["3367_maximize_sum_of_weights_after_edge_removals"] = r'''# LeetCode 3367 - Maximize Sum of Weights after Edge Removals
# https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

from typing import List, Tuple


class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))

        def dfs(u: int, p: int) -> Tuple[int, int]:
            base = 0
            gains = []
            for to, w in g[u]:
                if to == p:
                    continue
                child = dfs(to, u)
                base += child[1]
                gain = child[0] + w - child[1]
                if gain > 0:
                    gains.append(gain)
            gains.sort(reverse=True)
            with_p = base
            without = base
            for i in range(min(len(gains), k - 1)):
                with_p += gains[i]
            for i in range(min(len(gains), k)):
                without += gains[i]
            return with_p, without

        return dfs(0, -1)[1]
'''

FILES["3369_design_an_array_statistics_tracker"] = r'''# LeetCode 3369 - Design an Array Statistics Tracker
# https://leetcode.com/problems/design-an-array-statistics-tracker/


class StatisticsTracker:
    def __init__(self) -> None:
        self.arr = []
        self.sum = 0
        self.freq = {}
        self.modeFreq = 0
        self.modes = set()

    def addNumber(self, num: int) -> None:
        self.arr.append(num)
        self.sum += num
        f = self.freq.get(num, 0) + 1
        self.freq[num] = f
        if f > self.modeFreq:
            self.modeFreq = f
            self.modes.clear()
            self.modes.add(num)
        elif f == self.modeFreq:
            self.modes.add(num)

    def removeFirst(self) -> None:
        if not self.arr:
            return
        num = self.arr.pop(0)
        self.sum -= num
        f = self.freq[num] - 1
        if f == 0:
            del self.freq[num]
        else:
            self.freq[num] = f
        self.modeFreq = 0
        self.modes.clear()
        for v, ff in self.freq.items():
            if ff > self.modeFreq:
                self.modeFreq = ff
                self.modes.clear()
                self.modes.add(v)
            elif ff == self.modeFreq:
                self.modes.add(v)

    def getMean(self) -> int:
        if not self.arr:
            return 0
        return self.sum // len(self.arr)

    def getMedian(self) -> int:
        n = len(self.arr)
        tmp = sorted(self.arr)
        if n % 2 == 1:
            return tmp[n // 2]
        return tmp[n // 2 - 1]

    def getMode(self) -> int:
        best = 9007199254740991
        for v in self.modes:
            if v < best:
                best = v
        if best == 9007199254740991:
            return 0
        return best
'''

FILES["3370_smallest_number_with_all_set_bits"] = r'''# LeetCode 3370 - Smallest Number With All Set Bits
# https://leetcode.com/problems/smallest-number-with-all-set-bits/


class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = x * 2 + 1
        return x
'''

FILES["3371_identify_the_largest_outlier_in_an_array"] = r'''# LeetCode 3371 - Identify the Largest Outlier in an Array
# https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

from typing import List


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = 0
        freq = {}
        for x in nums:
            total += x
            freq[x] = freq.get(x, 0) + 1
        ans = -2147483648
        for x in nums:
            freq[x] -= 1
            rem = total - x
            if rem % 2 == 0:
                cand = rem // 2
                if freq.get(cand, 0) > 0 and x > ans:
                    ans = x
            freq[x] += 1
        return ans
'''

FILES["3372_maximize_the_number_of_target_nodes_after_connecting_trees_i"] = r'''# LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

from typing import List


def buildTree(n: int, edges: List[List[int]]) -> List[List[int]]:
    g = [[] for _ in range(n)]
    for e in edges:
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])
    return g


def countWithin(g: List[List[int]], start: int, k: int) -> int:
    if k < 0:
        return 0
    n = len(g)
    vis = [False] * n
    q = [[start, 0]]
    vis[start] = True
    cnt = 0
    qi = 0
    while qi < len(q):
        u, d = q[qi]
        qi += 1
        cnt += 1
        if d == k:
            continue
        for v in g[u]:
            if not vis[v]:
                vis[v] = True
                q.append([v, d + 1])
    return cnt


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        g1 = buildTree(n, edges1)
        g2 = buildTree(m, edges2)
        cnt1 = [countWithin(g1, i, k) for i in range(n)]
        best2 = 0
        if k > 0:
            for i in range(m):
                c = countWithin(g2, i, k - 1)
                if c > best2:
                    best2 = c
        return [cnt1[i] + best2 for i in range(n)]
'''

FILES["3373_maximize_the_number_of_target_nodes_after_connecting_trees_ii"] = r'''# LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

from typing import List


def buildTree(n: int, edges: List[List[int]]) -> List[List[int]]:
    g = [[] for _ in range(n)]
    for e in edges:
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])
    return g


def bipartiteCount(g: List[List[int]], color: List[int]) -> List[int]:
    for i in range(len(color)):
        color[i] = -1
    q = [0]
    color[0] = 0
    cnt = [1, 0]
    qi = 0
    while qi < len(q):
        u = q[qi]
        qi += 1
        for v in g[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                cnt[color[v]] += 1
                q.append(v)
    return cnt


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        g1 = buildTree(n, edges1)
        g2 = buildTree(m, edges2)
        color1 = [0] * n
        color2 = [0] * m
        c1 = bipartiteCount(g1, color1)
        c2 = bipartiteCount(g2, color2)
        best2 = max(c2[0], c2[1])
        return [c1[color1[i]] + best2 for i in range(n)]
'''

FILES["3375_minimum_operations_to_make_array_values_equal_to_k"] = r'''# LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        for x in nums:
            if x < k:
                return -1
            if x > k:
                seen.add(x)
        return len(seen)
'''

FILES["3376_minimum_time_to_break_locks_i"] = r'''# LeetCode 3376 - Minimum Time to Break Locks I
# https://leetcode.com/problems/minimum-time-to-break-locks-i/

from typing import List


def bitsOnes(x: int) -> int:
    c = 0
    while x > 0:
        c += x & 1
        x >>= 1
    return c


class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        n = len(strength)
        inf = 1000000000
        N = 1 << n
        dp = [inf] * N
        dp[0] = 0
        for mask in range(N):
            if dp[mask] == inf:
                continue
            opened = bitsOnes(mask)
            x = 1 + opened * k
            for i in range(n):
                if (mask & (1 << i)) != 0:
                    continue
                t = (strength[i] + x - 1) // x
                nmask = mask | (1 << i)
                if dp[mask] + t < dp[nmask]:
                    dp[nmask] = dp[mask] + t
        return dp[N - 1]
'''

FILES["3377_digit_operations_to_make_two_integers_equal"] = r'''# LeetCode 3377 - Digit Operations to Make Two Integers Equal
# https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

from typing import List


def sieve(n: int) -> List[bool]:
    is_p = [False] * n
    for i in range(2, n):
        is_p[i] = True
    i = 2
    while i * i < n:
        if is_p[i]:
            for j in range(i * i, n, i):
                is_p[j] = False
        i += 1
    return is_p


class Solution:
    def minOperations(self, n: int, m: int) -> int:
        is_prime = sieve(100000)
        if is_prime[n]:
            return -1
        dist = [-1] * 100000
        pq = [[n, n]]
        dist[n] = n
        while pq:
            pq.sort(key=lambda a: a[0])
            cost, val = pq.pop(0)
            if cost != dist[val]:
                continue
            if val == m:
                return cost
            s = list(str(val))
            for i in range(len(s)):
                orig = s[i]
                for d in (-1, 1):
                    nd = (ord(orig) - 48) + d
                    if nd < 0 or nd > 9:
                        continue
                    if i == 0 and nd == 0 and len(s) > 1:
                        continue
                    s[i] = str(nd)
                    nv = int("".join(s), 10)
                    s[i] = orig
                    if is_prime[nv]:
                        continue
                    nc = cost + nv
                    if dist[nv] == -1 or nc < dist[nv]:
                        dist[nv] = nc
                        pq.append([nc, nv])
        return -1
'''

FILES["3378_count_connected_components_in_lcm_graph"] = r'''# LeetCode 3378 - Count Connected Components in LCM Graph
# https://leetcode.com/problems/count-connected-components-in-lcm-graph/

from typing import List


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        idx = {}
        for i, v in enumerate(nums):
            idx[v] = i
        for d in range(1, threshold + 1):
            first = -1
            for m in range(d, threshold + 1, d):
                if m in idx:
                    i = idx[m]
                    if first == -1:
                        first = i
                    elif nums[first] * nums[i] // gcd(nums[first], nums[i]) <= threshold:
                        unite(first, i)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = nums[i], nums[j]
                g = gcd(a, b)
                if (a // g) * b <= threshold:
                    unite(i, j)
        return len({find(i) for i in range(n)})
'''

FILES["3379_transformed_array"] = r'''# LeetCode 3379 - Transformed Array
# https://leetcode.com/problems/transformed-array/

from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            j = ((i + nums[i]) % n + n) % n
            ans[i] = nums[j]
        return ans
'''

FILES["3380_maximum_area_rectangle_with_point_constraints_i"] = r'''# LeetCode 3380 - Maximum Area Rectangle With Point Constraints I
# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/

from typing import List


def pack(x: int, y: int) -> int:
    return (x << 32) ^ (y & 0xFFFFFFFF)


class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        s = set()
        for p in points:
            s.add(pack(p[0], p[1]))
        ans = -1
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                if x1 == x2 or y1 == y2:
                    continue
                if pack(x1, y2) not in s or pack(x2, y1) not in s:
                    continue
                min_x, max_x = min(x1, x2), max(x1, x2)
                min_y, max_y = min(y1, y2), max(y1, y2)
                good = True
                for p in points:
                    x, y = p[0], p[1]
                    if min_x < x < max_x and min_y < y < max_y:
                        good = False
                        break
                    on_border = ((x == min_x or x == max_x) and min_y <= y <= max_y) or (
                        (y == min_y or y == max_y) and min_x <= x <= max_x
                    )
                    if on_border:
                        is_corner = (x == min_x or x == max_x) and (y == min_y or y == max_y)
                        if not is_corner:
                            good = False
                            break
                if good:
                    area = (max_x - min_x) * (max_y - min_y)
                    if area > ans:
                        ans = area
        return ans
'''

FILES["3381_maximum_subarray_sum_with_length_divisible_by_k"] = r'''# LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        INF = 9007199254740991
        best = [INF] * k
        best[0] = 0
        ans = -INF
        for i in range(1, n + 1):
            r = i % k
            if best[r] != INF:
                cand = pref[i] - best[r]
                if cand > ans:
                    ans = cand
            if pref[i] < best[r]:
                best[r] = pref[i]
        return ans
'''

FILES["3382_maximum_area_rectangle_with_point_constraints_ii"] = r'''# LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

from typing import List


def pack(x: int, y: int) -> int:
    return (x << 32) ^ (y & 0xFFFFFFFF)


class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        n = len(xCoord)
        points = [[xCoord[i], yCoord[i]] for i in range(n)]
        s = set()
        for p in points:
            s.add(pack(p[0], p[1]))
        ans = -1
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                if x1 == x2 or y1 == y2:
                    continue
                if pack(x1, y2) not in s or pack(x2, y1) not in s:
                    continue
                min_x, max_x = min(x1, x2), max(x1, x2)
                min_y, max_y = min(y1, y2), max(y1, y2)
                good = True
                for p in points:
                    x, y = p[0], p[1]
                    if min_x < x < max_x and min_y < y < max_y:
                        good = False
                        break
                    on_border = ((x == min_x or x == max_x) and min_y <= y <= max_y) or (
                        (y == min_y or y == max_y) and min_x <= x <= max_x
                    )
                    if on_border:
                        is_corner = (x == min_x or x == max_x) and (y == min_y or y == max_y)
                        if not is_corner:
                            good = False
                            break
                if good:
                    area = (max_x - min_x) * (max_y - min_y)
                    if area > ans:
                        ans = area
        return ans
'''

FILES["3383_minimum_runes_to_add_to_cast_spell"] = r'''# LeetCode 3383 - Minimum Runes to Add to Cast Spell
# https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

from typing import List


class Solution:
    def minRunesToAdd(
        self, n: int, crystals: List[int], flowFrom: List[int], flowTo: List[int]
    ) -> int:
        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        for i in range(len(flowFrom)):
            a, b = flowFrom[i], flowTo[i]
            g[a].append(b)
            rg[b].append(a)
        vis = [False] * n
        order = []

        def dfs1(u: int) -> None:
            vis[u] = True
            for v in g[u]:
                if not vis[v]:
                    dfs1(v)
            order.append(u)

        for i in range(n):
            if not vis[i]:
                dfs1(i)
        comp = [-1] * n
        cid = 0

        def dfs2(u: int) -> None:
            comp[u] = cid
            for v in rg[u]:
                if comp[v] == -1:
                    dfs2(v)

        for i in range(n - 1, -1, -1):
            u = order[i]
            if comp[u] == -1:
                dfs2(u)
                cid += 1
        has_crystal = [False] * cid
        for c in crystals:
            has_crystal[comp[c]] = True
        indeg = [0] * cid
        for u in range(n):
            for v in g[u]:
                if comp[u] != comp[v]:
                    indeg[comp[v]] += 1
        ans = 0
        for i in range(cid):
            if indeg[i] == 0 and not has_crystal[i]:
                ans += 1
        return ans
'''

FILES["3385_minimum_time_to_break_locks_ii"] = r'''# LeetCode 3385 - Minimum Time to Break Locks II
# https://leetcode.com/problems/minimum-time-to-break-locks-ii/

from typing import List


def bitsOnes(x: int) -> int:
    c = 0
    while x > 0:
        c += x & 1
        x >>= 1
    return c


class Solution:
    def findMinimumTime(self, strength: List[int]) -> int:
        n = len(strength)
        N = 1 << n
        inf = 1e18
        dp = [inf] * N
        dp[0] = 0
        k = 1
        for mask in range(N):
            if dp[mask] == inf:
                continue
            opened = bitsOnes(mask)
            x = 1 + opened * k
            for i in range(n):
                if (mask & (1 << i)) != 0:
                    continue
                t = (strength[i] + x - 1) // x
                nmask = mask | (1 << i)
                if dp[mask] + t < dp[nmask]:
                    dp[nmask] = dp[mask] + t
        return int(dp[N - 1])
'''

FILES["3386_button_with_longest_push_time"] = r'''# LeetCode 3386 - Button with Longest Push Time
# https://leetcode.com/problems/button-with-longest-push-time/

from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        best_t = events[0][1]
        best_i = events[0][0]
        for i in range(1, len(events)):
            t = events[i][1] - events[i - 1][1]
            if t > best_t or (t == best_t and events[i][0] < best_i):
                best_t = t
                best_i = events[i][0]
        return best_i
'''

FILES["3387_maximize_amount_after_two_days_of_conversions"] = r'''# LeetCode 3387 - Maximize Amount After Two Days of Conversions
# https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

from typing import Dict, List


def buildRateGraph(pairs: List[List[str]], rates: List[float]) -> Dict[str, Dict[str, float]]:
    g = {}
    for i in range(len(pairs)):
        a, b = pairs[i][0], pairs[i][1]
        if a not in g:
            g[a] = {}
        if b not in g:
            g[b] = {}
        g[a][b] = rates[i]
        g[b][a] = 1.0 / rates[i]
    return g


def bellman(start: str, pairs: List[List[str]], rates: List[float]) -> Dict[str, float]:
    g = buildRateGraph(pairs, rates)
    dist = {start: 1.0}
    for _ in range(100):
        updated = False
        for frm, tos in g.items():
            if frm not in dist or dist[frm] == 0:
                continue
            for to, rate in tos.items():
                nv = dist[frm] * rate
                if to not in dist or nv > dist[to]:
                    dist[to] = nv
                    updated = True
        if not updated:
            break
    return dist


class Solution:
    def maxAmount(
        self,
        initialCurrency: str,
        pairs1: List[List[str]],
        rates1: List[float],
        pairs2: List[List[str]],
        rates2: List[float],
    ) -> float:
        amt1 = bellman(initialCurrency, pairs1, rates1)
        ans = 1.0
        g2 = buildRateGraph(pairs2, rates2)
        for c, a in amt1.items():
            if a <= 0:
                continue
            dist = {c: a}
            updated = True
            it = 0
            while it < 100 and updated:
                updated = False
                for frm, tos in g2.items():
                    if frm not in dist or dist[frm] == 0:
                        continue
                    for to, rate in tos.items():
                        nv = dist[frm] * rate
                        if to not in dist or nv > dist[to]:
                            dist[to] = nv
                            updated = True
                it += 1
            if initialCurrency in dist and dist[initialCurrency] > ans:
                ans = dist[initialCurrency]
        return ans
'''

FILES["3388_count_beautiful_splits_in_an_array"] = r'''# LeetCode 3388 - Count Beautiful Splits in an Array
# https://leetcode.com/problems/count-beautiful-splits-in-an-array/

from typing import List


def equal(a: List[int], as_: int, ae: int, b: List[int], bs: int, be: int) -> bool:
    if ae - as_ != be - bs:
        return False
    for i in range(ae - as_):
        if a[as_ + i] != b[bs + i]:
            return False
    return True


class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                ok = False
                if i <= j - i and equal(nums, 0, i, nums, i, i + i):
                    ok = True
                if (not ok) and j - i <= n - j and equal(nums, i, j, nums, j, j + (j - i)):
                    ok = True
                if ok:
                    ans += 1
        return ans
'''

FILES["3389_minimum_operations_to_make_character_frequencies_equal"] = r'''# LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
# https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/


class Solution:
    def makeStringGood(self, s: str) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1
        ans = len(s)
        for t in range(1, len(s) + 1):
            pool = 0
            for i in range(26):
                if freq[i] > t:
                    pool += freq[i] - t
            deficit = 0
            for i in range(26):
                if freq[i] < t:
                    deficit += t - freq[i]
            ops = max(pool, deficit)
            if ops < ans:
                ans = ops
        if len(s) < ans:
            ans = len(s)
        return ans
'''

FILES["3391_design_a_3d_binary_matrix_with_efficient_layer_tracking"] = r'''# LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
# https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/


class Matrix3D:
    def __init__(self, n: int) -> None:
        self.n = n
        self.m = [[[0] * n for _ in range(n)] for _ in range(n)]
        self.ones = [0] * n

    def setCell(self, x: int, y: int, z: int) -> None:
        if self.m[x][y][z] == 0:
            self.m[x][y][z] = 1
            self.ones[x] += 1

    def unsetCell(self, x: int, y: int, z: int) -> None:
        if self.m[x][y][z] == 1:
            self.m[x][y][z] = 0
            self.ones[x] -= 1

    def largestMatrix(self) -> int:
        best = -1
        idx = 0
        for i in range(self.n):
            if self.ones[i] >= best:
                best = self.ones[i]
                idx = i
        return idx
'''


def main() -> None:
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.py"
        path.write_text(content, encoding="utf-8", newline="\n")
        print("wrote", folder)
    print("part3", len(FILES))


if __name__ == "__main__":
    main()
