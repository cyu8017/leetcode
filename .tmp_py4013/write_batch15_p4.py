#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["3712_sum_of_elements_with_frequency_divisible_by_k"] = r'''# LeetCode 3712 - Sum of Elements With Frequency Divisible by K
# https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

from typing import List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        ans = 0
        for key, val in cnt.items():
            if val % k == 0:
                ans += key * val
        return ans
'''

FILES["3713_longest_balanced_substring_i"] = r'''# LeetCode 3713 - Longest Balanced Substring I
# https://leetcode.com/problems/longest-balanced-substring-i/


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            cnt = [0] * 26
            mx = 0
            v = 0
            for j in range(i, n):
                c = ord(s[j]) - 97
                cnt[c] += 1
                if cnt[c] == 1:
                    v += 1
                mx = max(mx, cnt[c])
                if mx * v == j - i + 1:
                    ans = max(ans, j - i + 1)
        return ans
'''

FILES["3714_longest_balanced_substring_ii"] = r'''# LeetCode 3714 - Longest Balanced Substring II
# https://leetcode.com/problems/longest-balanced-substring-ii/


class Solution:
    def longestBalanced(self, s: str) -> int:
        def calc1(st: str) -> int:
            res = 0
            n = len(st)
            i = 0
            while i < n:
                j = i + 1
                while j < n and st[j] == st[i]:
                    j += 1
                res = max(res, j - i)
                i = j
            return res

        def calc2(st: str, a: str, b: str) -> int:
            res = 0
            n = len(st)
            i = 0
            while i < n:
                while i < n and st[i] != a and st[i] != b:
                    i += 1
                pos = {0: i - 1}
                d = 0
                while i < n and (st[i] == a or st[i] == b):
                    if st[i] == a:
                        d += 1
                    else:
                        d -= 1
                    if d in pos:
                        res = max(res, i - pos[d])
                    else:
                        pos[d] = i
                    i += 1
            return res

        def calc3(st: str) -> int:
            pos = {"0,0": -1}
            cnt = [0, 0, 0]
            res = 0
            for i, ch in enumerate(st):
                cnt[ord(ch) - 97] += 1
                x = cnt[0] - cnt[1]
                y = cnt[1] - cnt[2]
                k = f"{x},{y}"
                if k in pos:
                    res = max(res, i - pos[k])
                else:
                    pos[k] = i
            return res

        x = calc1(s)
        y = max(calc2(s, "a", "b"), calc2(s, "b", "c"), calc2(s, "a", "c"))
        z = calc3(s)
        return max(x, y, z)
'''

FILES["3715_sum_of_perfect_square_ancestors"] = r'''# LeetCode 3715 - Sum of Perfect Square Ancestors
# https://leetcode.com/problems/sum-of-perfect-square-ancestors/

from typing import List


class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def kernel(x: int) -> int:
            res = 1
            p = 2
            while p * p <= x:
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                if cnt % 2 == 1:
                    res *= p
                p += 1
            if x > 1:
                res *= x
            return res

        ks = [kernel(nums[i]) for i in range(n)]
        freq = {}
        ans = 0

        def dfs(u: int, p: int) -> None:
            nonlocal ans
            ans += freq.get(ks[u], 0)
            freq[ks[u]] = freq.get(ks[u], 0) + 1
            for v in graph[u]:
                if v != p:
                    dfs(v, u)
            freq[ks[u]] = freq.get(ks[u], 0) - 1

        dfs(0, -1)
        return ans
'''

FILES["3717_minimum_operations_to_make_the_array_beautiful"] = r'''# LeetCode 3717 - Minimum Operations to Make the Array Beautiful
# https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

from typing import List
import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        f = {nums[0]: 0}
        for i in range(1, len(nums)):
            x = nums[i]
            g = {}
            for pre, s in f.items():
                cur = math.ceil(x / pre) * pre
                while cur <= 100:
                    val = s + (cur - x)
                    old = g.get(cur)
                    if old is None or old > val:
                        g[cur] = val
                    cur += pre
            f = g
        return min(f.values()) if f else 0
'''

FILES["3718_smallest_missing_multiple_of_k"] = r'''# LeetCode 3718 - Smallest Missing Multiple of K
# https://leetcode.com/problems/smallest-missing-multiple-of-k/

from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        i = 1
        while True:
            x = k * i
            if x not in s:
                return x
            i += 1
'''

FILES["3719_longest_balanced_subarray_i"] = r'''# LeetCode 3719 - Longest Balanced Subarray I
# https://leetcode.com/problems/longest-balanced-subarray-i/

from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            vis = set()
            cnt = [0, 0]
            for j in range(i, n):
                if nums[j] not in vis:
                    vis.add(nums[j])
                    cnt[nums[j] & 1] += 1
                if cnt[0] == cnt[1]:
                    ans = max(ans, j - i + 1)
        return ans
'''

FILES["3720_lexicographically_smallest_permutation_greater_than_target"] = r'''# LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
# https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        n = len(s)
        ans = [""] * n

        def dfs(pos: int, greater: bool) -> bool:
            if pos == n:
                return greater
            start = 0 if greater else (ord(target[pos]) - 97)
            for c in range(start, 26):
                if cnt[c] == 0:
                    continue
                cnt[c] -= 1
                ans[pos] = chr(97 + c)
                ng = greater or c > (ord(target[pos]) - 97)
                if dfs(pos + 1, ng):
                    return True
                cnt[c] += 1
            return False

        if dfs(0, False):
            return "".join(ans)
        return ""
'''

FILES["3721_longest_balanced_subarray_ii"] = r'''# LeetCode 3721 - Longest Balanced Subarray II
# https://leetcode.com/problems/longest-balanced-subarray-ii/

from typing import List


class Node:
    def __init__(self) -> None:
        self.l = 0
        self.r = 0
        self.mn = 0
        self.mx = 0
        self.lazy = 0


class SegmentTree:
    def __init__(self, n: int) -> None:
        self.tr = [Node() for _ in range(n << 2)]
        self.build(1, 0, n)

    def build(self, u: int, l: int, r: int) -> None:
        tr = self.tr
        tr[u].l = l
        tr[u].r = r
        tr[u].mn = 0
        tr[u].mx = 0
        tr[u].lazy = 0
        if l == r:
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)

    def apply(self, u: int, v: int) -> None:
        self.tr[u].mn += v
        self.tr[u].mx += v
        self.tr[u].lazy += v

    def pushup(self, u: int) -> None:
        tr = self.tr
        tr[u].mn = min(tr[u << 1].mn, tr[u << 1 | 1].mn)
        tr[u].mx = max(tr[u << 1].mx, tr[u << 1 | 1].mx)

    def pushdown(self, u: int) -> None:
        if self.tr[u].lazy != 0:
            v = self.tr[u].lazy
            self.apply(u << 1, v)
            self.apply(u << 1 | 1, v)
            self.tr[u].lazy = 0

    def modify(self, u: int, l: int, r: int, v: int) -> None:
        tr = self.tr
        if tr[u].l >= l and tr[u].r <= r:
            self.apply(u, v)
            return
        self.pushdown(u)
        mid = (tr[u].l + tr[u].r) >> 1
        if l <= mid:
            self.modify(u << 1, l, r, v)
        if r > mid:
            self.modify(u << 1 | 1, l, r, v)
        self.pushup(u)

    def query(self, u: int, target: int) -> int:
        tr = self.tr
        if tr[u].l == tr[u].r:
            return tr[u].l
        self.pushdown(u)
        left = u << 1
        right = u << 1 | 1
        if tr[left].mn <= target <= tr[left].mx:
            return self.query(left, target)
        return self.query(right, target)


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        st = SegmentTree(n)
        last = {}
        now = 0
        ans = 0
        for i in range(1, n + 1):
            x = nums[i - 1]
            det = 1 if (x & 1) != 0 else -1
            if x in last:
                st.modify(1, last[x], n, -det)
                now -= det
            last[x] = i
            st.modify(1, i, n, det)
            now += det
            pos = st.query(1, now)
            ans = max(ans, i - pos)
        return ans
'''

FILES["3722_lexicographically_smallest_string_after_reverse"] = r'''# LeetCode 3722 - Lexicographically Smallest String After Reverse
# https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/


class Solution:
    def lexSmallest(self, s: str) -> str:
        ans = s
        n = len(s)

        def reverse(a: list, l: int, r: int) -> None:
            i, j = l, r - 1
            while i < j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        for k in range(1, n + 1):
            a1 = list(s)
            reverse(a1, 0, k)
            t1 = "".join(a1)
            a2 = list(s)
            reverse(a2, n - k, n)
            t2 = "".join(a2)
            if t1 < ans:
                ans = t1
            if t2 < ans:
                ans = t2
        return ans
'''

FILES["3723_maximize_sum_of_squares_of_digits"] = r'''# LeetCode 3723 - Maximize Sum of Squares of Digits
# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/


class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num * 9 < sum:
            return ""
        k, rem = divmod(sum, 9)
        ans = "9" * k
        if rem > 0:
            ans += chr(48 + rem)
        while len(ans) < num:
            ans += "0"
        return ans
'''

FILES["3724_minimum_operations_to_transform_array"] = r'''# LeetCode 3724 - Minimum Operations to Transform Array
# https://leetcode.com/problems/minimum-operations-to-transform-array/

from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 1
        n = len(nums1)
        ok = False
        d = 1 << 30
        for i in range(n):
            x = max(nums1[i], nums2[i])
            y = min(nums1[i], nums2[i])
            ans += x - y
            d = min(d, min(abs(x - nums2[n]), abs(y - nums2[n])))
            if nums2[n] >= y and nums2[n] <= x:
                ok = True
        if not ok:
            ans += d
        return ans
'''

FILES["3725_count_ways_to_choose_coprime_integers_from_rows"] = r'''# LeetCode 3725 - Count Ways to Choose Coprime Integers from Rows
# https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

from typing import List
import math


class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 1000000007
        m = len(mat)
        dp = {}
        for v in mat[0]:
            dp[v] = dp.get(v, 0) + 1
        for i in range(1, m):
            ndp = {}
            for v in mat[i]:
                for key, val in dp.items():
                    ng = math.gcd(key, v)
                    ndp[ng] = (ndp.get(ng, 0) + val) % MOD
            dp = ndp
        return dp.get(1, 0)
'''

FILES["3726_remove_zeros_in_decimal_representation"] = r'''# LeetCode 3726 - Remove Zeros in Decimal Representation
# https://leetcode.com/problems/remove-zeros-in-decimal-representation/


class Solution:
    def removeZeros(self, n: int) -> int:
        ans = 0
        k = 1
        while n > 0:
            x = n % 10
            if x > 0:
                ans = k * x + ans
                k *= 10
            n //= 10
        return ans
'''

FILES["3727_maximum_alternating_sum_of_squares"] = r'''# LeetCode 3727 - Maximum Alternating Sum of Squares
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/

from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a = [x * x for x in nums]
        a.sort()
        m = len(a) // 2
        ans = 0
        for i in range(m):
            ans -= a[i]
        for i in range(m, len(a)):
            ans += a[i]
        return ans
'''

FILES["3728_stable_subarrays_with_equal_boundary_and_interior_sum"] = r'''# LeetCode 3728 - Stable Subarrays With Equal Boundary and Interior Sum
# https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

from typing import List


class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        s = [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = s[i - 1] + capacity[i - 1]
        cnt = {}
        ans = 0
        for r in range(2, n):
            l = r - 2
            key_l = (capacity[l], capacity[l] + s[l + 1])
            cnt[key_l] = cnt.get(key_l, 0) + 1
            key_r = (capacity[r], s[r])
            ans += cnt.get(key_r, 0)
        return ans
'''

FILES["3729_count_distinct_subarrays_divisible_by_k_in_sorted_array"] = r'''# LeetCode 3729 - Count Distinct Subarrays Divisible by K in Sorted Array
# https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

from typing import List


class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        s = 0
        cnt = {0: 1}
        for x in nums:
            s = (s + x) % k
            ans += cnt.get(s, 0)
            cnt[s] = cnt.get(s, 0) + 1
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            m = j - i
            for h in range(1, m + 1):
                if (nums[i] * h) % k == 0:
                    ans -= m - h
            i = j
        return ans
'''

FILES["3730_maximum_calories_burnt_from_jumps"] = r'''# LeetCode 3730 - Maximum Calories Burnt from Jumps
# https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

from typing import List


class Solution:
    def maxCaloriesBurnt(self, heights: List[int]) -> int:
        heights = sorted(heights)
        ans = 0
        pre = 0
        l, r = 0, len(heights) - 1
        while l < r:
            d1 = heights[r] - pre
            ans += d1 * d1
            d2 = heights[l] - heights[r]
            ans += d2 * d2
            pre = heights[l]
            l += 1
            r -= 1
        d = heights[r] - pre
        ans += d * d
        return ans
'''

FILES["3731_find_missing_elements"] = r'''# LeetCode 3731 - Find Missing Elements
# https://leetcode.com/problems/find-missing-elements/

from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn, mx = 100, 0
        s = set()
        for x in nums:
            mn = min(mn, x)
            mx = max(mx, x)
            s.add(x)
        ans = []
        for x in range(mn + 1, mx):
            if x not in s:
                ans.append(x)
        return ans
'''

FILES["3732_maximum_product_of_three_elements_after_one_replacement"] = r'''# LeetCode 3732 - Maximum Product of Three Elements After One Replacement
# https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = sorted(nums)
        n = len(a)
        A, B, C, D = a[0], a[1], a[n - 2], a[n - 1]
        x = 100000
        return max(A * B * x, C * D * x, -A * D * x)
'''

FILES["3733_minimum_time_to_complete_all_deliveries"] = r'''# LeetCode 3733 - Minimum Time to Complete All Deliveries
# https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

from typing import List


class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        def ok(T: int) -> bool:
            w0 = T - T // r[0]
            w1 = T - T // r[1]
            return w0 + w1 >= d[0] + d[1]

        lo, hi = 1, 10**18
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
'''

FILES["3734_lexicographically_smallest_palindromic_permutation_greater_than_target"] = r'''# LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
# https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        odd = 0
        mid = -1
        for i in range(26):
            if cnt[i] % 2 == 1:
                odd += 1
                mid = i
        if odd > 1:
            return ""
        half = [cnt[i] // 2 for i in range(26)]
        n = len(s)
        half_len = n // 2
        left = [""] * half_len

        def dfs(pos: int, greater: bool) -> bool:
            if pos == half_len:
                if mid >= 0:
                    if greater:
                        return True
                    return chr(97 + mid) > target[half_len]
                return greater
            start = 0 if greater else (ord(target[pos]) - 97)
            for c in range(start, 26):
                if half[c] == 0:
                    continue
                half[c] -= 1
                left[pos] = chr(97 + c)
                if dfs(pos + 1, greater or c > (ord(target[pos]) - 97)):
                    return True
                half[c] += 1
            return False

        if not dfs(0, False):
            return ""
        res = "".join(left)
        if mid >= 0:
            res += chr(97 + mid)
        for i in range(half_len - 1, -1, -1):
            res += left[i]
        if res <= target:
            return ""
        return res
'''

FILES["3735_lexicographically_smallest_string_after_reverse_ii"] = r'''# LeetCode 3735 - Lexicographically Smallest String After Reverse II
# https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/


class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        best = s

        def reverse(a: list, l: int, r: int) -> None:
            i, j = l, r - 1
            while i < j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        for i in range(1, n + 1):
            t = list(s)
            reverse(t, 0, i)
            ts = "".join(t)
            if ts < best:
                best = ts
        for i in range(n):
            t = list(s)
            reverse(t, i, n)
            ts = "".join(t)
            if ts < best:
                best = ts
        return best
'''

FILES["3736_minimum_moves_to_equal_array_elements_iii"] = r'''# LeetCode 3736 - Minimum Moves to Equal Array Elements III
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = 0
        s = 0
        for x in nums:
            mx = max(mx, x)
            s += x
        return mx * len(nums) - s
'''

FILES["3737_count_subarrays_with_majority_element_i"] = r'''# LeetCode 3737 - Count Subarrays With Majority Element I
# https://leetcode.com/problems/count-subarrays-with-majority-element-i/

from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] == target:
                    cnt += 1
                if cnt * 2 > j - i + 1:
                    ans += 1
        return ans
'''

FILES["3738_longest_non_decreasing_subarray_after_replacing_at_most_one_element"] = r'''# LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
# https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                right[i] = right[i + 1] + 1
        ans = max(left)
        for i in range(n):
            a = left[i - 1] if i > 0 else 0
            b = right[i + 1] if i + 1 < n else 0
            if i > 0 and i + 1 < n and nums[i - 1] > nums[i + 1]:
                ans = max(ans, a + 1, b + 1)
            else:
                ans = max(ans, a + b + 1)
        return ans
'''

FILES["3739_count_subarrays_with_majority_element_ii"] = r'''# LeetCode 3739 - Count Subarrays With Majority Element II
# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

from typing import List


class BIT:
    def __init__(self, n_: int) -> None:
        self.n = n_
        self.c = [0] * (n_ + 1)

    def update(self, x: int, delta: int) -> None:
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]
            x -= x & -x
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        tree = BIT(2 * n + 1)
        s = n + 1
        tree.update(s, 1)
        ans = 0
        for x in nums:
            if x == target:
                s += 1
            else:
                s -= 1
            ans += tree.query(s - 1)
            tree.update(s, 1)
        return ans
'''


def main():
    written = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.py"
        if not path.parent.exists():
            print("MISSING FOLDER", folder)
            continue
        path.write_text(content, encoding="utf-8", newline="\n")
        written += 1
    print("wrote", written)


if __name__ == "__main__":
    main()
