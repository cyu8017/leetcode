from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
files = {}

files["2732_find_a_good_subset_of_the_matrix"] = '''# LeetCode 2732 - Find a Good Subset of the Matrix
# https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

from typing import List


class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        first = {}
        for i, row in enumerate(grid):
            mask = 0
            for j in range(n):
                if row[j] == 1:
                    mask |= 1 << j
            if mask == 0:
                return [i]
            for pm, idx in first.items():
                if (pm & mask) == 0:
                    return [idx, i] if idx < i else [i, idx]
            if mask not in first:
                first[mask] = i
        return []
'''

files["2733_neither_minimum_nor_maximum"] = '''# LeetCode 2733 - Neither Minimum nor Maximum
# https://leetcode.com/problems/neither-minimum-nor-maximum/

from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        a, b, c = nums[0], nums[1], nums[2]
        return a + b + c - max(a, b, c) - min(a, b, c)
'''

files["2734_lexicographically_smallest_string_after_substring_operation"] = '''# LeetCode 2734 - Lexicographically Smallest String After Substring Operation
# https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/


class Solution:
    def smallestString(self, s: str) -> str:
        arr = list(s)
        n = len(arr)
        i = 0
        while i < n and arr[i] == "a":
            i += 1
        if i == n:
            arr[n - 1] = "z"
            return "".join(arr)
        while i < n and arr[i] != "a":
            arr[i] = chr(ord(arr[i]) - 1)
            i += 1
        return "".join(arr)
'''

files["2735_collecting_chocolates"] = '''# LeetCode 2735 - Collecting Chocolates
# https://leetcode.com/problems/collecting-chocolates/

from typing import List


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        best = nums[:]
        ans = sum(nums)
        for rot in range(1, n):
            cur = rot * x
            for i in range(n):
                best[i] = min(best[i], nums[(i + rot) % n])
                cur += best[i]
            ans = min(ans, cur)
        return ans
'''

files["2736_maximum_sum_queries"] = '''# LeetCode 2736 - Maximum Sum Queries
# https://leetcode.com/problems/maximum-sum-queries/

from typing import List


class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        pts = [(nums1[i], nums2[i], nums1[i] + nums2[i]) for i in range(n)]
        pts.sort(key=lambda p: -p[0])
        qs = [(q[0], q[1], i) for i, q in enumerate(queries)]
        qs.sort(key=lambda q: -q[0])
        ys = sorted(list(nums2) + [q[1] for q in queries])
        uniq = []
        for y in ys:
            if not uniq or uniq[-1] != y:
                uniq.append(y)
        m = len(uniq)
        bit = [-1] * (m + 2)

        def rank(y: int) -> int:
            lo, hi = 0, m
            while lo < hi:
                mid = (lo + hi) >> 1
                if uniq[mid] < y:
                    lo = mid + 1
                else:
                    hi = mid
            return lo + 1

        def update(i: int, v: int) -> None:
            while i <= m:
                bit[i] = max(bit[i], v)
                i += i & -i

        def query(i: int) -> int:
            best = -1
            while i > 0:
                best = max(best, bit[i])
                i -= i & -i
            return best

        ans = [0] * len(queries)
        j = 0
        for q in qs:
            while j < n and pts[j][0] >= q[0]:
                update(m - rank(pts[j][1]) + 1, pts[j][2])
                j += 1
            ans[q[2]] = query(m - rank(q[1]) + 1)
        return ans
'''

files["2737_find_the_closest_marked_node"] = '''# LeetCode 2737 - Find the Closest Marked Node
# https://leetcode.com/problems/find-the-closest-marked-node/

import heapq
from typing import List


class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
        mark = set(marked)
        dist = [10**18] * n
        dist[s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if u in mark:
                return d
            if d > dist[u]:
                continue
            for v, w in g[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        return -1
'''

files["2739_total_distance_traveled"] = '''# LeetCode 2739 - Total Distance Traveled
# https://leetcode.com/problems/total-distance-traveled/


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank > 0:
            if mainTank >= 5:
                ans += 50
                mainTank -= 5
                if additionalTank > 0:
                    additionalTank -= 1
                    mainTank += 1
            else:
                ans += mainTank * 10
                mainTank = 0
        return ans
'''

files["2740_find_the_value_of_the_partition"] = '''# LeetCode 2740 - Find the Value of the Partition
# https://leetcode.com/problems/find-the-value-of-the-partition/

from typing import List


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans = 10**18
        for i in range(1, len(nums)):
            ans = min(ans, nums[i] - nums[i - 1])
        return ans
'''

files["2741_special_permutations"] = '''# LeetCode 2741 - Special Permutations
# https://leetcode.com/problems/special-permutations/

from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 1000000007
        n = len(nums)
        memo = [[-1] * n for _ in range(1 << n)]

        def dfs(mask: int, last: int) -> int:
            if mask == (1 << n) - 1:
                return 1
            if memo[mask][last] != -1:
                return memo[mask][last]
            res = 0
            for i in range(n):
                if mask & (1 << i):
                    continue
                if nums[i] % nums[last] == 0 or nums[last] % nums[i] == 0:
                    res = (res + dfs(mask | (1 << i), i)) % MOD
            memo[mask][last] = res
            return res

        ans = 0
        for i in range(n):
            ans = (ans + dfs(1 << i, i)) % MOD
        return ans
'''

files["2742_painting_the_walls"] = '''# LeetCode 2742 - Painting the Walls
# https://leetcode.com/problems/painting-the-walls/

from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(n, -1, -1):
                nj = min(n, j + time[i] + 1)
                if dp[j] + cost[i] < dp[nj]:
                    dp[nj] = dp[j] + cost[i]
        return dp[n]
'''

files["2743_count_substrings_without_repeating_character"] = '''# LeetCode 2743 - Count Substrings Without Repeating Character
# https://leetcode.com/problems/count-substrings-without-repeating-character/


class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        n = len(s)
        ans, left = 0, 0
        cnt = [0] * 26
        for i in range(n):
            c = ord(s[i]) - 97
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[ord(s[left]) - 97] -= 1
                left += 1
            ans += i - left + 1
        return ans
'''

files["2744_find_maximum_number_of_string_pairs"] = '''# LeetCode 2744 - Find Maximum Number of String Pairs
# https://leetcode.com/problems/find-maximum-number-of-string-pairs/

from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        freq = {}
        ans = 0
        for w in words:
            rev = w[::-1]
            c = freq.get(rev, 0)
            if c > 0:
                ans += 1
                freq[rev] = c - 1
            else:
                freq[w] = freq.get(w, 0) + 1
        return ans
'''

files["2745_construct_the_longest_new_string"] = '''# LeetCode 2745 - Construct the Longest New String
# https://leetcode.com/problems/construct-the-longest-new-string/


class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x < y:
            return (2 * x + 1 + z) * 2
        if y < x:
            return (2 * y + 1 + z) * 2
        return (x + y + z) * 2
'''

files["2746_decremental_string_concatenation"] = '''# LeetCode 2746 - Decremental String Concatenation
# https://leetcode.com/problems/decremental-string-concatenation/

from typing import List


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        memo = {}
        w0 = words[0]

        def dfs(i: int, first: str, last: str) -> int:
            if i == n:
                return 0
            key = (i, first, last)
            if key in memo:
                return memo[key]
            w = words[i]
            wf, wl = w[0], w[-1]
            add1 = len(w) - (1 if last == wf else 0)
            add2 = len(w) - (1 if wl == first else 0)
            a = add1 + dfs(i + 1, first, wl)
            b = add2 + dfs(i + 1, wf, last)
            ans = min(a, b)
            memo[key] = ans
            return ans

        return len(w0) + dfs(1, w0[0], w0[-1])
'''

files["2747_count_zero_request_servers"] = '''# LeetCode 2747 - Count Zero Request Servers
# https://leetcode.com/problems/count-zero-request-servers/

from typing import List


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda e: e[1])
        qs = sorted(((t, i) for i, t in enumerate(queries)), key=lambda q: q[0])
        ans = [0] * len(queries)
        cnt = {}
        active, l, r = 0, 0, 0
        for t, qi in qs:
            while r < len(logs) and logs[r][1] <= t:
                sid = logs[r][0]
                c = cnt.get(sid, 0)
                if c == 0:
                    active += 1
                cnt[sid] = c + 1
                r += 1
            while l < r and logs[l][1] < t - x:
                sid = logs[l][0]
                c = cnt[sid] - 1
                cnt[sid] = c
                if c == 0:
                    active -= 1
                l += 1
            ans[qi] = n - active
        return ans
'''

files["2748_number_of_beautiful_pairs"] = '''# LeetCode 2748 - Number of Beautiful Pairs
# https://leetcode.com/problems/number-of-beautiful-pairs/

from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        def first_digit(x: int) -> int:
            while x >= 10:
                x //= 10
            return x

        ans = 0
        freq = [0] * 10
        for x in nums:
            last = x % 10
            for d in range(1, 10):
                if freq[d] > 0 and gcd(d, last) == 1:
                    ans += freq[d]
            freq[first_digit(x)] += 1
        return ans
'''

written = 0
for folder, content in files.items():
    if not content.endswith("\n"):
        content += "\n"
    path = root / folder / "solution.py"
    path.write_text(content, encoding="utf-8", newline="\n")
    written += 1
    text = path.read_text(encoding="utf-8")
    assert not text.startswith("\ufeff"), folder
    assert "def solve(self) -> None:\n        pass" not in text, folder

print(f"wrote {written}")
