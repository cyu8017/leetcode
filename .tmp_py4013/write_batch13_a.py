from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def write(folder: str, body: str) -> None:
    path = ROOT / folder / "solution.py"
    path.write_text(body.lstrip("\n"), encoding="utf-8")
    if path.read_bytes().startswith(b"\xef\xbb\xbf"):
        raise SystemExit(f"BOM in {folder}")


write(
    "3418_maximum_amount_of_money_robot_can_earn",
    '''
# LeetCode 3418 - Maximum Amount of Money Robot Can Earn
# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        neg = -(1 << 30)
        dp = [[[neg] * 3 for _ in range(n)] for _ in range(m)]
        if coins[0][0] < 0:
            dp[0][0][0] = coins[0][0]
            dp[0][0][1] = 0
            dp[0][0][2] = 0
        else:
            dp[0][0][0] = coins[0][0]
            dp[0][0][1] = coins[0][0]
            dp[0][0][2] = coins[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                for k in range(3):
                    best = neg
                    if i > 0:
                        best = max(best, dp[i - 1][j][k])
                    if j > 0:
                        best = max(best, dp[i][j - 1][k])
                    if best == neg:
                        continue
                    if coins[i][j] >= 0:
                        dp[i][j][k] = best + coins[i][j]
                    else:
                        dp[i][j][k] = max(dp[i][j][k], best + coins[i][j])
                for k in range(1, 3):
                    best = neg
                    if i > 0:
                        best = max(best, dp[i - 1][j][k - 1])
                    if j > 0:
                        best = max(best, dp[i][j - 1][k - 1])
                    if best != neg and coins[i][j] < 0:
                        dp[i][j][k] = max(dp[i][j][k], best)
        return max(dp[m - 1][n - 1][0], dp[m - 1][n - 1][1], dp[m - 1][n - 1][2])
''',
)

write(
    "3419_minimize_the_maximum_edge_weight_of_graph",
    '''
# LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
# https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

from typing import List


class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        def ok(mid: int) -> bool:
            g = [[] for _ in range(n)]
            for e in edges:
                if e[2] <= mid:
                    g[e[1]].append(e[0])
            vis = [False] * n
            q = [0]
            vis[0] = True
            cnt = 1
            while q:
                u = q.pop(0)
                for v in g[u]:
                    if not vis[v]:
                        vis[v] = True
                        cnt += 1
                        q.append(v)
            return cnt == n

        lo, hi, ans = 1, 1000001, -1
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = mid
                hi = mid
            else:
                lo = mid + 1
        return ans
''',
)

write(
    "3420_count_non_decreasing_subarrays_after_k_operations",
    '''
# LeetCode 3420 - Count Non-Decreasing Subarrays After K Operations
# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

from typing import List


class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            cost = 0
            max_v = nums[i]
            for j in range(i, n):
                if nums[j] >= max_v:
                    max_v = nums[j]
                else:
                    cost += max_v - nums[j]
                if cost > k:
                    break
                ans += 1
        return ans
''',
)

write(
    "3422_minimum_operations_to_make_subarray_elements_equal",
    '''
# LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
# https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 10**18
        for i in range(n - k + 1):
            sub = sorted(nums[i : i + k])
            med = sub[k // 2]
            cost = 0
            for x in sub:
                cost += abs(x - med)
            if cost < ans:
                ans = cost
        return ans
''',
)

write(
    "3423_maximum_difference_between_adjacent_elements_in_a_circular_array",
    '''
# LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            d = abs(nums[i] - nums[(i + 1) % n])
            if d > ans:
                ans = d
        return ans
''',
)

write(
    "3424_minimum_cost_to_make_arrays_identical",
    '''
# LeetCode 3424 - Minimum Cost to Make Arrays Identical
# https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

from typing import List


class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        no_swap = 0
        for i in range(len(arr)):
            no_swap += abs(arr[i] - brr[i])
        a2 = sorted(arr)
        b2 = sorted(brr)
        with_swap = k
        for i in range(len(a2)):
            with_swap += abs(a2[i] - b2[i])
        return no_swap if no_swap < with_swap else with_swap
''',
)

write(
    "3425_longest_special_path",
    '''
# LeetCode 3425 - Longest Special Path
# https://leetcode.com/problems/longest-special-path/

from typing import List


class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        best_len, best_nodes = 0, 1
        last = {}
        path = []

        def dfs(u: int, p: int, dist: int, left: int) -> None:
            nonlocal best_len, best_nodes
            seen = nums[u] in last
            prev_pos = last[nums[u]] if seen else -1
            last[nums[u]] = len(path)
            new_left = left
            if seen and prev_pos >= left:
                new_left = prev_pos + 1
            path.append(dist)
            length = dist - path[new_left]
            nodes = len(path) - new_left
            if length > best_len or (length == best_len and nodes < best_nodes):
                best_len = length
                best_nodes = nodes
            for v, w in g[u]:
                if v == p:
                    continue
                dfs(v, u, dist + w, new_left)
            path.pop()
            if seen:
                last[nums[u]] = prev_pos
            else:
                del last[nums[u]]

        dfs(0, -1, 0, 0)
        return [best_len, best_nodes]
''',
)

write(
    "3426_manhattan_distances_of_all_arrangements_of_pieces",
    '''
# LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
# https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/


class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        mod = 1000000007

        def mod_pow(a: int, e: int) -> int:
            r = 1
            base = a % mod
            while e > 0:
                if e & 1:
                    r = (r * base) % mod
                base = (base * base) % mod
                e >>= 1
            return r

        def comb(nn: int, kk: int) -> int:
            if kk < 0 or kk > nn:
                return 0
            num, den = 1, 1
            for i in range(kk):
                num = num * (nn - i) % mod
                den = den * (i + 1) % mod
            return num * mod_pow(den, mod - 2) % mod

        if k < 2:
            return 0
        total_cells = m * n
        pair_choose = comb(total_cells - 2, k - 2)
        sum_dist = 0
        for d in range(1, m):
            sum_dist += d * (m - d) * n * n
        for d in range(1, n):
            sum_dist += d * (n - d) * m * m
        return sum_dist % mod * pair_choose % mod
''',
)

write(
    "3427_sum_of_variable_length_subarrays",
    '''
# LeetCode 3427 - Sum of Variable Length Subarrays
# https://leetcode.com/problems/sum-of-variable-length-subarrays/

from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        ans = 0
        for i in range(n):
            start = i - nums[i]
            if start < 0:
                start = 0
            ans += pref[i + 1] - pref[start]
        return ans
''',
)

write(
    "3428_maximum_and_minimum_sums_of_at_most_size_k_subsequences",
    '''
# LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

from typing import List


class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        mod = 1000000007
        nums = sorted(nums)
        n = len(nums)
        C = [[0] * k for _ in range(n + 1)]
        for i in range(n + 1):
            C[i][0] = 1
            j = 1
            while j < k and j <= i:
                C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % mod
                j += 1
        ans = 0
        for i in range(n):
            ways_max = 0
            j = 0
            while j < k and j <= i:
                ways_max = (ways_max + C[i][j]) % mod
                j += 1
            ways_min = 0
            right = n - i - 1
            j = 0
            while j < k and j <= right:
                ways_min = (ways_min + C[right][j]) % mod
                j += 1
            ans = (ans + nums[i] * ways_max % mod + nums[i] * ways_min % mod) % mod
        return ans
''',
)

write(
    "3429_paint_house_iv",
    '''
# LeetCode 3429 - Paint House IV
# https://leetcode.com/problems/paint-house-iv/

from typing import List


class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        inf = 10**18
        m = n // 2
        dp = [[0] * 3 for _ in range(3)]
        for a in range(3):
            for b in range(3):
                dp[a][b] = inf if a == b else cost[0][a] + cost[n - 1][b]
        for i in range(1, m):
            ndp = [[inf] * 3 for _ in range(3)]
            for pa in range(3):
                for pb in range(3):
                    if dp[pa][pb] >= inf:
                        continue
                    for a in range(3):
                        if a == pa:
                            continue
                        for b in range(3):
                            if b == pb or a == b:
                                continue
                            v = dp[pa][pb] + cost[i][a] + cost[n - 1 - i][b]
                            if v < ndp[a][b]:
                                ndp[a][b] = v
            dp = ndp
        ans = inf
        for a in range(3):
            for b in range(3):
                if dp[a][b] < ans:
                    ans = dp[a][b]
        return ans
''',
)

write(
    "3430_maximum_and_minimum_sums_of_at_most_size_k_subarrays",
    '''
# LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

from typing import List


class Solution:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            mn = mx = nums[i]
            j = i
            while j < n and j - i + 1 <= k:
                if nums[j] < mn:
                    mn = nums[j]
                if nums[j] > mx:
                    mx = nums[j]
                ans += mn + mx
                j += 1
        return ans
''',
)

write(
    "3431_minimum_unlocked_indices_to_sort_nums",
    '''
# LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
# https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

from typing import List


class Solution:
    def minUnlockedIndices(self, nums: List[int], locked: List[int]) -> int:
        n = len(nums)
        need = False
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                need = True
                break
        if not need:
            return 0
        left, right = n, -1
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    if i < left:
                        left = i
                    if j > right:
                        right = j
        if right < left:
            return 0
        ans = 0
        for i in range(left, right + 1):
            if locked[i] == 1:
                ans += 1
        tmp = nums[:]
        lock = locked[:]
        for i in range(left, right + 1):
            lock[i] = 0
        changed = True
        while changed:
            changed = False
            for i in range(n - 1):
                if lock[i] == 0 and lock[i + 1] == 0 and tmp[i] > tmp[i + 1]:
                    tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
                    changed = True
        for i in range(1, n):
            if tmp[i] < tmp[i - 1]:
                return -1
        return ans
''',
)

write(
    "3432_count_partitions_with_even_sum_difference",
    '''
# LeetCode 3432 - Count Partitions with Even Sum Difference
# https://leetcode.com/problems/count-partitions-with-even-sum-difference/

from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = 0
        for x in nums:
            total += x
        ans = left = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            if (left - (total - left)) % 2 == 0:
                ans += 1
        return ans
''',
)

write(
    "3433_count_mentions_per_user",
    '''
# LeetCode 3433 - Count Mentions Per User
# https://leetcode.com/problems/count-mentions-per-user/

from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events = sorted(events, key=lambda e: (int(e[1]), 0 if e[0] == "OFFLINE" else 1))
        online = [True] * numberOfUsers
        offline_until = [0] * numberOfUsers
        ans = [0] * numberOfUsers
        for e in events:
            t = int(e[1])
            for i in range(numberOfUsers):
                if not online[i] and offline_until[i] <= t:
                    online[i] = True
            if e[0] == "OFFLINE":
                uid = int(e[2])
                online[uid] = False
                offline_until[uid] = t + 60
            else:
                msg = e[2]
                if msg == "ALL":
                    for i in range(numberOfUsers):
                        ans[i] += 1
                elif msg == "HERE":
                    for i in range(numberOfUsers):
                        if online[i]:
                            ans[i] += 1
                else:
                    for part in msg.split(" "):
                        uid = int(part[2:])
                        ans[uid] += 1
        return ans
''',
)

print("wrote group a (15)")
