#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3576_transform_array_to_all_equal_elements"] = r'''# LeetCode 3576 - Transform Array to All Equal Elements
# https://leetcode.com/problems/transform-array-to-all-equal-elements/

from typing import List


def check3576(nums: List[int], target: int, kk: int) -> bool:
    cnt = 0
    sign = 1
    for i in range(len(nums) - 1):
        x = nums[i] * sign
        if x == target:
            sign = 1
        else:
            sign = -1
            cnt += 1
    return cnt <= kk and nums[-1] * sign == target


class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        return check3576(nums, nums[0], k) or check3576(nums, -nums[0], k)
'''

FILES["3577_count_the_number_of_computer_unlocking_permutations"] = r'''# LeetCode 3577 - Count the Number of Computer Unlocking Permutations
# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 1000000007
        ans = 1
        for i in range(1, len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
            ans = ans * i % mod
        return ans
'''

FILES["3578_count_partitions_with_max_min_difference_at_most_k"] = r'''# LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 1000000007
        sl = {}
        n = len(nums)
        f = [0] * (n + 1)
        g = [0] * (n + 1)
        f[0] = g[0] = 1
        keys = []

        def add(v: int) -> None:
            if v not in sl:
                sl[v] = 0
                lo, hi = 0, len(keys)
                while lo < hi:
                    mid = (lo + hi) >> 1
                    if keys[mid] < v:
                        lo = mid + 1
                    else:
                        hi = mid
                keys.insert(lo, v)
            sl[v] += 1

        def rem(v: int) -> None:
            c = sl[v] - 1
            if c == 0:
                del sl[v]
                ix = keys.index(v)
                if ix >= 0:
                    keys.pop(ix)
            else:
                sl[v] = c

        l = 1
        for r in range(1, n + 1):
            add(nums[r - 1])
            while keys[-1] - keys[0] > k:
                rem(nums[l - 1])
                l += 1
            f[r] = g[r - 1]
            if l >= 2:
                f[r] = (f[r] - g[l - 2] + mod) % mod
            g[r] = (g[r - 1] + f[r]) % mod
        return f[n]
'''

FILES["3579_minimum_steps_to_convert_string_with_operations"] = r'''# LeetCode 3579 - Minimum Steps to Convert String with Operations
# https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/


class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        def calc(l: int, r: int, rev: bool) -> int:
            cnt = [[0] * 26 for _ in range(26)]
            res = 0
            for i in range(l, r + 1):
                j = r - (i - l) if rev else i
                a = ord(word1[j]) - 97
                b = ord(word2[i]) - 97
                if a != b:
                    if cnt[b][a] > 0:
                        cnt[b][a] -= 1
                    else:
                        cnt[a][b] += 1
                        res += 1
            return res

        n = len(word1)
        f = [2147483647 // 2] * (n + 1)
        f[0] = 0
        for i in range(1, n + 1):
            for j in range(i):
                a = calc(j, i - 1, False)
                b = 1 + calc(j, i - 1, True)
                f[i] = min(f[i], f[j] + min(a, b))
        return f[n]
'''

FILES["3581_count_odd_letters_from_number"] = r'''# LeetCode 3581 - Count Odd Letters from Number
# https://leetcode.com/problems/count-odd-letters-from-number/


class Solution:
    def countOddLetters(self, n: int) -> int:
        d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        mask = 0
        while n > 0:
            for c in d[n % 10]:
                mask ^= 1 << (ord(c) - 97)
            n //= 10
        cnt = 0
        while mask:
            cnt += mask & 1
            mask >>= 1
        return cnt
'''

FILES["3582_generate_tag_for_video_caption"] = r'''# LeetCode 3582 - Generate Tag for Video Caption
# https://leetcode.com/problems/generate-tag-for-video-caption/


class Solution:
    def generateTag(self, caption: str) -> str:
        ans = "#"
        words = caption.strip().split()
        i = 0
        for word in words:
            if not word:
                continue
            w = word.lower()
            if i == 0:
                ans += w
            else:
                if w:
                    w = w[0].upper() + w[1:]
                ans += w
            if len(ans) >= 100:
                break
            i += 1
        if len(ans) > 100:
            ans = ans[:100]
        return ans
'''

FILES["3583_count_special_triplets"] = r'''# LeetCode 3583 - Count Special Triplets
# https://leetcode.com/problems/count-special-triplets/

from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left = {}
        right = {}
        for x in nums:
            right[x] = right.get(x, 0) + 1
        ans = 0
        mod = 1000000007
        for x in nums:
            right[x] -= 1
            lv = left.get(x * 2, 0)
            rv = right.get(x * 2, 0)
            ans = (ans + lv * rv % mod) % mod
            left[x] = left.get(x, 0) + 1
        return ans
'''

FILES["3584_maximum_product_of_first_and_last_elements_of_a_subsequence"] = r'''# LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
# https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        ans = -(10**18)
        mx = -(10**18)
        mi = 10**18
        for i in range(m - 1, len(nums)):
            x = nums[i]
            y = nums[i - m + 1]
            mi = min(mi, y)
            mx = max(mx, y)
            ans = max(ans, max(x * mi, x * mx))
        return ans
'''

FILES["3585_find_weighted_median_node_in_tree"] = r'''# LeetCode 3585 - Find Weighted Median Node in Tree
# https://leetcode.com/problems/find-weighted-median-node-in-tree/

from collections import deque
from typing import List


class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        ans = [0] * len(queries)
        for qi, q in enumerate(queries):
            u, v = q[0], q[1]
            parent = [-2] * n
            pw = [0] * n
            parent[u] = -1
            dq = deque([u])
            while dq:
                x = dq.popleft()
                if x == v:
                    break
                for to, w in g[x]:
                    if parent[to] == -2:
                        parent[to] = x
                        pw[to] = w
                        dq.append(to)
            nodes = [v]
            weights = []
            cur = v
            while cur != u:
                weights.append(pw[cur])
                cur = parent[cur]
                nodes.append(cur)
            nodes.reverse()
            weights.reverse()
            total = sum(weights)
            need = (total + 1) // 2
            sm = 0
            med = u
            for i, w in enumerate(weights):
                sm += w
                med = nodes[i + 1]
                if sm >= need:
                    break
            ans[qi] = med
        return ans
'''

FILES["3587_minimum_adjacent_swaps_to_alternate_parity"] = r'''# LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
# https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

from typing import List


def calc3587(pos: List[List[int]], n: int, k: int) -> int:
    res = 0
    for i in range(0, n, 2):
        res += abs(pos[k][i // 2] - i)
    return res


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        pos = [[], []]
        for i, x in enumerate(nums):
            pos[x & 1].append(i)
        if abs(len(pos[0]) - len(pos[1])) > 1:
            return -1
        if len(pos[0]) > len(pos[1]):
            return calc3587(pos, len(nums), 0)
        if len(pos[0]) < len(pos[1]):
            return calc3587(pos, len(nums), 1)
        return min(calc3587(pos, len(nums), 0), calc3587(pos, len(nums), 1))
'''

FILES["3588_find_maximum_area_of_a_triangle"] = r'''# LeetCode 3588 - Find Maximum Area of a Triangle
# https://leetcode.com/problems/find-maximum-area-of-a-triangle/

from typing import List


def calc3588(coords: List[List[int]]) -> int:
    mn, mx = 10**9, 0
    f = {}
    g = {}
    for c in coords:
        x, y = c[0], c[1]
        mn = min(mn, x)
        mx = max(mx, x)
        if x in f:
            f[x] = min(f[x], y)
            g[x] = max(g[x], y)
        else:
            f[x] = y
            g[x] = y
    ans = 0
    for x, y in f.items():
        d = g[x] - y
        ans = max(ans, d * max(mx - x, x - mn))
    return ans


class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        ans = calc3588(coords)
        for c in coords:
            c[0], c[1] = c[1], c[0]
        ans = max(ans, calc3588(coords))
        return ans if ans > 0 else -1
'''

FILES["3589_count_prime_gap_balanced_subarrays"] = r'''# LeetCode 3589 - Count Prime-Gap Balanced Subarrays
# https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

from typing import List


class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        is_prime = [False] * (mx + 1)
        for i in range(2, mx + 1):
            is_prime[i] = True
        i = 2
        while i * i <= mx:
            if is_prime[i]:
                for j in range(i * i, mx + 1, i):
                    is_prime[j] = False
            i += 1
        n = len(nums)
        ans = 0
        for l in range(n):
            primes = []
            for r in range(l, n):
                if is_prime[nums[r]]:
                    primes.append(nums[r])
                if len(primes) >= 2:
                    mn = mxp = primes[0]
                    for p in primes:
                        mn = min(mn, p)
                        mxp = max(mxp, p)
                    if mxp - mn <= k:
                        ans += 1
        return ans
'''

FILES["3590_kth_smallest_path_xor_sum"] = r'''# LeetCode 3590 - Kth Smallest Path XOR Sum
# https://leetcode.com/problems/kth-smallest-path-xor-sum/

from typing import List


class Solution:
    def kthSmallest(
        self, par: List[int], vals: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(par)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[par[i]].append(i)
        xor_path = [0] * n

        def dfs(u: int) -> None:
            xor_path[u] ^= vals[u]
            for v in g[u]:
                xor_path[v] = xor_path[u]
                dfs(v)

        dfs(0)
        in_t = [0] * n
        out_t = [0] * n
        order = []

        def dfs2(u: int) -> None:
            in_t[u] = len(order)
            order.append(xor_path[u])
            for v in g[u]:
                dfs2(v)
            out_t[u] = len(order)

        dfs2(0)
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            u, k = q[0], q[1]
            sub = sorted(order[in_t[u] : out_t[u]])
            uniq = []
            for x in sub:
                if not uniq or uniq[-1] != x:
                    uniq.append(x)
            ans[i] = -1 if k > len(uniq) else uniq[k - 1]
        return ans
'''

FILES["3591_check_if_any_element_has_prime_frequency"] = r'''# LeetCode 3591 - Check if Any Element Has Prime Frequency
# https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

from typing import List


def is_prime3591(x: int) -> bool:
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        for v in cnt.values():
            if is_prime3591(v):
                return True
        return False
'''

FILES["3592_inverse_coin_change"] = r'''# LeetCode 3592 - Inverse Coin Change
# https://leetcode.com/problems/inverse-coin-change/

from typing import List


class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        dp = [0] * (n + 1)
        coins = []
        dp[0] = 1
        for amt in range(1, n + 1):
            ways = numWays[amt - 1]
            if dp[amt] == ways:
                continue
            if dp[amt] + 1 == ways:
                coins.append(amt)
                for x in range(amt, n + 1):
                    dp[x] += dp[x - amt]
                if dp[amt] != ways:
                    return []
                continue
            return []
        return coins
'''

FILES["3593_minimum_increments_to_equalize_leaf_paths"] = r'''# LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
# https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

from typing import List


class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        ans = 0

        def dfs(u: int, p: int) -> int:
            nonlocal ans
            if len(graph[u]) == 1 and p != -1:
                return cost[u]
            child_vals = []
            for v in graph[u]:
                if v == p:
                    continue
                child_vals.append(dfs(v, u))
            if not child_vals:
                return cost[u]
            mx = max(child_vals)
            for c in child_vals:
                if c < mx:
                    ans += 1
            return mx + cost[u]

        dfs(0, -1)
        return ans
'''

FILES["3594_minimum_time_to_transport_all_individuals"] = r'''# LeetCode 3594 - Minimum Time to Transport All Individuals
# https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

from typing import List


class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        t = sorted(time)
        total = 0.0
        stage = 0
        left = n
        while left > 0:
            take = min(k, left)
            slow = t[left - 1]
            total += slow * mul[stage % m]
            left -= take
            stage += 1
            if left > 0:
                total += t[0] * mul[stage % m]
                stage += 1
        return total
'''

FILES["3595_once_twice"] = r'''# LeetCode 3595 - Once Twice
# https://leetcode.com/problems/once-twice/

from typing import List


class Solution:
    def onceTwice(self, nums: List[int]) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        a = b = 0
        for key, v in freq.items():
            if v == 1:
                a = key
            elif v == 2:
                b = key
        return [a, b]
'''

FILES["3596_minimum_cost_path_with_alternating_directions_i"] = r'''# LeetCode 3596 - Minimum Cost Path with Alternating Directions I
# https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-i/


class Solution:
    def minCost(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        if m == 1 and n == 2:
            return 3
        if m == 2 and n == 1:
            return 3
        return -1
'''

FILES["3597_partition_string"] = r'''# LeetCode 3597 - Partition String
# https://leetcode.com/problems/partition-string/

from typing import List


class Solution:
    def partitionString(self, s: str) -> List[str]:
        vis = set()
        ans = []
        t = ""
        for c in s:
            t += c
            if t not in vis:
                vis.add(t)
                ans.append(t)
                t = ""
        return ans
'''

FILES["3598_longest_common_prefix_between_adjacent_strings_after_removals"] = r'''# LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
# https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

from typing import List


class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        tm = {}
        keys = []

        def calc(s: str, t: str) -> int:
            m = min(len(s), len(t))
            for k in range(m):
                if s[k] != t[k]:
                    return k
            return m

        def add_key(x: int) -> None:
            if x not in tm:
                tm[x] = 0
                lo, hi = 0, len(keys)
                while lo < hi:
                    mid = (lo + hi) >> 1
                    if keys[mid] < x:
                        lo = mid + 1
                    else:
                        hi = mid
                keys.insert(lo, x)
            tm[x] += 1

        def rem_key(x: int) -> None:
            c = tm[x] - 1
            if c == 0:
                del tm[x]
                ix = keys.index(x)
                if ix >= 0:
                    keys.pop(ix)
            else:
                tm[x] = c

        def add(i: int, j: int) -> None:
            if 0 <= i < n and 0 <= j < n:
                add_key(calc(words[i], words[j]))

        def remove(i: int, j: int) -> None:
            if 0 <= i < n and 0 <= j < n:
                rem_key(calc(words[i], words[j]))

        for i in range(n - 1):
            add(i, i + 1)
        ans = [0] * n
        for i in range(n):
            remove(i, i + 1)
            remove(i - 1, i)
            add(i - 1, i + 1)
            if keys and keys[-1] > 0:
                ans[i] = keys[-1]
            remove(i - 1, i + 1)
            add(i - 1, i)
            add(i, i + 1)
        return ans
'''

FILES["3599_partition_array_to_minimize_xor"] = r'''# LeetCode 3599 - Partition Array to Minimize XOR
# https://leetcode.com/problems/partition-array-to-minimize-xor/

from typing import List


class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        g = [0] * (n + 1)
        for i in range(1, n + 1):
            g[i] = g[i - 1] ^ nums[i - 1]
        Inf = 2147483647 // 2
        f = [[Inf] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                for h in range(j - 1, i):
                    f[i][j] = min(f[i][j], max(f[h][j - 1], g[i] ^ g[h]))
        return f[n][k]
'''

FILES["3600_maximize_spanning_tree_stability_with_upgrades"] = r'''# LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

from typing import List


class UnionFind3600:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))
        self.size = [1] * n
        self.cnt = n

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
        self.cnt -= 1
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        def check(lim: int) -> bool:
            uf = UnionFind3600(n)
            for e in edges:
                if e[2] >= lim:
                    uf.unite(e[0], e[1])
            rem = k
            for e in edges:
                if e[2] * 2 >= lim and rem > 0:
                    if uf.unite(e[0], e[1]):
                        rem -= 1
            return uf.cnt == 1

        uf = UnionFind3600(n)
        mn = 1000000
        for e in edges:
            if e[3] == 1:
                mn = min(mn, e[2])
                if not uf.unite(e[0], e[1]):
                    return -1
        for e in edges:
            uf.unite(e[0], e[1])
        if uf.cnt > 1:
            return -1
        l, r = 1, mn
        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l
'''

FILES["3602_hexadecimal_and_hexatrigesimal_conversion"] = r'''# LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
# https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/


def f3602(x: int, k: int) -> str:
    res = []
    while x > 0:
        v = x % k
        res.append(chr(48 + v) if v <= 9 else chr(65 + v - 10))
        x //= k
    return "".join(reversed(res))


class Solution:
    def concatHex36(self, n: int) -> str:
        return f3602(n * n, 16) + f3602(n * n * n, 36)
'''

FILES["3603_minimum_cost_path_with_alternating_directions_ii"] = r'''# LeetCode 3603 - Minimum Cost Path with Alternating Directions II
# https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

from typing import List


def entry3603(i: int, j: int) -> int:
    return (i + 1) * (j + 1)


class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        INF = 10**18
        dp = [[INF] * n for _ in range(m)]
        dp[0][0] = entry3603(0, 0)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i > 0:
                    cand = dp[i - 1][j] + entry3603(i, j)
                    if not (i - 1 == 0 and j == 0):
                        cand += waitCost[i - 1][j]
                    dp[i][j] = min(dp[i][j], cand)
                if j > 0:
                    cand = dp[i][j - 1] + entry3603(i, j)
                    if not (i == 0 and j - 1 == 0):
                        cand += waitCost[i][j - 1]
                    dp[i][j] = min(dp[i][j], cand)
        return dp[m - 1][n - 1]
'''

FILES["3604_minimum_time_to_reach_destination_in_directed_graph"] = r'''# LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
# https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2], e[3]))
        Inf = 10**18
        dist = [Inf] * n
        dist[0] = 0
        pq = [[0, 0]]

        def push(t: int, u: int) -> None:
            lo, hi = 0, len(pq)
            while lo < hi:
                mid = (lo + hi) >> 1
                if pq[mid][0] < t:
                    lo = mid + 1
                else:
                    hi = mid
            pq.insert(lo, [t, u])

        while pq:
            t, u = pq.pop(0)
            if t != dist[u]:
                continue
            if u == n - 1:
                return t
            for to, start, end in g[u]:
                nt = t
                if nt > end:
                    continue
                if nt < start:
                    nt = start
                nt += 1
                if nt < dist[to]:
                    dist[to] = nt
                    push(nt, to)
        return -1 if dist[n - 1] == Inf else dist[n - 1]
'''


def main() -> None:
    for folder, text in FILES.items():
        path = ROOT / folder / "solution.py"
        path.write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {folder}")
    print(f"done {len(FILES)}")


if __name__ == "__main__":
    main()
