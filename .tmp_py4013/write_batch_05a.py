#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}


def add(folder, body):
    SOLUTIONS[folder] = body if body.endswith("\n") else body + "\n"


add("2541_minimum_operations_to_make_array_equal_ii", r'''# LeetCode 2541 - Minimum Operations to Make Array Equal II
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            for i in range(len(nums1)):
                if nums1[i] != nums2[i]:
                    return -1
            return 0
        pos = 0
        neg = 0
        for i in range(len(nums1)):
            d = nums1[i] - nums2[i]
            if d % k != 0:
                return -1
            if d > 0:
                pos += d // k
            else:
                neg += (-d) // k
        return -1 if pos != neg else pos
''')

add("2542_maximum_subsequence_score", r'''# LeetCode 2542 - Maximum Subsequence Score
# https://leetcode.com/problems/maximum-subsequence-score/

import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        idx = list(range(n))
        idx.sort(key=lambda i: -nums2[i])
        pq = []
        s = 0
        ans = 0
        for i in idx:
            heapq.heappush(pq, nums1[i])
            s += nums1[i]
            if len(pq) > k:
                s -= heapq.heappop(pq)
            if len(pq) == k:
                cand = s * nums2[i]
                if cand > ans:
                    ans = cand
        return ans
''')

add("2543_check_if_point_is_reachable", r'''# LeetCode 2543 - Check if Point Is Reachable
# https://leetcode.com/problems/check-if-point-is-reachable/

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        g = gcd(targetX, targetY)
        while g % 2 == 0:
            g //= 2
        return g == 1
''')

add("2544_alternating_digit_sum", r'''# LeetCode 2544 - Alternating Digit Sum
# https://leetcode.com/problems/alternating-digit-sum/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = []
        x = n
        while x > 0:
            digits.append(x % 10)
            x //= 10
        ans = 0
        sign = 1
        for i in range(len(digits) - 1, -1, -1):
            ans += sign * digits[i]
            sign = -sign
        return ans
''')

add("2545_sort_the_students_by_their_kth_score", r'''# LeetCode 2545 - Sort the Students by Their Kth Score
# https://leetcode.com/problems/sort-the-students-by-their-kth-score/

from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda row: -row[k])
        return score
''')

add("2546_apply_bitwise_operations_to_make_strings_equal", r'''# LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        has1s = False
        has1t = False
        for i in range(len(s)):
            if s[i] == "1":
                has1s = True
            if target[i] == "1":
                has1t = True
        return has1s == has1t
''')

add("2547_minimum_cost_to_split_an_array", r'''# LeetCode 2547 - Minimum Cost to Split an Array
# https://leetcode.com/problems/minimum-cost-to-split-an-array/

from typing import List


class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            freq = {}
            trimmed = 0
            for j in range(i, n):
                c = freq.get(nums[j], 0) + 1
                freq[nums[j]] = c
                if c == 2:
                    trimmed += 2
                elif c > 2:
                    trimmed += 1
                cost = dp[i] + k + trimmed
                if cost < dp[j + 1]:
                    dp[j + 1] = cost
        return dp[n]
''')

add("2548_maximum_price_to_fill_a_bag", r'''# LeetCode 2548 - Maximum Price to Fill a Bag
# https://leetcode.com/problems/maximum-price-to-fill-a-bag/

from typing import List


class Solution:
    def maxPrice(self, items: List[List[int]], capacity: int) -> float:
        items.sort(key=lambda it: -(it[0] / it[1]))
        ans = 0.0
        remain = capacity
        for price, weight in items:
            if remain >= weight:
                ans += price
                remain -= weight
            else:
                ans += price * remain / weight
                remain = 0
                break
        if remain > 0:
            return -1
        return ans
''')

add("2549_count_distinct_numbers_on_board", r'''# LeetCode 2549 - Count Distinct Numbers on Board
# https://leetcode.com/problems/count-distinct-numbers-on-board/

class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n == 1:
            return 1
        return n - 1
''')

add("2550_count_collisions_of_monkeys_on_a_polygon", r'''# LeetCode 2550 - Count Collisions of Monkeys on a Polygon
# https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 1000000007

        def pow_mod(a: int, e: int) -> int:
            res = 1
            while e > 0:
                if e & 1:
                    res = res * a % MOD
                a = a * a % MOD
                e >>= 1
            return res

        return (pow_mod(2, n) - 2 + MOD) % MOD
''')

add("2551_put_marbles_in_bags", r'''# LeetCode 2551 - Put Marbles in Bags
# https://leetcode.com/problems/put-marbles-in-bags/

from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1 or k == n:
            return 0
        pair = [weights[i] + weights[i + 1] for i in range(n - 1)]
        pair.sort()
        mn = 0
        mx = 0
        for i in range(k - 1):
            mn += pair[i]
            mx += pair[n - 2 - i]
        return mx - mn
''')

add("2552_count_increasing_quadruplets", r'''# LeetCode 2552 - Count Increasing Quadruplets
# https://leetcode.com/problems/count-increasing-quadruplets/

from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        great = [0] * n
        for j in range(n):
            for i in range(j):
                if nums[i] < nums[j]:
                    ans += great[i]
                elif nums[i] > nums[j]:
                    great[i] += 1
        return ans
''')

add("2553_separate_the_digits_in_an_array", r'''# LeetCode 2553 - Separate the Digits in an Array
# https://leetcode.com/problems/separate-the-digits-in-an-array/

from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            digits = []
            while num > 0:
                digits.append(num % 10)
                num //= 10
            for i in range(len(digits) - 1, -1, -1):
                ans.append(digits[i])
        return ans
''')

add("2554_maximum_number_of_integers_to_choose_from_a_range_i", r'''# LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban = set(banned)
        ans = 0
        s = 0
        for i in range(1, n + 1):
            if i in ban:
                continue
            if s + i > maxSum:
                break
            s += i
            ans += 1
        return ans
''')

add("2555_maximize_win_from_two_segments", r'''# LeetCode 2555 - Maximize Win From Two Segments
# https://leetcode.com/problems/maximize-win-from-two-segments/

from typing import List


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        dp = [0] * (n + 1)
        ans = 0
        left = 0
        for right in range(n):
            while prizePositions[right] - prizePositions[left] > k:
                left += 1
            cur = right - left + 1
            if dp[left] + cur > ans:
                ans = dp[left] + cur
            best = cur
            if dp[right] > best:
                best = dp[right]
            dp[right + 1] = best
        return ans
''')

add("2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip", r'''# LeetCode 2556 - Disconnect Path in a Binary Matrix by at Most One Flip
# https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

from typing import List


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> bool:
            if r == m - 1 and c == n - 1:
                return True
            if r >= m or c >= n or grid[r][c] == 0:
                return False
            if not (r == 0 and c == 0):
                grid[r][c] = 0
            return dfs(r + 1, c) or dfs(r, c + 1)

        if not dfs(0, 0):
            return True
        grid[0][0] = 1
        return not dfs(0, 0)
''')

add("2557_maximum_number_of_integers_to_choose_from_a_range_ii", r'''# LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        uniq = []
        for x in banned:
            if 1 <= x <= n and (not uniq or uniq[-1] != x):
                uniq.append(x)
        ans = 0
        remain = maxSum
        prev = 0

        def check(l: int, r: int) -> None:
            nonlocal ans, remain
            if l > r or remain <= 0:
                return
            lo, hi = l, r
            best = l - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                cnt = mid - l + 1
                s = (l + mid) * cnt // 2
                if s <= remain:
                    best = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            if best >= l:
                cnt = best - l + 1
                ans += cnt
                remain -= (l + best) * cnt // 2

        for b in uniq:
            check(prev + 1, b - 1)
            prev = b
        check(prev + 1, n)
        return ans
''')

add("2558_take_gifts_from_the_richest_pile", r'''# LeetCode 2558 - Take Gifts From the Richest Pile
# https://leetcode.com/problems/take-gifts-from-the-richest-pile/

import heapq
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = [-g for g in gifts]
        heapq.heapify(h)
        for _ in range(k):
            x = -heapq.heappop(h)
            heapq.heappush(h, -int(math.sqrt(x)))
        return -sum(h)
''')

add("2559_count_vowel_strings_in_ranges", r'''# LeetCode 2559 - Count Vowel Strings in Ranges
# https://leetcode.com/problems/count-vowel-strings-in-ranges/

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_v(c: str) -> bool:
            return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"

        n = len(words)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i]
            w = words[i]
            if len(w) > 0 and is_v(w[0]) and is_v(w[-1]):
                pref[i + 1] += 1
        ans = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            ans[i] = pref[r + 1] - pref[l]
        return ans
''')

add("2560_house_robber_iv", r'''# LeetCode 2560 - House Robber IV
# https://leetcode.com/problems/house-robber-iv/

from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        lo, hi = min(nums), max(nums)

        def ok(cap: int) -> bool:
            cnt = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= k

        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
''')

add("2561_rearranging_fruits", r'''# LeetCode 2561 - Rearranging Fruits
# https://leetcode.com/problems/rearranging-fruits/

from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = {}
        mn = float("inf")
        for x in basket1:
            freq[x] = freq.get(x, 0) + 1
            mn = min(mn, x)
        for x in basket2:
            freq[x] = freq.get(x, 0) - 1
            mn = min(mn, x)
        extra = []
        for k, v in freq.items():
            if v % 2 != 0:
                return -1
            for _ in range(abs(v) // 2):
                extra.append(k)
        extra.sort()
        ans = 0
        for i in range(len(extra) // 2):
            ans += min(extra[i], 2 * mn)
        return ans
''')

add("2562_find_the_array_concatenation_value", r'''# LeetCode 2562 - Find the Array Concatenation Value
# https://leetcode.com/problems/find-the-array-concatenation-value/

from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                ans += nums[l]
                break
            left, right = nums[l], nums[r]
            p = 1
            t = right
            while t > 0:
                p *= 10
                t //= 10
            ans += left * p + right
            l += 1
            r -= 1
        return ans
''')

add("2563_count_the_number_of_fair_pairs", r'''# LeetCode 2563 - Count the Number of Fair Pairs
# https://leetcode.com/problems/count-the-number-of-fair-pairs/

from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def count(x: int) -> int:
            ans = 0
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] <= x:
                    ans += r - l
                    l += 1
                else:
                    r -= 1
            return ans

        return count(upper) - count(lower - 1)
''')

add("2564_substring_xor_queries", r'''# LeetCode 2564 - Substring XOR Queries
# https://leetcode.com/problems/substring-xor-queries/

from typing import List


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        pos = {}
        n = len(s)
        for i in range(n):
            if s[i] == "0":
                if 0 not in pos:
                    pos[0] = [i, i]
                continue
            val = 0
            for j in range(i, min(n, i + 30)):
                val = val * 2 + (ord(s[j]) - 48)
                if val not in pos:
                    pos[val] = [i, j]
        ans = [None] * len(queries)
        for i, (a, b) in enumerate(queries):
            need = a ^ b
            ans[i] = pos[need][:] if need in pos else [-1, -1]
        return ans
''')

add("2565_subsequence_with_the_minimum_score", r'''# LeetCode 2565 - Subsequence With the Minimum Score
# https://leetcode.com/problems/subsequence-with-the-minimum-score/

class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        left = [-1] * m
        right = [-1] * m
        j = 0
        i = 0
        while i < n and j < m:
            if s[i] == t[j]:
                left[j] = i
                j += 1
            i += 1
        j = m - 1
        i = n - 1
        while i >= 0 and j >= 0:
            if s[i] == t[j]:
                right[j] = i
                j -= 1
            i -= 1
        if m > 0 and left[m - 1] != -1:
            return 0
        ans = m
        for i in range(m):
            if right[i] != -1:
                if i < ans:
                    ans = i
                break
        for i in range(m - 1, -1, -1):
            if left[i] != -1:
                if m - 1 - i < ans:
                    ans = m - 1 - i
                break
        j = 0
        for i in range(m):
            if left[i] == -1:
                break
            while j < m and (right[j] == -1 or right[j] <= left[i]):
                j += 1
            if j < m:
                rem = j - i - 1
                if rem < ans:
                    ans = rem
        return ans
''')

add("2566_maximum_difference_by_remapping_a_digit", r'''# LeetCode 2566 - Maximum Difference by Remapping a Digit
# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        def remap(frm: str, to: str) -> int:
            v = 0
            for c in s:
                d = to if c == frm else c
                v = v * 10 + (ord(d) - 48)
            return v

        max_v = num
        for c in s:
            if c != "9":
                max_v = remap(c, "9")
                break
        min_v = remap(s[0], "0")
        return max_v - min_v
''')

add("2567_minimum_score_by_changing_two_elements", r'''# LeetCode 2567 - Minimum Score by Changing Two Elements
# https://leetcode.com/problems/minimum-score-by-changing-two-elements/

from typing import List


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return min(nums[n - 1] - nums[2], nums[n - 3] - nums[0], nums[n - 2] - nums[1])
''')

add("2568_minimum_impossible_or", r'''# LeetCode 2568 - Minimum Impossible OR
# https://leetcode.com/problems/minimum-impossible-or/

from typing import List


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        s = set(nums)
        x = 1
        while x in s:
            x <<= 1
        return x
''')

add("2569_handling_sum_queries_after_update", r'''# LeetCode 2569 - Handling Sum Queries After Update
# https://leetcode.com/problems/handling-sum-queries-after-update/

from typing import List


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        ones = [0] * (4 * n)
        lazy = [False] * (4 * n)

        def build(idx: int, l: int, r: int) -> None:
            if l == r:
                ones[idx] = nums1[l]
                return
            m = (l + r) >> 1
            build(idx * 2, l, m)
            build(idx * 2 + 1, m + 1, r)
            ones[idx] = ones[idx * 2] + ones[idx * 2 + 1]

        def apply(idx: int, l: int, r: int) -> None:
            ones[idx] = (r - l + 1) - ones[idx]
            lazy[idx] = not lazy[idx]

        def push(idx: int, l: int, r: int) -> None:
            if lazy[idx] and l != r:
                m = (l + r) >> 1
                apply(idx * 2, l, m)
                apply(idx * 2 + 1, m + 1, r)
                lazy[idx] = False

        def update(idx: int, l: int, r: int, ql: int, qr: int) -> None:
            if ql <= l and r <= qr:
                apply(idx, l, r)
                return
            push(idx, l, r)
            m = (l + r) >> 1
            if ql <= m:
                update(idx * 2, l, m, ql, qr)
            if qr > m:
                update(idx * 2 + 1, m + 1, r, ql, qr)
            ones[idx] = ones[idx * 2] + ones[idx * 2 + 1]

        build(1, 0, n - 1)
        sum2 = sum(nums2)
        ans = []
        for q in queries:
            if q[0] == 1:
                update(1, 0, n - 1, q[1], q[2])
            elif q[0] == 2:
                sum2 += q[1] * ones[1]
            else:
                ans.append(sum2)
        return ans
''')

add("2570_merge_two_2d_arrays_by_summing_values", r'''# LeetCode 2570 - Merge Two 2D Arrays by Summing Values
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                ans.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                ans.append([nums1[i][0], nums1[i][1]])
                i += 1
            else:
                ans.append([nums2[j][0], nums2[j][1]])
                j += 1
        while i < len(nums1):
            ans.append([nums1[i][0], nums1[i][1]])
            i += 1
        while j < len(nums2):
            ans.append([nums2[j][0], nums2[j][1]])
            j += 1
        return ans
''')

add("2571_minimum_operations_to_reduce_an_integer_to_0", r'''# LeetCode 2571 - Minimum Operations to Reduce an Integer to 0
# https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/

class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        while n > 0:
            if (n & 3) == 3:
                n += 1
                ans += 1
            elif (n & 1) != 0:
                n -= 1
                ans += 1
            else:
                n >>= 1
        return ans
''')

add("2572_count_the_number_of_square_free_subsets", r'''# LeetCode 2572 - Count the Number of Square-Free Subsets
# https://leetcode.com/problems/count-the-number-of-square-free-subsets/

from typing import List


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 1000000007
        PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        def mask_of(x: int) -> int:
            mask = 0
            for i, p in enumerate(PRIMES):
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                    if cnt > 1:
                        return -1
                if cnt == 1:
                    mask |= 1 << i
            return mask

        dp = [0] * (1 << 10)
        dp[0] = 1
        for x, c in freq.items():
            if x == 1:
                continue
            m = mask_of(x)
            if m < 0:
                continue
            for state in range((1 << 10) - 1, -1, -1):
                if (state & m) == 0:
                    dp[state | m] = (dp[state | m] + dp[state] * c) % MOD
        ans = 0
        for v in dp:
            ans = (ans + v) % MOD
        ones = freq.get(1, 0)
        mul = 1
        for _ in range(ones):
            mul = mul * 2 % MOD
        ans = ans * mul % MOD
        ans = (ans - 1 + MOD) % MOD
        return ans
''')

add("2573_find_the_string_with_lcp", r'''# LeetCode 2573 - Find the String with LCP
# https://leetcode.com/problems/find-the-string-with-lcp/

from typing import List


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        s = [0] * n
        c = 97
        for i in range(n):
            if s[i] != 0:
                continue
            if c > 122:
                return ""
            s[i] = c
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    s[j] = c
            c += 1
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                v = 0
                if s[i] == s[j]:
                    v = 1
                    if i + 1 < n and j + 1 < n:
                        v += lcp[i + 1][j + 1]
                if lcp[i][j] != v:
                    return ""
        return "".join(chr(x) for x in s)
''')

add("2574_left_and_right_sum_differences", r'''# LeetCode 2574 - Left and Right Sum Differences
# https://leetcode.com/problems/left-and-right-sum-differences/

from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        ans = [0] * len(nums)
        left = 0
        for i, x in enumerate(nums):
            right = total - left - x
            ans[i] = abs(left - right)
            left += x
        return ans
''')

add("2575_find_the_divisibility_array_of_a_string", r'''# LeetCode 2575 - Find the Divisibility Array of a String
# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = [0] * len(word)
        cur = 0
        for i, ch in enumerate(word):
            cur = (cur * 10 + (ord(ch) - 48)) % m
            if cur == 0:
                ans[i] = 1
        return ans
''')

add("2576_find_the_maximum_number_of_marked_indices", r'''# LeetCode 2576 - Find the Maximum Number of Marked Indices
# https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        ans = 0
        for j in range((n + 1) // 2, n):
            if 2 * nums[i] <= nums[j]:
                ans += 2
                i += 1
        return ans
''')

add("2577_minimum_time_to_visit_a_cell_in_a_grid", r'''# LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

import heapq
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        m, n = len(grid), len(grid[0])
        dist = [[1 << 30] * n for _ in range(m)]
        h = [(0, 0, 0)]
        dist[0][0] = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while h:
            t, r, c = heapq.heappop(h)
            if r == m - 1 and c == n - 1:
                return t
            if t > dist[r][c]:
                continue
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                nt = t + 1
                if nt < grid[nr][nc]:
                    wait = grid[nr][nc] - nt
                    if wait % 2 == 1:
                        wait += 1
                    nt += wait
                if nt < dist[nr][nc]:
                    dist[nr][nc] = nt
                    heapq.heappush(h, (nt, nr, nc))
        return -1
''')

add("2578_split_with_minimum_sum", r'''# LeetCode 2578 - Split With Minimum Sum
# https://leetcode.com/problems/split-with-minimum-sum/

class Solution:
    def splitNum(self, num: int) -> int:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10
        digits.sort()
        a = b = 0
        for i, d in enumerate(digits):
            if i % 2 == 0:
                a = a * 10 + d
            else:
                b = b * 10 + d
        return a + b
''')

add("2579_count_total_number_of_colored_cells", r'''# LeetCode 2579 - Count Total Number of Colored Cells
# https://leetcode.com/problems/count-total-number-of-colored-cells/

class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * n * (n - 1)
''')

add("2580_count_ways_to_group_overlapping_ranges", r'''# LeetCode 2580 - Count Ways to Group Overlapping Ranges
# https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

from typing import List


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 1000000007
        ranges.sort(key=lambda r: r[0])
        groups = 0
        end = -1
        for r in ranges:
            if r[0] > end:
                groups += 1
                end = r[1]
            elif r[1] > end:
                end = r[1]
        ans = 1
        for _ in range(groups):
            ans = ans * 2 % MOD
        return ans
''')


def main():
    written = 0
    for folder, body in SOLUTIONS.items():
        path = ROOT / folder / "solution.py"
        path.write_text(body, encoding="utf-8")
        if body.startswith("\ufeff"):
            raise SystemExit(f"BOM in {folder}")
        written += 1
    print(f"wrote {written}")


if __name__ == "__main__":
    main()
