#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["3662_filter_characters_by_frequency"] = r'''# LeetCode 3662 - Filter Characters by Frequency
# https://leetcode.com/problems/filter-characters-by-frequency/


class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        return "".join(c for c in s if cnt[ord(c) - 97] < k)
'''

FILES["3663_find_the_least_frequent_digit"] = r'''# LeetCode 3663 - Find The Least Frequent Digit
# https://leetcode.com/problems/find-the-least-frequent-digit/


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        cnt = [0] * 10
        ans = 0
        f = 1 << 30
        while n > 0:
            cnt[n % 10] += 1
            n //= 10
        for x in range(10):
            if cnt[x] > 0 and cnt[x] < f:
                f = cnt[x]
                ans = x
        return ans
'''

FILES["3664_two_letter_card_game"] = r'''# LeetCode 3664 - Two-Letter Card Game
# https://leetcode.com/problems/two-letter-card-game/

from typing import List


class Solution:
    def score(self, cards: List[str], x: str) -> int:
        def pair_group(arr: List[int]) -> List[int]:
            total = 0
            mx = 0
            for i in range(26):
                total += arr[i]
                mx = max(mx, arr[i])
            pairs = total // 2
            if total - mx < pairs:
                pairs = total - mx
            return [pairs, total - 2 * pairs]

        xx = 0
        left = [0] * 26
        right = [0] * 26
        for c in cards:
            a, b = c[0], c[1]
            if a == x and b == x:
                xx += 1
            elif a == x:
                left[ord(b) - 97] += 1
            elif b == x:
                right[ord(a) - 97] += 1
        lp = pair_group(left)
        rp = pair_group(right)
        ans = lp[0] + rp[0]
        rem = lp[1] + rp[1]
        use = min(xx, rem)
        ans += use
        xx -= use
        ans += xx // 2
        return ans
'''

FILES["3665_twisted_mirror_path_count"] = r'''# LeetCode 3665 - Twisted Mirror Path Count
# https://leetcode.com/problems/twisted-mirror-path-count/

from typing import List, Optional, Tuple


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 1000000007
        m, n = len(grid), len(grid[0])

        def next_cell(i: int, j: int, di: int, dj: int) -> Optional[Tuple[int, int]]:
            ni, nj = i + di, j + dj
            while 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                if dj == 1:
                    di, dj = 1, 0
                else:
                    di, dj = 0, 1
                ni += di
                nj += dj
            if ni < 0 or nj < 0 or ni >= m or nj >= n:
                return None
            return (ni, nj)

        dp = [[0] * n for _ in range(m)]
        if grid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or dp[i][j] == 0:
                    continue
                a = next_cell(i, j, 0, 1)
                if a:
                    dp[a[0]][a[1]] = (dp[a[0]][a[1]] + dp[i][j]) % MOD
                b = next_cell(i, j, 1, 0)
                if b:
                    dp[b[0]][b[1]] = (dp[b[0]][b[1]] + dp[i][j]) % MOD
        return dp[m - 1][n - 1]
'''

FILES["3666_minimum_operations_to_equalize_binary_string"] = r'''# LeetCode 3666 - Minimum Operations to Equalize Binary String
# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        ts = [set(), set()]
        for i in range(n + 1):
            ts[i % 2].add(i)
        cnt0 = s.count("0")
        ts[cnt0 % 2].discard(cnt0)
        q = [cnt0]
        ans = 0
        while q:
            nq = []
            for cur in q:
                if cur == 0:
                    return ans
                l = cur + k - 2 * min(cur, k)
                r = cur + k - 2 * max(k - n + cur, 0)
                t = ts[l % 2]
                for it in sorted(t):
                    if it < l:
                        continue
                    if it > r:
                        break
                    nq.append(it)
                    t.discard(it)
            q = nq
            ans += 1
        return -1
'''

FILES["3667_sort_array_by_absolute_value"] = r'''# LeetCode 3667 - Sort Array By Absolute Value
# https://leetcode.com/problems/sort-array-by-absolute-value/

from typing import List


class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        nums.sort(key=abs)
        return nums
'''

FILES["3668_restore_finishing_order"] = r'''# LeetCode 3668 - Restore Finishing Order
# https://leetcode.com/problems/restore-finishing-order/

from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        n = len(order)
        d = [0] * (n + 1)
        for i, x in enumerate(order):
            d[x] = i
        friends.sort(key=lambda a: d[a])
        return friends
'''

FILES["3669_balanced_k_factor_decomposition"] = r'''# LeetCode 3669 - Balanced K-Factor Decomposition
# https://leetcode.com/problems/balanced-k-factor-decomposition/

from typing import List


class Solution:
    _g = None

    def minDifference(self, n: int, k: int) -> List[int]:
        MX = 100001
        if Solution._g is None:
            g = [[] for _ in range(MX)]
            for i in range(1, MX):
                for j in range(i, MX, i):
                    g[j].append(i)
            Solution._g = g
        g = Solution._g
        cur = float("inf")
        ans = []
        path = [0] * k

        def dfs(i: int, x: int, mi: int, mx: int) -> None:
            nonlocal cur, ans
            if i == 0:
                d = max(mx, x) - min(mi, x)
                if d < cur:
                    cur = d
                    path[i] = x
                    ans = path[:]
                return
            for y in g[x]:
                path[i] = y
                dfs(i - 1, x // y, min(mi, y), max(mx, y))

        dfs(k - 1, n, 10**18, 0)
        return ans
'''

FILES["3670_maximum_product_of_two_integers_with_no_common_bits"] = r'''# LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
# https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_v = max(nums) if nums else 0
        bits_n = 0
        x = max_v
        while x > 0:
            bits_n += 1
            x >>= 1
        if bits_n == 0:
            bits_n = 1
        size = 1 << bits_n
        best = [0] * size
        for v in nums:
            if v > best[v]:
                best[v] = v
        for mask in range(size):
            for b in range(bits_n):
                if mask & (1 << b):
                    sub = mask ^ (1 << b)
                    if best[sub] > best[mask]:
                        best[mask] = best[sub]
        ans = 0
        for v in nums:
            comp = (size - 1) ^ v
            if best[comp] > 0:
                p = v * best[comp]
                if p > ans:
                    ans = p
        return ans
'''

FILES["3671_sum_of_beautiful_subsequences"] = r'''# LeetCode 3671 - Sum of Beautiful Subsequences
# https://leetcode.com/problems/sum-of-beautiful-subsequences/

from typing import List


class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        MOD = 1000000007
        mx = max(nums)
        pos = [[] for _ in range(mx + 1)]
        for i, v in enumerate(nums):
            pos[v].append(i)
        cnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            seq = []
            for m in range(g, mx + 1, g):
                seq.extend(pos[m])
            if not seq:
                continue
            seq.sort()
            ways = 1
            for _ in range(len(seq)):
                ways = (ways * 2) % MOD
            cnt[g] = (ways - 1 + MOD) % MOD
        ans = 0
        for g in range(mx, 0, -1):
            for m in range(2 * g, mx + 1, g):
                cnt[g] = (cnt[g] - cnt[m] + MOD) % MOD
            ans = (ans + cnt[g] * g) % MOD
        return ans
'''

FILES["3672_sum_of_weighted_modes_in_subarrays"] = r'''# LeetCode 3672 - Sum of Weighted Modes in Subarrays
# https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

from typing import List
import heapq


class Solution:
    def modeWeight(self, nums: List[int], k: int) -> int:
        cnt = {}
        pq = []

        def push(freq: int, val: int) -> None:
            heapq.heappush(pq, (-freq, val))

        def get_mode() -> int:
            while True:
                freq, val = -pq[0][0], pq[0][1]
                if cnt.get(val, 0) == freq:
                    return freq * val
                heapq.heappop(pq)

        for i in range(k):
            x = nums[i]
            cnt[x] = cnt.get(x, 0) + 1
            push(cnt[x], x)
        ans = get_mode()
        for i in range(k, len(nums)):
            x, y = nums[i], nums[i - k]
            cnt[x] = cnt.get(x, 0) + 1
            cnt[y] = cnt.get(y, 0) - 1
            push(cnt[x], x)
            push(cnt[y], y)
            ans += get_mode()
        return ans
'''

FILES["3674_minimum_operations_to_equalize_array"] = r'''# LeetCode 3674 - Minimum Operations to Equalize Array
# https://leetcode.com/problems/minimum-operations-to-equalize-array/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        for x in nums:
            if x != nums[0]:
                return 1
        return 0
'''

FILES["3675_minimum_operations_to_transform_string"] = r'''# LeetCode 3675 - Minimum Operations to Transform String
# https://leetcode.com/problems/minimum-operations-to-transform-string/


class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        for c in s:
            if c != "a":
                ans = max(ans, 26 - (ord(c) - 97))
        return ans
'''

FILES["3676_count_bowl_subarrays"] = r'''# LeetCode 3676 - Count Bowl Subarrays
# https://leetcode.com/problems/count-bowl-subarrays/

from typing import List


class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        ngr = [-1] * n
        ngl = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                ngr[i] = stack[-1]
            stack.append(i)
        stack.clear()
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                ngl[i] = stack[-1]
            stack.append(i)
        for i in range(n):
            if ngr[i] != -1 and ngr[i] - i >= 2:
                ans += 1
            if ngl[i] != -1 and i - ngl[i] >= 2:
                ans += 1
        return ans
'''

FILES["3677_count_binary_palindromic_numbers"] = r'''# LeetCode 3677 - Count Binary Palindromic Numbers
# https://leetcode.com/problems/count-binary-palindromic-numbers/


class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 1
        s = ""
        x = n
        while x > 0:
            s += str(x & 1)
            x //= 2
        s = s[::-1]
        L = len(s)
        for length in range(1, L):
            half = (length + 1) // 2
            ans += 1 << (half - 1)
        half = (L + 1) // 2
        prefix = s[:half]
        start = 1 << (half - 1)
        pref_val = 0
        for c in prefix:
            pref_val = (pref_val << 1) | (ord(c) - 48)
        ans += pref_val - start
        pal = prefix
        for i in range(half - 1 - (L % 2), -1, -1):
            pal += prefix[i]
        pval = 0
        for c in pal:
            pval = (pval << 1) | (ord(c) - 48)
        if pval <= n:
            ans += 1
        return ans
'''

FILES["3678_smallest_absent_positive_greater_than_average"] = r'''# LeetCode 3678 - Smallest Absent Positive Greater Than Average
# https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        s = set()
        total = 0
        for x in nums:
            s.add(x)
            total += x
        ans = max(1, total // len(nums) + 1)
        while ans in s:
            ans += 1
        return ans
'''

FILES["3679_minimum_discards_to_balance_inventory"] = r'''# LeetCode 3679 - Minimum Discards to Balance Inventory
# https://leetcode.com/problems/minimum-discards-to-balance-inventory/

from typing import List


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = {}
        n = len(arrivals)
        marked = [0] * n
        ans = 0
        for i in range(n):
            x = arrivals[i]
            if i >= w:
                cnt[arrivals[i - w]] = cnt.get(arrivals[i - w], 0) - marked[i - w]
            if cnt.get(x, 0) >= m:
                ans += 1
            else:
                marked[i] = 1
                cnt[x] = cnt.get(x, 0) + 1
        return ans
'''

FILES["3680_generate_schedule"] = r'''# LeetCode 3680 - Generate Schedule
# https://leetcode.com/problems/generate-schedule/

from typing import List


class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n < 5:
            return []
        matches = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    matches.append([i, j])
        used = [False] * len(matches)
        sched = []
        last0, last1 = -1, -1

        def dfs() -> bool:
            nonlocal last0, last1
            if len(sched) == len(matches):
                return True
            for i in range(len(matches)):
                if used[i]:
                    continue
                m = matches[i]
                if m[0] == last0 or m[0] == last1 or m[1] == last0 or m[1] == last1:
                    continue
                used[i] = True
                sched.append(m)
                p0, p1 = last0, last1
                last0, last1 = m[0], m[1]
                if dfs():
                    return True
                last0, last1 = p0, p1
                sched.pop()
                used[i] = False
            return False

        if dfs():
            return sched
        return []
'''

FILES["3681_maximum_xor_of_subsequences"] = r'''# LeetCode 3681 - Maximum XOR of Subsequences
# https://leetcode.com/problems/maximum-xor-of-subsequences/

from typing import List


class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        basis = [0] * 32
        for x in nums:
            cur = x
            for b in range(31, -1, -1):
                if (cur & (1 << b)) == 0:
                    continue
                if basis[b] == 0:
                    basis[b] = cur
                    break
                cur ^= basis[b]
        ans = 0
        for b in range(31, -1, -1):
            if (ans ^ basis[b]) > ans:
                ans ^= basis[b]
        return ans
'''

FILES["3682_minimum_index_sum_of_common_elements"] = r'''# LeetCode 3682 - Minimum Index Sum of Common Elements
# https://leetcode.com/problems/minimum-index-sum-of-common-elements/

from typing import List


class Solution:
    def minimumSum(self, nums1: List[int], nums2: List[int]) -> int:
        inf = 1 << 30
        d = {}
        for i, x in enumerate(nums2):
            if x not in d:
                d[x] = i
        ans = inf
        for i, x in enumerate(nums1):
            if x in d:
                ans = min(ans, i + d[x])
        return -1 if ans == inf else ans
'''

FILES["3683_earliest_time_to_finish_one_task"] = r'''# LeetCode 3683 - Earliest Time to Finish One Task
# https://leetcode.com/problems/earliest-time-to-finish-one-task/

from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = 200
        for task in tasks:
            ans = min(ans, task[0] + task[1])
        return ans
'''

FILES["3684_maximize_sum_of_at_most_k_distinct_elements"] = r'''# LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
# https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

from typing import List


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 1, -1, -1):
            if i + 1 < n and nums[i] == nums[i + 1]:
                continue
            ans.append(nums[i])
            k -= 1
            if k == 0:
                break
        return ans
'''

FILES["3685_subsequence_sum_after_capping_elements"] = r'''# LeetCode 3685 - Subsequence Sum After Capping Elements
# https://leetcode.com/problems/subsequence-sum-after-capping-elements/

from typing import List


class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        sorted_nums = sorted(nums)
        ans = [False] * n
        reach = [False] * (k + 1)
        reach[0] = True
        idx = 0
        for x in range(1, n + 1):
            while idx < n and sorted_nums[idx] <= x:
                v = sorted_nums[idx]
                for s in range(k, v - 1, -1):
                    if reach[s - v]:
                        reach[s] = True
                idx += 1
            tmp = reach[:]
            rem = n - idx
            for s in range(k + 1):
                if not reach[s]:
                    continue
                t = 1
                while t <= rem and s + t * x <= k:
                    tmp[s + t * x] = True
                    t += 1
            ans[x - 1] = tmp[k]
        return ans
'''

FILES["3686_number_of_stable_subsequences"] = r'''# LeetCode 3686 - Number of Stable Subsequences
# https://leetcode.com/problems/number-of-stable-subsequences/

from typing import List


class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 1000000007
        a1 = a2 = b1 = b2 = 0
        for x in nums:
            if x % 2 == 1:
                na1 = (1 + b1 + b2) % MOD
                na2 = a1
                a1 = (a1 + na1) % MOD
                a2 = (a2 + na2) % MOD
            else:
                nb1 = (1 + a1 + a2) % MOD
                nb2 = b1
                b1 = (b1 + nb1) % MOD
                b2 = (b2 + nb2) % MOD
        return (((a1 + a2) % MOD + b1) % MOD + b2) % MOD
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
