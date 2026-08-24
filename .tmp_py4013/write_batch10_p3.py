#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["3138_minimum_length_of_anagram_concatenation"] = r'''# LeetCode 3138 - Minimum Length of Anagram Concatenation
# https://leetcode.com/problems/minimum-length-of-anagram-concatenation/


class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        def check(k: int) -> bool:
            for i in range(0, n, k):
                cnt1 = [0] * 26
                for j in range(i, i + k):
                    cnt1[ord(s[j]) - 97] += 1
                for j in range(26):
                    if cnt1[j] * (n // k) != cnt[j]:
                        return False
            return True

        i = 1
        while True:
            if n % i == 0 and check(i):
                return i
            i += 1
'''

FILES["3139_minimum_cost_to_equalize_array"] = r'''# LeetCode 3139 - Minimum Cost to Equalize Array
# https://leetcode.com/problems/minimum-cost-to-equalize-array/

from typing import List


class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        MOD = 1000000007
        n = len(nums)
        min_num = nums[0]
        max_num = nums[0]
        total = 0
        for v in nums:
            min_num = min(min_num, v)
            max_num = max(max_num, v)
            total += v
        if cost1 * 2 <= cost2 or n < 3:
            total_gap = max_num * n - total
            return (cost1 * total_gap) % MOD
        ans = 10**18
        for target in range(max_num, 2 * max_num):
            max_gap = target - min_num
            total_gap = target * n - total
            pairs = total_gap // 2
            alt = total_gap - max_gap
            if alt < pairs:
                pairs = alt
            cost = cost1 * (total_gap - 2 * pairs) + cost2 * pairs
            ans = min(ans, cost)
        return ans % MOD
'''

FILES["3141_maximum_hamming_distances"] = r'''# LeetCode 3141 - Maximum Hamming Distances
# https://leetcode.com/problems/maximum-hamming-distances/

from typing import List


class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        dist = [-1] * (1 << m)
        q = []
        for x in nums:
            dist[x] = 0
            q.append(x)
        k = 1
        while q:
            t = []
            for x in q:
                for i in range(m):
                    y = x ^ (1 << i)
                    if dist[y] == -1:
                        dist[y] = k
                        t.append(y)
            q = t
            k += 1
        ans = list(nums)
        for i in range(len(ans)):
            x = ans[i]
            ans[i] = m - dist[x ^ ((1 << m) - 1)]
        return ans
'''

FILES["3142_check_if_grid_satisfies_conditions"] = r'''# LeetCode 3142 - Check if Grid Satisfies Conditions
# https://leetcode.com/problems/check-if-grid-satisfies-conditions/

from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                x = grid[i][j]
                if i + 1 < m and x != grid[i + 1][j]:
                    return False
                if j + 1 < n and x == grid[i][j + 1]:
                    return False
        return True
'''

FILES["3143_maximum_points_inside_the_square"] = r'''# LeetCode 3143 - Maximum Points Inside the Square
# https://leetcode.com/problems/maximum-points-inside-the-square/

import bisect
from typing import List


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        g = {}
        keys = []
        for i, p in enumerate(points):
            key = max(max(p[0], -p[0]), max(p[1], -p[1]))
            if key not in g:
                g[key] = []
                bisect.insort(keys, key)
            g[key].append(i)
        vis = [False] * 26
        ans = 0
        for key in keys:
            lst = g[key]
            for i in lst:
                j = ord(s[i]) - 97
                if vis[j]:
                    return ans
                vis[j] = True
            ans += len(lst)
        return ans
'''

FILES["3144_minimum_substring_partition_of_equal_character_frequency"] = r'''# LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
# https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        memo = [-1] * n

        def dfs(i: int) -> int:
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            cnt = [0] * 26
            freq = {}
            memo[i] = n - i
            for j in range(i, n):
                k = ord(s[j]) - 97
                if cnt[k] > 0:
                    c = cnt[k]
                    nv = freq[c] - 1
                    if nv == 0:
                        del freq[c]
                    else:
                        freq[c] = nv
                cnt[k] += 1
                freq[cnt[k]] = freq.get(cnt[k], 0) + 1
                if len(freq) == 1:
                    memo[i] = min(memo[i], 1 + dfs(j + 1))
            return memo[i]

        return dfs(0)
'''

FILES["3145_find_products_of_elements_of_big_array"] = r'''# LeetCode 3145 - Find Products of Elements of Big Array
# https://leetcode.com/problems/find-products-of-elements-of-big-array/

from typing import List


class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        M = 50
        cnt = [0] * (M + 1)
        s = [0] * (M + 1)
        p = 1
        for i in range(1, M + 1):
            cnt[i] = cnt[i - 1] * 2 + p
            s[i] = s[i - 1] * 2 + p * (i - 1)
            p *= 2

        def num_idx_and_sum(x: int):
            idx = 0
            total_sum = 0
            while x > 0:
                i = 0
                t = x
                while t > 1:
                    t >>= 1
                    i += 1
                idx += cnt[i]
                total_sum += s[i]
                x -= 1 << i
                total_sum += (x + 1) * i
                idx += x + 1
            return idx, total_sum

        def f(i: int) -> int:
            l = 0
            r = 1 << M
            while l < r:
                mid = (l + r + 1) >> 1
                p0 = num_idx_and_sum(mid)
                if p0[0] < i:
                    l = mid
                else:
                    r = mid - 1
            p0 = num_idx_and_sum(l)
            total_sum = p0[1]
            i -= p0[0]
            x = l + 1
            for _ in range(i):
                y = x & -x
                tz = 0
                yy = y
                while (yy & 1) == 0:
                    tz += 1
                    yy >>= 1
                total_sum += tz
                x -= y
            return total_sum

        def qpow(a: int, n: int, mod: int) -> int:
            ans = 1 % mod
            a %= mod
            while n > 0:
                if (n & 1) != 0:
                    ans = ans * a % mod
                a = a * a % mod
                n >>= 1
            return ans

        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            left, right, mod = q[0], q[1], q[2]
            power = f(right + 1) - f(left)
            ans[i] = qpow(2, power, mod)
        return ans
'''

FILES["3146_permutation_difference_between_two_strings"] = r'''# LeetCode 3146 - Permutation Difference between Two Strings
# https://leetcode.com/problems/permutation-difference-between-two-strings/


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d = [0] * 26
        for i, ch in enumerate(s):
            d[ord(ch) - 97] = i
        ans = 0
        for i, ch in enumerate(t):
            ans += abs(d[ord(ch) - 97] - i)
        return ans
'''

FILES["3147_taking_maximum_energy_from_the_mystic_dungeon"] = r'''# LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = -(1 << 30)
        n = len(energy)
        for i in range(n - k, n):
            s = 0
            j = i
            while j >= 0:
                s += energy[j]
                ans = max(ans, s)
                j -= k
        return ans
'''

FILES["3148_maximum_difference_score_in_a_grid"] = r'''# LeetCode 3148 - Maximum Difference Score in a Grid
# https://leetcode.com/problems/maximum-difference-score-in-a-grid/

from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        INF = 1 << 30
        f = [[0] * n for _ in range(m)]
        ans = -INF
        for i in range(m):
            for j in range(n):
                x = grid[i][j]
                mi = INF
                if i > 0:
                    mi = min(mi, f[i - 1][j])
                if j > 0:
                    mi = min(mi, f[i][j - 1])
                ans = max(ans, x - mi)
                f[i][j] = min(x, mi)
        return ans
'''

FILES["3149_find_the_minimum_cost_array_permutation"] = r'''# LeetCode 3149 - Find the Minimum Cost Array Permutation
# https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

from typing import List


class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        memo = [[-1] * n for _ in range(1 << n)]

        def absv(x: int) -> int:
            return -x if x < 0 else x

        def dfs(mask: int, pre: int) -> int:
            if mask == (1 << n) - 1:
                return absv(pre - nums[0])
            if memo[mask][pre] != -1:
                return memo[mask][pre]
            res = 10**18
            for cur in range(1, n):
                if ((mask >> cur) & 1) == 0:
                    res = min(res, absv(pre - nums[cur]) + dfs(mask | (1 << cur), cur))
            memo[mask][pre] = res
            return res

        ans = []

        def g(mask: int, pre: int) -> None:
            ans.append(pre)
            if mask == (1 << n) - 1:
                return
            res = dfs(mask, pre)
            for cur in range(1, n):
                if ((mask >> cur) & 1) == 0:
                    if absv(pre - nums[cur]) + dfs(mask | (1 << cur), cur) == res:
                        g(mask | (1 << cur), cur)
                        break

        g(1, 0)
        return ans
'''

FILES["3151_special_array_i"] = r'''# LeetCode 3151 - Special Array I
# https://leetcode.com/problems/special-array-i/

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                return False
        return True
'''

FILES["3152_special_array_ii"] = r'''# LeetCode 3152 - Special Array II
# https://leetcode.com/problems/special-array-ii/

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        d = list(range(n))
        for i in range(1, n):
            if nums[i] % 2 != nums[i - 1] % 2:
                d[i] = d[i - 1]
        ans = [False] * len(queries)
        for i, q in enumerate(queries):
            ans[i] = d[q[1]] <= q[0]
        return ans
'''

FILES["3153_sum_of_digit_differences_of_all_pairs"] = r'''# LeetCode 3153 - Sum of Digit Differences of All Pairs
# https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

from typing import List


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        m = 0
        x = nums[0]
        while x > 0:
            m += 1
            x //= 10
        if m == 0:
            m = 1
        ans = 0
        vals = nums[:]
        for _ in range(m):
            cnt = [0] * 10
            for i in range(n):
                cnt[vals[i] % 10] += 1
                vals[i] //= 10
            for v in cnt:
                ans += v * (n - v)
        return ans // 2
'''

FILES["3154_find_number_of_ways_to_reach_the_k_th_stair"] = r'''# LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
# https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/


class Solution:
    def waysToReachStair(self, k: int) -> int:
        f = {}

        def dfs(i: int, j: int, jump: int) -> int:
            if i > k + 1:
                return 0
            key = (i, j, jump)
            if key in f:
                return f[key]
            ans = 0
            if i == k:
                ans += 1
            if i > 0 and j == 0:
                ans += dfs(i - 1, 1, jump)
            ans += dfs(i + (2 ** jump), 0, jump + 1)
            f[key] = ans
            return ans

        return dfs(1, 0, 0)
'''

FILES["3155_maximum_number_of_upgradable_servers"] = r'''# LeetCode 3155 - Maximum Number of Upgradable Servers
# https://leetcode.com/problems/maximum-number-of-upgradable-servers/

from typing import List


class Solution:
    def maxUpgrades(
        self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]
    ) -> List[int]:
        ans = [0] * len(count)
        for i in range(len(count)):
            cnt = count[i]
            ans[i] = min(cnt, (cnt * sell[i] + money[i]) // (upgrade[i] + sell[i]))
        return ans
'''

FILES["3157_find_the_level_of_tree_with_minimum_sum"] = r'''# LeetCode 3157 - Find the Level of Tree with Minimum Sum
# https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        s = 10**18
        ans = 0
        level = 1
        while q:
            t = 0
            m = len(q)
            while m > 0:
                node = q.popleft()
                t += node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                m -= 1
            if s > t:
                s = t
                ans = level
            level += 1
        return ans
'''

FILES["3158_find_the_xor_of_numbers_which_appear_twice"] = r'''# LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        cnt = [0] * 51
        ans = 0
        for x in nums:
            cnt[x] += 1
            if cnt[x] == 2:
                ans ^= x
        return ans
'''

FILES["3159_find_occurrences_of_an_element_in_an_array"] = r'''# LeetCode 3159 - Find Occurrences of an Element in an Array
# https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ids = [i for i, v in enumerate(nums) if v == x]
        ans = [0] * len(queries)
        for qi, i in enumerate(queries):
            if i - 1 < len(ids):
                ans[qi] = ids[i - 1]
            else:
                ans[qi] = -1
        return ans
'''

FILES["3160_find_the_number_of_distinct_colors_among_the_balls"] = r'''# LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        g = {}
        cnt = {}
        ans = [0] * len(queries)
        ai = 0
        for q in queries:
            x, y = q[0], q[1]
            cnt[y] = cnt.get(y, 0) + 1
            old = g.get(x)
            if old is not None:
                nv = cnt[old] - 1
                if nv == 0:
                    del cnt[old]
                else:
                    cnt[old] = nv
            g[x] = y
            ans[ai] = len(cnt)
            ai += 1
        return ans
'''

FILES["3161_block_placement_queries"] = r'''# LeetCode 3161 - Block Placement Queries
# https://leetcode.com/problems/block-placement-queries/

import bisect
from typing import List


class FenwickMax:
    def __init__(self, n: int):
        self.vals = [0] * (n + 1)

    def maximize(self, i: int, val: int) -> None:
        while i < len(self.vals):
            self.vals[i] = max(self.vals[i], val)
            i += i & -i

    def get(self, i: int) -> int:
        res = 0
        while i > 0:
            res = max(res, self.vals[i])
            i -= i & -i
        return res


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        n = len(queries) * 3
        if n > 50000:
            n = 50000
        tree = FenwickMax(n + 1)
        obs = [0, n]
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = bisect.bisect_left(obs, x)
                if idx == len(obs) or obs[idx] != x:
                    obs.insert(idx, x)
        for i in range(len(obs) - 1):
            tree.maximize(obs[i + 1], obs[i + 1] - obs[i])
        ans = []
        for i in range(len(queries) - 1, -1, -1):
            typ, x = queries[i][0], queries[i][1]
            if typ == 1:
                j = bisect.bisect_left(obs, x)
                prev, nxt = obs[j - 1], obs[j + 1]
                obs.pop(j)
                tree.maximize(nxt, nxt - prev)
            else:
                sz = queries[i][2]
                j = bisect.bisect_left(obs, x + 1) - 1
                prev = obs[j]
                ans.append(tree.get(prev) >= sz or x - prev >= sz)
        ans.reverse()
        return ans
'''

FILES["3162_find_the_number_of_good_pairs_i"] = r'''# LeetCode 3162 - Find the Number of Good Pairs I
# https://leetcode.com/problems/find-the-number-of-good-pairs-i/

from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for x in nums1:
            for y in nums2:
                if x % (y * k) == 0:
                    ans += 1
        return ans
'''

FILES["3163_string_compression_iii"] = r'''# LeetCode 3163 - String Compression III
# https://leetcode.com/problems/string-compression-iii/


class Solution:
    def compressedString(self, word: str) -> str:
        ans = []
        n = len(word)
        i = 0
        while i < n:
            j = i + 1
            while j < n and word[j] == word[i]:
                j += 1
            k = j - i
            while k > 0:
                x = min(9, k)
                ans.append(str(x))
                ans.append(word[i])
                k -= x
            i = j
        return "".join(ans)
'''

FILES["3164_find_the_number_of_good_pairs_ii"] = r'''# LeetCode 3164 - Find the Number of Good Pairs II
# https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt1 = {}
        for x in nums1:
            if x % k == 0:
                cnt1[x // k] = cnt1.get(x // k, 0) + 1
        if not cnt1:
            return 0
        cnt2 = {}
        for x in nums2:
            cnt2[x] = cnt2.get(x, 0) + 1
        mx = 0
        for x in cnt1:
            mx = max(mx, x)
        ans = 0
        for x, v in cnt2.items():
            s = 0
            y = x
            while y <= mx:
                c = cnt1.get(y)
                if c is not None:
                    s += c
                y += x
            ans += s * v
        return ans
'''

FILES["3165_maximum_sum_of_subsequence_with_non_adjacent_elements"] = r'''# LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
# https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

from typing import List


class Node:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.s00 = 0
        self.s01 = 0
        self.s10 = 0
        self.s11 = 0


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        tr = [Node() for _ in range(n * 4)]

        def build(u: int, l: int, r: int) -> None:
            tr[u].l = l
            tr[u].r = r
            if l == r:
                return
            mid = (l + r) >> 1
            build(u << 1, l, mid)
            build(u << 1 | 1, mid + 1, r)

        def pushup(u: int) -> None:
            left = tr[u << 1]
            right = tr[u << 1 | 1]
            tr[u].s00 = max(left.s00 + right.s10, left.s01 + right.s00)
            tr[u].s01 = max(left.s00 + right.s11, left.s01 + right.s01)
            tr[u].s10 = max(left.s10 + right.s10, left.s11 + right.s00)
            tr[u].s11 = max(left.s10 + right.s11, left.s11 + right.s01)

        def modify(u: int, x: int, v: int) -> None:
            if tr[u].l == tr[u].r:
                tr[u].s11 = max(0, v)
                return
            mid = (tr[u].l + tr[u].r) >> 1
            if x <= mid:
                modify(u << 1, x, v)
            else:
                modify(u << 1 | 1, x, v)
            pushup(u)

        def query(u: int, l: int, r: int) -> int:
            if tr[u].l >= l and tr[u].r <= r:
                return tr[u].s11
            mid = (tr[u].l + tr[u].r) >> 1
            ans = 0
            if r <= mid:
                ans = query(u << 1, l, r)
            if l > mid:
                ans = max(ans, query(u << 1 | 1, l, r))
            return ans

        build(1, 1, n)
        for i in range(n):
            modify(1, i + 1, nums[i])
        MOD = 1000000007
        ans = 0
        for q in queries:
            modify(1, q[0] + 1, q[1])
            ans = (ans + query(1, 1, n)) % MOD
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
