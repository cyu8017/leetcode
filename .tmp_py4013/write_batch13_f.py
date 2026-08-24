from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def write(folder: str, body: str) -> None:
    (ROOT / folder / "solution.py").write_text(body.lstrip("\n"), encoding="utf-8")


write(
    "3500_minimum_cost_to_divide_array_into_subarrays",
    '''
# LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
# https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

from typing import List


class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)
        pn = [0] * (n + 1)
        pc = [0] * (n + 1)
        for i in range(n):
            pn[i + 1] = pn[i] + nums[i]
            pc[i + 1] = pc[i] + cost[i]
        inf = 10**18
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i] = inf
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                cand = pn[j + 1] * (pc[j + 1] - pc[i]) + k * (pc[n] - pc[i]) + dp[j + 1]
                if cand < dp[i]:
                    dp[i] = cand
        return dp[0]
''',
)

write(
    "3501_maximize_active_section_with_trade_ii",
    '''
# LeetCode 3501 - Maximize Active Section with Trade II
# https://leetcode.com/problems/maximize-active-section-with-trade-ii/

from typing import List


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        ones = 0
        for c in s:
            if c == "1":
                ones += 1
        ans = [ones] * len(queries)
        return ans
''',
)

write(
    "3502_minimum_cost_to_reach_every_position",
    '''
# LeetCode 3502 - Minimum Cost to Reach Every Position
# https://leetcode.com/problems/minimum-cost-to-reach-every-position/

from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        ans = [0] * n
        mi = cost[0]
        for i in range(n):
            mi = min(mi, cost[i])
            ans[i] = mi
        return ans
''',
)

write(
    "3503_longest_palindrome_after_substring_concatenation_i",
    '''
# LeetCode 3503 - Longest Palindrome After Substring Concatenation I
# https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

from typing import List


class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def expand(st: str, g: List[int], l: int, r: int) -> None:
            while l >= 0 and r < len(st) and st[l] == st[r]:
                g[l] = max(g[l], r - l + 1)
                l -= 1
                r += 1

        def calc(st: str) -> List[int]:
            n = len(st)
            g = [0] * n
            for i in range(n):
                expand(st, g, i, i)
                expand(st, g, i, i + 1)
            return g

        m, n = len(s), len(t)
        t = t[::-1]
        g1, g2 = calc(s), calc(t)
        ans = 0
        for v in g1:
            ans = max(ans, v)
        for v in g2:
            ans = max(ans, v)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                    a = g1[i] if i < m else 0
                    b = g2[j] if j < n else 0
                    ans = max(ans, f[i][j] * 2 + a)
                    ans = max(ans, f[i][j] * 2 + b)
        return ans
''',
)

write(
    "3504_longest_palindrome_after_substring_concatenation_ii",
    '''
# LeetCode 3504 - Longest Palindrome After Substring Concatenation II
# https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/

from typing import List


def expand(s: str, g: List[int], l: int, r: int) -> None:
    while l >= 0 and r < len(s) and s[l] == s[r]:
        g[l] = max(g[l], r - l + 1)
        l -= 1
        r += 1


def calc(s: str) -> List[int]:
    n = len(s)
    g = [0] * n
    for i in range(n):
        expand(s, g, i, i)
        expand(s, g, i, i + 1)
    return g


class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        t = t[::-1]
        g1, g2 = calc(s), calc(t)
        ans = 0
        for v in g1:
            ans = max(ans, v)
        for v in g2:
            ans = max(ans, v)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                    a = g1[i] if i < m else 0
                    b = g2[j] if j < n else 0
                    ans = max(ans, f[i][j] * 2 + a)
                    ans = max(ans, f[i][j] * 2 + b)
        return ans
''',
)

write(
    "3505_minimum_operations_to_make_elements_within_k_subarrays_equal",
    '''
# LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        min_ops = [0] * (n - x + 1)
        for i in range(n - x + 1):
            w = sorted(nums[i : i + x])
            med = w[(x - 1) // 2]
            ops = 0
            for v in w:
                ops += abs(v - med)
            min_ops[i] = ops
        inf = 10**18
        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[n][0] = 0
        for i in range(n - 1, -1, -1):
            for j in range(k + 1):
                dp[i][j] = dp[i + 1][j]
                if j > 0 and i + x <= n and min_ops[i] + dp[i + x][j - 1] < dp[i][j]:
                    dp[i][j] = min_ops[i] + dp[i + x][j - 1]
        return dp[0][k]
''',
)

write(
    "3506_find_time_required_to_eliminate_bacterial_strains",
    '''
# LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
# https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

from typing import List


class Solution:
    def minEliminationTime(self, timeReq: List[int], splitTime: int) -> int:
        pq = sorted(timeReq)
        while len(pq) > 1:
            pq.pop(0)
            x = pq.pop(0)
            v = x + splitTime
            lo, hi = 0, len(pq)
            while lo < hi:
                mid = (lo + hi) >> 1
                if pq[mid] < v:
                    lo = mid + 1
                else:
                    hi = mid
            pq.insert(lo, v)
        return pq[0]
''',
)

write(
    "3507_minimum_pair_removal_to_sort_array_i",
    '''
# LeetCode 3507 - Minimum Pair Removal to Sort Array I
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

from typing import List


def isNonDecreasing(a: List[int]) -> bool:
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            return False
    return True


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        arr = nums[:]
        ans = 0
        while not isNonDecreasing(arr):
            k = 0
            s = arr[0] + arr[1]
            for i in range(1, len(arr) - 1):
                t = arr[i] + arr[i + 1]
                if s > t:
                    s = t
                    k = i
            arr[k] = s
            arr.pop(k + 1)
            ans += 1
        return ans
''',
)

write(
    "3508_implement_router",
    '''
# LeetCode 3508 - Implement Router
# https://leetcode.com/problems/implement-router/

from typing import List


def lowerBound(a: List[int], frm: int, target: int) -> int:
    lo, hi = frm, len(a)
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Router:
    def __init__(self, memoryLimit: int):
        self.lim = memoryLimit
        self.vis = set()
        self.q = []
        self.idx = {}
        self.d = {}

    def f(self, a: int, b: int, c: int) -> int:
        return (a << 46) | (b << 29) | c

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        x = self.f(source, destination, timestamp)
        if x in self.vis:
            return False
        self.vis.add(x)
        if len(self.q) >= self.lim:
            self.forwardPacket()
        self.q.append([source, destination, timestamp])
        if destination not in self.d:
            self.d[destination] = []
        self.d[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        packet = self.q.pop(0)
        s, dest, t = packet[0], packet[1], packet[2]
        self.vis.discard(self.f(s, dest, t))
        self.idx[dest] = self.idx.get(dest, 0) + 1
        return [s, dest, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ls = self.d.get(destination)
        if not ls:
            return 0
        k = self.idx.get(destination, 0)
        return lowerBound(ls, k, endTime + 1) - lowerBound(ls, k, startTime)
''',
)

write(
    "3509_maximum_product_of_subsequences_with_an_alternating_sum_equal_to_k",
    '''
# LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
# https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        MIN = -5000
        memo = {}
        sum_all = 0
        for v in nums:
            sum_all += v
        if abs(k) > sum_all:
            return -1

        def dp(i: int, product: int, state: int, kk: int) -> int:
            if i == len(nums):
                if kk == 0 and state != 0 and product <= limit:
                    return product
                return MIN
            key = (i, product, state, kk)
            if key in memo:
                return memo[key]
            res = dp(i + 1, product, state, kk)
            if state == 0:
                res = max(res, dp(i + 1, nums[i], 1, kk - nums[i]))
            if state == 1:
                np = product * nums[i]
                if np > limit + 1:
                    np = limit + 1
                res = max(res, dp(i + 1, np, 2, kk + nums[i]))
            if state == 2:
                np = product * nums[i]
                if np > limit + 1:
                    np = limit + 1
                res = max(res, dp(i + 1, np, 1, kk - nums[i]))
            memo[key] = res
            return res

        ans = dp(0, 1, 0, k)
        return -1 if ans == MIN else ans
''',
)

write(
    "3510_minimum_pair_removal_to_sort_array_ii",
    '''
# LeetCode 3510 - Minimum Pair Removal to Sort Array II
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

from typing import List, Optional, Set


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        inv = ans = 0
        sl: List[List[int]] = []
        idx: Set[int] = set(range(n))

        def key(sm: int, i: int) -> int:
            return sm * 1000000007 + i

        sl_map = {}

        def addSl(sm: int, i: int) -> None:
            sl_map[key(sm, i)] = [sm, i]
            lo, hi = 0, len(sl)
            while lo < hi:
                mid = (lo + hi) >> 1
                if sl[mid][0] < sm or (sl[mid][0] == sm and sl[mid][1] < i):
                    lo = mid + 1
                else:
                    hi = mid
            sl.insert(lo, [sm, i])

        def remSl(sm: int, i: int) -> None:
            k = key(sm, i)
            if k not in sl_map:
                return
            del sl_map[k]
            for t in range(len(sl)):
                if sl[t][0] == sm and sl[t][1] == i:
                    sl.pop(t)
                    break

        def ceiling(st: Set[int], x: int) -> Optional[int]:
            best = None
            for v in st:
                if v >= x and (best is None or v < best):
                    best = v
            return best

        def floor(st: Set[int], x: int) -> Optional[int]:
            best = None
            for v in st:
                if v <= x and (best is None or v > best):
                    best = v
            return best

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                inv += 1
            addSl(nums[i] + nums[i + 1], i)
        while inv > 0:
            ans += 1
            p = sl.pop(0)
            sl_map.pop(key(p[0], p[1]), None)
            s, i = p[0], p[1]
            j = ceiling(idx, i + 1)
            if nums[i] > nums[j]:
                inv -= 1
            h = floor(idx, i - 1)
            if h is not None:
                if nums[h] > nums[i]:
                    inv -= 1
                remSl(nums[h] + nums[i], h)
                if nums[h] > s:
                    inv += 1
                addSl(nums[h] + s, h)
            kk = ceiling(idx, j + 1)
            if kk is not None:
                if nums[j] > nums[kk]:
                    inv -= 1
                remSl(nums[j] + nums[kk], j)
                if s > nums[kk]:
                    inv += 1
                addSl(s + nums[kk], i)
            nums[i] = s
            idx.discard(j)
        return ans
''',
)

write(
    "3511_make_a_positive_array",
    '''
# LeetCode 3511 - Make a Positive Array
# https://leetcode.com/problems/make-a-positive-array/

from typing import List


class Solution:
    def makeArrayPositive(self, nums: List[int]) -> int:
        ans = 0
        l = -1
        pre_mx = 0
        s = 0
        for r in range(len(nums)):
            s += nums[r]
            if r - l > 2 and s <= pre_mx:
                ans += 1
                l = r
                pre_mx = 0
                s = 0
            elif r - l >= 2:
                pre_mx = max(pre_mx, s - nums[r] - nums[r - 1])
        return ans
''',
)

write(
    "3512_minimum_operations_to_make_array_sum_divisible_by_k",
    '''
# LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for x in nums:
            ans = (ans + x) % k
        return ans
''',
)

write(
    "3513_number_of_unique_xor_triplets_i",
    '''
# LeetCode 3513 - Number of Unique XOR Triplets I
# https://leetcode.com/problems/number-of-unique-xor-triplets-i/

from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        x = n
        length = 0
        while x != 0:
            length += 1
            x >>= 1
        return 1 << length
''',
)

write(
    "3514_number_of_unique_xor_triplets_ii",
    '''
# LeetCode 3514 - Number of Unique XOR Triplets II
# https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        mx = 0
        for v in nums:
            mx = max(mx, v)
        mx <<= 1
        st = [False] * mx
        for a in nums:
            for b in nums:
                st[a ^ b] = True
        s = [0] * mx
        for ab in range(mx):
            if st[ab]:
                for c in nums:
                    s[ab ^ c] = 1
        ans = 0
        for v in s:
            ans += v
        return ans
''',
)

print("wrote group f (15)")
