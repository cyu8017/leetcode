#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["3635_earliest_finish_time_for_land_and_water_rides_ii"] = r'''# LeetCode 3635 - Earliest Finish Time for Land and Water Rides II
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        def calc(a1: List[int], t1: List[int], a2: List[int], t2: List[int]) -> int:
            min_end = min(a1[i] + t1[i] for i in range(len(a1)))
            ans = min(max(min_end, a2[i]) + t2[i] for i in range(len(a2)))
            return ans

        return min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration),
        )
'''

FILES["3636_threshold_majority_queries"] = r'''# LeetCode 3636 - Threshold Majority Queries
# https://leetcode.com/problems/threshold-majority-queries/

from typing import List


class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        for qi, (l, r, t) in enumerate(queries):
            cnt = {}
            for i in range(l, r + 1):
                cnt[nums[i]] = cnt.get(nums[i], 0) + 1
            best = -1
            best_c = 0
            for v, c in cnt.items():
                if c >= t and (c > best_c or (c == best_c and (best == -1 or v < best))):
                    best_c = c
                    best = v
            ans[qi] = best
        return ans
'''

FILES["3637_trionic_array_i"] = r'''# LeetCode 3637 - Trionic Array I
# https://leetcode.com/problems/trionic-array-i/

from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        p = 0
        while p < n - 2 and nums[p] < nums[p + 1]:
            p += 1
        if p == 0:
            return False
        q = p
        while q < n - 1 and nums[q] > nums[q + 1]:
            q += 1
        if q == p or q == n - 1:
            return False
        while q < n - 1 and nums[q] < nums[q + 1]:
            q += 1
        return q == n - 1
'''

FILES["3638_maximum_balanced_shipments"] = r'''# LeetCode 3638 - Maximum Balanced Shipments
# https://leetcode.com/problems/maximum-balanced-shipments/

from typing import List


class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        ans = 0
        mx = 0
        for x in weight:
            mx = max(mx, x)
            if x < mx:
                ans += 1
                mx = 0
        return ans
'''

FILES["3639_minimum_time_to_activate_string"] = r'''# LeetCode 3639 - Minimum Time to Activate String
# https://leetcode.com/problems/minimum-time-to-activate-string/

from typing import List


class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        total = n * (n + 1) // 2
        if k > total:
            return -1

        def count_valid(t: int) -> int:
            star = [False] * n
            for i in range(t + 1):
                star[order[i]] = True
            invalid = 0
            i = 0
            while i < n:
                if star[i]:
                    i += 1
                    continue
                j = i
                while j < n and not star[j]:
                    j += 1
                L = j - i
                invalid += L * (L + 1) // 2
                i = j
            return total - invalid

        lo, hi, ans = 0, n - 1, -1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if count_valid(mid) >= k:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
'''

FILES["3640_trionic_array_ii"] = r'''# LeetCode 3640 - Trionic Array II
# https://leetcode.com/problems/trionic-array-ii/

from typing import List


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        ans = float("-inf")
        while i < n:
            l = i
            i += 1
            while i < n and nums[i - 1] < nums[i]:
                i += 1
            if i == l + 1:
                continue
            p = i - 1
            s = nums[p - 1] + nums[p]
            while i < n and nums[i - 1] > nums[i]:
                s += nums[i]
                i += 1
            if i == p + 1 or i == n or nums[i - 1] == nums[i]:
                continue
            q = i - 1
            s += nums[i]
            i += 1
            mx = 0
            t = 0
            while i < n and nums[i - 1] < nums[i]:
                t += nums[i]
                i += 1
                mx = max(mx, t)
            s += mx
            mx = t = 0
            for j in range(p - 2, l - 1, -1):
                t += nums[j]
                mx = max(mx, t)
            s += mx
            ans = max(ans, s)
            i = q
        return int(ans)
'''

FILES["3641_longest_semi_repeating_subarray"] = r'''# LeetCode 3641 - Longest Semi-Repeating Subarray
# https://leetcode.com/problems/longest-semi-repeating-subarray/

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        cnt = {}
        ans = 0
        cur = 0
        l = 0
        for r, x in enumerate(nums):
            c = cnt.get(x, 0) + 1
            cnt[x] = c
            if c == 2:
                cur += 1
            while cur > k:
                c2 = cnt.get(nums[l], 0) - 1
                cnt[nums[l]] = c2
                if c2 == 1:
                    cur -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
'''

FILES["3643_flip_square_submatrix_vertically"] = r'''# LeetCode 3643 - Flip Square Submatrix Vertically
# https://leetcode.com/problems/flip-square-submatrix-vertically/

from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(x, x + k // 2):
            i2 = x + k - 1 - (i - x)
            for j in range(y, y + k):
                grid[i][j], grid[i2][j] = grid[i2][j], grid[i][j]
        return grid
'''

FILES["3644_maximum_k_to_sort_a_permutation"] = r'''# LeetCode 3644 - Maximum K to Sort a Permutation
# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1
        for i, v in enumerate(nums):
            if i != v:
                ans &= v
        return max(ans, 0)
'''

FILES["3645_maximum_total_from_optimal_activation_order"] = r'''# LeetCode 3645 - Maximum Total from Optimal Activation Order
# https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

from typing import List


class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        g = {}
        for i, lim in enumerate(limit):
            g.setdefault(lim, []).append(value[i])
        ans = 0
        for lim, vs in g.items():
            vs.sort(reverse=True)
            ans += sum(vs[:lim])
        return ans
'''

FILES["3646_next_special_palindrome_number"] = r'''# LeetCode 3646 - Next Special Palindrome Number
# https://leetcode.com/problems/next-special-palindrome-number/


class Solution:
    def specialPalindrome(self, n: int) -> int:
        cands = []
        half_cnt = [0] * 10
        mid = 0
        half_len = 0

        def dfs(pos: int, cur: list) -> None:
            if pos == half_len:
                left = "".join(str(d) for d in cur)
                s = left
                if mid > 0:
                    s += str(mid)
                s += left[::-1]
                cands.append(int(s))
                return
            for d in range(1, 10):
                if half_cnt[d] == 0:
                    continue
                half_cnt[d] -= 1
                cur.append(d)
                dfs(pos + 1, cur)
                cur.pop()
                half_cnt[d] += 1

        def gen(mask: int) -> None:
            nonlocal mid, half_len
            total = 0
            odd = 0
            for d in range(1, 10):
                if (mask >> d) & 1:
                    total += d
                    if d % 2 == 1:
                        odd += 1
            if total == 0 or total > 18 or odd > 1:
                return
            for i in range(10):
                half_cnt[i] = 0
            mid = 0
            for d in range(1, 10):
                if ((mask >> d) & 1) == 0:
                    continue
                half_cnt[d] = d // 2
                if d % 2 == 1:
                    mid = d
            half_len = total // 2
            dfs(0, [])

        for mask in range(1, 1 << 10):
            if mask & 1:
                continue
            gen(mask)
        cands.sort()
        for v in cands:
            if v > n:
                return v
        return -1
'''

FILES["3647_maximum_weight_in_two_bags"] = r'''# LeetCode 3647 - Maximum Weight in Two Bags
# https://leetcode.com/problems/maximum-weight-in-two-bags/

from typing import List


class Solution:
    def maxWeight(self, weights: List[int], w1: int, w2: int) -> int:
        f = [[0] * (w2 + 1) for _ in range(w1 + 1)]
        for x in weights:
            for j in range(w1, -1, -1):
                for k in range(w2, -1, -1):
                    if x <= j:
                        f[j][k] = max(f[j][k], f[j - x][k] + x)
                    if x <= k:
                        f[j][k] = max(f[j][k], f[j][k - x] + x)
        return f[w1][w2]
'''

FILES["3648_minimum_sensors_to_cover_grid"] = r'''# LeetCode 3648 - Minimum Sensors to Cover Grid
# https://leetcode.com/problems/minimum-sensors-to-cover-grid/


class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        cover = 2 * k + 1
        return ((n + cover - 1) // cover) * ((m + cover - 1) // cover)
'''

FILES["3649_number_of_perfect_pairs"] = r'''# LeetCode 3649 - Number of Perfect Pairs
# https://leetcode.com/problems/number-of-perfect-pairs/

from typing import List


class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        n = len(nums)
        abs_nums = sorted(abs(x) for x in nums)
        ans = 0
        j = 0
        for i in range(n):
            if j < i + 1:
                j = i + 1
            while j < n and abs_nums[j] <= 2 * abs_nums[i]:
                j += 1
            ans += j - i - 1
        return ans
'''

FILES["3650_minimum_cost_path_with_edge_reversals"] = r'''# LeetCode 3650 - Minimum Cost Path with Edge Reversals
# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

from typing import List
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w * 2))
        inf = 1073741823
        dist = [inf] * n
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == n - 1:
                return d
            for v, w in g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return -1
'''

FILES["3651_minimum_cost_path_with_teleportations"] = r'''# LeetCode 3651 - Minimum Cost Path with Teleportations
# https://leetcode.com/problems/minimum-cost-path-with-teleportations/

from typing import List


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        inf = 536870911
        f = [[[inf] * n for _ in range(m)] for _ in range(k + 1)]
        f[0][0][0] = 0
        for i in range(m):
            for j in range(n):
                if i > 0:
                    f[0][i][j] = min(f[0][i][j], f[0][i - 1][j] + grid[i][j])
                if j > 0:
                    f[0][i][j] = min(f[0][i][j], f[0][i][j - 1] + grid[i][j])
        g = {}
        for i in range(m):
            for j in range(n):
                g.setdefault(grid[i][j], []).append((i, j))
        keys = sorted(g.keys(), reverse=True)
        for t in range(1, k + 1):
            mn = inf
            for key in keys:
                pos = g[key]
                for p in pos:
                    mn = min(mn, f[t - 1][p[0]][p[1]])
                for p in pos:
                    f[t][p[0]][p[1]] = mn
            for i in range(m):
                for j in range(n):
                    if i > 0:
                        f[t][i][j] = min(f[t][i][j], f[t][i - 1][j] + grid[i][j])
                    if j > 0:
                        f[t][i][j] = min(f[t][i][j], f[t][i][j - 1] + grid[i][j])
        ans = inf
        for t in range(k + 1):
            ans = min(ans, f[t][m - 1][n - 1])
        return ans
'''

FILES["3652_best_time_to_buy_and_sell_stock_using_strategy"] = r'''# LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        s = [0] * (n + 1)
        t = [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = s[i - 1] + prices[i - 1] * strategy[i - 1]
            t[i] = t[i - 1] + prices[i - 1]
        ans = s[n]
        for i in range(k, n + 1):
            ans = max(ans, s[n] - (s[i] - s[i - k]) + (t[i] - t[i - k // 2]))
        return ans
'''

FILES["3653_xor_after_range_multiplication_queries_i"] = r'''# LeetCode 3653 - XOR After Range Multiplication Queries I
# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 1000000007
        for l, r, k, v in queries:
            for idx in range(l, r + 1, k):
                nums[idx] = nums[idx] * v % mod
        ans = 0
        for x in nums:
            ans ^= x
        return ans
'''

FILES["3654_minimum_sum_after_divisible_sum_deletions"] = r'''# LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
# https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] + nums[i]) % k
        inf = 10**18
        dp = [0] * (n + 1)
        best = [inf] * k
        best[0] = 0
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + nums[i - 1]
            if best[prefix[i]] < dp[i]:
                dp[i] = best[prefix[i]]
            if dp[i] < best[prefix[i]]:
                best[prefix[i]] = dp[i]
        return dp[n]
'''

FILES["3655_xor_after_range_multiplication_queries_ii"] = r'''# LeetCode 3655 - XOR After Range Multiplication Queries II
# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1000000007
        n = len(nums)
        by_k = {}
        for q in queries:
            by_k.setdefault(q[2], []).append(q)
        res = nums[:]
        for lst in by_k.values():
            fac = [1] * n
            for u in lst:
                for i in range(u[0], u[1] + 1, u[2]):
                    fac[i] = fac[i] * u[3] % MOD
            for i in range(n):
                res[i] = res[i] * fac[i] % MOD
        ans = 0
        for v in res:
            ans ^= v
        return ans
'''

FILES["3656_determine_if_a_simple_graph_exists"] = r'''# LeetCode 3656 - Determine if a Simple Graph Exists
# https://leetcode.com/problems/determine-if-a-simple-graph-exists/

from typing import List


class Solution:
    def simpleGraphExists(self, degrees: List[int]) -> bool:
        n = len(degrees)
        d = sorted(degrees, reverse=True)
        total = 0
        for x in d:
            if x < 0 or x >= n:
                return False
            total += x
        if total % 2 == 1:
            return False
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + d[i]
        for k in range(1, n + 1):
            right = 0
            for i in range(k, n):
                right += d[i] if d[i] < k else k
            if prefix[k] > k * (k - 1) + right:
                return False
        return True
'''

FILES["3658_gcd_of_odd_and_even_sums"] = r'''# LeetCode 3658 - GCD of Odd and Even Sums
# https://leetcode.com/problems/gcd-of-odd-and-even-sums/


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
'''

FILES["3659_partition_array_into_k_distinct_groups"] = r'''# LeetCode 3659 - Partition Array Into K-Distinct Groups
# https://leetcode.com/problems/partition-array-into-k-distinct-groups/

from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        m = n // k
        mx = max(nums)
        cnt = [0] * (mx + 1)
        for x in nums:
            cnt[x] += 1
            if cnt[x] > m:
                return False
        return True
'''

FILES["3660_jump_game_ix"] = r'''# LeetCode 3660 - Jump Game IX
# https://leetcode.com/problems/jump-game-ix/

from typing import List


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pre_max = [0] * n
        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])
        suf_min = 1073741823
        for i in range(n - 1, -1, -1):
            if pre_max[i] > suf_min:
                ans[i] = ans[i + 1]
            else:
                ans[i] = pre_max[i]
            suf_min = min(suf_min, nums[i])
        return ans
'''

FILES["3661_maximum_walls_destroyed_by_robots"] = r'''# LeetCode 3661 - Maximum Walls Destroyed by Robots
# https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

from typing import List
import bisect


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        arr = sorted(zip(robots, distance))
        walls = sorted(walls)
        memo = {}

        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0
            key = (i << 1) | j
            if key in memo:
                return memo[key]
            left = arr[i][0] - arr[i][1]
            if i > 0:
                left = max(left, arr[i - 1][0] + 1)
            l = bisect.bisect_left(walls, left)
            r = bisect.bisect_left(walls, arr[i][0] + 1)
            ans = dfs(i - 1, 0) + (r - l)
            right = arr[i][0] + arr[i][1]
            if i + 1 < len(arr):
                if j == 0:
                    right = min(right, arr[i + 1][0] - arr[i + 1][1] - 1)
                else:
                    right = min(right, arr[i + 1][0] - 1)
            l = bisect.bisect_left(walls, arr[i][0])
            r = bisect.bisect_left(walls, right + 1)
            ans = max(ans, dfs(i - 1, 1) + (r - l))
            memo[key] = ans
            return ans

        return dfs(n - 1, 1)
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
