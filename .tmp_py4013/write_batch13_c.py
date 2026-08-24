from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def write(folder: str, body: str) -> None:
    (ROOT / folder / "solution.py").write_text(body.lstrip("\n"), encoding="utf-8")


write(
    "3450_maximum_students_on_a_single_bench",
    '''
# LeetCode 3450 - Maximum Students on a Single Bench
# https://leetcode.com/problems/maximum-students-on-a-single-bench/

from typing import List


class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        bench = {}
        for s in students:
            if s[1] not in bench:
                bench[s[1]] = set()
            bench[s[1]].add(s[0])
        ans = 0
        for st in bench.values():
            if len(st) > ans:
                ans = len(st)
        return ans
''',
)

write(
    "3452_sum_of_good_numbers",
    '''
# LeetCode 3452 - Sum of Good Numbers
# https://leetcode.com/problems/sum-of-good-numbers/

from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            x = nums[i]
            good = True
            if i - k >= 0 and x <= nums[i - k]:
                good = False
            if i + k < n and x <= nums[i + k]:
                good = False
            if good:
                ans += x
        return ans
''',
)

write(
    "3453_separate_squares_i",
    '''
# LeetCode 3453 - Separate Squares I
# https://leetcode.com/problems/separate-squares-i/

from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = 0
        for sq in squares:
            l = sq[2]
            total += l * l

        def area_below(y: float) -> float:
            below = 0.0
            for sq in squares:
                yi, l = sq[1], sq[2]
                top = yi + l
                if y <= yi:
                    continue
                if y >= top:
                    below += l * l
                else:
                    below += l * (y - yi)
            return below

        lo, hi = 0.0, 2e9
        for _ in range(60):
            mid = (lo + hi) / 2
            if area_below(mid) * 2 < total:
                lo = mid
            else:
                hi = mid
        return hi
''',
)

write(
    "3454_separate_squares_ii",
    '''
# LeetCode 3454 - Separate Squares II
# https://leetcode.com/problems/separate-squares-ii/

from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = 0
        for sq in squares:
            l = sq[2]
            total += l * l

        def area_below(y: float) -> float:
            below = 0.0
            for sq in squares:
                yi, l = sq[1], sq[2]
                top = yi + l
                if y <= yi:
                    continue
                elif y >= top:
                    below += l * l
                else:
                    below += l * (y - yi)
            return below

        lo, hi = 0.0, 2e9
        for _ in range(60):
            mid = (lo + hi) / 2
            if area_below(mid) * 2 < total:
                lo = mid
            else:
                hi = mid
        return hi
''',
)

write(
    "3455_shortest_matching_substring",
    '''
# LeetCode 3455 - Shortest Matching Substring
# https://leetcode.com/problems/shortest-matching-substring/

from typing import List


class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        parts: List[str] = []
        cur = ""
        for c in p:
            if c == "*":
                parts.append(cur)
                cur = ""
            else:
                cur += c
        parts.append(cur)
        while len(parts) < 3:
            parts.append("")
        a, b, c = parts[0], parts[1], parts[2]
        n = len(s)

        def find_all(sub: str) -> List[int]:
            res = []
            if len(sub) == 0:
                for i in range(n + 1):
                    res.append(i)
                return res
            for i in range(n - len(sub) + 1):
                if s.startswith(sub, i):
                    res.append(i)
            return res

        def sort_search(arr: List[int], x: int) -> int:
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) >> 1
                if arr[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        pos_a, pos_b, pos_c = find_all(a), find_all(b), find_all(c)
        ans = n + 1
        for ia in pos_a:
            end_a = ia + len(a)
            bi = sort_search(pos_b, end_a)
            while bi < len(pos_b):
                end_b = pos_b[bi] + len(b)
                ci = sort_search(pos_c, end_b)
                if ci < len(pos_c):
                    length = pos_c[ci] + len(c) - ia
                    if length < ans:
                        ans = length
                break
        return -1 if ans == n + 1 else ans
''',
)

write(
    "3456_find_special_substring_of_length_k",
    '''
# LeetCode 3456 - Find Special Substring of Length K
# https://leetcode.com/problems/find-special-substring-of-length-k/


class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        for i in range(n - k + 1):
            ok = True
            for j in range(i + 1, i + k):
                if s[j] != s[i]:
                    ok = False
                    break
            if not ok:
                continue
            if i > 0 and s[i - 1] == s[i]:
                continue
            if i + k < n and s[i + k] == s[i]:
                continue
            return True
        return False
''',
)

write(
    "3457_eat_pizzas",
    '''
# LeetCode 3457 - Eat Pizzas!
# https://leetcode.com/problems/eat-pizzas/

from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas = sorted(pizzas)
        n = len(pizzas)
        days = n // 4
        ans = 0
        odd_days = (days + 1) // 2
        even_days = days // 2
        idx = n - 1
        for _ in range(odd_days):
            ans += pizzas[idx]
            idx -= 1
        for _ in range(even_days):
            idx -= 1
            ans += pizzas[idx]
            idx -= 1
        return ans
''',
)

write(
    "3458_select_k_disjoint_special_substrings",
    '''
# LeetCode 3458 - Select K Disjoint Special Substrings
# https://leetcode.com/problems/select-k-disjoint-special-substrings/


class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            ci = ord(ch) - 97
            if first[ci] == n:
                first[ci] = i
            last[ci] = i
        segs = []
        for c in range(26):
            if last[c] == -1:
                continue
            l, r = first[c], last[c]
            i = l
            while i <= r:
                ci = ord(s[i]) - 97
                if first[ci] < l:
                    l = first[ci]
                    i = l - 1
                    i += 1
                    continue
                if last[ci] > r:
                    r = last[ci]
                i += 1
            if not (l == 0 and r == n - 1):
                segs.append((l, r))
        uniq = set()
        arr = []
        for sg in segs:
            key = (sg[0] << 32) | (sg[1] & 0xFFFFFFFF)
            if key not in uniq:
                uniq.add(key)
                arr.append(sg)
        arr.sort(key=lambda x: x[1])
        cnt, end = 0, -1
        for sg in arr:
            if sg[0] > end:
                cnt += 1
                end = sg[1]
        return cnt >= k
''',
)

write(
    "3459_length_of_longest_v_shaped_diagonal_segment",
    '''
# LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        next_dir = [1, 2, 3, 0]
        memo = {}

        def key(i: int, j: int, d: int, turned: int, expect: int) -> int:
            return ((((i * 101 + j) * 5 + d) * 3 + turned) * 5 + expect)

        def dfs(i: int, j: int, d: int, turned: int, expect: int) -> int:
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != expect:
                return 0
            k = key(i, j, d, turned, expect)
            if k in memo:
                return memo[k]
            ni, nj = i + dirs[d][0], j + dirs[d][1]
            nx = 0 if expect == 2 else 2
            best = 1 + dfs(ni, nj, d, turned, nx)
            if turned == 0:
                nd = next_dir[d]
                ti, tj = i + dirs[nd][0], j + dirs[nd][1]
                cand = 1 + dfs(ti, tj, nd, 1, nx)
                if cand > best:
                    best = cand
            memo[k] = best
            return best

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                for d in range(4):
                    ni, nj = i + dirs[d][0], j + dirs[d][1]
                    best = 1 + dfs(ni, nj, d, 0, 2)
                    if best > ans:
                        ans = best
                if ans < 1:
                    ans = 1
        return ans
''',
)

write(
    "3460_longest_common_prefix_after_at_most_one_removal",
    '''
# LeetCode 3460 - Longest Common Prefix After at Most One Removal
# https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/


class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        i = j = 0
        removed = False
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                continue
            if removed:
                break
            removed = True
            i += 1
        return j
''',
)

write(
    "3461_check_if_digits_are_equal_in_string_after_operations_i",
    '''
# LeetCode 3461 - Check If Digits Are Equal in String After Operations I
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        b = list(s)
        while len(b) > 2:
            nb = [""] * (len(b) - 1)
            for i in range(len(b) - 1):
                nb[i] = str((ord(b[i]) - 48 + ord(b[i + 1]) - 48) % 10)
            b = nb
        return b[0] == b[1]
''',
)

write(
    "3462_maximum_sum_with_at_most_k_elements",
    '''
# LeetCode 3462 - Maximum Sum With at Most K Elements
# https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        h: List[int] = []
        s = 0

        def push(v: int) -> None:
            h.append(v)
            h.sort()

        def poll() -> int:
            return h.pop(0)

        for i in range(len(grid)):
            r = sorted(grid[i])
            lim = limits[i]
            if lim > len(r):
                lim = len(r)
            for j in range(lim):
                val = r[len(r) - 1 - j]
                push(val)
                s += val
                if len(h) > k:
                    s -= poll()
        return s
''',
)

write(
    "3463_check_if_digits_are_equal_in_string_after_operations_ii",
    '''
# LeetCode 3463 - Check If Digits Are Equal in String After Operations II
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def mod_pow_p(a: int, e: int, p: int) -> int:
            r = 1
            while e > 0:
                if e % 2 == 1:
                    r = r * a % p
                a = a * a % p
                e //= 2
            return r

        def mod_inv_prime(a: int, p: int) -> int:
            return mod_pow_p(a, p - 2, p)

        def binom_mod(n: int, k: int, p: int) -> int:
            if k < 0 or k > n:
                return 0
            num, den = 1, 1
            for i in range(k):
                num = num * (n - i) % p
                den = den * (i + 1) % p
            return num * mod_inv_prime(den, p) % p

        def crt(a1: int, m1: int, a2: int, m2: int) -> int:
            for x in range(m1 * m2):
                if x % m1 == a1 and x % m2 == a2:
                    return x
            return 0

        def binom_mod10(n: int, k: int) -> int:
            return crt(binom_mod(n, k, 2), 2, binom_mod(n, k, 5), 5)

        def combine_digit(offset: int) -> int:
            n = len(s)
            total = 0
            for i in range(n - 1):
                total = (total + binom_mod10(n - 2, i) * (ord(s[i + offset]) - 48)) % 10
            return total

        return combine_digit(0) == combine_digit(1)
''',
)

write(
    "3464_maximize_the_distance_between_points_on_a_square",
    '''
# LeetCode 3464 - Maximize the Distance Between Points on a Square
# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

from typing import List


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def can_place(arr: List[int], perim: int, mid: int) -> bool:
            n = len(arr)
            for s in range(n):
                cnt = 1
                last = arr[s]
                idx = s
                while cnt < k:
                    target = last + mid
                    found = False
                    for step in range(1, n):
                        ni = (idx + step) % n
                        val = arr[ni]
                        add = perim if ni <= idx else 0
                        if val + add >= target:
                            last = val + add
                            idx = ni
                            cnt += 1
                            found = True
                            break
                    if not found:
                        break
                if cnt == k and last - arr[s] <= perim - mid:
                    return True
            return False

        arr = [0] * len(points)
        for i, (x, y) in enumerate(points):
            if y == 0:
                d = x
            elif x == side:
                d = side + y
            elif y == side:
                d = 2 * side + (side - x)
            else:
                d = 3 * side + (side - y)
            arr[i] = d
        arr.sort()
        perim = 4 * side
        lo, hi = 0, 2 * side
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_place(arr, perim, mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
''',
)

write(
    "3466_maximum_coin_collection",
    '''
# LeetCode 3466 - Maximum Coin Collection
# https://leetcode.com/problems/maximum-coin-collection/

from typing import List


class Solution:
    def maxCoins(self, lane1: List[int], lane2: List[int]) -> int:
        n = len(lane1)
        neg = -(10**18)
        dp = [[lane1[0], neg], [lane2[0], neg]]
        ans = max(dp[0][0], dp[1][0])
        for i in range(1, n):
            ndp = [[0, 0], [0, 0]]
            ndp[0][0] = max(dp[0][0], 0) + lane1[i]
            ndp[1][0] = max(dp[1][0], 0) + lane2[i]
            ndp[0][1] = max(dp[0][1], dp[1][0]) + lane1[i]
            ndp[1][1] = max(dp[1][1], dp[0][0]) + lane2[i]
            if lane1[i] > ndp[0][0]:
                ndp[0][0] = lane1[i]
            if lane2[i] > ndp[1][0]:
                ndp[1][0] = lane2[i]
            for a in range(2):
                for b in range(2):
                    dp[a][b] = ndp[a][b]
                    if dp[a][b] > ans:
                        ans = dp[a][b]
        return ans
''',
)

print("wrote group c (15)")
