from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
files = {}

files["2916_subarrays_distinct_element_sum_of_squares_ii"] = '''# LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        mod = 1000000007
        n = len(nums)
        tree = [{"sum": 0, "sumSq": 0, "lazy": 0} for _ in range(4 * (n + 2))]

        def apply(idx: int, l: int, r: int, val: int) -> None:
            length = r - l + 1
            tree[idx]["sumSq"] = (
                tree[idx]["sumSq"]
                + 2 * val % mod * tree[idx]["sum"] % mod
                + val % mod * val % mod * length % mod
            ) % mod
            tree[idx]["sum"] = (tree[idx]["sum"] + val % mod * length % mod) % mod
            tree[idx]["lazy"] = (tree[idx]["lazy"] + val) % mod

        def update(idx: int, l: int, r: int, ql: int, qr: int, val: int) -> None:
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                apply(idx, l, r, val)
                return
            if tree[idx]["lazy"] != 0 and l != r:
                mid = (l + r) // 2
                apply(idx * 2, l, mid, tree[idx]["lazy"])
                apply(idx * 2 + 1, mid + 1, r, tree[idx]["lazy"])
                tree[idx]["lazy"] = 0
            mid = (l + r) // 2
            update(idx * 2, l, mid, ql, qr, val)
            update(idx * 2 + 1, mid + 1, r, ql, qr, val)
            tree[idx]["sum"] = (tree[idx * 2]["sum"] + tree[idx * 2 + 1]["sum"]) % mod
            tree[idx]["sumSq"] = (tree[idx * 2]["sumSq"] + tree[idx * 2 + 1]["sumSq"]) % mod

        last = {}
        ans = 0
        for i in range(1, n + 1):
            v = nums[i - 1]
            prev = last.get(v, 0)
            update(1, 1, n, prev + 1, i, 1)
            ans = (ans + tree[1]["sumSq"]) % mod
            last[v] = i
        return ans
'''

files["2917_find_the_k_or_of_an_array"] = '''# LeetCode 2917 - Find the K-or of an Array
# https://leetcode.com/problems/find-the-k-or-of-an-array/

from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        for b in range(31):
            cnt = 0
            for v in nums:
                if (v & (1 << b)) != 0:
                    cnt += 1
            if cnt >= k:
                ans |= 1 << b
        return ans
'''

files["2918_minimum_equal_sum_of_two_arrays_after_replacing_zeros"] = '''# LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = s2 = z1 = z2 = 0
        for v in nums1:
            if v == 0:
                z1 += 1
                s1 += 1
            else:
                s1 += v
        for v in nums2:
            if v == 0:
                z2 += 1
                s2 += 1
            else:
                s2 += v
        if z1 == 0 and s1 < s2:
            return -1
        if z2 == 0 and s2 < s1:
            return -1
        return s1 if s1 > s2 else s2
'''

files["2919_minimum_increment_operations_to_make_array_beautiful"] = '''# LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
# https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

from typing import List


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        dp0 = dp1 = dp2 = 0
        for v in nums:
            cost = k - v if v < k else 0
            nd0 = cost + min(dp0, dp1, dp2)
            dp0, dp1, dp2 = dp1, dp2, nd0
        return min(dp0, dp1, dp2)
'''

files["2920_maximum_points_after_collecting_coins_from_all_nodes"] = '''# LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
# https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

from typing import List


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        memo = {}

        def dfs(u: int, p: int, shifts: int) -> int:
            if shifts > 14:
                shifts = 14
            key = (u << 5) | shifts
            if key in memo:
                return memo[key]
            c = coins[u] >> shifts
            opt1 = c - k
            opt2 = c // 2
            for v in g[u]:
                if v == p:
                    continue
                opt1 += dfs(v, u, shifts)
                opt2 += dfs(v, u, shifts + 1)
            best = max(opt1, opt2)
            memo[key] = best
            return best

        return dfs(0, -1, 0)
'''

files["2921_maximum_profitable_triplets_with_increasing_prices_ii"] = '''# LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
# https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        ans = -1
        bit = [0] * 5002

        def update(i: int, val: int) -> None:
            while i < len(bit):
                if val > bit[i]:
                    bit[i] = val
                i += i & -i

        def query(i: int) -> int:
            best = -1
            while i > 0:
                if bit[i] > best:
                    best = bit[i]
                i -= i & -i
            return best

        max_left = [0] * n
        for j in range(n):
            max_left[j] = query(prices[j] - 1)
            update(prices[j], profits[j])
        for j in range(n):
            best_r = -1
            for k in range(j + 1, n):
                if prices[k] > prices[j] and profits[k] > best_r:
                    best_r = profits[k]
            if max_left[j] >= 0 and best_r >= 0:
                cand = max_left[j] + profits[j] + best_r
                if cand > ans:
                    ans = cand
        return ans
'''

files["2923_find_champion_i"] = '''# LeetCode 2923 - Find Champion I
# https://leetcode.com/problems/find-champion-i/

from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            win = True
            for j in range(n):
                if i != j and grid[i][j] == 0:
                    win = False
                    break
            if win:
                return i
        return -1
'''

files["2924_find_champion_ii"] = '''# LeetCode 2924 - Find Champion II
# https://leetcode.com/problems/find-champion-ii/

from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = [0] * n
        for e in edges:
            indeg[e[1]] += 1
        ans = -1
        for i in range(n):
            if indeg[i] == 0:
                if ans != -1:
                    return -1
                ans = i
        return ans
'''

files["2925_maximum_score_after_applying_operations_on_a_tree"] = '''# LeetCode 2925 - Maximum Score After Applying Operations on a Tree
# https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

from typing import List


class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        total = sum(values)

        def dfs(u: int, p: int) -> int:
            sum_kids = 0
            is_leaf = True
            for v in g[u]:
                if v == p:
                    continue
                is_leaf = False
                sum_kids += dfs(v, u)
            if is_leaf:
                return values[u]
            return values[u] if values[u] < sum_kids else sum_kids

        return total - dfs(0, -1)
'''

files["2926_maximum_balanced_subsequence_sum"] = '''# LeetCode 2926 - Maximum Balanced Subsequence Sum
# https://leetcode.com/problems/maximum-balanced-subsequence-sum/

from typing import List


class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        neg_inf = -(2**53) // 4
        n = len(nums)
        keys = [v - i for i, v in enumerate(nums)]
        uniq = sorted(set(keys))
        bit = [neg_inf] * (len(uniq) + 2)

        def idx_of(v: int) -> int:
            lo, hi = 0, len(uniq)
            while lo < hi:
                mid = (lo + hi) // 2
                if uniq[mid] < v:
                    lo = mid + 1
                else:
                    hi = mid
            return lo + 1

        def update(i: int, val: int) -> None:
            while i < len(bit):
                if val > bit[i]:
                    bit[i] = val
                i += i & -i

        def query(i: int) -> int:
            best = neg_inf
            while i > 0:
                if bit[i] > best:
                    best = bit[i]
                i -= i & -i
            return best

        ans = neg_inf
        for i in range(n):
            id_ = idx_of(keys[i])
            best = query(id_)
            cur = nums[i]
            if best > neg_inf / 2:
                cand = best + nums[i]
                if cand > cur:
                    cur = cand
            update(id_, cur)
            if cur > ans:
                ans = cur
        return ans
'''

files["2927_distribute_candies_among_children_iii"] = '''# LeetCode 2927 - Distribute Candies Among Children III
# https://leetcode.com/problems/distribute-candies-among-children-iii/


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb(x: int) -> int:
            if x < 2:
                return 0
            return x * (x - 1) // 2

        ans = comb(n + 2)
        ans -= 3 * comb(n - limit + 1)
        ans += 3 * comb(n - 2 * (limit + 1) + 2)
        ans -= comb(n - 3 * (limit + 1) + 2)
        if ans < 0:
            ans = 0
        return ans
'''

files["2928_distribute_candies_among_children_i"] = '''# LeetCode 2928 - Distribute Candies Among Children I
# https://leetcode.com/problems/distribute-candies-among-children-i/


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                k = n - i - j
                if 0 <= k <= limit:
                    ans += 1
        return ans
'''

files["2929_distribute_candies_among_children_ii"] = '''# LeetCode 2929 - Distribute Candies Among Children II
# https://leetcode.com/problems/distribute-candies-among-children-ii/


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb2(x: int) -> int:
            if x < 0:
                return 0
            return (x + 1) * (x + 2) // 2

        ans = comb2(n)
        ans -= 3 * comb2(n - (limit + 1))
        ans += 3 * comb2(n - 2 * (limit + 1))
        ans -= comb2(n - 3 * (limit + 1))
        return ans
'''

files["2930_number_of_strings_which_can_be_rearranged_to_contain_substring"] = '''# LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
# https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/


class Solution:
    def stringCount(self, n: int) -> int:
        if n < 4:
            return 0
        mod = 1000000007

        def modPow(a: int, b: int) -> int:
            res = 1
            a %= mod
            while b > 0:
                if b & 1:
                    res = (res * a) % mod
                a = (a * a) % mod
                b >>= 1
            return res

        ans = modPow(26, n)
        ans = (ans - 3 * modPow(25, n) % mod + mod) % mod
        ans = (ans + 3 * modPow(24, n) % mod) % mod
        ans = (ans - modPow(23, n) + mod) % mod
        ans = (ans + n % mod * modPow(25, n - 1) % mod) % mod
        ans = (ans - 2 * (n % mod) % mod * modPow(24, n - 1) % mod + mod) % mod
        ans = (ans + n % mod * modPow(23, n - 1) % mod) % mod
        ans = (ans - n % mod * ((n - 1 + mod) % mod) % mod * modPow(24, n - 2) % mod + mod) % mod
        ans = (ans + n % mod * ((n - 1 + mod) % mod) % mod * modPow(23, n - 2) % mod) % mod
        return ans
'''

files["2931_maximum_spending_after_buying_items"] = '''# LeetCode 2931 - Maximum Spending After Buying Items
# https://leetcode.com/problems/maximum-spending-after-buying-items/

from typing import List


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m, n = len(values), len(values[0])
        idx = [n - 1] * m
        ans = 0
        day = 1
        total = m * n
        for _ in range(total):
            best_i = -1
            best_v = 10**18
            for i in range(m):
                if idx[i] >= 0 and values[i][idx[i]] < best_v:
                    best_v = values[i][idx[i]]
                    best_i = i
            ans += best_v * day
            idx[best_i] -= 1
            day += 1
        return ans
'''

files["2932_maximum_strong_pair_xor_i"] = '''# LeetCode 2932 - Maximum Strong Pair XOR I
# https://leetcode.com/problems/maximum-strong-pair-xor-i/

from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                x, y = nums[i], nums[j]
                if abs(x - y) <= min(x, y):
                    xorr = x ^ y
                    if xorr > ans:
                        ans = xorr
        return ans
'''

files["2933_high_access_employees"] = '''# LeetCode 2933 - High-Access Employees
# https://leetcode.com/problems/high-access-employees/

from typing import List


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        m = {}
        for name, t in access_times:
            hh = (ord(t[0]) - 48) * 10 + (ord(t[1]) - 48)
            mm = (ord(t[2]) - 48) * 10 + (ord(t[3]) - 48)
            if name not in m:
                m[name] = []
            m[name].append(hh * 60 + mm)
        ans = []
        for name, times in m.items():
            times.sort()
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] < 60:
                    ans.append(name)
                    break
        ans.sort()
        return ans
'''

files["2934_minimum_operations_to_maximize_last_elements_in_arrays"] = '''# LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
# https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        def calc(a1: List[int], a2: List[int]) -> int:
            n = len(a1)
            ops = 0
            last1, last2 = a1[n - 1], a2[n - 1]
            for i in range(n - 1):
                x, y = a1[i], a2[i]
                if x <= last1 and y <= last2:
                    continue
                if y <= last1 and x <= last2:
                    ops += 1
                    continue
                return 1 << 30
            return ops

        n = len(nums1)
        ans = calc(nums1, nums2)
        t = nums1[n - 1]
        nums1[n - 1] = nums2[n - 1]
        nums2[n - 1] = t
        cand = calc(nums1, nums2) + 1
        if cand < ans:
            ans = cand
        nums2[n - 1] = nums1[n - 1]
        nums1[n - 1] = t
        return -1 if ans >= (1 << 30) else ans
'''

files["2935_maximum_strong_pair_xor_ii"] = '''# LeetCode 2935 - Maximum Strong Pair XOR II
# https://leetcode.com/problems/maximum-strong-pair-xor-ii/

from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0
        for i, x in enumerate(nums):
            j = i
            while j < len(nums) and nums[j] <= 2 * x:
                xorr = x ^ nums[j]
                if xorr > ans:
                    ans = xorr
                j += 1
        return ans
'''

files["2936_number_of_equal_numbers_blocks"] = '''# LeetCode 2936 - Number of Equal Numbers Blocks
# https://leetcode.com/problems/number-of-equal-numbers-blocks/

from typing import List


class Solution:
    def blockCount(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                ans += 1
        return ans
'''

written = 0
for folder, content in files.items():
    path = root / folder / "solution.py"
    path.write_text(content, encoding="utf-8", newline="\n")
    written += 1
    print("wrote", folder)
print("p4 written", written)
