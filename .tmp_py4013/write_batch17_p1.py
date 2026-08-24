#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["3845_maximum_subarray_xor_with_bounded_range"] = r'''# LeetCode 3845 - Maximum Subarray XOR with Bounded Range
# https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

from typing import List


class Solution:
    def maxSubarrayXor(self, nums: List[int], k: int) -> int:
        nodes = [{"next": [0, 0], "count": 0}]

        def add(x: int, delta: int) -> None:
            u = 0
            nodes[u]["count"] += delta
            for b in range(15, -1, -1):
                bit = (x >> b) & 1
                if nodes[u]["next"][bit] == 0:
                    nodes[u]["next"][bit] = len(nodes)
                    nodes.append({"next": [0, 0], "count": 0})
                u = nodes[u]["next"][bit]
                nodes[u]["count"] += delta

        def query(x: int) -> int:
            u = 0
            res = 0
            for b in range(15, -1, -1):
                bit = (x >> b) & 1
                want = bit ^ 1
                v = nodes[u]["next"][want]
                if v != 0 and nodes[v]["count"] > 0:
                    res |= 1 << b
                    u = v
                else:
                    u = nodes[u]["next"][bit]
            return res

        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] ^ nums[i]
        max_q: List[int] = []
        min_q: List[int] = []
        left = 0
        trie_left = 0
        ans = 0
        for r in range(n):
            x = nums[r]
            while max_q and nums[max_q[-1]] <= x:
                max_q.pop()
            max_q.append(r)
            while min_q and nums[min_q[-1]] >= x:
                min_q.pop()
            min_q.append(r)
            while nums[max_q[0]] - nums[min_q[0]] > k:
                if max_q[0] == left:
                    max_q.pop(0)
                if min_q[0] == left:
                    min_q.pop(0)
                left += 1
            add(pref[r], 1)
            while trie_left < left:
                add(pref[trie_left], -1)
                trie_left += 1
            cur = query(pref[r + 1])
            if cur > ans:
                ans = cur
        return ans
'''

FILES["3846_total_distance_to_type_a_string_using_one_finger"] = r'''# LeetCode 3846 - Total Distance To Type A String Using One Finger
# https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

from typing import Dict, List, Tuple

_POS: Dict[str, Tuple[int, int]] = {}
_KEYS = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
for _i in range(3):
    for _j in range(len(_KEYS[_i])):
        _POS[_KEYS[_i][_j]] = (_i, _j)


class Solution:
    def totalDistance(self, s: str) -> int:
        pre = "a"
        ans = 0
        for cur in s:
            p1 = _POS[pre]
            p2 = _POS[cur]
            ans += abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            pre = cur
        return ans
'''

FILES["3847_find_the_score_difference_in_a_game"] = r'''# LeetCode 3847 - Find The Score Difference In A Game
# https://leetcode.com/problems/find-the-score-difference-in-a-game/

from typing import List


class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        ans = 0
        k = 1
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                k = -k
            if i % 6 == 5:
                k = -k
            ans += k * nums[i]
        return ans
'''

FILES["3848_check_digitorial_permutation"] = r'''# LeetCode 3848 - Check Digitorial Permutation
# https://leetcode.com/problems/check-digitorial-permutation/


class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        f = [0] * 10
        f[0] = 1
        for i in range(1, 10):
            f[i] = f[i - 1] * i
        x = 0
        y = n
        while y > 0:
            x += f[y % 10]
            y //= 10
        a = "".join(sorted(str(x)))
        b = "".join(sorted(str(n)))
        return a == b
'''

FILES["3849_maximum_bitwise_xor_after_rearrangement"] = r'''# LeetCode 3849 - Maximum Bitwise XOR After Rearrangement
# https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

from typing import List


class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        cnt = [0, 0]
        for c in t:
            cnt[ord(c) - 48] += 1
        ans: List[str] = [""] * len(s)
        for i in range(len(s)):
            x = ord(s[i]) - 48
            if cnt[x ^ 1] > 0:
                cnt[x ^ 1] -= 1
                ans[i] = "1"
            else:
                cnt[x] -= 1
                ans[i] = "0"
        return "".join(ans)
'''

FILES["3850_count_sequences_to_k"] = r'''# LeetCode 3850 - Count Sequences To K
# https://leetcode.com/problems/count-sequences-to-k/

from typing import Dict, List


class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        f: Dict[str, int] = {}

        def dfs(i: int, p: int, q: int) -> int:
            if i == len(nums):
                return 1 if p == k and q == 1 else 0
            key = f"{i},{p},{q}"
            if key in f:
                return f[key]
            res = dfs(i + 1, p, q)
            x = nums[i]
            g1 = gcd(p * x, q)
            res += dfs(i + 1, (p * x) // g1, q // g1)
            g2 = gcd(p, q * x)
            res += dfs(i + 1, p // g2, (q * x) // g2)
            f[key] = res
            return res

        return dfs(0, 1, 1)
'''

FILES["3851_maximum_requests_without_violating_the_limit"] = r'''# LeetCode 3851 - Maximum Requests Without Violating The Limit
# https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

from typing import Dict, List


class Solution:
    def maxRequests(self, requests: List[List[int]], k: int, window: int) -> int:
        g: Dict[int, List[int]] = {}
        for r in requests:
            g.setdefault(r[0], []).append(r[1])
        ans = len(requests)
        for ts in g.values():
            ts.sort()
            kept: List[int] = []
            for t in ts:
                while kept and t - kept[0] > window:
                    kept.pop(0)
                if len(kept) < k:
                    kept.append(t)
                else:
                    ans -= 1
        return ans
'''

FILES["3852_smallest_pair_with_different_frequencies"] = r'''# LeetCode 3852 - Smallest Pair With Different Frequencies
# https://leetcode.com/problems/smallest-pair-with-different-frequencies/

from typing import Dict, List


class Solution:
    def minDistinctFreqPair(self, nums: List[int]) -> List[int]:
        cnt: Dict[int, int] = {}
        for v in nums:
            cnt[v] = cnt.get(v, 0) + 1
        x = nums[0]
        for v in nums:
            x = min(x, v)
        min_y = float("inf")
        for y in cnt:
            if y < min_y and cnt[x] != cnt[y]:
                min_y = y
        if min_y == float("inf"):
            return [-1, -1]
        return [x, int(min_y)]
'''

FILES["3853_merge_close_characters"] = r'''# LeetCode 3853 - Merge Close Characters
# https://leetcode.com/problems/merge-close-characters/

from typing import Dict


class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        last: Dict[str, int] = {}
        ans = ""
        for c in s:
            cur = len(ans)
            if c in last and cur - last[c] <= k:
                continue
            ans += c
            last[c] = cur
        return ans
'''

FILES["3854_minimum_operations_to_make_array_parity_alternating"] = r'''# LeetCode 3854 - Minimum Operations To Make Array Parity Alternating
# https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

from typing import List


class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        def f(k: int, mn: int, mx: int) -> List[int]:
            cnt = 0
            a = float("inf")
            b = float("-inf")
            for i in range(len(nums)):
                x = nums[i]
                if ((x - i) & 1) != k:
                    cnt += 1
                    if x == mn:
                        x += 1
                    elif x == mx:
                        x -= 1
                a = min(a, x)
                b = max(b, x)
            return [cnt, max(1, int(b - a))]

        if len(nums) == 1:
            return [0, 0]
        mn = nums[0]
        mx = nums[0]
        for x in nums:
            mn = min(mn, x)
            mx = max(mx, x)
        r0 = f(0, mn, mx)
        r1 = f(1, mn, mx)
        if r0[0] != r1[0]:
            return r0 if r0[0] < r1[0] else r1
        return r0 if r0[1] <= r1[1] else r1
'''

FILES["3855_sum_of_k_digit_numbers_in_a_range"] = r'''# LeetCode 3855 - Sum Of K Digit Numbers In A Range
# https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/


class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        def qpow(a: int, n: int, mod: int) -> int:
            a %= mod
            A = a
            N = n
            MOD = mod
            res = 1
            while N > 0:
                if N & 1:
                    res = res * A % MOD
                A = A * A % MOD
                N >>= 1
            return res

        MOD = 1000000007
        n = r - l + 1
        s = ((l + r) * n // 2) % MOD
        part1 = qpow(n % MOD, k - 1, MOD)
        part2 = (qpow(10, k, MOD) - 1 + MOD) % MOD
        inv9 = qpow(9, MOD - 2, MOD)
        ans = s
        ans = ans * part1 % MOD
        ans = ans * part2 % MOD
        ans = ans * inv9 % MOD
        return ans
'''

FILES["3856_trim_trailing_vowels"] = r'''# LeetCode 3856 - Trim Trailing Vowels
# https://leetcode.com/problems/trim-trailing-vowels/


class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        def is_vowel(c: str) -> bool:
            return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"

        i = len(s) - 1
        while i >= 0 and is_vowel(s[i]):
            i -= 1
        return s[: i + 1]
'''

FILES["3857_minimum_cost_to_split_into_ones"] = r'''# LeetCode 3857 - Minimum Cost To Split Into Ones
# https://leetcode.com/problems/minimum-cost-to-split-into-ones/


class Solution:
    def minCost(self, n: int) -> int:
        return n * (n - 1) // 2
'''

FILES["3858_minimum_bitwise_or_from_grid"] = r'''# LeetCode 3858 - Minimum Bitwise Or From Grid
# https://leetcode.com/problems/minimum-bitwise-or-from-grid/

from typing import List


class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        def bit_len(x: int) -> int:
            if x == 0:
                return 0
            n = 0
            while x > 0:
                n += 1
                x >>= 1
            return n

        mx = 0
        for row in grid:
            for x in row:
                mx = max(mx, x)
        m = bit_len(mx)
        ans = 0
        for i in range(m - 1, -1, -1):
            mask = ans | ((1 << i) - 1)
            for row in grid:
                found = False
                for x in row:
                    if (x | mask) == mask:
                        found = True
                        break
                if not found:
                    ans |= 1 << i
                    break
        return ans
'''

FILES["3859_count_subarrays_with_k_distinct_integers"] = r'''# LeetCode 3859 - Count Subarrays With K Distinct Integers
# https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

from typing import Dict, List


class Solution:
    def countSubarrays(self, nums: List[int], k: int, m: int) -> int:
        def f(lim: int) -> int:
            cnt: Dict[int, int] = {}
            ans = 0
            l = 0
            t = 0
            for x in nums:
                c = cnt.get(x, 0) + 1
                cnt[x] = c
                if c == m:
                    t += 1
                while len(cnt) >= lim and t >= k:
                    y = nums[l]
                    l += 1
                    cy = cnt[y] - 1
                    if cy == m - 1:
                        t -= 1
                    if cy == 0:
                        del cnt[y]
                    else:
                        cnt[y] = cy
                ans += l
            return ans

        return f(k) - f(k + 1)
'''

FILES["3860_unique_email_groups"] = r'''# LeetCode 3860 - Unique Email Groups
# https://leetcode.com/problems/unique-email-groups/

from typing import List, Set


class Solution:
    def uniqueEmailGroups(self, emails: List[str]) -> int:
        st: Set[str] = set()
        for email in emails:
            at = email.find("@")
            local = email[:at]
            domain = email[at + 1 :].lower()
            plus = local.find("+")
            if plus >= 0:
                local = local[:plus]
            cleaned = ""
            for c in local:
                if c != ".":
                    cleaned += c.lower()
            st.add(cleaned + domain)
        return len(st)
'''

FILES["3861_minimum_capacity_box"] = r'''# LeetCode 3861 - Minimum Capacity Box
# https://leetcode.com/problems/minimum-capacity-box/

from typing import List


class Solution:
    def minimumIndex(self, capacity: List[int], itemSize: int) -> int:
        ans = -1
        for i in range(len(capacity)):
            if capacity[i] >= itemSize and (ans == -1 or capacity[i] < capacity[ans]):
                ans = i
        return ans
'''

FILES["3862_find_the_smallest_balanced_index"] = r'''# LeetCode 3862 - Find The Smallest Balanced Index
# https://leetcode.com/problems/find-the-smallest-balanced-index/

from typing import List


class Solution:
    def smallestBalancedIndex(self, nums: List[int]) -> int:
        s = 0
        p = 1
        for x in nums:
            s += x
        for i in range(len(nums) - 1, -1, -1):
            s -= nums[i]
            if s == p:
                return i
            p *= nums[i]
            if p >= s:
                break
        return -1
'''

FILES["3863_minimum_operations_to_sort_a_string"] = r'''# LeetCode 3863 - Minimum Operations To Sort A String
# https://leetcode.com/problems/minimum-operations-to-sort-a-string/


class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        sorted_ok = True
        for i in range(1, n):
            if s[i] < s[i - 1]:
                sorted_ok = False
                break
        if sorted_ok:
            return 0
        if n == 2:
            return -1
        mn = s[0]
        mx = s[0]
        for c in s:
            if c < mn:
                mn = c
            if c > mx:
                mx = c
        if s[0] == mn or s[n - 1] == mx:
            return 1
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2
        return 3
'''

FILES["3864_minimum_cost_to_partition_a_binary_string"] = r'''# LeetCode 3864 - Minimum Cost To Partition A Binary String
# https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/


class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        n = len(s)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + (ord(s[i - 1]) - 48)

        def dfs(l: int, r: int) -> int:
            x = pre[r] - pre[l]
            res = (r - l) * x * encCost if x != 0 else flatCost
            if (r - l) % 2 == 0:
                m = (l + r) // 2
                res = min(res, dfs(l, m) + dfs(m, r))
            return res

        return dfs(0, n)
'''

FILES["3865_reverse_k_subarrays"] = r'''# LeetCode 3865 - Reverse K Subarrays
# https://leetcode.com/problems/reverse-k-subarrays/

from typing import List


class Solution:
    def reverseSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        m = n // k
        for i in range(0, n, m if m else n):
            lo = i
            hi = i + m - 1
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1
        return nums
'''

FILES["3866_first_unique_even_element"] = r'''# LeetCode 3866 - First Unique Even Element
# https://leetcode.com/problems/first-unique-even-element/

from typing import List


class Solution:
    def firstUniqueEven(self, nums: List[int]) -> int:
        cnt = [0] * 101
        for x in nums:
            cnt[x] += 1
        for x in nums:
            if x % 2 == 0 and cnt[x] == 1:
                return x
        return -1
'''

FILES["3867_sum_of_gcd_of_formed_pairs"] = r'''# LeetCode 3867 - Sum Of Gcd Of Formed Pairs
# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

from typing import List


class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        n = len(nums)
        prefix_gcd = [0] * n
        mx = 0
        for i in range(n):
            mx = max(mx, nums[i])
            prefix_gcd[i] = gcd(nums[i], mx)
        prefix_gcd.sort()
        ans = 0
        for i in range(n // 2):
            ans += gcd(prefix_gcd[i], prefix_gcd[n - i - 1])
        return ans
'''

FILES["3868_minimum_cost_to_equalize_arrays_using_swaps"] = r'''# LeetCode 3868 - Minimum Cost To Equalize Arrays Using Swaps
# https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

from typing import Dict, List


class Solution:
    def minCost(self, nums1: List[int], nums2: List[int]) -> int:
        cnt2: Dict[int, int] = {}
        for x in nums2:
            cnt2[x] = cnt2.get(x, 0) + 1
        cnt1: Dict[int, int] = {}
        for x in nums1:
            c = cnt2.get(x, 0)
            if c > 0:
                cnt2[x] = c - 1
            else:
                cnt1[x] = cnt1.get(x, 0) + 1
        ans = 0
        for v in cnt1.values():
            if v % 2 == 1:
                return -1
            ans += v // 2
        for v in cnt2.values():
            if v % 2 == 1:
                return -1
        return ans
'''

FILES["3869_count_fancy_numbers_in_a_range"] = r'''# LeetCode 3869 - Count Fancy Numbers In A Range
# https://leetcode.com/problems/count-fancy-numbers-in-a-range/

from typing import List


class Solution:
    def countFancy(self, l: int, r: int) -> int:
        def check(s: int) -> bool:
            if s < 100:
                return s % 11 != 0
            mid = (s // 10) % 10
            last = s % 10
            return mid > 1 and mid < last

        num = ""
        n = 0
        f: List = []

        def dfs(pos: int, s: int, prev: int, st: int, lim: bool) -> int:
            if pos >= n:
                if st != 3:
                    return 1
                return 1 if check(s) else 0
            if not lim and f[pos][s][prev][st] != -1:
                return f[pos][s][prev][st]
            up = ord(num[pos]) - 48 if lim else 9
            res = 0
            for i in range(up + 1):
                nxt_st = st
                if st == 0:
                    if prev == 0:
                        nxt_st = 0
                    elif i > prev:
                        nxt_st = 1
                    elif i < prev:
                        nxt_st = 2
                    else:
                        nxt_st = 3
                elif st == 1:
                    nxt_st = 1 if i > prev else 3
                elif st == 2:
                    nxt_st = 2 if i < prev else 3
                else:
                    nxt_st = 3
                res += dfs(pos + 1, s + i, i, nxt_st, lim and i == up)
            if not lim:
                f[pos][s][prev][st] = res
            return res

        def calc(x: int) -> int:
            nonlocal num, n, f
            if x < 0:
                return 0
            num = str(x)
            n = len(num)
            f = [
                [[[-1] * 4 for _ in range(10)] for _ in range(9 * n + 1)]
                for _ in range(n)
            ]
            return dfs(0, 0, 0, 0, True)

        return calc(r) - calc(l - 1)
'''

FILES["3870_count_commas_in_range"] = r'''# LeetCode 3870 - Count Commas In Range
# https://leetcode.com/problems/count-commas-in-range/


class Solution:
    def countCommas(self, n: int) -> int:
        return max(0, n - 999)
'''

FILES["3871_count_commas_in_range_ii"] = r'''# LeetCode 3871 - Count Commas In Range II
# https://leetcode.com/problems/count-commas-in-range-ii/


class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        x = 1000
        while x <= n:
            ans += n - x + 1
            x *= 1000
        return ans
'''

FILES["3872_longest_arithmetic_sequence_after_changing_at_most_one_element"] = r'''# LeetCode 3872 - Longest Arithmetic Sequence After Changing At Most One Element
# https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

from typing import List


class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        d = [0] * n
        for i in range(1, n):
            d[i] = nums[i] - nums[i - 1]
        f = [2] * n
        g = [2] * n
        f[0] = 1
        g[n - 1] = 1
        for i in range(2, n):
            if d[i] == d[i - 1]:
                f[i] = f[i - 1] + 1
        for i in range(n - 3, -1, -1):
            if d[i + 1] == d[i + 2]:
                g[i] = g[i + 1] + 1
        ans = 3
        for i in range(n):
            ans = max(ans, max(f[i], g[i]))
            if i > 0:
                ans = max(ans, f[i - 1] + 1)
            if i + 1 < n:
                ans = max(ans, g[i + 1] + 1)
            if i > 0 and i < n - 1:
                diff = nums[i + 1] - nums[i - 1]
                if diff % 2 == 0:
                    diff = diff // 2
                    k = 3
                    if i > 1 and diff == d[i - 1]:
                        k += f[i - 1] - 1
                    if i < n - 2 and diff == d[i + 2]:
                        k += g[i + 1] - 1
                    ans = max(ans, k)
        return ans
'''

FILES["3873_maximum_points_activated_with_one_addition"] = r'''# LeetCode 3873 - Maximum Points Activated With One Addition
# https://leetcode.com/problems/maximum-points-activated-with-one-addition/

from typing import Dict, List


class Solution:
    def maxActivated(self, points: List[List[int]]) -> int:
        p: Dict[int, int] = {}
        size: Dict[int, int] = {}

        def find(x: int) -> int:
            if x not in p:
                p[x] = x
                size[x] = 1
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def unite(a: int, b: int) -> bool:
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return False
            if size[pa] > size[pb]:
                p[pb] = pa
                size[pa] = size[pa] + size[pb]
            else:
                p[pa] = pb
                size[pb] = size[pb] + size[pa]
            return True

        m = 3000000000
        for pt in points:
            unite(pt[0], pt[1] + m)
        cnt: Dict[int, int] = {}
        for pt in points:
            r = find(pt[0])
            cnt[r] = cnt.get(r, 0) + 1
        mx1 = 0
        mx2 = 0
        for x in cnt.values():
            if mx1 < x:
                mx2 = mx1
                mx1 = x
            elif mx2 < x:
                mx2 = x
        return mx1 + mx2 + 1
'''

FILES["3874_valid_subarrays_with_exactly_one_peak"] = r'''# LeetCode 3874 - Valid Subarrays With Exactly One Peak
# https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

from typing import List


class Solution:
    def validSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        peaks: List[int] = []
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                peaks.append(i)
        ans = 0
        for j in range(len(peaks)):
            p = peaks[j]
            left_min = max(p - k, 0)
            if j > 0:
                left_min = max(left_min, peaks[j - 1] + 1)
            right_max = min(p + k, n - 1)
            if j < len(peaks) - 1:
                right_max = min(right_max, peaks[j + 1] - 1)
            ans += (p - left_min + 1) * (right_max - p + 1)
        return ans
'''

FILES["3875_construct_uniform_parity_array_i"] = r'''# LeetCode 3875 - Construct Uniform Parity Array I
# https://leetcode.com/problems/construct-uniform-parity-array-i/

from typing import List


class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        return True
'''

FILES["3876_construct_uniform_parity_array_ii"] = r'''# LeetCode 3876 - Construct Uniform Parity Array II
# https://leetcode.com/problems/construct-uniform-parity-array-ii/

from typing import List


class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        mn = float("inf")
        for x in nums1:
            if x % 2 == 1 and x < mn:
                mn = x
        for x in nums1:
            if x % 2 == 0 and mn != float("inf") and x < mn:
                return False
        return True
'''


def main() -> None:
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.py"
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"wrote {folder}")
    print(f"done {len(FILES)}")


if __name__ == "__main__":
    main()
