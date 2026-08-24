#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3605_minimum_stability_factor_of_array"] = r'''# LeetCode 3605 - Minimum Stability Factor of Array
# https://leetcode.com/problems/minimum-stability-factor-of-array/

from typing import List


def gcd3605(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def ok3605(nums: List[int], max_c: int, x: int) -> bool:
    n = len(nums)
    if x >= n:
        return True
    changes = 0
    i = 0
    while i + x < n:
        g = nums[i]
        for j in range(i + 1, i + x + 1):
            g = gcd3605(g, nums[j])
        if g > 1:
            changes += 1
            i += x + 1
        else:
            i += 1
    return changes <= max_c


class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if ok3605(nums, maxC, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
'''

FILES["3606_coupon_code_validator"] = r'''# LeetCode 3606 - Coupon Code Validator
# https://leetcode.com/problems/coupon-code-validator/

from typing import List


def check3606(s: str) -> bool:
    if not s:
        return False
    for c in s:
        if not (c.isalnum() or c == "_"):
            return False
    return True


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        bs = {"electronics", "grocery", "pharmacy", "restaurant"}
        idx = []
        for i in range(len(code)):
            if isActive[i] and businessLine[i] in bs and check3606(code[i]):
                idx.append(i)
        idx.sort(key=lambda i: (businessLine[i], code[i]))
        return [code[i] for i in idx]
'''

FILES["3607_power_grid_maintenance"] = r'''# LeetCode 3607 - Power Grid Maintenance
# https://leetcode.com/problems/power-grid-maintenance/

from typing import List


class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        parent = list(range(c + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                if ra < rb:
                    parent[rb] = ra
                else:
                    parent[ra] = rb

        for e in connections:
            unite(e[0], e[1])
        online = [True] * (c + 1)
        comp = {}
        for i in range(1, c + 1):
            r = find(i)
            comp.setdefault(r, []).append(i)
        for ids in comp.values():
            ids.sort()
        ptr = {}
        ans = []
        for q in queries:
            t, x = q[0], q[1]
            if t == 2:
                online[x] = False
                continue
            if online[x]:
                ans.append(x)
                continue
            r = find(x)
            ids = comp[r]
            p = ptr.get(r, 0)
            while p < len(ids) and not online[ids[p]]:
                p += 1
            ptr[r] = p
            ans.append(ids[p] if p < len(ids) else -1)
        return ans
'''

FILES["3608_minimum_time_for_k_connected_components"] = r'''# LeetCode 3608 - Minimum Time for K Connected Components
# https://leetcode.com/problems/minimum-time-for-k-connected-components/

from typing import List


class UnionFind3608:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def unite(self, a: int, b: int) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True


class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        edges = sorted(edges, key=lambda e: e[2])
        uf = UnionFind3608(n)
        cnt = n
        for i in range(len(edges) - 1, -1, -1):
            if uf.unite(edges[i][0], edges[i][1]):
                cnt -= 1
                if cnt < k:
                    return edges[i][2]
        return 0
'''

FILES["3609_minimum_moves_to_reach_target_in_grid"] = r'''# LeetCode 3609 - Minimum Moves to Reach Target in Grid
# https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/


class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        ans = 0
        while tx > sx or ty > sy:
            if tx < sx or ty < sy:
                return -1
            if tx == ty:
                return -1
            if tx > ty:
                if ty > sy:
                    if tx >= 2 * ty:
                        if tx % 2 != 0:
                            return -1
                        tx //= 2
                    else:
                        tx -= ty
                    ans += 1
                else:
                    if ty != sy:
                        return -1
                    while tx > sx:
                        if tx >= 2 * ty:
                            if tx % 2 != 0:
                                return -1
                            tx //= 2
                        else:
                            tx -= ty
                        ans += 1
                        if tx < sx:
                            return -1
            else:
                if tx > sx:
                    if ty >= 2 * tx:
                        if ty % 2 != 0:
                            return -1
                        ty //= 2
                    else:
                        ty -= tx
                    ans += 1
                else:
                    if tx != sx:
                        return -1
                    while ty > sy:
                        if ty >= 2 * tx:
                            if ty % 2 != 0:
                                return -1
                            ty //= 2
                        else:
                            ty -= tx
                        ans += 1
                        if ty < sy:
                            return -1
        return ans if tx == sx and ty == sy else -1
'''

FILES["3610_minimum_number_of_primes_to_sum_to_target"] = r'''# LeetCode 3610 - Minimum Number of Primes to Sum to Target
# https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/


_primes3610 = []


def ensure_primes3610() -> None:
    if _primes3610:
        return
    x = 2
    while len(_primes3610) < 1000:
        is_prime = True
        for p in _primes3610:
            if p * p > x:
                break
            if x % p == 0:
                is_prime = False
                break
        if is_prime:
            _primes3610.append(x)
        x += 1


class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        ensure_primes3610()
        Inf = 2147483647 // 2
        f = [Inf] * (n + 1)
        f[0] = 0
        for pi in range(m):
            x = _primes3610[pi]
            for i in range(x, n + 1):
                if f[i - x] + 1 < f[i]:
                    f[i] = f[i - x] + 1
        return f[n] if f[n] < Inf else -1
'''

FILES["3612_process_string_with_special_operations_i"] = r'''# LeetCode 3612 - Process String with Special Operations I
# https://leetcode.com/problems/process-string-with-special-operations-i/


class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for c in s:
            if c.isalpha():
                result.append(c)
            elif c == "*":
                if result:
                    result.pop()
            elif c == "#":
                result = result + result
            elif c == "%":
                result.reverse()
        return "".join(result)
'''

FILES["3613_minimize_maximum_component_cost"] = r'''# LeetCode 3613 - Minimize Maximum Component Cost
# https://leetcode.com/problems/minimize-maximum-component-cost/

from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        p = list(range(n))

        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        if k == n:
            return 0
        edges.sort(key=lambda e: e[2])
        cnt = n
        for e in edges:
            pu, pv = find(e[0]), find(e[1])
            if pu != pv:
                p[pu] = pv
                cnt -= 1
                if cnt <= k:
                    return e[2]
        return 0
'''

FILES["3614_process_string_with_special_operations_ii"] = r'''# LeetCode 3614 - Process String with Special Operations II
# https://leetcode.com/problems/process-string-with-special-operations-ii/


class Solution:
    def processStr(self, s: str, k: int) -> str:
        m = 0
        for c in s:
            if c == "*":
                m = m - 1 if m > 0 else 0
            elif c == "#":
                m <<= 1
            elif c != "%":
                m += 1
        k2 = k
        if k2 >= m:
            return "."
        i = len(s) - 1
        while True:
            c = s[i]
            if c == "*":
                m += 1
            elif c == "#":
                m //= 2
                if k2 >= m:
                    k2 -= m
            elif c == "%":
                k2 = m - 1 - k2
            else:
                m -= 1
                if k2 == m:
                    return c
            i -= 1
'''

FILES["3615_longest_palindromic_path_in_graph"] = r'''# LeetCode 3615 - Longest Palindromic Path in Graph
# https://leetcode.com/problems/longest-palindromic-path-in-graph/

from collections import deque
from typing import List


class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        def pack(a: int, b: int) -> int:
            return (a << 32) | (b & 0xFFFFFFFF)

        def expand_pal(l: int, r: int) -> int:
            vis = set()
            q = deque()
            len0 = 2 if l != r else 1
            q.append((l, r, len0))
            best = len0
            vis.add(pack(min(l, r), max(l, r)))
            while q:
                cur0, cur1, cur2 = q.popleft()
                for a in g[cur0]:
                    for b in g[cur1]:
                        if a == b or label[a] != label[b]:
                            continue
                        p = pack(min(a, b), max(a, b))
                        if p in vis:
                            continue
                        vis.add(p)
                        nl = cur2 + 2
                        best = max(best, nl)
                        q.append((a, b, nl))
            return best

        ans = 1
        for i in range(n):
            ans = max(ans, expand_pal(i, i))
            for j in g[i]:
                if i < j and label[i] == label[j]:
                    ans = max(ans, expand_pal(i, j))
        return ans
'''

FILES["3616_number_of_student_replacements"] = r'''# LeetCode 3616 - Number of Student Replacements
# https://leetcode.com/problems/number-of-student-replacements/

from typing import List


class Solution:
    def totalReplacements(self, ranks: List[int]) -> int:
        ans = 0
        cur = ranks[0]
        for x in ranks:
            if x < cur:
                cur = x
                ans += 1
        return ans
'''

FILES["3618_split_array_by_prime_indices"] = r'''# LeetCode 3618 - Split Array by Prime Indices
# https://leetcode.com/problems/split-array-by-prime-indices/

from typing import List, Optional

_PRIMES3618: Optional[List[bool]] = None


def primes3618() -> List[bool]:
    global _PRIMES3618
    if _PRIMES3618 is None:
        m = 100010
        primes = [True] * m
        primes[0] = primes[1] = False
        for i in range(2, m):
            if primes[i]:
                for j in range(i + i, m, i):
                    primes[j] = False
        _PRIMES3618 = primes
    return _PRIMES3618


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        pr = primes3618()
        ans = 0
        for i, x in enumerate(nums):
            if pr[i]:
                ans += x
            else:
                ans -= x
        return abs(ans)
'''

FILES["3619_count_islands_with_total_value_divisible_by_k"] = r'''# LeetCode 3619 - Count Islands With Total Value Divisible by K
# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [-1, 0, 1, 0, -1]

        def dfs(i: int, j: int) -> int:
            s = grid[i][j]
            grid[i][j] = 0
            for d in range(4):
                x, y = i + dirs[d], j + dirs[d + 1]
                if 0 <= x < m and 0 <= y < n and grid[x][y] > 0:
                    s += dfs(x, y)
            return s

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and dfs(i, j) % k == 0:
                    ans += 1
        return ans
'''

FILES["3620_network_recovery_pathways"] = r'''# LeetCode 3620 - Network Recovery Pathways
# https://leetcode.com/problems/network-recovery-pathways/

from typing import List


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        l, r = 2147483647, 0
        for e in edges:
            u, v, w = e[0], e[1], e[2]
            if not online[u] or not online[v]:
                continue
            g[u].append((v, w))
            l = min(l, w)
            r = max(r, w)
        if l == 2147483647:
            return -1

        def check(mid: int) -> bool:
            INF = 1073741823
            dist = [INF] * n
            dist[0] = 0
            pq = [[0, 0]]
            while pq:
                pq.sort(key=lambda x: x[0])
                d, u = pq.pop(0)
                if d > k:
                    return False
                if u == n - 1:
                    return True
                if dist[u] < d:
                    continue
                for v, w in g[u]:
                    if w < mid:
                        continue
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        pq.append([nd, v])
            return False

        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l if check(l) else -1
'''

FILES["3621_number_of_integers_with_popcount_depth_equal_to_k_i"] = r'''# LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
# https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/


class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0:
            return 1 if n >= 1 else 0

        def bit_count(x: int) -> int:
            c = 0
            while x:
                c += x & 1
                x >>= 1
            return c

        def depth(x: int) -> int:
            if x <= 0:
                return 100
            d = 0
            while x > 1:
                x = bit_count(x)
                d += 1
            return d

        bits = []
        x = n
        while x > 0:
            bits.append(str(x & 1))
            x //= 2
        s = "".join(reversed(bits)) if bits else "0"
        memo = {}

        def dfs(pos: int, tight: int, started: int, pc: int) -> int:
            if pos == len(s):
                if started == 0:
                    return 0
                if pc == 1:
                    return 1 if k == 1 else 0
                return 1 if depth(pc) == k - 1 else 0
            key = (pos, tight, started, pc)
            if key in memo:
                return memo[key]
            up = int(s[pos]) if tight == 1 else 1
            res = 0
            for dig in range(up + 1):
                nt = 1 if tight == 1 and dig == up else 0
                if started == 0 and dig == 0:
                    res += dfs(pos + 1, nt, 0, 0)
                else:
                    res += dfs(pos + 1, nt, 1, pc + dig)
            memo[key] = res
            return res

        return dfs(0, 1, 0, 0)
'''

FILES["3622_check_divisibility_by_digit_sum_and_product"] = r'''# LeetCode 3622 - Check Divisibility by Digit Sum and Product
# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        x = n
        while x != 0:
            v = x % 10
            x //= 10
            s += v
            p *= v
        return n % (s + p) == 0
'''

FILES["3623_count_number_of_trapezoids_i"] = r'''# LeetCode 3623 - Count Number of Trapezoids I
# https://leetcode.com/problems/count-number-of-trapezoids-i/

from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 1000000007
        cnt = {}
        for p in points:
            cnt[p[1]] = cnt.get(p[1], 0) + 1
        ans = 0
        pre = 0
        for c in cnt.values():
            lines = c * (c - 1) // 2
            ans = (ans + pre * lines) % MOD
            pre = (pre + lines) % MOD
        return ans
'''

FILES["3624_number_of_integers_with_popcount_depth_equal_to_k_ii"] = r'''# LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
# https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

from typing import List


class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def bit_count(x: int) -> int:
            c = 0
            v = x
            while v:
                c += v & 1
                v >>= 1
            return c

        def depth(x: int) -> int:
            v = x
            if v == 1:
                return 0
            d = 0
            while v > 1:
                v = bit_count(v)
                d += 1
            return d

        a = nums[:]
        ans = []
        for q in queries:
            if q[0] == 1:
                l, r, k = q[1], q[2], q[3]
                cnt = 0
                for i in range(l, r + 1):
                    if depth(a[i]) == k:
                        cnt += 1
                ans.append(cnt)
            else:
                a[q[1]] = q[2]
        return ans
'''

FILES["3625_count_number_of_trapezoids_ii"] = r'''# LeetCode 3625 - Count Number of Trapezoids II
# https://leetcode.com/problems/count-number-of-trapezoids-ii/

from typing import Dict, List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        cnt1 = {}
        cnt2 = {}

        def get_or(m: dict, k) -> dict:
            if k not in m:
                m[k] = {}
            return m[k]

        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i):
                x2, y2 = points[j][0], points[j][1]
                dx, dy = x2 - x1, y2 - y1
                if dx == 0:
                    k = 1e9
                    b = x1
                else:
                    k = dy / dx
                    b = (y1 * dx - x1 * dy) / dx
                m1 = get_or(cnt1, k)
                m1[b] = m1.get(b, 0) + 1
                p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000)
                m2 = get_or(cnt2, p)
                m2[k] = m2.get(k, 0) + 1
        ans = 0
        for e in cnt1.values():
            s = 0
            for t in e.values():
                ans += s * t
                s += t
        for e in cnt2.values():
            s = 0
            for t in e.values():
                ans -= s * t
                s += t
        return ans
'''

FILES["3627_maximum_median_sum_of_subsequences_of_size_3"] = r'''# LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
# https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

from typing import List


class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n // 3, n, 2):
            ans += nums[i]
        return ans
'''

FILES["3628_maximum_number_of_subsequences_after_one_inserting"] = r'''# LeetCode 3628 - Maximum Number of Subsequences After One Inserting
# https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/


class Solution:
    def numOfSubsequences(self, s: str) -> int:
        def calc(st: str, t: str) -> int:
            cnt = 0
            a = 0
            for c in st:
                if c == t[1]:
                    cnt += a
                if c == t[0]:
                    a += 1
            return cnt

        l = r = 0
        for c in s:
            if c == "T":
                r += 1
        ans = 0
        mx = 0
        for c in s:
            if c == "T":
                r -= 1
            if c == "C":
                ans += l * r
            if c == "L":
                l += 1
            mx = max(mx, l * r)
        mx = max(mx, max(calc(s, "LC"), calc(s, "CT")))
        return ans + mx
'''

FILES["3629_minimum_jumps_to_reach_end_via_prime_teleportation"] = r'''# LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

from typing import List, Optional

_FACTORS3629: Optional[List[List[int]]] = None


def factors3629() -> List[List[int]]:
    global _FACTORS3629
    if _FACTORS3629 is None:
        mx = 1000001
        factors = [[] for _ in range(mx)]
        for i in range(2, mx):
            if not factors[i]:
                for j in range(i, mx, i):
                    factors[j].append(i)
        _FACTORS3629 = factors
    return _FACTORS3629


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        fac = factors3629()
        n = len(nums)
        g = {}
        for i, v in enumerate(nums):
            for p in fac[v]:
                g.setdefault(p, []).append(i)
        ans = 0
        vis = [False] * n
        vis[0] = True
        q = [0]
        while True:
            nq = []
            for i in q:
                if i == n - 1:
                    return ans
                idx = list(g.get(nums[i], []))
                idx.append(i + 1)
                if i > 0:
                    idx.append(i - 1)
                for j in idx:
                    if 0 <= j < n and not vis[j]:
                        vis[j] = True
                        nq.append(j)
                g[nums[i]] = []
            q = nq
            ans += 1
'''

FILES["3630_partition_array_for_maximum_xor_and_and"] = r'''# LeetCode 3630 - Partition Array for Maximum XOR and AND
# https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/

from typing import List


class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0
        for mask in range(1 << n):
            and_val = -1
            xor_rest = 0
            for i in range(n):
                if ((mask >> i) & 1) != 0:
                    and_val = nums[i] if and_val < 0 else (and_val & nums[i])
                else:
                    xor_rest ^= nums[i]
            if and_val < 0:
                and_val = 0
            comp = ((1 << n) - 1) ^ mask
            sub = comp
            while True:
                x1 = 0
                for i in range(n):
                    if ((sub >> i) & 1) != 0:
                        x1 ^= nums[i]
                x2 = xor_rest ^ x1
                best = max(best, and_val + x1 + x2)
                if sub == 0:
                    break
                sub = (sub - 1) & comp
        return best
'''

FILES["3631_sort_threats_by_severity_and_exploitability"] = r'''# LeetCode 3631 - Sort Threats by Severity and Exploitability
# https://leetcode.com/problems/sort-threats-by-severity-and-exploitability/

from typing import List


class Solution:
    def sortThreats(self, threats: List[List[int]]) -> List[List[int]]:
        threats.sort(key=lambda a: (-(2 * a[1] + a[2]), a[0]))
        return threats
'''

FILES["3632_subarrays_with_xor_at_least_k"] = r'''# LeetCode 3632 - Subarrays With XOR At Least K
# https://leetcode.com/problems/subarrays-with-xor-at-least-k/

from typing import List


class Solution:
    def subarraysWithXorAtLeastK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            x = 0
            for j in range(i, n):
                x ^= nums[j]
                if x >= k:
                    ans += 1
        return ans
'''

FILES["3633_earliest_finish_time_for_land_and_water_rides_i"] = r'''# LeetCode 3633 - Earliest Finish Time for Land and Water Rides I
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        def calc(a1: List[int], t1: List[int], a2: List[int], t2: List[int]) -> int:
            min_end = min(a1[i] + t1[i] for i in range(len(a1)))
            ans = min(max(min_end, a2[i]) + t2[i] for i in range(len(a2)))
            return ans

        return min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration),
        )
'''

FILES["3634_minimum_removals_to_balance_array"] = r'''# LeetCode 3634 - Minimum Removals to Balance Array
# https://leetcode.com/problems/minimum-removals-to-balance-array/

from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def lower_bound(a: List[int], target: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) >> 1
                if a[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        cnt = 0
        for i in range(n):
            j = n
            if nums[i] * k <= nums[n - 1]:
                target = nums[i] * k + 1
                j = lower_bound(nums, target)
            cnt = max(cnt, j - i)
        return n - cnt
'''


def main() -> None:
    for folder, text in FILES.items():
        path = ROOT / folder / "solution.py"
        path.write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {folder}")
    print(f"done {len(FILES)}")


if __name__ == "__main__":
    main()
