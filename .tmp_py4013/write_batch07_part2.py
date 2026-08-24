#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2779_maximum_beauty_of_an_array_after_applying_operation"] = r'''# LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            ans = max(ans, right - left + 1)
        return ans
'''

FILES["2780_minimum_index_of_a_valid_split"] = r'''# LeetCode 2780 - Minimum Index of a Valid Split
# https://leetcode.com/problems/minimum-index-of-a-valid-split/

from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = {}
        dom = 0
        best = 0
        for v in nums:
            c = freq.get(v, 0) + 1
            freq[v] = c
            if c > best:
                best = c
                dom = v
        left = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == dom:
                left += 1
            right = best - left
            if left * 2 > i + 1 and right * 2 > n - i - 1:
                return i
        return -1
'''

FILES["2781_length_of_the_longest_valid_substring"] = r'''# LeetCode 2781 - Length of the Longest Valid Substring
# https://leetcode.com/problems/length-of-the-longest-valid-substring/

from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbid = set(forbidden)
        max_len = 0
        for f in forbidden:
            max_len = max(max_len, len(f))
        ans = 0
        right = len(word) - 1
        for left in range(len(word) - 1, -1, -1):
            for k in range(left, right + 1):
                if k - left + 1 > max_len:
                    break
                if word[left : k + 1] in forbid:
                    right = k - 1
                    break
            ans = max(ans, right - left + 1)
        return ans
'''

FILES["2782_number_of_unique_categories"] = r'''# LeetCode 2782 - Number of Unique Categories
# https://leetcode.com/problems/number-of-unique-categories/


class Solution:
    def numberOfCategories(self, n: int, categoryHandler) -> int:
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(n):
            for j in range(i + 1, n):
                if categoryHandler.haveSameCategory(i, j):
                    a, b = find(i), find(j)
                    if a != b:
                        parent[a] = b
        return sum(1 for i in range(n) if find(i) == i)
'''

FILES["2784_check_if_array_is_good"] = r'''# LeetCode 2784 - Check if Array is Good
# https://leetcode.com/problems/check-if-array-is-good/

from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        if n < 1:
            return False
        freq = [0] * (n + 1)
        for v in nums:
            if v < 1 or v > n:
                return False
            freq[v] += 1
        for i in range(1, n):
            if freq[i] != 1:
                return False
        return freq[n] == 2
'''

FILES["2785_sort_vowels_in_a_string"] = r'''# LeetCode 2785 - Sort Vowels in a String
# https://leetcode.com/problems/sort-vowels-in-a-string/


class Solution:
    def sortVowels(self, s: str) -> str:
        def is_vowel(c: str) -> bool:
            return c in "aeiouAEIOU"

        vowels = [c for c in s if is_vowel(c)]
        vowels.sort()
        arr = list(s)
        vi = 0
        for i, c in enumerate(arr):
            if is_vowel(c):
                arr[i] = vowels[vi]
                vi += 1
        return "".join(arr)
'''

FILES["2786_visit_array_positions_to_maximize_score"] = r'''# LeetCode 2786 - Visit Array Positions to Maximize Score
# https://leetcode.com/problems/visit-array-positions-to-maximize-score/

from typing import List


class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        NEG = -10**18
        even = odd = nums[0]
        if nums[0] % 2 == 0:
            odd = NEG
        else:
            even = NEG
        for i in range(1, len(nums)):
            v = nums[i]
            if v % 2 == 0:
                even = max(even + v, odd + v - x)
            else:
                odd = max(odd + v, even + v - x)
        return max(even, odd)
'''

FILES["2787_ways_to_express_an_integer_as_sum_of_powers"] = r'''# LeetCode 2787 - Ways to Express an Integer as Sum of Powers
# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 1000000007
        powers = []
        i = 1
        while True:
            p = 1
            for _ in range(x):
                p *= i
                if p > n:
                    break
            if p > n:
                break
            powers.append(p)
            i += 1
        dp = [0] * (n + 1)
        dp[0] = 1
        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD
        return dp[n]
'''

FILES["2788_split_strings_by_separator"] = r'''# LeetCode 2788 - Split Strings by Separator
# https://leetcode.com/problems/split-strings-by-separator/

from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for w in words:
            start = 0
            for i in range(len(w) + 1):
                if i == len(w) or w[i] == separator:
                    if i > start:
                        ans.append(w[start:i])
                    start = i + 1
        return ans
'''

FILES["2789_largest_element_in_an_array_after_merge_operations"] = r'''# LeetCode 2789 - Largest Element in an Array after Merge Operations
# https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

from typing import List


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        cur = nums[n - 1]
        ans = cur
        for i in range(n - 2, -1, -1):
            if nums[i] <= cur:
                cur += nums[i]
            else:
                cur = nums[i]
            ans = max(ans, cur)
        return ans
'''

FILES["2790_maximum_number_of_groups_with_increasing_length"] = r'''# LeetCode 2790 - Maximum Number of Groups With Increasing Length
# https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

from typing import List


class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        arr = sorted(usageLimits)
        ans = 0
        total = 0
        for v in arr:
            total += v
            need = (ans + 1) * (ans + 2) / 2
            if total >= need:
                ans += 1
        return ans
'''

FILES["2791_count_paths_that_can_form_a_palindrome_in_a_tree"] = r'''# LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
# https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

from typing import List


class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
        freq = {0: 1}
        ans = 0

        def dfs(u: int, mask: int) -> None:
            nonlocal ans
            for v in g[u]:
                nm = mask ^ (1 << (ord(s[v]) - 97))
                ans += freq.get(nm, 0)
                for b in range(26):
                    ans += freq.get(nm ^ (1 << b), 0)
                freq[nm] = freq.get(nm, 0) + 1
                dfs(v, nm)

        dfs(0, 0)
        return ans
'''

FILES["2792_count_nodes_that_are_great_enough"] = r'''# LeetCode 2792 - Count Nodes That Are Great Enough
# https://leetcode.com/problems/count-nodes-that-are-great-enough/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countGreatEnoughNodes(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> List[int]:
            nonlocal ans
            if not node:
                return []
            vals = [node.val] + dfs(node.left) + dfs(node.right)
            smaller = sum(1 for v in vals if v < node.val)
            if smaller >= k:
                ans += 1
            return vals

        dfs(root)
        return ans
'''

FILES["2794_create_object_from_two_arrays"] = r'''# LeetCode 2794 - Create Object from Two Arrays
# https://leetcode.com/problems/create-object-from-two-arrays/

from typing import Any, Dict, List


class Solution:
    def createObject(self, keysArr: List[Any], valuesArr: List[Any]) -> Dict[Any, Any]:
        output = {}
        n = min(len(keysArr), len(valuesArr))
        for i in range(n):
            if keysArr[i] not in output:
                output[keysArr[i]] = valuesArr[i]
        return output
'''

FILES["2795_parallel_execution_of_promises_for_individual_results_retrieval"] = r'''# LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
# https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/

import asyncio
from typing import Callable, List


class Solution:
    def promiseAllSettled(self, functions: List[Callable]):
        async def run_one(fn: Callable):
            try:
                value = fn()
                if hasattr(value, "__await__"):
                    value = await value
                return {"status": "fulfilled", "value": value}
            except Exception as reason:
                return {"status": "rejected", "reason": reason}

        async def run_all():
            return await asyncio.gather(*(run_one(fn) for fn in functions))

        return run_all()
'''

FILES["2796_repeat_string"] = r'''# LeetCode 2796 - Repeat String
# https://leetcode.com/problems/repeat-string/


class Solution:
    def replicate(self, s: str, times: int) -> str:
        res = ""
        for _ in range(times):
            res += s
        return res
'''

FILES["2797_partial_function_with_placeholders"] = r'''# LeetCode 2797 - Partial Function with Placeholders
# https://leetcode.com/problems/partial-function-with-placeholders/

from typing import Any, Callable, List


class Solution:
    def partial(self, fn: Callable, args: List[Any]) -> Callable:
        def wrapped(*rest_args):
            full = []
            ri = 0
            for a in args:
                if a == "_":
                    if ri < len(rest_args):
                        full.append(rest_args[ri])
                        ri += 1
                else:
                    full.append(a)
            while ri < len(rest_args):
                full.append(rest_args[ri])
                ri += 1
            return fn(*full)

        return wrapped
'''

FILES["2798_number_of_employees_who_met_the_target"] = r'''# LeetCode 2798 - Number of Employees Who Met the Target
# https://leetcode.com/problems/number-of-employees-who-met-the-target/

from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        for h in hours:
            if h >= target:
                ans += 1
        return ans
'''

FILES["2799_count_complete_subarrays_in_an_array"] = r'''# LeetCode 2799 - Count Complete Subarrays in an Array
# https://leetcode.com/problems/count-complete-subarrays-in-an-array/

from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        need = len(set(nums))
        ans = 0
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                if len(seen) == need:
                    ans += n - j
                    break
        return ans
'''

FILES["2800_shortest_string_that_contains_three_strings"] = r'''# LeetCode 2800 - Shortest String That Contains Three Strings
# https://leetcode.com/problems/shortest-string-that-contains-three-strings/


class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(x: str, y: str) -> str:
            if y in x:
                return x
            best = x + y
            n = min(len(x), len(y))
            for i in range(n, 0, -1):
                if x[-i:] == y[:i]:
                    cand = x + y[i:]
                    if len(cand) < len(best) or (len(cand) == len(best) and cand < best):
                        best = cand
                    break
            return best

        perms = [
            [a, b, c],
            [a, c, b],
            [b, a, c],
            [b, c, a],
            [c, a, b],
            [c, b, a],
        ]
        ans = ""
        for p in perms:
            cur = merge(merge(p[0], p[1]), p[2])
            if not ans or len(cur) < len(ans) or (len(cur) == len(ans) and cur < ans):
                ans = cur
        return ans
'''

FILES["2801_count_stepping_numbers_in_range"] = r'''# LeetCode 2801 - Count Stepping Numbers in Range
# https://leetcode.com/problems/count-stepping-numbers-in-range/


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 1000000007

        def dec(s: str) -> str:
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == "0":
                arr[i] = "9"
                i -= 1
            if i >= 0:
                arr[i] = chr(ord(arr[i]) - 1)
            j = 0
            while j < len(arr) - 1 and arr[j] == "0":
                j += 1
            return "".join(arr[j:])

        def count_to(s: str) -> int:
            memo = [
                [[[-1] * 2 for _ in range(11)] for _ in range(2)] for _ in range(85)
            ]

            def dfs(pos: int, tight: int, last: int, started: int) -> int:
                if pos == len(s):
                    return started
                if memo[pos][tight][last + 1][started] != -1:
                    return memo[pos][tight][last + 1][started]
                up = ord(s[pos]) - 48 if tight else 9
                ans = 0
                for d in range(up + 1):
                    nt = 1 if tight and d == up else 0
                    if not started:
                        if d == 0:
                            ans += dfs(pos + 1, nt, -1, 0)
                        else:
                            ans += dfs(pos + 1, nt, d, 1)
                    elif abs(d - last) == 1:
                        ans += dfs(pos + 1, nt, d, 1)
                memo[pos][tight][last + 1][started] = ans % MOD
                return memo[pos][tight][last + 1][started]

            return dfs(0, 1, -1, 0)

        ans = (count_to(high) - count_to(dec(low))) % MOD
        if ans < 0:
            ans += MOD
        return ans
'''

FILES["2802_find_the_k_th_lucky_number"] = r'''# LeetCode 2802 - Find The K-th Lucky Number
# https://leetcode.com/problems/find-the-k-th-lucky-number/


class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        k += 1
        bits = ""
        while k > 1:
            if k % 2 == 0:
                bits = "4" + bits
            else:
                bits = "7" + bits
            k //= 2
        return bits
'''

FILES["2803_factorial_generator"] = r'''# LeetCode 2803 - Factorial Generator
# https://leetcode.com/problems/factorial-generator/

from typing import Generator


class Solution:
    def factorialGenerator(self, n: int) -> Generator[int, None, None]:
        cur = 1
        for i in range(1, n + 1):
            cur *= i
            yield cur
'''

FILES["2804_array_prototype_foreach"] = r'''# LeetCode 2804 - Array Prototype ForEach
# https://leetcode.com/problems/array-prototype-foreach/

from typing import Any, Callable, List, Optional


class Solution:
    def forEach(self, arr: List[Any], callback: Callable, context: Optional[Any] = None) -> None:
        for i, val in enumerate(arr):
            if context is None:
                callback(val, i, arr)
            else:
                callback(val, i, arr)
'''

FILES["2805_custom_interval"] = r'''# LeetCode 2805 - Custom Interval
# https://leetcode.com/problems/custom-interval/

import threading
from typing import Callable, Dict


class Solution:
    _next_id = 1
    _timers: Dict[int, threading.Timer] = {}
    _cancelled: Dict[int, Callable] = {}

    def customInterval(self, fn: Callable, delay: int, period: int) -> int:
        count = 0
        cancelled = False
        Solution._next_id += 1
        interval_id = Solution._next_id

        def schedule() -> None:
            nonlocal count

            def fire() -> None:
                nonlocal count
                if cancelled:
                    return
                fn()
                count += 1
                schedule()

            t = threading.Timer((delay + period * count) / 1000.0, fire)
            Solution._timers[interval_id] = t
            t.daemon = True
            t.start()

        def cancel() -> None:
            nonlocal cancelled
            cancelled = True
            t = Solution._timers.get(interval_id)
            if t:
                t.cancel()

        Solution._cancelled[interval_id] = cancel
        schedule()
        return interval_id

    def customClearInterval(self, interval_id: int) -> None:
        cancel = Solution._cancelled.get(interval_id)
        if cancel:
            cancel()
'''

FILES["2806_account_balance_after_rounded_purchase"] = r'''# LeetCode 2806 - Account Balance After Rounded Purchase
# https://leetcode.com/problems/account-balance-after-rounded-purchase/


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        r = ((purchaseAmount + 5) // 10) * 10
        return 100 - r
'''

FILES["2807_insert_greatest_common_divisors_in_linked_list"] = r'''# LeetCode 2807 - Insert Greatest Common Divisors in Linked List
# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        cur = head
        while cur and cur.next:
            g = gcd(cur.val, cur.next.val)
            node = ListNode(g, cur.next)
            cur.next = node
            cur = node.next
        return head
'''

FILES["2808_minimum_seconds_to_equalize_a_circular_array"] = r'''# LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
# https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

from typing import List


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        pos = {}
        for i, v in enumerate(nums):
            pos.setdefault(v, []).append(i)
        ans = n
        for p in pos.values():
            max_gap = 0
            for i in range(len(p)):
                gap = p[i + 1] - p[i] if i + 1 < len(p) else p[0] + n - p[i]
                max_gap = max(max_gap, gap // 2)
            ans = min(ans, max_gap)
        return ans
'''

FILES["2809_minimum_time_to_make_array_sum_at_most_x"] = r'''# LeetCode 2809 - Minimum Time to Make Array Sum At Most x
# https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

from typing import List


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        arr = [[nums1[i], nums2[i]] for i in range(n)]
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        arr.sort(key=lambda p: p[1])
        dp = [0] * (n + 1)
        for i in range(n):
            for j in range(i + 1, 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + arr[i][0] + j * arr[i][1])
        for t in range(n + 1):
            if sum1 + sum2 * t - dp[t] <= x:
                return t
        return -1
'''

FILES["2810_faulty_keyboard"] = r'''# LeetCode 2810 - Faulty Keyboard
# https://leetcode.com/problems/faulty-keyboard/


class Solution:
    def finalString(self, s: str) -> str:
        b = ""
        for c in s:
            if c == "i":
                b = b[::-1]
            else:
                b += c
        return b
'''

FILES["2811_check_if_it_is_possible_to_split_array"] = r'''# LeetCode 2811 - Check if it is Possible to Split Array
# https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

from typing import List


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        for i in range(n - 1):
            if nums[i] + nums[i + 1] >= m:
                return True
        return False
'''

FILES["2812_find_the_safest_path_in_a_grid"] = r'''# LeetCode 2812 - Find the Safest Path in a Grid
# https://leetcode.com/problems/find-the-safest-path-in-a-grid/

from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        h = 0
        while h < len(q):
            x, y = q[h]
            h += 1
            for dx, dy in dirs:
                ni, nj = x + dx, y + dy
                if 0 <= ni < n and 0 <= nj < n and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[x][y] + 1
                    q.append((ni, nj))

        def ok(sf: int) -> bool:
            if dist[0][0] < sf:
                return False
            seen = [[False] * n for _ in range(n)]
            st = [(0, 0)]
            seen[0][0] = True
            while st:
                x, y = st.pop()
                if x == n - 1 and y == n - 1:
                    return True
                for dx, dy in dirs:
                    ni, nj = x + dx, y + dy
                    if 0 <= ni < n and 0 <= nj < n and not seen[ni][nj] and dist[ni][nj] >= sf:
                        seen[ni][nj] = True
                        st.append((ni, nj))
            return False

        lo, hi, ans = 0, n * n, 0
        while lo <= hi:
            mid = (lo + hi) >> 1
            if ok(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
'''

FILES["2813_maximum_elegance_of_a_k_length_subsequence"] = r'''# LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
# https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

from typing import List


class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda it: -it[0])
        seen = set()
        total = 0
        dup = []
        for i in range(k):
            total += items[i][0]
            c = items[i][1]
            if c in seen:
                dup.append(items[i][0])
            else:
                seen.add(c)
        ans = total + len(seen) * len(seen)
        for i in range(k, len(items)):
            c = items[i][1]
            if c in seen or not dup:
                continue
            total += items[i][0] - dup.pop()
            seen.add(c)
            ans = max(ans, total + len(seen) * len(seen))
        return ans
'''

FILES["2814_minimum_time_takes_to_reach_destination_without_drowning"] = r'''# LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
# https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

from typing import List


class Solution:
    def minimumSeconds(self, land: List[List[str]]) -> int:
        m, n = len(land), len(land[0])
        INF = 10**9
        water = [[INF] * n for _ in range(m)]
        wq = []
        sx = sy = dx = dy = 0
        for i in range(m):
            for j in range(n):
                cell = land[i][j]
                if cell == "*":
                    water[i][j] = 0
                    wq.append((i, j))
                elif cell == "S":
                    sx, sy = i, j
                elif cell == "D":
                    dx, dy = i, j
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        h = 0
        while h < len(wq):
            x, y = wq[h]
            h += 1
            for ddx, ddy in dirs:
                ni, nj = x + ddx, y + ddy
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue
                cell = land[ni][nj]
                if cell in ("X", "D"):
                    continue
                if water[ni][nj] > water[x][y] + 1:
                    water[ni][nj] = water[x][y] + 1
                    wq.append((ni, nj))
        dist = [[-1] * n for _ in range(m)]
        q = [(sx, sy)]
        dist[sx][sy] = 0
        h = 0
        while h < len(q):
            x, y = q[h]
            h += 1
            if x == dx and y == dy:
                return dist[x][y]
            for ddx, ddy in dirs:
                ni, nj = x + ddx, y + ddy
                if ni < 0 or nj < 0 or ni >= m or nj >= n or dist[ni][nj] != -1:
                    continue
                if land[ni][nj] == "X":
                    continue
                nd = dist[x][y] + 1
                if land[ni][nj] != "D" and nd >= water[ni][nj]:
                    continue
                dist[ni][nj] = nd
                q.append((ni, nj))
        return -1
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
