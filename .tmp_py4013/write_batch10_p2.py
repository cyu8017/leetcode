#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["3110_score_of_a_string"] = r'''# LeetCode 3110 - Score of a String
# https://leetcode.com/problems/score-of-a-string/


class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            ans += abs(ord(s[i - 1]) - ord(s[i]))
        return ans
'''

FILES["3111_minimum_rectangles_to_cover_points"] = r'''# LeetCode 3111 - Minimum Rectangles to Cover Points
# https://leetcode.com/problems/minimum-rectangles-to-cover-points/

from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points = sorted(points, key=lambda p: p[0])
        ans = 0
        x1 = -1
        for p in points:
            if p[0] > x1:
                ans += 1
                x1 = p[0] + w
        return ans
'''

FILES["3112_minimum_time_to_visit_disappearing_nodes"] = r'''# LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
# https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

import heapq
from typing import List


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        INF = 1 << 30
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            du, u = heapq.heappop(pq)
            if du > dist[u]:
                continue
            for v, w in g[u]:
                if dist[v] > dist[u] + w and dist[u] + w < disappear[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return [dist[i] if dist[i] < disappear[i] else -1 for i in range(n)]
'''

FILES["3113_find_the_number_of_subarrays_where_boundary_elements_are_maximum"] = r'''# LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
# https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        stk = []
        ans = 0
        for x in nums:
            while stk and stk[-1][0] < x:
                stk.pop()
            if not stk or stk[-1][0] > x:
                stk.append([x, 1])
            else:
                stk[-1][1] += 1
            ans += stk[-1][1]
        return ans
'''

FILES["3114_latest_time_you_can_obtain_after_replacing_characters"] = r'''# LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/


class Solution:
    def findLatestTime(self, s: str) -> str:
        h = 11
        while True:
            for m in range(59, -1, -1):
                t = f"{h:02d}:{m:02d}"
                ok = True
                for i in range(5):
                    if s[i] != "?" and s[i] != t[i]:
                        ok = False
                        break
                if ok:
                    return t
            h -= 1
'''

FILES["3115_maximum_prime_difference"] = r'''# LeetCode 3115 - Maximum Prime Difference
# https://leetcode.com/problems/maximum-prime-difference/

from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True

        i = 0
        while True:
            if is_prime(nums[i]):
                j = len(nums) - 1
                while True:
                    if is_prime(nums[j]):
                        return j - i
                    j -= 1
            i += 1
'''

FILES["3116_kth_smallest_amount_with_single_denomination_combination"] = r'''# LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

from typing import List


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def gcdll(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        def lcmll(a: int, b: int) -> int:
            return a // gcdll(a, b) * b

        def bit_count(x: int) -> int:
            c = 0
            while x != 0:
                c += x & 1
                x >>= 1
            return c

        n = len(coins)

        def check(mx: int) -> bool:
            cnt = 0
            for i in range(1, 1 << n):
                v = 1
                for j in range(n):
                    if ((i >> j) & 1) != 0:
                        v = lcmll(v, coins[j])
                        if v > mx:
                            break
                m = bit_count(i)
                if m % 2 == 1:
                    cnt += mx // v
                else:
                    cnt -= mx // v
            return cnt >= k

        lo, hi = 1, 100000000000
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
'''

FILES["3117_minimum_sum_of_values_by_dividing_array"] = r'''# LeetCode 3117 - Minimum Sum of Values by Dividing Array
# https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

from typing import List


class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        INF = 1 << 29
        n = len(nums)
        m = len(andValues)
        f = {}

        def dfs(i: int, j: int, a: int) -> int:
            if n - i < m - j:
                return INF
            if j == m:
                return 0 if i == n else INF
            a &= nums[i]
            if a < andValues[j]:
                return INF
            key = (i, j, a)
            if key in f:
                return f[key]
            ans = dfs(i + 1, j, a)
            if a == andValues[j]:
                ans = min(ans, dfs(i + 1, j + 1, -1) + nums[i])
            f[key] = ans
            return ans

        ans = dfs(0, 0, -1)
        return ans if ans < INF else -1
'''

FILES["3119_maximum_number_of_potholes_that_can_be_fixed"] = r'''# LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
# https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/


class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        road = road + "."
        n = len(road)
        cnt = [0] * n
        k = 0
        ans = 0
        for c in road:
            if c == "x":
                k += 1
            elif k > 0:
                cnt[k] += 1
                k = 0
        k = n - 1
        while k > 0 and budget > 0:
            t = min(budget // (k + 1), cnt[k])
            ans += t * k
            budget -= t * (k + 1)
            cnt[k - 1] += cnt[k] - t
            k -= 1
        return ans
'''

FILES["3120_count_the_number_of_special_characters_i"] = r'''# LeetCode 3120 - Count the Number of Special Characters I
# https://leetcode.com/problems/count-the-number-of-special-characters-i/


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = [False] * 128
        for ch in word:
            s[ord(ch)] = True
        ans = 0
        for i in range(26):
            if s[97 + i] and s[65 + i]:
                ans += 1
        return ans
'''

FILES["3121_count_the_number_of_special_characters_ii"] = r'''# LeetCode 3121 - Count the Number of Special Characters II
# https://leetcode.com/problems/count-the-number-of-special-characters-ii/


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first = [0] * 128
        last = [0] * 128
        for i, ch in enumerate(word):
            c = ord(ch)
            if first[c] == 0:
                first[c] = i + 1
            last[c] = i + 1
        ans = 0
        for i in range(26):
            if last[97 + i] > 0 and last[97 + i] < first[65 + i]:
                ans += 1
        return ans
'''

FILES["3122_minimum_number_of_operations_to_satisfy_conditions"] = r'''# LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
# https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        INF = 1 << 29
        f = [[INF] * 10 for _ in range(n)]
        for i in range(n):
            cnt = [0] * 10
            for j in range(m):
                cnt[grid[j][i]] += 1
            if i == 0:
                for j in range(10):
                    f[i][j] = m - cnt[j]
            else:
                for j in range(10):
                    for k in range(10):
                        if j != k:
                            f[i][j] = min(f[i][j], f[i - 1][k] + m - cnt[j])
        ans = INF
        for j in range(10):
            ans = min(ans, f[n - 1][j])
        return ans
'''

FILES["3123_find_edges_in_shortest_paths"] = r'''# LeetCode 3123 - Find Edges in Shortest Paths
# https://leetcode.com/problems/find-edges-in-shortest-paths/

import heapq
from collections import deque
from typing import List


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        g = [[] for _ in range(n)]
        for i, (a, b, w) in enumerate(edges):
            g[a].append((b, w, i))
            g[b].append((a, w, i))
        INF = 1 << 30
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            da, a = heapq.heappop(pq)
            if da > dist[a]:
                continue
            for b, w, _ in g[a]:
                if dist[b] > dist[a] + w:
                    dist[b] = dist[a] + w
                    heapq.heappush(pq, (dist[b], b))
        ans = [False] * len(edges)
        if dist[n - 1] == INF:
            return ans
        q = deque([n - 1])
        while q:
            a = q.popleft()
            for b, w, i in g[a]:
                if dist[a] == dist[b] + w:
                    ans[i] = True
                    q.append(b)
        return ans
'''

FILES["3125_maximum_number_that_makes_result_of_bitwise_and_zero"] = r'''# LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
# https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/


class Solution:
    def maxNumber(self, n: int) -> int:
        length = 0
        x = n
        while x > 0:
            length += 1
            x >>= 1
        return (1 << (length - 1)) - 1
'''

FILES["3127_make_a_square_with_the_same_color"] = r'''# LeetCode 3127 - Make a Square with the Same Color
# https://leetcode.com/problems/make-a-square-with-the-same-color/

from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        dirs = [0, 0, 1, 1, 0]
        for i in range(2):
            for j in range(2):
                cnt1 = 0
                cnt2 = 0
                for k in range(4):
                    x = i + dirs[k]
                    y = j + dirs[k + 1]
                    if grid[x][y] == "W":
                        cnt1 += 1
                    else:
                        cnt2 += 1
                if cnt1 != cnt2:
                    return True
        return False
'''

FILES["3128_right_triangles"] = r'''# LeetCode 3128 - Right Triangles
# https://leetcode.com/problems/right-triangles/

from typing import List


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += (rows[i] - 1) * (cols[j] - 1)
        return ans
'''

FILES["3129_find_all_possible_stable_binary_arrays_i"] = r'''# LeetCode 3129 - Find All Possible Stable Binary Arrays I
# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1000000007
        f = [[[-1, -1] for _ in range(one + 1)] for _ in range(zero + 1)]

        def dfs(i: int, j: int, k: int) -> int:
            if i < 0 or j < 0:
                return 0
            if i == 0:
                return 1 if k == 1 and j <= limit else 0
            if j == 0:
                return 1 if k == 0 and i <= limit else 0
            if f[i][j][k] != -1:
                return f[i][j][k]
            if k == 0:
                res = (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - dfs(i - limit - 1, j, 1) + MOD) % MOD
            else:
                res = (dfs(i, j - 1, 0) + dfs(i, j - 1, 1) - dfs(i, j - limit - 1, 0) + MOD) % MOD
            f[i][j][k] = res
            return res

        return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD
'''

FILES["3130_find_all_possible_stable_binary_arrays_ii"] = r'''# LeetCode 3130 - Find All Possible Stable Binary Arrays II
# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1000000007
        f = [[[-1, -1] for _ in range(one + 1)] for _ in range(zero + 1)]

        def dfs(i: int, j: int, k: int) -> int:
            if i < 0 or j < 0:
                return 0
            if i == 0:
                return 1 if k == 1 and j <= limit else 0
            if j == 0:
                return 1 if k == 0 and i <= limit else 0
            if f[i][j][k] != -1:
                return f[i][j][k]
            if k == 0:
                res = (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - dfs(i - limit - 1, j, 1) + MOD) % MOD
            else:
                res = (dfs(i, j - 1, 0) + dfs(i, j - 1, 1) - dfs(i, j - limit - 1, 0) + MOD) % MOD
            f[i][j][k] = res
            return res

        return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD
'''

FILES["3131_find_the_integer_added_to_array_i"] = r'''# LeetCode 3131 - Find the Integer Added to Array I
# https://leetcode.com/problems/find-the-integer-added-to-array-i/

from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        min1 = nums1[0]
        min2 = nums2[0]
        for x in nums1:
            min1 = min(min1, x)
        for x in nums2:
            min2 = min(min2, x)
        return min2 - min1
'''

FILES["3132_find_the_integer_added_to_array_ii"] = r'''# LeetCode 3132 - Find the Integer Added to Array II
# https://leetcode.com/problems/find-the-integer-added-to-array-ii/

from typing import List


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        def ok(x: int) -> bool:
            i = 0
            j = 0
            cnt = 0
            while i < len(nums1) and j < len(nums2):
                if nums2[j] - nums1[i] != x:
                    cnt += 1
                else:
                    j += 1
                i += 1
            return cnt <= 2

        ans = 1 << 30
        for t in range(3):
            x = nums2[0] - nums1[t]
            if ok(x):
                ans = min(ans, x)
        return ans
'''

FILES["3133_minimum_array_end"] = r'''# LeetCode 3133 - Minimum Array End
# https://leetcode.com/problems/minimum-array-end/


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        ans = x
        for i in range(31):
            if ((x >> i) & 1) == 0:
                ans |= (n & 1) << i
                n >>= 1
        ans |= n << 31
        return ans
'''

FILES["3134_find_the_median_of_the_uniqueness_array"] = r'''# LeetCode 3134 - Find the Median of the Uniqueness Array
# https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

from typing import List


class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        m = (1 + n) * n // 2

        def check(mx: int) -> bool:
            cnt = {}
            l = 0
            k = 0
            for r in range(n):
                cnt[nums[r]] = cnt.get(nums[r], 0) + 1
                while len(cnt) > mx:
                    y = nums[l]
                    l += 1
                    nv = cnt[y] - 1
                    if nv == 0:
                        del cnt[y]
                    else:
                        cnt[y] = nv
                k += r - l + 1
                if k >= (m + 1) // 2:
                    return True
            return False

        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
'''

FILES["3135_equalize_strings_by_adding_or_removing_characters_at_ends"] = r'''# LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
# https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/


class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        m = len(initial)
        n = len(target)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        mx = 0
        for i in range(m):
            for j in range(n):
                if initial[i] == target[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
                    mx = max(mx, f[i + 1][j + 1])
        return m + n - 2 * mx
'''

FILES["3136_valid_word"] = r'''# LeetCode 3136 - Valid Word
# https://leetcode.com/problems/valid-word/


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        has_vowel = False
        has_consonant = False
        vs = [False] * 26
        for c in "aeiou":
            vs[ord(c) - 97] = True
        for c in word:
            if c.isalpha():
                lower = c.lower()
                if vs[ord(lower) - 97]:
                    has_vowel = True
                else:
                    has_consonant = True
            elif not c.isdigit():
                return False
        return has_vowel and has_consonant
'''

FILES["3137_minimum_number_of_operations_to_make_word_k_periodic"] = r'''# LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
# https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        cnt = {}
        n = len(word)
        mx = 0
        for i in range(0, n, k):
            s = word[i : i + k]
            v = cnt.get(s, 0) + 1
            cnt[s] = v
            mx = max(mx, v)
        return n // k - mx
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
