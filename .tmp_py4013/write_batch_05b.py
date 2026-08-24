#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}


def add(folder, body):
    SOLUTIONS[folder] = body if body.endswith("\n") else body + "\n"


add("2581_count_number_of_possible_root_nodes", r'''# LeetCode 2581 - Count Number of Possible Root Nodes
# https://leetcode.com/problems/count-number-of-possible-root-nodes/

from typing import List


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        guess_set = set()

        def pack(a: int, b: int) -> str:
            return f"{a},{b}"

        for a, b in guesses:
            guess_set.add(pack(a, b))

        def dfs1(u: int, p: int) -> int:
            cnt = 0
            for v in g[u]:
                if v == p:
                    continue
                if pack(u, v) in guess_set:
                    cnt += 1
                cnt += dfs1(v, u)
            return cnt

        ans = 0

        def dfs2(u: int, p: int, cur: int) -> None:
            nonlocal ans
            if cur >= k:
                ans += 1
            for v in g[u]:
                if v == p:
                    continue
                nxt = cur
                if pack(u, v) in guess_set:
                    nxt -= 1
                if pack(v, u) in guess_set:
                    nxt += 1
                dfs2(v, u, nxt)

        base_cnt = dfs1(0, -1)
        dfs2(0, -1, base_cnt)
        return ans
''')

add("2582_pass_the_pillow", r'''# LeetCode 2582 - Pass the Pillow
# https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = 2 * (n - 1)
        t = time % cycle
        if t < n:
            return 1 + t
        return n - (t - (n - 1))
''')

add("2583_kth_largest_sum_in_a_binary_tree", r'''# LeetCode 2583 - Kth Largest Sum in a Binary Tree
# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        sums = []
        q = deque([root])
        while q:
            sz = len(q)
            s = 0
            for _ in range(sz):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            sums.append(s)
        sums.sort(reverse=True)
        if k > len(sums):
            return -1
        return sums[k - 1]
''')

add("2584_split_the_array_to_make_coprime_products", r'''# LeetCode 2584 - Split the Array to Make Coprime Products
# https://leetcode.com/problems/split-the-array-to-make-coprime-products/

from typing import List


class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        first = {}
        last = {}

        def factorize(x: int, idx: int) -> None:
            p = 2
            while p * p <= x:
                if x % p == 0:
                    if p not in first:
                        first[p] = idx
                    last[p] = idx
                    while x % p == 0:
                        x //= p
                p += 1
            if x > 1:
                if x not in first:
                    first[x] = idx
                last[x] = idx

        n = len(nums)
        for i, num in enumerate(nums):
            factorize(num, i)
        far = 0
        for i in range(n - 1):
            x = nums[i]
            p = 2
            while p * p <= x:
                if x % p == 0:
                    if last[p] > far:
                        far = last[p]
                    while x % p == 0:
                        x //= p
                p += 1
            if x > 1 and last[x] > far:
                far = last[x]
            if far == i:
                return i
        return -1
''')

add("2585_number_of_ways_to_earn_points", r'''# LeetCode 2585 - Number of Ways to Earn Points
# https://leetcode.com/problems/number-of-ways-to-earn-points/

from typing import List


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 1000000007
        dp = [0] * (target + 1)
        dp[0] = 1
        for count, marks in types:
            for s in range(target, -1, -1):
                k = 1
                while k <= count and s - k * marks >= 0:
                    dp[s] = (dp[s] + dp[s - k * marks]) % MOD
                    k += 1
        return dp[target]
''')

add("2586_count_the_number_of_vowel_strings_in_range", r'''# LeetCode 2586 - Count the Number of Vowel Strings in Range
# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        def is_v(c: str) -> bool:
            return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"

        ans = 0
        for i in range(left, right + 1):
            w = words[i]
            if is_v(w[0]) and is_v(w[-1]):
                ans += 1
        return ans
''')

add("2587_rearrange_array_to_maximize_prefix_score", r'''# LeetCode 2587 - Rearrange Array to Maximize Prefix Score
# https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            s += nums[i]
            if s > 0:
                ans += 1
            else:
                break
        return ans
''')

add("2588_count_the_number_of_beautiful_subarrays", r'''# LeetCode 2588 - Count the Number of Beautiful Subarrays
# https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        freq = {0: 1}
        xorv = 0
        ans = 0
        for x in nums:
            xorv ^= x
            ans += freq.get(xorv, 0)
            freq[xorv] = freq.get(xorv, 0) + 1
        return ans
''')

add("2589_minimum_time_to_complete_all_tasks", r'''# LeetCode 2589 - Minimum Time to Complete All Tasks
# https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1])
        on = [False] * 2001
        ans = 0
        for start, end, dur in tasks:
            have = 0
            for i in range(start, end + 1):
                if on[i]:
                    have += 1
            need = dur - have
            i = end
            while i >= start and need > 0:
                if not on[i]:
                    on[i] = True
                    need -= 1
                    ans += 1
                i -= 1
        return ans
''')

add("2590_design_a_todo_list", r'''# LeetCode 2590 - Design a Todo List
# https://leetcode.com/problems/design-a-todo-list/

from typing import List


class TodoList:
    def __init__(self):
        self.nextID = 1
        self.tasks = {}
        self.users = {}

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        tid = self.nextID
        self.nextID += 1
        self.tasks[tid] = {
            "id": tid,
            "description": taskDescription,
            "dueDate": dueDate,
            "userId": userId,
            "tags": set(tags),
            "done": False,
        }
        if userId not in self.users:
            self.users[userId] = []
        self.users[userId].append(tid)
        return tid

    def getAllTasks(self, userId: int) -> List[str]:
        if userId not in self.users:
            return []
        ids = self.users[userId][:]
        ids.sort(key=lambda i: self.tasks[i]["dueDate"])
        ans = []
        for tid in ids:
            if not self.tasks[tid]["done"]:
                ans.append(self.tasks[tid]["description"])
        return ans

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        if userId not in self.users:
            return []
        ids = self.users[userId][:]
        ids.sort(key=lambda i: self.tasks[i]["dueDate"])
        ans = []
        for tid in ids:
            tk = self.tasks[tid]
            if not tk["done"] and tag in tk["tags"]:
                ans.append(tk["description"])
        return ans

    def completeTask(self, userId: int, taskId: int) -> None:
        tk = self.tasks.get(taskId)
        if not tk or tk["userId"] != userId or tk["done"]:
            return
        tk["done"] = True
''')

add("2591_distribute_money_to_maximum_children", r'''# LeetCode 2591 - Distribute Money to Maximum Children
# https://leetcode.com/problems/distribute-money-to-maximum-children/

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        ans = money // 7
        if ans > children:
            ans = children
        remain_money = money - ans * 7
        remain_child = children - ans
        if remain_child == 0 and remain_money > 0:
            ans -= 1
        elif remain_child == 1 and remain_money == 3:
            ans -= 1
        if ans < 0:
            return 0
        return ans
''')

add("2592_maximize_greatness_of_an_array", r'''# LeetCode 2592 - Maximize Greatness of an Array
# https://leetcode.com/problems/maximize-greatness-of-an-array/

from typing import List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for x in nums:
            if x > nums[i]:
                i += 1
        return i
''')

add("2593_find_score_of_an_array_after_marking_all_elements", r'''# LeetCode 2593 - Find Score of an Array After Marking All Elements
# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        idx = list(range(n))
        idx.sort(key=lambda i: (nums[i], i))
        marked = [False] * n
        ans = 0
        for i in idx:
            if marked[i]:
                continue
            ans += nums[i]
            marked[i] = True
            if i - 1 >= 0:
                marked[i - 1] = True
            if i + 1 < n:
                marked[i + 1] = True
        return ans
''')

add("2594_minimum_time_to_repair_cars", r'''# LeetCode 2594 - Minimum Time to Repair Cars
# https://leetcode.com/problems/minimum-time-to-repair-cars/

from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        mn = min(ranks)
        lo, hi = 1, mn * cars * cars

        def ok(t: int) -> bool:
            done = 0
            for r in ranks:
                l, h = 0, cars
                while l < h:
                    mid = (l + h + 1) // 2
                    if r * mid * mid <= t:
                        l = mid
                    else:
                        h = mid - 1
                done += l
                if done >= cars:
                    return True
            return done >= cars

        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
''')

add("2595_number_of_even_and_odd_bits", r'''# LeetCode 2595 - Number of Even and Odd Bits
# https://leetcode.com/problems/number-of-even-and-odd-bits/

from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        i = 0
        while n > 0:
            if (n & 1) != 0:
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
            i += 1
            n >>= 1
        return [even, odd]
''')

add("2596_check_knight_tour_configuration", r'''# LeetCode 2596 - Check Knight Tour Configuration
# https://leetcode.com/problems/check-knight-tour-configuration/

from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        if grid[0][0] != 0:
            return False
        pos = [None] * (n * n)
        for i in range(n):
            for j in range(n):
                pos[grid[i][j]] = [i, j]
        dirs = [
            [1, 2], [1, -2], [-1, 2], [-1, -2],
            [2, 1], [2, -1], [-2, 1], [-2, -1],
        ]
        for v in range(n * n - 1):
            r, c = pos[v]
            ok = False
            for dr, dc in dirs:
                if r + dr == pos[v + 1][0] and c + dc == pos[v + 1][1]:
                    ok = True
                    break
            if not ok:
                return False
        return True
''')

add("2597_the_number_of_beautiful_subsets", r'''# LeetCode 2597 - The Number of Beautiful Subsets
# https://leetcode.com/problems/the-number-of-beautiful-subsets/

from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        groups = {}
        for key in freq:
            rem = key % k
            if rem not in groups:
                groups[rem] = []
            groups[rem].append(key)
        ans = 1
        for vals in groups.values():
            vals.sort()
            prev_take = 0
            prev_skip = 1
            prev_val = float("-inf")
            for v in vals:
                ways = 1
                for _ in range(freq[v]):
                    ways *= 2
                ways -= 1
                skip = prev_take + prev_skip
                take = ways * prev_skip
                if prev_val + k != v:
                    take += ways * prev_take
                prev_take = take
                prev_skip = skip
                prev_val = v
            ans *= prev_take + prev_skip
        return ans - 1
''')

add("2598_smallest_missing_non_negative_integer_after_operations", r'''# LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = [0] * value
        for x in nums:
            r = x % value
            if r < 0:
                r += value
            cnt[r] += 1
        mex = 0
        while cnt[mex % value] > 0:
            cnt[mex % value] -= 1
            mex += 1
        return mex
''')

add("2599_make_the_prefix_sum_non_negative", r'''# LeetCode 2599 - Make the Prefix Sum Non-negative
# https://leetcode.com/problems/make-the-prefix-sum-non-negative/

import heapq
from typing import List


class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        h = []
        s = 0
        ans = 0
        for x in nums:
            s += x
            if x < 0:
                heapq.heappush(h, x)
            if s < 0:
                worst = heapq.heappop(h)
                s -= worst
                ans += 1
        return ans
''')

add("2600_k_items_with_the_maximum_sum", r'''# LeetCode 2600 - K Items With the Maximum Sum
# https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        take = min(numOnes, k)
        ans += take
        k -= take
        take = min(numZeros, k)
        k -= take
        take = min(numNegOnes, k)
        ans -= take
        return ans
''')

add("2601_prime_subtraction_operation", r'''# LeetCode 2601 - Prime Subtraction Operation
# https://leetcode.com/problems/prime-subtraction-operation/

from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        max_v = 0
        for x in nums:
            if x > max_v:
                max_v = x
        is_p = [True] * (max_v + 1)
        if max_v >= 0:
            is_p[0] = False
        if max_v >= 1:
            is_p[1] = False
        i = 2
        while i * i <= max_v:
            if is_p[i]:
                for j in range(i * i, max_v + 1, i):
                    is_p[j] = False
            i += 1
        primes = [i for i in range(2, max_v + 1) if is_p[i]]
        prev = 0
        for x in nums:
            need = x - prev
            best = -1
            for p in primes:
                if p >= need:
                    break
                best = p
            cur = x if best < 0 else x - best
            if cur <= prev:
                return False
            prev = cur
        return True
''')

add("2602_minimum_operations_to_make_all_array_elements_equal", r'''# LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
# https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        def lower_bound(x: int) -> int:
            lo, hi = 0, n
            while lo < hi:
                mid = (lo + hi) >> 1
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        ans = [0] * len(queries)
        for qi, q in enumerate(queries):
            i = lower_bound(q)
            left = q * i - pref[i]
            right = pref[n] - pref[i] - q * (n - i)
            ans[qi] = left + right
        return ans
''')

add("2603_collect_coins_in_a_tree", r'''# LeetCode 2603 - Collect Coins in a Tree
# https://leetcode.com/problems/collect-coins-in-a-tree/

from collections import deque
from typing import List


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = [set() for _ in range(n)]
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        deg = [len(g[i]) for i in range(n)]
        q = deque()
        for i in range(n):
            if deg[i] == 1 and coins[i] == 0:
                q.append(i)
        while q:
            u = q.popleft()
            for v in list(g[u]):
                g[v].discard(u)
                deg[v] -= 1
                if deg[v] == 1 and coins[v] == 0:
                    q.append(v)
            g[u].clear()
            deg[u] = 0
        for _ in range(2):
            leaves = [i for i in range(n) if deg[i] == 1]
            for u in leaves:
                for v in list(g[u]):
                    g[v].discard(u)
                    deg[v] -= 1
                g[u].clear()
                deg[u] = 0
        remain = 0
        for i in range(n):
            remain += len(g[i])
        return remain
''')

add("2604_minimum_time_to_eat_all_grains", r'''# LeetCode 2604 - Minimum Time to Eat All Grains
# https://leetcode.com/problems/minimum-time-to-eat-all-grains/

from typing import List


class Solution:
    def minimumTime(self, hens: List[int], grains: List[int]) -> int:
        hens.sort()
        grains.sort()

        def ok(t: int) -> bool:
            j = 0
            for h in hens:
                if j >= len(grains):
                    return True
                if grains[j] >= h:
                    while j < len(grains) and grains[j] - h <= t:
                        j += 1
                else:
                    if h - grains[j] > t:
                        return False
                    left = h - grains[j]
                    max_right1 = t - 2 * left
                    max_right2 = (t - left) // 2
                    reach = h
                    if max_right1 > max_right2:
                        if max_right1 > 0:
                            reach = h + max_right1
                    else:
                        if max_right2 > 0:
                            reach = h + max_right2
                    while j < len(grains) and grains[j] <= reach:
                        j += 1
            return j >= len(grains)

        lo, hi = 0, 2000000000
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
''')

add("2605_form_smallest_number_from_two_digit_arrays", r'''# LeetCode 2605 - Form Smallest Number From Two Digit Arrays
# https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = set(nums1), set(nums2)
        common = 10
        for x in s1:
            if x in s2 and x < common:
                common = x
        if common < 10:
            return common
        a = min(nums1)
        b = min(nums2)
        return min(a * 10 + b, b * 10 + a)
''')

add("2606_find_the_substring_with_maximum_cost", r'''# LeetCode 2606 - Find the Substring With Maximum Cost
# https://leetcode.com/problems/find-the-substring-with-maximum-cost/

from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        val = [i + 1 for i in range(26)]
        for i, ch in enumerate(chars):
            val[ord(ch) - 97] = vals[i]
        best = 0
        cur = 0
        for c in s:
            cur += val[ord(c) - 97]
            if cur < 0:
                cur = 0
            if cur > best:
                best = cur
        return best
''')

add("2607_make_k_subarray_sums_equal", r'''# LeetCode 2607 - Make K-Subarray Sums Equal
# https://leetcode.com/problems/make-k-subarray-sums-equal/

from typing import List


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        n = len(arr)
        g = gcd(n, k)
        ans = 0
        for r in range(g):
            group = [arr[i] for i in range(r, n, g)]
            group.sort()
            med = group[len(group) // 2]
            for x in group:
                ans += abs(x - med)
        return ans
''')

add("2608_shortest_cycle_in_a_graph", r'''# LeetCode 2608 - Shortest Cycle in a Graph
# https://leetcode.com/problems/shortest-cycle-in-a-graph/

from collections import deque
from typing import List


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        INF = 1000000000
        ans = INF
        for start in range(n):
            dist = [-1] * n
            parent = [-1] * n
            q = deque([start])
            dist[start] = 0
            while q:
                u = q.popleft()
                for v in g[u]:
                    if dist[v] < 0:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v:
                        c = dist[u] + dist[v] + 1
                        if c < ans:
                            ans = c
        return -1 if ans == INF else ans
''')

add("2609_find_the_longest_balanced_substring_of_a_binary_string", r'''# LeetCode 2609 - Find the Longest Balanced Substring of a Binary String
# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        zeros = 0
        ones = 0
        for c in s:
            if c == "0":
                if ones > 0:
                    zeros = ones = 0
                zeros += 1
            else:
                ones += 1
                cur = min(ones, zeros)
                if 2 * cur > ans:
                    ans = 2 * cur
        return ans
''')

add("2610_convert_an_array_into_a_2d_array_with_conditions", r'''# LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = {}
        ans = []
        for x in nums:
            f = freq.get(x, 0)
            if f == len(ans):
                ans.append([])
            ans[f].append(x)
            freq[x] = f + 1
        return ans
''')

add("2611_mice_and_cheese", r'''# LeetCode 2611 - Mice and Cheese
# https://leetcode.com/problems/mice-and-cheese/

from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        diff = [0] * n
        ans = 0
        for i in range(n):
            ans += reward2[i]
            diff[i] = reward1[i] - reward2[i]
        diff.sort(reverse=True)
        for i in range(k):
            ans += diff[i]
        return ans
''')

add("2612_minimum_reverse_operations", r'''# LeetCode 2612 - Minimum Reverse Operations
# https://leetcode.com/problems/minimum-reverse-operations/

from collections import deque
from typing import List


class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ban = set(banned)
        ans = [-1] * n
        ans[p] = 0
        q = deque([(p, 0)])
        while q:
            i, d = q.popleft()
            lo = i - (k - 1)
            if lo < 0:
                lo = 0
            hi = i
            if hi > n - k:
                hi = n - k
            for L in range(lo, hi + 1):
                R = L + k - 1
                ni = L + R - i
                if ni < 0 or ni >= n or ni in ban or ans[ni] != -1:
                    continue
                ans[ni] = d + 1
                q.append((ni, d + 1))
        return ans
''')

add("2613_beautiful_pairs", r'''# LeetCode 2613 - Beautiful Pairs
# https://leetcode.com/problems/beautiful-pairs/

from typing import List


class Solution:
    def beautifulPair(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        best = float("inf")
        ans = [0, 1]
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(nums1[i] - nums1[j]) + abs(nums2[i] - nums2[j])
                if d < best or (d == best and (i < ans[0] or (i == ans[0] and j < ans[1]))):
                    best = d
                    ans = [i, j]
        return ans
''')

add("2614_prime_in_diagonal", r'''# LeetCode 2614 - Prime In Diagonal
# https://leetcode.com/problems/prime-in-diagonal/

from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        n = len(nums)
        best = 0
        for i in range(n):
            a, b = nums[i][i], nums[i][n - 1 - i]
            if is_prime(a) and a > best:
                best = a
            if is_prime(b) and b > best:
                best = b
        return best
''')

add("2615_sum_of_distances", r'''# LeetCode 2615 - Sum of Distances
# https://leetcode.com/problems/sum-of-distances/

from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pos = {}
        for i, x in enumerate(nums):
            if x not in pos:
                pos[x] = []
            pos[x].append(i)
        for idxs in pos.values():
            m = len(idxs)
            pref = [0] * (m + 1)
            for i in range(m):
                pref[i + 1] = pref[i] + idxs[i]
            for j in range(m):
                idx = idxs[j]
                left = j * idx - pref[j]
                right = pref[m] - pref[j + 1] - (m - 1 - j) * idx
                ans[idx] = left + right
        return ans
''')

add("2616_minimize_the_maximum_difference_of_pairs", r'''# LeetCode 2616 - Minimize the Maximum Difference of Pairs
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]

        def ok(d: int) -> bool:
            cnt = 0
            i = 0
            while i + 1 < len(nums):
                if nums[i + 1] - nums[i] <= d:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p

        while lo < hi:
            mid = (lo + hi) >> 1
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
''')

add("2617_minimum_number_of_visited_cells_in_a_grid", r'''# LeetCode 2617 - Minimum Number of Visited Cells in a Grid
# https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

from collections import deque
from typing import List


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[-1] * n for _ in range(m)]
        q = deque([(0, 0)])
        dist[0][0] = 1
        while q:
            r, c = q.popleft()
            if r == m - 1 and c == n - 1:
                return dist[r][c]
            nc = c + 1
            while nc <= c + grid[r][c] and nc < n:
                if dist[r][nc] == -1:
                    dist[r][nc] = dist[r][c] + 1
                    q.append((r, nc))
                nc += 1
            nr = r + 1
            while nr <= r + grid[r][c] and nr < m:
                if dist[nr][c] == -1:
                    dist[nr][c] = dist[r][c] + 1
                    q.append((nr, c))
                nr += 1
        return -1
''')

add("2618_check_if_object_instance_of_class", r'''# LeetCode 2618 - Check if Object Instance of Class
# https://leetcode.com/problems/check-if-object-instance-of-class/

from typing import Any


class Solution:
    def checkIfInstanceOf(self, obj: Any, classFunction: Any) -> bool:
        if obj is None or not isinstance(classFunction, type):
            return False
        try:
            return isinstance(obj, classFunction)
        except TypeError:
            return False
''')

add("2619_array_prototype_last", r'''# LeetCode 2619 - Array Prototype Last
# https://leetcode.com/problems/array-prototype-last/

from typing import Any, List


class Solution:
    def last(self, nums: List[Any]) -> Any:
        if len(nums) == 0:
            return -1
        return nums[-1]
''')

add("2620_counter", r'''# LeetCode 2620 - Counter
# https://leetcode.com/problems/counter/

from typing import Callable


class Solution:
    def createCounter(self, n: int) -> Callable[[], int]:
        def counter() -> int:
            nonlocal n
            v = n
            n += 1
            return v

        return counter
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
