#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["3082_find_the_sum_of_the_power_of_all_subsequences"] = r'''# LeetCode 3082 - Find the Sum of the Power of All Subsequences
# https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

from typing import List


class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        MOD = 1000000007
        n = len(nums)
        f = [[0] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            for j in range(k + 1):
                f[i][j] = (f[i - 1][j] * 2) % MOD
                if j >= nums[i - 1]:
                    f[i][j] = (f[i][j] + f[i - 1][j - nums[i - 1]]) % MOD
        return f[n][k]
'''

FILES["3083_existence_of_a_substring_in_a_string_and_its_reverse"] = r'''# LeetCode 3083 - Existence of a Substring in a String and Its Reverse
# https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        st = [[False] * 26 for _ in range(26)]
        for i in range(len(s) - 1):
            st[ord(s[i + 1]) - 97][ord(s[i]) - 97] = True
        for i in range(len(s) - 1):
            if st[ord(s[i]) - 97][ord(s[i + 1]) - 97]:
                return True
        return False
'''

FILES["3084_count_substrings_starting_and_ending_with_given_character"] = r'''# LeetCode 3084 - Count Substrings Starting and Ending with Given Character
# https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        cnt = 0
        for ch in s:
            if ch == c:
                cnt += 1
        return cnt * (cnt + 1) // 2
'''

FILES["3085_minimum_deletions_to_make_string_k_special"] = r'''# LeetCode 3085 - Minimum Deletions to Make String K-Special
# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - 97] += 1
        nums = [v for v in freq if v > 0]
        ans = len(word)
        for i in range(len(word) + 1):
            cur = 0
            for x in nums:
                if x < i:
                    cur += x
                elif x > i + k:
                    cur += x - i - k
            ans = min(ans, cur)
        return ans
'''

FILES["3086_minimum_moves_to_pick_k_ones"] = r'''# LeetCode 3086 - Minimum Moves to Pick K Ones
# https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

from typing import List


class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        n = len(nums)
        cnt = [0] * (n + 1)
        s = [0] * (n + 1)
        for i in range(1, n + 1):
            cnt[i] = cnt[i - 1] + nums[i - 1]
            s[i] = s[i - 1] + i * nums[i - 1]
        ans = 10**18
        for i in range(1, n + 1):
            t = 0
            need = k - nums[i - 1]
            for j in (i - 1, i + 1):
                if need > 0 and 1 <= j <= n and nums[j - 1] == 1:
                    need -= 1
                    t += 1
            c = min(need, maxChanges)
            need -= c
            t += c * 2
            if need <= 0:
                ans = min(ans, t)
                continue
            l, r = 2, max(i - 1, n - i)
            while l <= r:
                mid = (l + r) >> 1
                l1 = max(1, i - mid)
                r1 = max(0, i - 2)
                l2 = min(n + 1, i + 2)
                r2 = min(n, i + mid)
                c1 = cnt[r1] - cnt[l1 - 1]
                c2 = cnt[r2] - cnt[l2 - 1]
                if c1 + c2 >= need:
                    t1 = c1 * i - (s[r1] - s[l1 - 1])
                    t2 = s[r2] - s[l2 - 1] - c2 * i
                    ans = min(ans, t + t1 + t2)
                    r = mid - 1
                else:
                    l = mid + 1
        return ans
'''

FILES["3088_make_string_anti_palindrome"] = r'''# LeetCode 3088 - Make String Anti-palindrome
# https://leetcode.com/problems/make-string-anti-palindrome/


class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        arr = sorted(s)
        n = len(arr)
        m = n // 2
        if arr[m] == arr[m - 1]:
            i = m
            while i < n and arr[i] == arr[i - 1]:
                i += 1
            j = m
            while j < n and arr[j] == arr[n - j - 1]:
                if i >= n:
                    return "-1"
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
        return "".join(arr)
'''

FILES["3090_maximum_length_substring_with_two_occurrences"] = r'''# LeetCode 3090 - Maximum Length Substring With Two Occurrences
# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        cnt = [0] * 26
        for r, ch in enumerate(s):
            idx = ord(ch) - 97
            cnt[idx] += 1
            while cnt[idx] > 2:
                cnt[ord(s[l]) - 97] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
'''

FILES["3091_apply_operations_to_make_sum_of_array_greater_than_or_equal_to_k"] = r'''# LeetCode 3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
# https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/


class Solution:
    def minOperations(self, k: int) -> int:
        ans = k
        for a in range(k):
            x = a + 1
            b = (k + x - 1) // x - 1
            ans = min(ans, a + b)
        return ans
'''

FILES["3092_most_frequent_ids"] = r'''# LeetCode 3092 - Most Frequent IDs
# https://leetcode.com/problems/most-frequent-ids/

import heapq
from typing import List


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        n = len(nums)
        cnt = {}
        lazy = {}
        ans = [0] * n
        pq = []
        for i in range(n):
            x, f = nums[i], freq[i]
            old = cnt.get(x, 0)
            lazy[old] = lazy.get(old, 0) + 1
            neu = old + f
            cnt[x] = neu
            heapq.heappush(pq, -neu)
            while pq and lazy.get(-pq[0], 0) > 0:
                top = -heapq.heappop(pq)
                lazy[top] -= 1
            ans[i] = -pq[0] if pq else 0
        return ans
'''

FILES["3093_longest_common_suffix_queries"] = r'''# LeetCode 3093 - Longest Common Suffix Queries
# https://leetcode.com/problems/longest-common-suffix-queries/

from typing import List

INF = 1 << 30


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.length = INF
        self.idx = INF


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        def insert(t: Trie, w: str, i: int) -> None:
            node = t
            if node.length > len(w):
                node.length = len(w)
                node.idx = i
            for k in range(len(w) - 1, -1, -1):
                cid = ord(w[k]) - 97
                if node.children[cid] is None:
                    node.children[cid] = Trie()
                node = node.children[cid]
                if node.length > len(w):
                    node.length = len(w)
                    node.idx = i

        def query(t: Trie, w: str) -> int:
            node = t
            for k in range(len(w) - 1, -1, -1):
                cid = ord(w[k]) - 97
                if node.children[cid] is None:
                    break
                node = node.children[cid]
            return node.idx

        trie = Trie()
        for i, w in enumerate(wordsContainer):
            insert(trie, w, i)
        return [query(trie, w) for w in wordsQuery]
'''

FILES["3094_guess_the_number_using_bitwise_questions_ii"] = r'''# LeetCode 3094 - Guess the Number Using Bitwise Questions II
# https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

# The commonBits API is patched by the test runner.


def commonBits(num: int) -> int:
    raise NotImplementedError


class Solution:
    def findNumber(self) -> int:
        n = 0
        for i in range(32):
            count1 = commonBits(1 << i)
            count2 = commonBits(1 << i)
            if count1 > count2:
                n |= 1 << i
        return n
'''

FILES["3095_shortest_subarray_with_or_at_least_k_i"] = r'''# LeetCode 3095 - Shortest Subarray With OR at Least K I
# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/

from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * 32
        ans = n + 1
        s = 0
        i = 0
        for j in range(n):
            x = nums[j]
            s |= x
            for h in range(32):
                if ((x >> h) & 1) != 0:
                    cnt[h] += 1
            while s >= k and i <= j:
                ans = min(ans, j - i + 1)
                for h in range(32):
                    if ((nums[i] >> h) & 1) != 0:
                        cnt[h] -= 1
                        if cnt[h] == 0:
                            s ^= 1 << h
                i += 1
        return -1 if ans == n + 1 else ans
'''

FILES["3096_minimum_levels_to_gain_more_points"] = r'''# LeetCode 3096 - Minimum Levels to Gain More Points
# https://leetcode.com/problems/minimum-levels-to-gain-more-points/

from typing import List


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        s = 0
        for x in possible:
            s += -1 if x == 0 else x
        t = 0
        for i in range(len(possible) - 1):
            x = -1 if possible[i] == 0 else possible[i]
            t += x
            if t > s - t:
                return i + 1
        return -1
'''

FILES["3097_shortest_subarray_with_or_at_least_k_ii"] = r'''# LeetCode 3097 - Shortest Subarray With OR at Least K II
# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * 32
        ans = n + 1
        s = 0
        i = 0
        for j in range(n):
            x = nums[j]
            s |= x
            for h in range(32):
                if ((x >> h) & 1) != 0:
                    cnt[h] += 1
            while s >= k and i <= j:
                ans = min(ans, j - i + 1)
                for h in range(32):
                    if ((nums[i] >> h) & 1) != 0:
                        cnt[h] -= 1
                        if cnt[h] == 0:
                            s ^= 1 << h
                i += 1
        return -1 if ans == n + 1 else ans
'''

FILES["3098_find_the_sum_of_subsequence_powers"] = r'''# LeetCode 3098 - Find the Sum of Subsequence Powers
# https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

from typing import List


class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 1000000007
        nums = sorted(nums)
        n = len(nums)
        f = {}

        def dfs(i: int, j: int, kk: int, mi: int) -> int:
            if i >= n:
                return mi if kk == 0 else 0
            if n - i < kk:
                return 0
            key = (mi, i, j, kk)
            if key in f:
                return f[key]
            ans = dfs(i + 1, j, kk, mi)
            if j == n:
                ans = (ans + dfs(i + 1, i, kk - 1, mi)) % MOD
            else:
                ans = (ans + dfs(i + 1, i, kk - 1, min(mi, nums[i] - nums[j]))) % MOD
            f[key] = ans
            return ans

        return dfs(0, n, k, 10**18)
'''

FILES["3099_harshad_number"] = r'''# LeetCode 3099 - Harshad Number
# https://leetcode.com/problems/harshad-number/


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        y = x
        while y > 0:
            s += y % 10
            y //= 10
        return s if x % s == 0 else -1
'''

FILES["3100_water_bottles_ii"] = r'''# LeetCode 3100 - Water Bottles II
# https://leetcode.com/problems/water-bottles-ii/


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange
            numExchange += 1
            ans += 1
            numBottles += 1
        return ans
'''

FILES["3101_count_alternating_subarrays"] = r'''# LeetCode 3101 - Count Alternating Subarrays
# https://leetcode.com/problems/count-alternating-subarrays/

from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = 1
        s = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                s += 1
            else:
                s = 1
            ans += s
        return ans
'''

FILES["3102_minimize_manhattan_distances"] = r'''# LeetCode 3102 - Minimize Manhattan Distances
# https://leetcode.com/problems/minimize-manhattan-distances/

import bisect
from typing import List


class _MultiSet:
    def __init__(self):
        self.m = {}
        self.keys = []

    def merge(self, x: int, v: int) -> None:
        nv = self.m.get(x, 0) + v
        if nv == 0:
            del self.m[x]
            i = bisect.bisect_left(self.keys, x)
            if i < len(self.keys) and self.keys[i] == x:
                self.keys.pop(i)
        else:
            if x not in self.m:
                bisect.insort(self.keys, x)
            self.m[x] = nv

    def first(self) -> int:
        return self.keys[0]

    def last(self) -> int:
        return self.keys[-1]


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        st1 = _MultiSet()
        st2 = _MultiSet()
        for p in points:
            st1.merge(p[0] + p[1], 1)
            st2.merge(p[0] - p[1], 1)
        ans = 10**18
        for p in points:
            x, y = p[0], p[1]
            st1.merge(x + y, -1)
            st2.merge(x - y, -1)
            ans = min(ans, max(st1.last() - st1.first(), st2.last() - st2.first()))
            st1.merge(x + y, 1)
            st2.merge(x - y, 1)
        return ans
'''

FILES["3104_find_longest_self_contained_substring"] = r'''# LeetCode 3104 - Find Longest Self-Contained Substring
# https://leetcode.com/problems/find-longest-self-contained-substring/


class Solution:
    def maxSubstringLength(self, s: str) -> int:
        first = [-1] * 26
        last = [0] * 26
        n = len(s)
        for i, ch in enumerate(s):
            j = ord(ch) - 97
            if first[j] == -1:
                first[j] = i
            last[j] = i
        ans = -1
        for k in range(26):
            i = first[k]
            if i == -1:
                continue
            mx = last[k]
            for j in range(i, n):
                a = first[ord(s[j]) - 97]
                b = last[ord(s[j]) - 97]
                if a < i:
                    break
                mx = max(mx, b)
                if mx == j and j - i + 1 < n:
                    ans = max(ans, j - i + 1)
        return ans
'''

FILES["3105_longest_strictly_increasing_or_strictly_decreasing_subarray"] = r'''# LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        t = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                t += 1
                ans = max(ans, t)
            else:
                t = 1
        t = 1
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                t += 1
                ans = max(ans, t)
            else:
                t = 1
        return ans
'''

FILES["3106_lexicographically_smallest_string_after_operations_with_constraint"] = r'''# LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
# https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/


class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        arr = list(s)
        for i in range(len(arr)):
            c1 = ord(arr[i])
            for c2 in range(97, c1):
                d = min(c1 - c2, 26 - (c1 - c2))
                if d <= k:
                    arr[i] = chr(c2)
                    k -= d
                    break
        return "".join(arr)
'''

FILES["3107_minimum_operations_to_make_median_of_array_equal_to_k"] = r'''# LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
# https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

from typing import List


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        m = n >> 1
        ans = abs(nums[m] - k)
        if nums[m] > k:
            i = m - 1
            while i >= 0 and nums[i] > k:
                ans += nums[i] - k
                i -= 1
        else:
            i = m + 1
            while i < n and nums[i] < k:
                ans += k - nums[i]
                i += 1
        return ans
'''

FILES["3108_minimum_cost_walk_in_weighted_graph"] = r'''# LeetCode 3108 - Minimum Cost Walk in Weighted Graph
# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

from typing import List


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        p = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def unite(a: int, b: int) -> None:
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if size[pa] > size[pb]:
                p[pb] = pa
                size[pa] += size[pb]
            else:
                p[pa] = pb
                size[pb] += size[pa]

        g = [-1] * n
        for e in edges:
            unite(e[0], e[1])
        for e in edges:
            root = find(e[0])
            g[root] &= e[2]
        ans = [0] * len(query)
        for i, (u, v) in enumerate(query):
            if u == v:
                ans[i] = 0
            else:
                a, b = find(u), find(v)
                ans[i] = g[a] if a == b else -1
        return ans
'''

FILES["3109_find_the_index_of_permutation"] = r'''# LeetCode 3109 - Find the Index of Permutation
# https://leetcode.com/problems/find-the-index-of-permutation/

from typing import List


class BIT:
    def __init__(self, n: int):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, delta: int) -> None:
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]
            x -= x & -x
        return s


class Solution:
    def getPermutationIndex(self, perm: List[int]) -> int:
        MOD = 1000000007
        n = len(perm)
        tree = BIT(n + 1)
        f = [0] * n
        f[0] = 1
        for i in range(1, n):
            f[i] = f[i - 1] * i % MOD
        ans = 0
        for i in range(n):
            x = perm[i]
            cnt = x - 1 - tree.query(x)
            ans = (ans + cnt * f[n - 1 - i]) % MOD
            tree.update(x, 1)
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
