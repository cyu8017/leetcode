from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def write(folder: str, body: str) -> None:
    (ROOT / folder / "solution.py").write_text(body.lstrip("\n"), encoding="utf-8")


write(
    "3515_shortest_path_in_a_weighted_tree",
    '''
# LeetCode 3515 - Shortest Path in a Weighted Tree
# https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

from typing import List


class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n + 1)]
        weight = {}
        for e in edges:
            u, v, w = e[0], e[1], e[2]
            g[u].append((v, w))
            g[v].append((u, w))
            a, b = min(u, v), max(u, v)
            weight[(a << 32) | b] = w
        in_t = [0] * (n + 1)
        out_t = [0] * (n + 1)
        dist = [0] * (n + 1)
        parent = [0] * (n + 1)
        time = 0

        def dfs(u: int, p: int) -> None:
            nonlocal time
            in_t[u] = time
            time += 1
            for to, w in g[u]:
                if to == p:
                    continue
                parent[to] = u
                dist[to] = dist[u] + w
                dfs(to, u)
            out_t[u] = time - 1

        dfs(1, 0)
        bit = [0] * (n + 2)

        def add(i: int, v: int) -> None:
            while i <= n:
                bit[i] += v
                i += i & -i

        def rangeAdd(l: int, r: int, v: int) -> None:
            add(l + 1, v)
            add(r + 2, -v)

        def point(i: int) -> int:
            s = 0
            i += 1
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        for i in range(1, n + 1):
            rangeAdd(in_t[i], in_t[i], dist[i])
        ans = []
        for q in queries:
            if q[0] == 1:
                u, v, nw = q[1], q[2], q[3]
                a, b = min(u, v), max(u, v)
                key = (a << 32) | b
                ow = weight[key]
                delta = nw - ow
                weight[key] = nw
                child = u if parent[u] == v else v
                rangeAdd(in_t[child], out_t[child], delta)
            else:
                ans.append(point(in_t[q[1]]))
        return ans
''',
)

write(
    "3516_find_closest_person",
    '''
# LeetCode 3516 - Find Closest Person
# https://leetcode.com/problems/find-closest-person/


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a, b = abs(x - z), abs(y - z)
        if a == b:
            return 0
        return 1 if a < b else 2
''',
)

write(
    "3517_smallest_palindromic_rearrangement_i",
    '''
# LeetCode 3517 - Smallest Palindromic Rearrangement I
# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        t = ""
        ch = ""
        for i in range(26):
            c = chr(97 + i)
            v = cnt[i] // 2
            t += c * v
            cnt[i] -= v * 2
            if cnt[i] == 1:
                ch = c
        sb = t
        if ch:
            sb += ch
        for i in range(len(t) - 1, -1, -1):
            sb += t[i]
        return sb
''',
)

write(
    "3518_smallest_palindromic_rearrangement_ii",
    '''
# LeetCode 3518 - Smallest Palindromic Rearrangement II
# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

from typing import List

MAX = 1000001


def nCk(n: int, kk: int) -> int:
    if kk < 0 or kk > n:
        return 0
    res = 1
    if kk > n - kk:
        kk = n - kk
    for i in range(1, kk + 1):
        res = res * (n - i + 1) // i
        if res >= MAX:
            return MAX
    return res


def countArr(h: List[int]) -> int:
    total = 0
    for f in h:
        total += f
    res = 1
    for f in h:
        res *= nCk(total, f)
        if res >= MAX:
            return MAX
        total -= f
    return res


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        odd = 0
        for c in cnt:
            if c % 2 != 0:
                odd += 1
        if odd > 1:
            return ""
        half = [0] * 26
        mid = ""
        for i in range(26):
            half[i] = cnt[i] // 2
            if cnt[i] % 2 != 0:
                mid = chr(97 + i)
        if countArr(half) < k:
            return ""
        half_len = 0
        for f in half:
            half_len += f
        left = ""
        for _ in range(half_len):
            for i in range(26):
                if half[i] == 0:
                    continue
                half[i] -= 1
                arr = countArr(half)
                if arr >= k:
                    left += chr(97 + i)
                    break
                k -= arr
                half[i] += 1
        res = left
        if mid:
            res += mid
        for i in range(len(left) - 1, -1, -1):
            res += left[i]
        return res
''',
)

write(
    "3519_count_numbers_with_non_decreasing_digits",
    '''
# LeetCode 3519 - Count Numbers with Non-Decreasing Digits
# https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

from typing import List

MOD = 1000000007


def toDigits(s: str, b: int) -> List[int]:
    if s == "0":
        return [0]
    digs = []
    while not (len(s) == 1 and s[0] == "0"):
        rem = 0
        q = ""
        for c in s:
            cur = rem * 10 + (ord(c) - 48)
            d = cur // b
            rem = cur % b
            if len(q) > 0 or d != 0:
                q += str(d)
        digs.append(rem)
        s = "0" if len(q) == 0 else q
    digs.reverse()
    return digs


def dec(s: str) -> str:
    a = list(s)
    i = len(a) - 1
    while i >= 0 and a[i] == "0":
        a[i] = "9"
        i -= 1
    if i < 0:
        return "0"
    a[i] = str(ord(a[i]) - 49)
    t = "".join(a)
    p = 0
    while p + 1 < len(t) and t[p] == "0":
        p += 1
    return t[p:]


def countUpto(digs: List[int], b: int) -> int:
    m = len(digs)
    memo = {}

    def dfs(pos: int, last: int, tight: bool) -> int:
        if pos == m:
            return 1
        key = (pos, last, 1 if tight else 0)
        if key in memo:
            return memo[key]
        up = digs[pos] if tight else b - 1
        res = 0
        for d in range(last, up + 1):
            res = (res + dfs(pos + 1, d, tight and d == up)) % MOD
        memo[key] = res
        return res

    return dfs(0, 0, True)


class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        rd = toDigits(r, b)
        ld = toDigits(dec(l), b)
        return (countUpto(rd, b) - countUpto(ld, b) + MOD) % MOD
''',
)

write(
    "3520_minimum_threshold_for_inversion_pairs_count",
    '''
# LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
# https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

from typing import List


def upperBound(a: List[int], target: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def countInv(nums: List[int], k: int, threshold: int) -> bool:
    sorted_arr: List[int] = []
    inv = 0
    for num in nums:
        left = upperBound(sorted_arr, num)
        right = upperBound(sorted_arr, num + threshold)
        inv += right - left
        sorted_arr.insert(upperBound(sorted_arr, num), num)
    return inv >= k


class Solution:
    def minThreshold(self, nums: List[int], k: int) -> int:
        mx = 0
        for v in nums:
            if v > mx:
                mx = v
        l, r = 0, mx + 1
        while l < r:
            m = (l + r) >> 1
            if countInv(nums, k, m):
                r = m
            else:
                l = m + 1
        return -1 if l > mx else l
''',
)

write(
    "3522_calculate_score_after_performing_instructions",
    '''
# LeetCode 3522 - Calculate Score After Performing Instructions
# https://leetcode.com/problems/calculate-score-after-performing-instructions/

from typing import List


class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(values)
        vis = [False] * n
        ans = 0
        i = 0
        while 0 <= i < n and not vis[i]:
            vis[i] = True
            if instructions[i][0] == "a":
                ans += values[i]
                i += 1
            else:
                i += values[i]
        return ans
''',
)

write(
    "3523_make_array_non_decreasing",
    '''
# LeetCode 3523 - Make Array Non-decreasing
# https://leetcode.com/problems/make-array-non-decreasing/

from typing import List


class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        ans = 0
        mx = 0
        for x in nums:
            if mx <= x:
                ans += 1
                mx = x
        return ans
''',
)

write(
    "3524_find_x_value_of_array_i",
    '''
# LeetCode 3524 - Find X Value of Array I
# https://leetcode.com/problems/find-x-value-of-array-i/

from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        for num in nums:
            new_dp = [0] * k
            nm = num % k
            new_dp[nm] = 1
            for i in range(k):
                new_dp[(i * nm) % k] += dp[i]
            for i in range(k):
                ans[i] += new_dp[i]
            dp = new_dp
        return ans
''',
)

write(
    "3525_find_x_value_of_array_ii",
    '''
# LeetCode 3525 - Find X Value of Array II
# https://leetcode.com/problems/find-x-value-of-array-ii/

from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = [0] * len(queries)
        for qi, q in enumerate(queries):
            idx, val, start, x = q[0], q[1], q[2], q[3]
            nums[idx] = val
            prod, cnt = 1, 0
            for i in range(start, n):
                prod = prod * (nums[i] % k) % k
                if prod == x:
                    cnt += 1
            ans[qi] = cnt
        return ans
''',
)

print("wrote group g (10)")
