from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def write(folder: str, body: str) -> None:
    (ROOT / folder / "solution.py").write_text(body.lstrip("\n"), encoding="utf-8")


write(
    "3484_design_spreadsheet",
    '''
# LeetCode 3484 - Design Spreadsheet
# https://leetcode.com/problems/design-spreadsheet/


class Spreadsheet:
    def __init__(self, rows: int):
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells.pop(cell, None)

    def getValue(self, formula: str) -> int:
        if formula and formula[0] == "=":
            formula = formula[1:]
        total = 0
        start = 0
        while start < len(formula):
            plus = formula.find("+", start)
            p = formula[start:] if plus < 0 else formula[start:plus]
            is_num = bool(p) and ((p[0] >= "0" and p[0] <= "9") or (p[0] == "-" and len(p) > 1))
            if is_num:
                for i in range(1, len(p)):
                    if p[i] < "0" or p[i] > "9":
                        is_num = False
                        break
            if is_num:
                total += int(p)
            else:
                total += self.cells.get(p, 0)
            if plus < 0:
                break
            start = plus + 1
        return total
''',
)

write(
    "3485_longest_common_prefix_of_k_strings_after_removal",
    '''
# LeetCode 3485 - Longest Common Prefix of K Strings After Removal
# https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

from typing import List


class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        def lcp_of(a: List[str]) -> int:
            if not a:
                return 0
            pref = a[0]
            for t in range(1, len(a)):
                s = a[t]
                i = 0
                while i < len(pref) and i < len(s) and pref[i] == s[i]:
                    i += 1
                pref = pref[:i]
                if not pref:
                    return 0
            return len(pref)

        n = len(words)
        ans = [0] * n
        for i in range(n):
            rest = [words[j] for j in range(n) if j != i]
            if len(rest) < k:
                ans[i] = 0
                continue
            rest.sort()
            best = 0
            for j in range(len(rest) - k + 1):
                best = max(best, lcp_of(rest[j : j + k]))
            ans[i] = best
        return ans
''',
)

write(
    "3486_longest_special_path_ii",
    '''
# LeetCode 3486 - Longest Special Path II
# https://leetcode.com/problems/longest-special-path-ii/

from typing import List


class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        best_len, best_nodes = 0, 1

        def dfs(u: int, p: int, dist: int, path_vals: List[int], path_dist: List[int]) -> None:
            nonlocal best_len, best_nodes
            path_vals.append(nums[u])
            path_dist.append(dist)
            freq = {}
            dups = 0
            left = 0
            for right in range(len(path_vals)):
                v = path_vals[right]
                freq[v] = freq.get(v, 0) + 1
                if freq[v] == 2:
                    dups += 1
                while dups > 1:
                    lv = path_vals[left]
                    if freq[lv] == 2:
                        dups -= 1
                    freq[lv] -= 1
                    left += 1
            length = dist - path_dist[left]
            nodes = len(path_vals) - left
            if length > best_len or (length == best_len and nodes < best_nodes):
                best_len = length
                best_nodes = nodes
            for v, w in g[u]:
                if v == p:
                    continue
                dfs(v, u, dist + w, path_vals, path_dist)
            path_vals.pop()
            path_dist.pop()

        dfs(0, -1, 0, [], [])
        return [best_len, best_nodes]
''',
)

write(
    "3487_maximum_unique_subarray_sum_after_deletion",
    '''
# LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = set()
        s = 0
        has_pos = False
        max_neg = -10**9
        for x in nums:
            if x < 0:
                if x > max_neg:
                    max_neg = x
                continue
            has_pos = True
            if x not in seen:
                seen.add(x)
                s += x
        return s if has_pos else max_neg
''',
)

write(
    "3488_closest_equal_element_queries",
    '''
# LeetCode 3488 - Closest Equal Element Queries
# https://leetcode.com/problems/closest-equal-element-queries/

from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos = {}
        for i, x in enumerate(nums):
            if x not in pos:
                pos[x] = []
            pos[x].append(i)
        ans = [0] * len(queries)
        for qi, idx in enumerate(queries):
            x = nums[idx]
            arr = pos[x]
            if len(arr) == 1:
                ans[qi] = -1
                continue
            best = n
            for p in arr:
                if p == idx:
                    continue
                d = abs(p - idx)
                d = min(d, n - d)
                if d < best:
                    best = d
            ans[qi] = best
        return ans
''',
)

write(
    "3489_zero_array_transformation_iv",
    '''
# LeetCode 3489 - Zero Array Transformation IV
# https://leetcode.com/problems/zero-array-transformation-iv/

from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def can_subset_sum(vals: List[int], target: int) -> bool:
            if target == 0:
                return True
            dp = [False] * (target + 1)
            dp[0] = True
            for v in vals:
                for s in range(target, v - 1, -1):
                    if dp[s - v]:
                        dp[s] = True
            return dp[target]

        def ok(k: int) -> bool:
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue
                vals = []
                for q in range(k):
                    l, r, v = queries[q]
                    if l <= i <= r:
                        vals.append(v)
                if not can_subset_sum(vals, nums[i]):
                    return False
            return True

        if ok(0):
            return 0
        lo, hi = 1, len(queries) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mid <= len(queries) and ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return -1 if lo > len(queries) else lo
''',
)

write(
    "3490_count_beautiful_numbers",
    '''
# LeetCode 3490 - Count Beautiful Numbers
# https://leetcode.com/problems/count-beautiful-numbers/


class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        def count_beautiful(n: int) -> int:
            if n <= 0:
                return 0
            s = str(n)

            def dfs(pos: int, tight: bool, sm: int, prod: int, started: bool) -> int:
                if pos == len(s):
                    if not started:
                        return 0
                    return 1 if sm > 0 and prod % sm == 0 else 0
                up = ord(s[pos]) - 48 if tight else 9
                ans = 0
                for d in range(up + 1):
                    nt = tight and d == up
                    if not started and d == 0:
                        ans += dfs(pos + 1, nt, 0, 1, False)
                    else:
                        ns = sm + d
                        np = d if not started else prod * d
                        ans += dfs(pos + 1, nt, ns, np, True)
                return ans

            return dfs(0, True, 0, 1, False)

        return count_beautiful(r) - count_beautiful(l - 1)
''',
)

write(
    "3491_phone_number_prefix",
    '''
# LeetCode 3491 - Phone Number Prefix
# https://leetcode.com/problems/phone-number-prefix/

from typing import List


class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:
        numbers = sorted(numbers)
        for i in range(len(numbers) - 1):
            if len(numbers[i]) <= len(numbers[i + 1]) and numbers[i + 1].startswith(numbers[i]):
                return False
        return True
''',
)

write(
    "3492_maximum_containers_on_a_ship",
    '''
# LeetCode 3492 - Maximum Containers on a Ship
# https://leetcode.com/problems/maximum-containers-on-a-ship/


class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        cap = n * n
        by_w = maxWeight // w
        return cap if cap < by_w else by_w
''',
)

write(
    "3493_properties_graph",
    '''
# LeetCode 3493 - Properties Graph
# https://leetcode.com/problems/properties-graph/

from typing import List


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        sets = [set(row) for row in properties]
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for i in range(n):
            for j in range(i + 1, n):
                cnt = 0
                for v in sets[i]:
                    if v in sets[j]:
                        cnt += 1
                if cnt >= k:
                    unite(i, j)
        comp = set()
        for i in range(n):
            comp.add(find(i))
        return len(comp)
''',
)

write(
    "3494_find_the_minimum_amount_of_time_to_brew_potions",
    '''
# LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        done = [0] * n
        for j in range(m):
            t = 0
            for i in range(n):
                if done[i] > t:
                    t = done[i]
                t += skill[i] * mana[j]
                done[i] = t
            for i in range(n - 2, -1, -1):
                done[i] = done[i + 1] - skill[i + 1] * mana[j]
        return done[n - 1]
''',
)

write(
    "3495_minimum_operations_to_make_array_elements_zero",
    '''
# LeetCode 3495 - Minimum Operations to Make Array Elements Zero
# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

from typing import List


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def ops_to_zero(x: int) -> int:
            ops = 0
            while x > 0:
                x //= 4
                ops += 1
            return ops

        ans = 0
        for q in queries:
            l, r = q[0], q[1]
            s = 0
            for x in range(l, r + 1):
                s += ops_to_zero(x)
            ans += (s + 1) // 2
        return ans
''',
)

write(
    "3496_maximize_score_after_pair_deletions",
    '''
# LeetCode 3496 - Maximize Score After Pair Deletions
# https://leetcode.com/problems/maximize-score-after-pair-deletions/

from typing import List


class Solution:
    def maximizeScore(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for x in nums:
            total += x
        if n % 2 == 1:
            mn = nums[0]
            for x in nums:
                if x < mn:
                    mn = x
            return total - mn
        mn = nums[0] + nums[1]
        for i in range(n - 1):
            mn = min(mn, nums[i] + nums[i + 1])
        return total - mn
''',
)

write(
    "3498_reverse_degree_of_a_string",
    '''
# LeetCode 3498 - Reverse Degree of a String
# https://leetcode.com/problems/reverse-degree-of-a-string/


class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s):
            ans += (26 - (ord(c) - 97)) * (i + 1)
        return ans
''',
)

write(
    "3499_maximize_active_section_with_trade_i",
    '''
# LeetCode 3499 - Maximize Active Section with Trade I
# https://leetcode.com/problems/maximize-active-section-with-trade-i/


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = 0
        for c in s:
            if c == "1":
                ones += 1
        zeros = []
        n = len(s)
        i = 0
        while i < n:
            if s[i] != "0":
                i += 1
                continue
            j = i
            while j < n and s[j] == "0":
                j += 1
            zeros.append((i, j - 1))
            i = j
        best = 0
        for i in range(len(zeros) - 1):
            gain = (zeros[i][1] - zeros[i][0] + 1) + (zeros[i + 1][1] - zeros[i + 1][0] + 1)
            if gain > best:
                best = gain
        return ones + best
''',
)

print("wrote group e (15)")
