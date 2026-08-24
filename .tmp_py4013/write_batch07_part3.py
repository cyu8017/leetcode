#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2815_max_pair_sum_in_an_array"] = r'''# LeetCode 2815 - Max Pair Sum in an Array
# https://leetcode.com/problems/max-pair-sum-in-an-array/

from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        best = {}
        ans = -1
        for v in nums:
            x = v
            md = 0
            while x > 0:
                md = max(md, x % 10)
                x //= 10
            if md in best:
                ans = max(ans, best[md] + v)
                best[md] = max(best[md], v)
            else:
                best[md] = v
        return ans
'''

FILES["2816_double_a_number_represented_as_a_linked_list"] = r'''# LeetCode 2816 - Double a Number Represented as a Linked List
# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev

        head = rev(head)
        carry = 0
        cur = head
        prev = None
        while cur:
            val = cur.val * 2 + carry
            cur.val = val % 10
            carry = val // 10
            prev = cur
            cur = cur.next
        if carry > 0 and prev is not None:
            prev.next = ListNode(carry)
        return rev(head)
'''

FILES["2817_minimum_absolute_difference_between_elements_with_constraint"] = r'''# LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
# https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

from typing import List


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0:
            ans0 = 10**18
            for i in range(1, len(nums)):
                ans0 = min(ans0, abs(nums[i] - nums[i - 1]))
            return ans0
        ans = 10**18
        arr = []

        def insert(v: int) -> None:
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) >> 1
                if arr[mid] < v:
                    lo = mid + 1
                else:
                    hi = mid
            arr.insert(lo, v)

        def lower_bound(v: int) -> int:
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) >> 1
                if arr[mid] < v:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        for i in range(x, len(nums)):
            insert(nums[i - x])
            cur = nums[i]
            idx = lower_bound(cur)
            if idx < len(arr):
                ans = min(ans, arr[idx] - cur)
            if idx > 0:
                ans = min(ans, cur - arr[idx - 1])
        return ans
'''

FILES["2818_apply_operations_to_maximize_score"] = r'''# LeetCode 2818 - Apply Operations to Maximize Score
# https://leetcode.com/problems/apply-operations-to-maximize-score/

from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 1000000007
        n = len(nums)
        max_v = max(nums) if nums else 0
        spf = [0] * (max_v + 1)
        for i in range(2, max_v + 1):
            if spf[i] == 0:
                for j in range(i, max_v + 1, i):
                    if spf[j] == 0:
                        spf[j] = i

        def prime_score(x: int) -> int:
            seen = set()
            while x > 1:
                p = spf[x]
                seen.add(p)
                while x % p == 0:
                    x //= p
            return len(seen)

        score = [prime_score(v) for v in nums]
        left = [0] * n
        right = [0] * n
        st = []
        for i in range(n):
            while st and score[st[-1]] < score[i]:
                st.pop()
            left[i] = st[-1] if st else -1
            st.append(i)
        st.clear()
        for i in range(n - 1, -1, -1):
            while st and score[st[-1]] <= score[i]:
                st.pop()
            right[i] = st[-1] if st else n
            st.append(i)
        arr = [[nums[i], (i - left[i]) * (right[i] - i)] for i in range(n)]
        arr.sort(key=lambda p: -p[0])

        def mod_pow(a: int, b: int) -> int:
            res = 1
            base = a % MOD
            exp = b
            while exp > 0:
                if exp & 1:
                    res = res * base % MOD
                base = base * base % MOD
                exp >>= 1
            return res

        ans = 1
        remain = k
        for val, cnt in arr:
            if remain <= 0:
                break
            use = cnt if cnt < remain else remain
            ans = ans * mod_pow(val, use) % MOD
            remain -= use
        return ans
'''

FILES["2819_minimum_relative_loss_after_buying_chocolates"] = r'''# LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
# https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

from typing import List


class Solution:
    def minimumRelativeLosses(self, prices: List[int], queries: List[List[int]]) -> List[int]:
        prices = sorted(prices)
        n = len(prices)
        ans = [0] * len(queries)
        for qi, (kk, m) in enumerate(queries):
            losses = [0] * n
            for i in range(n):
                if prices[i] <= kk:
                    losses[i] = prices[i]
                else:
                    losses[i] = 2 * kk - prices[i]
            losses.sort()
            total = 0
            for i in range(m):
                total += losses[i]
            ans[qi] = total
        return ans
'''

FILES["2821_delay_the_resolution_of_each_promise"] = r'''# LeetCode 2821 - Delay the Resolution of Each Promise
# https://leetcode.com/problems/delay-the-resolution-of-each-promise/

import asyncio
from typing import Callable, List


class Solution:
    def delayAll(self, functions: List[Callable], ms: int) -> List[Callable]:
        def wrap(fn: Callable) -> Callable:
            async def delayed():
                try:
                    result = fn()
                    if hasattr(result, "__await__"):
                        result = await result
                    await asyncio.sleep(ms / 1000.0)
                    return result
                except Exception:
                    await asyncio.sleep(ms / 1000.0)
                    raise

            return delayed

        return [wrap(fn) for fn in functions]
'''

FILES["2822_inversion_of_object"] = r'''# LeetCode 2822 - Inversion of Object
# https://leetcode.com/problems/inversion-of-object/

from typing import Any, Dict


class Solution:
    def invertObject(self, obj: Any) -> Dict[Any, Any]:
        inverted = {}
        keys = obj.keys() if isinstance(obj, dict) else range(len(obj))
        for key in keys:
            val = obj[key]
            key_s = str(key)
            if val in inverted:
                if not isinstance(inverted[val], list):
                    inverted[val] = [inverted[val]]
                inverted[val].append(key_s)
            else:
                inverted[val] = key_s
        return inverted
'''

FILES["2823_deep_object_filter"] = r'''# LeetCode 2823 - Deep Object Filter
# https://leetcode.com/problems/deep-object-filter/

from typing import Any, Callable, Optional


class Solution:
    def deepFilter(self, obj: Any, fn: Callable) -> Optional[Any]:
        if not isinstance(obj, (dict, list)) or obj is None:
            return obj if fn(obj) else None
        if isinstance(obj, list):
            res = []
            for v in obj:
                f = self.deepFilter(v, fn)
                if f is not None:
                    res.append(f)
            return res if res else None
        res = {}
        for k in obj:
            f = self.deepFilter(obj[k], fn)
            if f is not None:
                res[k] = f
        return res if res else None
'''

FILES["2824_count_pairs_whose_sum_is_less_than_target"] = r'''# LeetCode 2824 - Count Pairs Whose Sum is Less than Target
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
'''

FILES["2825_make_string_a_subsequence_using_cyclic_increments"] = r'''# LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        i = 0
        while i < len(str1) and j < len(str2):
            a = ord(str1[i]) - 97
            b = ord(str2[j]) - 97
            if a == b or (a + 1) % 26 == b:
                j += 1
            i += 1
        return j == len(str2)
'''

FILES["2826_sorting_three_groups"] = r'''# LeetCode 2826 - Sorting Three Groups
# https://leetcode.com/problems/sorting-three-groups/

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        dp = [[INF] * 4 for _ in range(n + 1)]
        dp[0][1] = dp[0][2] = dp[0][3] = 0
        for i in range(1, n + 1):
            v = nums[i - 1]
            for g in range(1, 4):
                cost = 0 if v == g else 1
                for prev in range(1, g + 1):
                    dp[i][g] = min(dp[i][g], dp[i - 1][prev] + cost)
        return min(dp[n][1], dp[n][2], dp[n][3])
'''

FILES["2827_number_of_beautiful_integers_in_the_range"] = r'''# LeetCode 2827 - Number of Beautiful Integers in the Range
# https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count(n: int) -> int:
            if n < 0:
                return 0
            s = str(n)
            memo = [
                [[[[-1] * 2 for _ in range(2)] for _ in range(22)] for _ in range(45)]
                for _ in range(12)
            ]

            def dfs(pos: int, diff: int, mod: int, tight: int, started: int) -> int:
                if pos == len(s):
                    return 1 if started and diff == 0 and mod == 0 else 0
                if memo[pos][diff + 20][mod][tight][started] != -1:
                    return memo[pos][diff + 20][mod][tight][started]
                up = ord(s[pos]) - 48 if tight else 9
                ans = 0
                for digit in range(up + 1):
                    nt = 1 if tight and digit == up else 0
                    if not started:
                        if digit == 0:
                            ans += dfs(pos + 1, diff, mod, nt, 0)
                        else:
                            nd = diff + (1 if digit % 2 == 0 else -1)
                            ans += dfs(pos + 1, nd, digit % k, nt, 1)
                    else:
                        nd = diff + (1 if digit % 2 == 0 else -1)
                        ans += dfs(pos + 1, nd, (mod * 10 + digit) % k, nt, 1)
                memo[pos][diff + 20][mod][tight][started] = ans
                return ans

            return dfs(0, 0, 0, 1, 0)

        return count(high) - count(low - 1)
'''

FILES["2828_check_if_a_string_is_an_acronym_of_words"] = r'''# LeetCode 2828 - Check if a String Is an Acronym of Words
# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        for i, w in enumerate(words):
            if not w or w[0] != s[i]:
                return False
        return True
'''

FILES["2829_determine_the_minimum_sum_of_a_k_avoiding_array"] = r'''# LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
# https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/


class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        used = set()
        total = 0
        x = 1
        while len(used) < n:
            if (k - x) not in used:
                used.add(x)
                total += x
            x += 1
        return total
'''

FILES["2830_maximize_the_profit_as_the_salesman"] = r'''# LeetCode 2830 - Maximize the Profit as the Salesman
# https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

from typing import List


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        by_end = [[] for _ in range(n)]
        for o in offers:
            by_end[o[1]].append(o)
        dp = [0] * (n + 1)
        for end in range(n):
            dp[end + 1] = dp[end]
            for o in by_end[end]:
                dp[end + 1] = max(dp[end + 1], dp[o[0]] + o[2])
        return dp[n]
'''

FILES["2831_find_the_longest_equal_subarray"] = r'''# LeetCode 2831 - Find the Longest Equal Subarray
# https://leetcode.com/problems/find-the-longest-equal-subarray/

from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos = {}
        for i, v in enumerate(nums):
            pos.setdefault(v, []).append(i)
        ans = 0
        for p in pos.values():
            left = 0
            for right in range(len(p)):
                while p[right] - p[left] - (right - left) > k:
                    left += 1
                ans = max(ans, right - left + 1)
        return ans
'''

FILES["2832_maximal_range_that_each_element_is_maximum_in_it"] = r'''# LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
# https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        st = []
        for i in range(n):
            while st and nums[st[-1]] < nums[i]:
                st.pop()
            left[i] = st[-1] if st else -1
            st.append(i)
        st.clear()
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            right[i] = st[-1] if st else n
            st.append(i)
        return [right[i] - left[i] - 1 for i in range(n)]
'''

FILES["2833_furthest_point_from_origin"] = r'''# LeetCode 2833 - Furthest Point From Origin
# https://leetcode.com/problems/furthest-point-from-origin/


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = right = u = 0
        for c in moves:
            if c == "L":
                left += 1
            elif c == "R":
                right += 1
            else:
                u += 1
        return abs(left - right) + u
'''

FILES["2834_find_the_minimum_possible_sum_of_a_beautiful_array"] = r'''# LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
# https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/


class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        MOD = 1000000007
        m = target // 2
        if n <= m:
            return (n * (n + 1) // 2) % MOD
        total = m * (m + 1) // 2
        remain = n - m
        total += remain * target + remain * (remain - 1) // 2
        return total % MOD
'''

FILES["2835_minimum_operations_to_form_subsequence_with_target_sum"] = r'''# LeetCode 2835 - Minimum Operations to Form Subsequence With Target Sum
# https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        cnt = [0] * 32
        total = 0
        for v in nums:
            total += v
            b = 0
            while (1 << b) < v:
                b += 1
            cnt[b] += 1
        if total < target:
            return -1
        ans = 0
        for i in range(31):
            if target & (1 << i):
                if cnt[i] > 0:
                    cnt[i] -= 1
                else:
                    j = i + 1
                    while j < 32 and cnt[j] == 0:
                        j += 1
                    if j == 32:
                        return -1
                    while j > i:
                        cnt[j] -= 1
                        cnt[j - 1] += 2
                        ans += 1
                        j -= 1
                    cnt[i] -= 1
            cnt[i + 1] += cnt[i] // 2
        return ans
'''

FILES["2836_maximize_value_of_function_in_a_ball_passing_game"] = r'''# LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
# https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

from typing import List


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        LOG = 36
        up = [[0] * n for _ in range(LOG)]
        sm = [[0] * n for _ in range(LOG)]
        for i in range(n):
            up[0][i] = receiver[i]
            sm[0][i] = receiver[i]
        for j in range(1, LOG):
            for i in range(n):
                mid = up[j - 1][i]
                up[j][i] = up[j - 1][mid]
                sm[j][i] = sm[j - 1][i] + sm[j - 1][mid]
        ans = 0
        for i in range(n):
            cur = i
            total = i
            kk = k
            for j in range(LOG):
                if kk & (1 << j):
                    total += sm[j][cur]
                    cur = up[j][cur]
            if total > ans:
                ans = total
        return ans
'''

FILES["2838_maximum_coins_heroes_can_collect"] = r'''# LeetCode 2838 - Maximum Coins Heroes Can Collect
# https://leetcode.com/problems/maximum-coins-heroes-can-collect/

from typing import List


class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        n = len(monsters)
        idx = list(range(n))
        idx.sort(key=lambda i: monsters[i])
        pref = [0] * (n + 1)
        ms = [0] * n
        for i in range(n):
            ms[i] = monsters[idx[i]]
            pref[i + 1] = pref[i] + coins[idx[i]]

        def upper_bound(a: List[int], x: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) >> 1
                if a[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        return [pref[upper_bound(ms, h)] for h in heroes]
'''

FILES["2839_check_if_strings_can_be_made_equal_with_operations_i"] = r'''# LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        a = "".join(sorted([s1[0], s1[2]]))
        b = "".join(sorted([s2[0], s2[2]]))
        c = "".join(sorted([s1[1], s1[3]]))
        d = "".join(sorted([s2[1], s2[3]]))
        return a == b and c == d
'''

FILES["2840_check_if_strings_can_be_made_equal_with_operations_ii"] = r'''# LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1 = [0] * 26
        odd1 = [0] * 26
        even2 = [0] * 26
        odd2 = [0] * 26
        for i in range(len(s1)):
            if i % 2 == 0:
                even1[ord(s1[i]) - 97] += 1
                even2[ord(s2[i]) - 97] += 1
            else:
                odd1[ord(s1[i]) - 97] += 1
                odd2[ord(s2[i]) - 97] += 1
        return even1 == even2 and odd1 == odd2
'''

FILES["2841_maximum_sum_of_almost_unique_subarray"] = r'''# LeetCode 2841 - Maximum Sum of Almost Unique Subarray
# https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        freq = {}
        total = 0
        ans = 0
        for i, v in enumerate(nums):
            freq[v] = freq.get(v, 0) + 1
            total += v
            if i >= k:
                out = nums[i - k]
                total -= out
                c = freq.get(out, 0) - 1
                if c == 0:
                    del freq[out]
                else:
                    freq[out] = c
            if i >= k - 1 and len(freq) >= m:
                ans = max(ans, total)
        return ans
'''

FILES["2842_count_k_subsequences_of_a_string_with_maximum_beauty"] = r'''# LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
# https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD = 1000000007
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        vals = sorted((f for f in freq if f > 0), reverse=True)
        if len(vals) < k:
            return 0
        threshold = vals[k - 1]
        need = 0
        avail = 0
        prod = 1
        for v in vals:
            if v > threshold:
                prod = (prod * v) % MOD
                need += 1
            elif v == threshold:
                avail += 1
        remain = k - need

        def mod_pow(a: int, b: int) -> int:
            res = 1
            a %= MOD
            while b > 0:
                if b & 1:
                    res = (res * a) % MOD
                a = (a * a) % MOD
                b >>= 1
            return res

        def comb(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0
            num = 1
            den = 1
            for i in range(r):
                num = (num * (n - i)) % MOD
                den = (den * (i + 1)) % MOD
            return (num * mod_pow(den, MOD - 2)) % MOD

        prod = (prod * comb(avail, remain)) % MOD
        for _ in range(remain):
            prod = (prod * threshold) % MOD
        return prod
'''

FILES["2843_count_symmetric_integers"] = r'''# LeetCode 2843 - Count Symmetric Integers
# https://leetcode.com/problems/count-symmetric-integers/


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for x in range(low, high + 1):
            s = str(x)
            if len(s) % 2 != 0:
                continue
            mid = len(s) // 2
            a = b = 0
            for i in range(mid):
                a += ord(s[i]) - 48
                b += ord(s[mid + i]) - 48
            if a == b:
                ans += 1
        return ans
'''

FILES["2844_minimum_operations_to_make_a_special_number"] = r'''# LeetCode 2844 - Minimum Operations to Make a Special Number
# https://leetcode.com/problems/minimum-operations-to-make-a-special-number/


class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        ans = n
        if "0" in num:
            ans = min(ans, n - 1)
        for t in ("00", "25", "50", "75"):
            j = n - 1
            while j >= 0 and num[j] != t[1]:
                j -= 1
            if j < 0:
                continue
            i = j - 1
            while i >= 0 and num[i] != t[0]:
                i -= 1
            if i < 0:
                continue
            ans = min(ans, n - i - 2)
        return ans
'''

FILES["2845_count_of_interesting_subarrays"] = r'''# LeetCode 2845 - Count of Interesting Subarrays
# https://leetcode.com/problems/count-of-interesting-subarrays/

from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        freq = {0: 1}
        ans = 0
        pref = 0
        for v in nums:
            if v % modulo == k:
                pref += 1
            need = (pref - k) % modulo
            if need < 0:
                need += modulo
            ans += freq.get(need, 0)
            key = pref % modulo
            freq[key] = freq.get(key, 0) + 1
        return ans
'''

FILES["2846_minimum_edge_weight_equilibrium_queries_in_a_tree"] = r'''# LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
# https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

from typing import List


class Solution:
    def minOperationsQueries(
        self, n: int, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        LOG = 15
        g = [[] for _ in range(n)]
        for a, b, w in edges:
            g[a].append((b, w))
            g[b].append((a, w))
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        cnt = [[0] * 27 for _ in range(n)]

        def dfs(u: int, p: int) -> None:
            up[0][u] = p
            for v, w in g[u]:
                if v == p:
                    continue
                depth[v] = depth[u] + 1
                for i in range(27):
                    cnt[v][i] = cnt[u][i]
                cnt[v][w] += 1
                dfs(v, u)

        dfs(0, 0)
        for j in range(1, LOG):
            for i in range(n):
                up[j][i] = up[j - 1][up[j - 1][i]]

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for j in range(LOG):
                if diff & (1 << j):
                    a = up[j][a]
            if a == b:
                return a
            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]
            return up[0][a]

        out = []
        for a, b in queries:
            c = lca(a, b)
            total = depth[a] + depth[b] - 2 * depth[c]
            best = 0
            for w in range(1, 27):
                f = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w]
                if f > best:
                    best = f
            out.append(total - best)
        return out
'''

FILES["2847_smallest_number_with_given_digit_product"] = r'''# LeetCode 2847 - Smallest Number With Given Digit Product
# https://leetcode.com/problems/smallest-number-with-given-digit-product/


class Solution:
    def smallestNumber(self, n: int) -> str:
        if n == 0:
            return "0"
        if n == 1:
            return "1"
        digits = []
        for d in range(9, 1, -1):
            while n % d == 0:
                digits.append(str(d))
                n //= d
        if n > 1:
            return "-1"
        return "".join(reversed(digits))
'''

FILES["2848_points_that_intersect_with_cars"] = r'''# LeetCode 2848 - Points That Intersect With Cars
# https://leetcode.com/problems/points-that-intersect-with-cars/

from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        cov = [0] * 102
        for a, b in nums:
            for x in range(a, b + 1):
                cov[x] = 1
        return sum(cov)
'''

FILES["2849_determine_if_a_cell_is_reachable_at_a_given_time"] = r'''# LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
# https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        need = max(abs(sx - fx), abs(sy - fy))
        if need == 0:
            return t != 1
        return t >= need
'''

FILES["2850_minimum_moves_to_spread_stones_over_grid"] = r'''# LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
# https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        extras = []
        zeros = []
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    zeros.append([i, j])
                elif grid[i][j] > 1:
                    for _ in range(grid[i][j] - 1):
                        extras.append([i, j])
        if not zeros:
            return 0
        best = 1 << 30

        def dfs(i: int, cost: int) -> None:
            nonlocal best
            if cost >= best:
                return
            if i == len(zeros):
                best = cost
                return
            for j in range(len(extras)):
                if extras[j][0] < 0:
                    continue
                e = extras[j]
                extras[j] = [-1, e[1]]
                d = abs(e[0] - zeros[i][0]) + abs(e[1] - zeros[i][1])
                dfs(i + 1, cost + d)
                extras[j] = e

        dfs(0, 0)
        return best
'''

FILES["2851_string_transformation"] = r'''# LeetCode 2851 - String Transformation
# https://leetcode.com/problems/string-transformation/


class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        MOD = 1000000007
        n = len(s)
        ss = s + s
        if t not in ss[: 2 * n - 1]:
            return 0
        cnt = 0
        for i in range(n):
            if ss[i : i + n] == t:
                cnt += 1
        same = s == t

        def mod_pow(a: int, b: int) -> int:
            res = 1
            a %= MOD
            bb = b
            while bb > 0:
                if bb & 1:
                    res = (res * a) % MOD
                a = (a * a) % MOD
                bb >>= 1
            return res

        pk = mod_pow(n - 1, k)
        invn = mod_pow(n, MOD - 2)
        sign = MOD - 1 if k % 2 == 1 else 1
        ways_same = ((pk + (n - 1) * sign % MOD) % MOD * invn) % MOD
        ways_diff = ((pk - sign + MOD) % MOD * invn) % MOD
        if same:
            return ways_same
        return (ways_diff * cnt) % MOD
'''

FILES["2852_sum_of_remoteness_of_all_cells"] = r'''# LeetCode 2852 - Sum of Remoteness of All Cells
# https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

from typing import List


class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    total += grid[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1 or seen[i][j]:
                    continue
                q = [(i, j)]
                seen[i][j] = True
                sm = 0
                cnt = 0
                h = 0
                while h < len(q):
                    x, y = q[h]
                    h += 1
                    sm += grid[x][y]
                    cnt += 1
                    for dx, dy in dirs:
                        ni, nj = x + dx, y + dy
                        if 0 <= ni < m and 0 <= nj < n and not seen[ni][nj] and grid[ni][nj] != -1:
                            seen[ni][nj] = True
                            q.append((ni, nj))
                ans += (total - sm) * cnt
        return ans
'''

FILES["2855_minimum_right_shifts_to_sort_the_array"] = r'''# LeetCode 2855 - Minimum Right Shifts to Sort the Array
# https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        drops = 0
        idx = -1
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1
                idx = i
        if drops == 0:
            return 0
        if drops > 1:
            return -1
        return n - 1 - idx
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
