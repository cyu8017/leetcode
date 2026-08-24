#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3335_total_characters_in_string_after_transformations_i"] = r'''# LeetCode 3335 - Total Characters in String After Transformations I
# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 1000000007
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        for _ in range(t):
            ncnt = [0] * 26
            for i in range(25):
                ncnt[i + 1] = (ncnt[i + 1] + cnt[i]) % mod
            ncnt[0] = (ncnt[0] + cnt[25]) % mod
            ncnt[1] = (ncnt[1] + cnt[25]) % mod
            cnt = ncnt
        ans = 0
        for v in cnt:
            ans = (ans + v) % mod
        return ans
'''

FILES["3336_find_the_number_of_subsequences_with_equal_gcd"] = r'''# LeetCode 3336 - Find the Number of Subsequences With Equal GCD
# https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

from typing import List


def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    while b != 0:
        a, b = b, a % b
    return a


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 1000000007
        max_v = 0
        for x in nums:
            if x > max_v:
                max_v = x
        dp = [[0] * (max_v + 1) for _ in range(max_v + 1)]
        dp[0][0] = 1
        for x in nums:
            ndp = [[0] * (max_v + 1) for _ in range(max_v + 1)]
            for a in range(max_v + 1):
                for b in range(max_v + 1):
                    ndp[a][b] = dp[a][b]
            for a in range(max_v + 1):
                for b in range(max_v + 1):
                    if dp[a][b] == 0:
                        continue
                    na = x if a == 0 else gcd(a, x)
                    nb = x if b == 0 else gcd(b, x)
                    ndp[na][b] = (ndp[na][b] + dp[a][b]) % mod
                    ndp[a][nb] = (ndp[a][nb] + dp[a][b]) % mod
            dp = ndp
        ans = 0
        for g in range(1, max_v + 1):
            ans = (ans + dp[g][g]) % mod
        return ans
'''

FILES["3337_total_characters_in_string_after_transformations_ii"] = r'''# LeetCode 3337 - Total Characters in String After Transformations II
# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

from typing import List


def matMul(a: List[List[int]], b: List[List[int]], mod: int) -> List[List[int]]:
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if a[i][k] == 0:
                continue
            for j in range(n):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j] % mod) % mod
    return c


def matPow(a: List[List[int]], e: int, mod: int) -> List[List[int]]:
    n = len(a)
    r = [[0] * n for _ in range(n)]
    for i in range(n):
        r[i][i] = 1
    while e > 0:
        if e & 1:
            r = matMul(r, a, mod)
        a = matMul(a, a, mod)
        e >>= 1
    return r


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 1000000007
        mat = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(1, nums[i] + 1):
                mat[i][(i + j) % 26] = 1
        mat = matPow(mat, t, mod)
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        ans = 0
        for i in range(26):
            for j in range(26):
                ans = (ans + cnt[i] * mat[i][j] % mod) % mod
        return ans
'''

FILES["3339_find_the_number_of_k_even_arrays"] = r'''# LeetCode 3339 - Find the Number of K-Even Arrays
# https://leetcode.com/problems/find-the-number-of-k-even-arrays/


class Solution:
    def countOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 1000000007
        even = m // 2
        odd = m - even
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n + 1)]
        dp[1][0][0] = odd
        dp[1][0][1] = even
        for i in range(1, n):
            for j in range(k + 1):
                dp[i + 1][j][0] = (
                    dp[i + 1][j][0]
                    + ((dp[i][j][0] + dp[i][j][1]) % mod) * odd % mod
                ) % mod
                dp[i + 1][j][1] = (dp[i + 1][j][1] + dp[i][j][0] * even % mod) % mod
                if j < k:
                    dp[i + 1][j + 1][1] = (
                        dp[i + 1][j + 1][1] + dp[i][j][1] * even % mod
                    ) % mod
        return (dp[n][k][0] + dp[n][k][1]) % mod
'''

FILES["3340_check_balanced_string"] = r'''# LeetCode 3340 - Check Balanced String
# https://leetcode.com/problems/check-balanced-string/


class Solution:
    def isBalanced(self, num: str) -> bool:
        even = 0
        odd = 0
        for i, ch in enumerate(num):
            if i % 2 == 0:
                even += ord(ch) - 48
            else:
                odd += ord(ch) - 48
        return even == odd
'''

FILES["3341_find_minimum_time_to_reach_last_room_i"] = r'''# LeetCode 3341 - Find Minimum Time to Reach Last Room I
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        dist = [[1 << 30] * n for _ in range(m)]
        h = [[0, 0, 0]]
        dist[0][0] = 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while h:
            h.sort(key=lambda a: a[0])
            t, r, c = h.pop(0)
            if t != dist[r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return t
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                start = max(t, moveTime[nr][nc])
                nt = start + 1
                if nt < dist[nr][nc]:
                    dist[nr][nc] = nt
                    h.append([nt, nr, nc])
        return -1
'''

FILES["3342_find_minimum_time_to_reach_last_room_ii"] = r'''# LeetCode 3342 - Find Minimum Time to Reach Last Room II
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        INF = 1 << 30
        dist = [[[INF, INF] for _ in range(n)] for _ in range(m)]
        pq = [[0, 0, 0, 0]]
        dist[0][0][0] = 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while pq:
            pq.sort(key=lambda a: a[0])
            t, r, c, parity = pq.pop(0)
            if t != dist[r][c][parity]:
                continue
            if r == m - 1 and c == n - 1:
                return t
            cost = 2 if parity == 1 else 1
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                start = max(t, moveTime[nr][nc])
                nt = start + cost
                np = 1 - parity
                if nt < dist[nr][nc][np]:
                    dist[nr][nc][np] = nt
                    pq.append([nt, nr, nc, np])
        return -1
'''

FILES["3343_count_number_of_balanced_permutations"] = r'''# LeetCode 3343 - Count Number of Balanced Permutations
# https://leetcode.com/problems/count-number-of-balanced-permutations/


def modPow(a: int, e: int, mod: int) -> int:
    r = 1
    a %= mod
    while e > 0:
        if e & 1:
            r = r * a % mod
        a = a * a % mod
        e >>= 1
    return r


def key(a: int, b: int) -> int:
    return (a << 32) | (b & 0xFFFFFFFF)


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 1000000007
        cnt = [0] * 10
        ssum = 0
        for c in num:
            d = ord(c) - 48
            cnt[d] += 1
            ssum += d
        if ssum % 2 == 1:
            return 0
        n = len(num)
        half_n = n // 2
        half_s = ssum // 2
        fact = [0] * (n + 1)
        inv_f = [0] * (n + 1)
        fact[0] = 1
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % mod
        inv_f[n] = modPow(fact[n], mod - 2, mod)
        for i in range(n, 0, -1):
            inv_f[i - 1] = inv_f[i] * i % mod
        dp = {key(0, 0): 1}
        for d in range(10):
            ndp = {}
            for st, ways in dp.items():
                used = st >> 32
                s = st & 0xFFFFFFFF
                for take in range(cnt[d] + 1):
                    nu = used + take
                    ns = s + take * d
                    if nu > half_n or ns > half_s:
                        continue
                    w = ways * inv_f[take] % mod * inv_f[cnt[d] - take] % mod
                    nk = key(nu, ns)
                    ndp[nk] = (ndp.get(nk, 0) + w) % mod
            dp = ndp
        ans = dp.get(key(half_n, half_s), 0)
        ans = ans * fact[half_n] % mod * fact[n - half_n] % mod
        for d in range(10):
            ans = ans * fact[cnt[d]] % mod
        return ans
'''

FILES["3344_maximum_sized_array"] = r'''# LeetCode 3344 - Maximum Sized Array
# https://leetcode.com/problems/maximum-sized-array/


def ok(n: int, s: int) -> bool:
    total = 0
    for i in range(n):
        for j in range(n):
            ij = i | j
            total += ij * (n - 1) * n // 2
            if total > s:
                return False
    return total <= s


class Solution:
    def maxSizedArray(self, s: int) -> int:
        lo, hi = 1, 2000
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid, s):
                lo = mid
            else:
                hi = mid - 1
        return lo
'''

FILES["3345_smallest_divisible_digit_product_i"] = r'''# LeetCode 3345 - Smallest Divisible Digit Product I
# https://leetcode.com/problems/smallest-divisible-digit-product-i/


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        x = n
        while True:
            p = 1
            y = x
            while y > 0:
                p *= y % 10
                y //= 10
            if p % t == 0:
                return x
            x += 1
'''

FILES["3346_maximum_frequency_of_an_element_after_performing_operations_i"] = r'''# LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

from typing import List


def lowerBound(a: List[int], x: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upperBound(a: List[int], x: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        ans = 1
        for t, f in freq.items():
            lo = lowerBound(nums, t - k)
            hi = upperBound(nums, t + k)
            can = hi - lo
            use = min(can, f + numOperations)
            if use > ans:
                ans = use
        l = 0
        for r in range(n):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            window = min(r - l + 1, numOperations)
            if window > ans:
                ans = window
        return ans
'''

FILES["3347_maximum_frequency_of_an_element_after_performing_operations_ii"] = r'''# LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

from typing import List


def lowerBound(a: List[int], x: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upperBound(a: List[int], x: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        ans = 1
        candidates = []
        seen = set()
        for x in nums:
            for t in (x - k, x, x + k):
                if t not in seen:
                    seen.add(t)
                    candidates.append(t)
        for t in candidates:
            lo = lowerBound(nums, t - k)
            hi = upperBound(nums, t + k)
            can = hi - lo
            f = freq.get(t, 0)
            use = min(can, f + numOperations)
            if use > ans:
                ans = use
        return ans
'''

FILES["3348_smallest_divisible_digit_product_ii"] = r'''# LeetCode 3348 - Smallest Divisible Digit Product II
# https://leetcode.com/problems/smallest-divisible-digit-product-ii/

from typing import List


def dfs(res: List[str], i: int, tight: bool, sameLen: bool, num: str, t: int) -> bool:
    if i == len(res):
        prod = 1
        for c in res:
            prod *= ord(c) - 48
            if prod == 0:
                break
        return prod % t == 0 and prod > 0
    start = "1" if i == 0 else "0"
    if tight and sameLen and i < len(num):
        start = num[i]
    for cc in range(ord(start), 58):
        c = chr(cc)
        res[i] = c
        nt = tight and sameLen and i < len(num) and c == num[i]
        if dfs(res, i + 1, nt, sameLen, num, t):
            return True
    return False


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        tt = t
        for d in range(9, 1, -1):
            while tt % d == 0:
                tt //= d
        if tt > 1:
            return "-1"
        for extra in range(61):
            L = len(num) + extra
            res = [""] * L
            if dfs(res, 0, True, extra == 0, num, t):
                return "".join(res)
        return "-1"
'''

FILES["3349_adjacent_increasing_subarrays_detection_i"] = r'''# LeetCode 3349 - Adjacent Increasing Subarrays Detection I
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

from typing import List


def inc(nums: List[int], start: int, k: int) -> bool:
    for i in range(start, start + k - 1):
        if nums[i] >= nums[i + 1]:
            return False
    return True


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n - 2 * k + 1):
            if inc(nums, i, k) and inc(nums, i + k, k):
                return True
        return False
'''

FILES["3350_adjacent_increasing_subarrays_detection_ii"] = r'''# LeetCode 3350 - Adjacent Increasing Subarrays Detection II
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

from typing import List


def ok(up: List[int], n: int, k: int) -> bool:
    for i in range(n - 2 * k + 1):
        if up[i] >= k and up[i + k] >= k:
            return True
    return False


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        up = [0] * n
        up[n - 1] = 1
        for i in range(n - 2, -1, -1):
            up[i] = up[i + 1] + 1 if nums[i] < nums[i + 1] else 1
        lo, hi = 1, n // 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(up, n, mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
'''

FILES["3351_sum_of_good_subsequences"] = r'''# LeetCode 3351 - Sum of Good Subsequences
# https://leetcode.com/problems/sum-of-good-subsequences/

from typing import List


class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        mod = 1000000007
        cnt = {}
        ssum = {}
        ans = 0
        for x in nums:
            c = 1
            s = x
            if cnt.get(x - 1, 0) > 0:
                c = (c + cnt[x - 1]) % mod
                s = (s + ssum[x - 1] + cnt[x - 1] * x % mod) % mod
            if cnt.get(x + 1, 0) > 0:
                c = (c + cnt[x + 1]) % mod
                s = (s + ssum[x + 1] + cnt[x + 1] * x % mod) % mod
            cnt[x] = (cnt.get(x, 0) + c) % mod
            ssum[x] = (ssum.get(x, 0) + s) % mod
            ans = (ans + s) % mod
        return ans
'''

FILES["3352_count_k_reducible_numbers_less_than_n"] = r'''# LeetCode 3352 - Count K-Reducible Numbers Less Than N
# https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/


def bitsPop(x: int) -> int:
    c = 0
    while x > 0:
        c += x & 1
        x >>= 1
    return c


class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        mod = 1000000007
        red = [0] * 801
        red[1] = 0
        for i in range(2, 801):
            red[i] = 1 + red[bitsPop(i)]
        memo = {}

        def key(pos: int, tight: int, ones: int) -> int:
            return (pos << 32) | (tight << 16) | ones

        def dfs(pos: int, tight: bool, ones: int) -> int:
            if pos == len(s):
                if ones == 0:
                    return 0
                return 1 if red[ones] <= k - 1 else 0
            ky = key(pos, 1 if tight else 0, ones)
            if ky in memo:
                return memo[ky]
            up = (ord(s[pos]) - 48) if tight else 1
            ans = 0
            for d in range(up + 1):
                nt = tight and d == up
                ans = (ans + dfs(pos + 1, nt, ones + d)) % mod
            memo[ky] = ans
            return ans

        return dfs(0, True, 0)
'''

FILES["3353_minimum_total_operations"] = r'''# LeetCode 3353 - Minimum Total Operations
# https://leetcode.com/problems/minimum-total-operations/

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] != nums[i + 1]:
                ops += 1
        return ops
'''

FILES["3354_make_array_elements_equal_to_zero"] = r'''# LeetCode 3354 - Make Array Elements Equal to Zero
# https://leetcode.com/problems/make-array-elements-equal-to-zero/

from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] != 0:
                continue
            for direction in (-1, 1):
                a = nums[:]
                cur, d = i, direction
                while 0 <= cur < n:
                    if a[cur] == 0:
                        cur += d
                    else:
                        a[cur] -= 1
                        d = -d
                        cur += d
                if all(v == 0 for v in a):
                    ans += 1
        return ans
'''

FILES["3355_zero_array_transformation_i"] = r'''# LeetCode 3355 - Zero Array Transformation I
# https://leetcode.com/problems/zero-array-transformation-i/

from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for q in queries:
            diff[q[0]] += 1
            diff[q[1] + 1] -= 1
        cur = 0
        for i in range(n):
            cur += diff[i]
            if cur < nums[i]:
                return False
        return True
'''

FILES["3356_zero_array_transformation_ii"] = r'''# LeetCode 3356 - Zero Array Transformation II
# https://leetcode.com/problems/zero-array-transformation-ii/

from typing import List


def ok(k: int, nums: List[int], queries: List[List[int]], n: int) -> bool:
    diff = [0] * (n + 1)
    for i in range(k):
        q = queries[i]
        diff[q[0]] += q[2]
        diff[q[1] + 1] -= q[2]
    cur = 0
    for i in range(n):
        cur += diff[i]
        if cur < nums[i]:
            return False
    return True


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        if ok(0, nums, queries, n):
            return 0
        lo, hi = 1, len(queries) + 1
        while lo < hi:
            mid = (lo + hi) >> 1
            if mid <= len(queries) and ok(mid, nums, queries, n):
                hi = mid
            else:
                lo = mid + 1
        if lo > len(queries):
            return -1
        return lo
'''

FILES["3357_minimize_the_maximum_adjacent_element_difference"] = r'''# LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
# https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

from typing import List


def ok(d: int, nums: List[int], n: int) -> bool:
    prev = -1
    i = 0
    while i < n:
        if nums[i] != -1:
            if prev != -1 and abs(nums[i] - prev) > d:
                return False
            prev = nums[i]
            i += 1
            continue
        j = i
        while j < n and nums[j] == -1:
            j += 1
        left = prev
        right = nums[j] if j < n else -1
        gap = j - i
        if left == -1 and right == -1:
            return True
        if left == -1 or right == -1:
            prev = -1
            i = j
            continue
        if abs(left - right) > d * (gap + 1):
            return False
        prev = -1
        i = j
    return True


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, 1000000000
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid, nums, n):
                hi = mid
            else:
                lo = mid + 1
        return lo
'''

FILES["3359_find_sorted_submatrices_with_maximum_element_at_most_k"] = r'''# LeetCode 3359 - Find Sorted Submatrices With Maximum Element at Most K
# https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/

from typing import List


class Solution:
    def countSortedMatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for r1 in range(m):
            for r2 in range(r1, m):
                for c1 in range(n):
                    for c2 in range(c1, n):
                        good = True
                        i = r1
                        while i <= r2 and good:
                            for j in range(c1, c2 + 1):
                                if grid[i][j] > k:
                                    good = False
                                    break
                                if j > c1 and grid[i][j] < grid[i][j - 1]:
                                    good = False
                                    break
                                if i > r1 and grid[i][j] < grid[i - 1][j]:
                                    good = False
                                    break
                            i += 1
                        if good:
                            ans += 1
        return ans
'''

FILES["3360_stone_removal_game"] = r'''# LeetCode 3360 - Stone Removal Game
# https://leetcode.com/problems/stone-removal-game/


class Solution:
    def canAliceWin(self, n: int) -> bool:
        take = 10
        alice = True
        while n >= take and take > 0:
            n -= take
            take -= 1
            alice = not alice
        return not alice
'''

FILES["3361_shift_distance_between_two_strings"] = r'''# LeetCode 3361 - Shift Distance Between Two Strings
# https://leetcode.com/problems/shift-distance-between-two-strings/

from typing import List


class Solution:
    def shiftDistance(
        self, s: str, t: str, nextCost: List[int], previousCost: List[int]
    ) -> int:
        ans = 0
        for i in range(len(s)):
            a = ord(s[i]) - 97
            b = ord(t[i]) - 97
            if a == b:
                continue
            fwd = 0
            x = a
            while x != b:
                fwd += nextCost[x]
                x = (x + 1) % 26
            bwd = 0
            x = a
            while x != b:
                bwd += previousCost[x]
                x = (x + 25) % 26
            ans += fwd if fwd < bwd else bwd
        return ans
'''


def main() -> None:
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.py"
        path.write_text(content, encoding="utf-8", newline="\n")
        print("wrote", folder)
    print("part2", len(FILES))


if __name__ == "__main__":
    main()
