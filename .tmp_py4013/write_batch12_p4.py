#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3392_count_subarrays_of_length_three_with_a_condition"] = r'''# LeetCode 3392 - Count Subarrays of Length Three With a Condition
# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            if nums[i] * 2 + nums[i + 2] * 2 == nums[i + 1]:
                ans += 1
        return ans
'''

FILES["3393_count_paths_with_the_given_xor_value"] = r'''# LeetCode 3393 - Count Paths With the Given XOR Value
# https://leetcode.com/problems/count-paths-with-the-given-xor-value/

from typing import List


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        mod = 1000000007
        m, n = len(grid), len(grid[0])
        dp = [[[0] * 16 for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = 1
        for i in range(m):
            for j in range(n):
                for x in range(16):
                    if dp[i][j][x] == 0:
                        continue
                    if i + 1 < m:
                        nx = x ^ grid[i + 1][j]
                        dp[i + 1][j][nx] = (dp[i + 1][j][nx] + dp[i][j][x]) % mod
                    if j + 1 < n:
                        nx = x ^ grid[i][j + 1]
                        dp[i][j + 1][nx] = (dp[i][j + 1][nx] + dp[i][j][x]) % mod
        return dp[m - 1][n - 1][k]
'''

FILES["3394_check_if_grid_can_be_cut_into_sections"] = r'''# LeetCode 3394 - Check if Grid can be Cut into Sections
# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

from typing import List


def checkCut(rects: List[List[int]], axis: int) -> bool:
    arr = [[r[0], r[2]] if axis == 0 else [r[1], r[3]] for r in rects]
    arr.sort(key=lambda x: (x[0], x[1]))
    cuts = 0
    end = arr[0][1]
    for i in range(1, len(arr)):
        if arr[i][0] >= end:
            cuts += 1
            end = arr[i][1]
            if cuts >= 2:
                return True
        elif arr[i][1] > end:
            end = arr[i][1]
    return False


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        return checkCut(rectangles, 0) or checkCut(rectangles, 1)
'''

FILES["3395_subsequences_with_a_unique_middle_mode_i"] = r'''# LeetCode 3395 - Subsequences with a Unique Middle Mode I
# https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/

from typing import List


class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        mod = 1000000007
        n = len(nums)
        ans = 0

        def uniqueMode(a: List[int]) -> bool:
            freq = {}
            for x in a:
                freq[x] = freq.get(x, 0) + 1
            best = 0
            cnt = 0
            for f in freq.values():
                if f > best:
                    best = f
                    cnt = 1
                elif f == best:
                    cnt += 1
            return cnt == 1

        for mid in range(2, n - 2):
            for a in range(mid):
                for b in range(a + 1, mid):
                    for c in range(mid + 1, n):
                        for d in range(c + 1, n):
                            if uniqueMode([nums[a], nums[b], nums[mid], nums[c], nums[d]]):
                                ans += 1
        return ans % mod
'''

FILES["3396_minimum_number_of_operations_to_make_elements_in_array_distinct"] = r'''# LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        lst = nums[:]
        ops = 0
        while True:
            seen = set()
            dup = False
            for x in lst:
                if x in seen:
                    dup = True
                    break
                seen.add(x)
            if not dup:
                return ops
            if len(lst) <= 3:
                return ops + 1
            lst = lst[3:]
            ops += 1
'''

FILES["3397_maximum_number_of_distinct_elements_after_operations"] = r'''# LeetCode 3397 - Maximum Number of Distinct Elements After Operations
# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        ans = 0
        prev = -4503599627370496
        for x in nums:
            cur = x - k
            if cur <= prev:
                cur = prev + 1
            if cur > x + k:
                continue
            ans += 1
            prev = cur
        return ans
'''

FILES["3398_smallest_substring_with_identical_characters_i"] = r'''# LeetCode 3398 - Smallest Substring With Identical Characters I
# https://leetcode.com/problems/smallest-substring-with-identical-characters-i/


class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        def ok(L: int) -> bool:
            if L == 0:
                return False
            ops = 0
            i = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                ops += (j - i) // (L + 1)
                i = j
            return ops <= numOps

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
'''

FILES["3399_smallest_substring_with_identical_characters_ii"] = r'''# LeetCode 3399 - Smallest Substring With Identical Characters II
# https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/


class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        def ok(L: int) -> bool:
            ops = 0
            i = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                ops += (j - i) // (L + 1)
                i = j
            return ops <= numOps

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
'''

FILES["3400_maximum_number_of_matching_indices_after_right_shifts"] = r'''# LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
# https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

from typing import List


class Solution:
    def maximumMatchingIndices(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        ans = 0
        for shift in range(n):
            cnt = 0
            for i in range(n):
                if nums1[(i - shift + n) % n] == nums2[i]:
                    cnt += 1
            if cnt > ans:
                ans = cnt
        return ans
'''

FILES["3402_minimum_operations_to_make_columns_strictly_increasing"] = r'''# LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for j in range(n):
            for i in range(1, m):
                if grid[i][j] <= grid[i - 1][j]:
                    need = grid[i - 1][j] + 1
                    ans += need - grid[i][j]
                    grid[i][j] = need
        return ans
'''

FILES["3403_find_the_lexicographically_largest_string_from_the_box_i"] = r'''# LeetCode 3403 - Find the Lexicographically Largest String From the Box I
# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        max_len = n - (numFriends - 1)
        ans = ""
        for i in range(n):
            end = i + max_len
            if end > n:
                end = n
            cand = word[i:end]
            if cand > ans:
                ans = cand
        return ans
'''

FILES["3404_count_special_subsequences"] = r'''# LeetCode 3404 - Count Special Subsequences
# https://leetcode.com/problems/count-special-subsequences/

from typing import List


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 2, n):
                for k in range(j + 2, n):
                    for l in range(k + 2, n):
                        if nums[i] * nums[k] == nums[j] * nums[l]:
                            ans += 1
        return ans
'''

FILES["3405_count_the_number_of_arrays_with_k_matching_adjacent_elements"] = r'''# LeetCode 3405 - Count the Number of Arrays with K Matching Adjacent Elements
# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 1000000007

        def modPow(a: int, e: int) -> int:
            r = 1
            base = ((a % mod) + mod) % mod
            exp = e
            while exp > 0:
                if exp & 1:
                    r = (r * base) % mod
                base = (base * base) % mod
                exp >>= 1
            return r

        def comb(nn: int, kk: int) -> int:
            if kk < 0 or kk > nn:
                return 0
            num = 1
            den = 1
            for i in range(kk):
                num = (num * (nn - i)) % mod
                den = (den * (i + 1)) % mod
            return (num * modPow(den, mod - 2)) % mod

        return comb(n - 1, k) * m % mod * modPow(m - 1, n - 1 - k) % mod
'''

FILES["3406_find_the_lexicographically_largest_string_from_the_box_ii"] = r'''# LeetCode 3406 - Find the Lexicographically Largest String From the Box II
# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-ii/


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        max_len = n - (numFriends - 1)
        ans = ""
        for i in range(n):
            end = i + max_len
            if end > n:
                end = n
            cand = word[i:end]
            if cand > ans:
                ans = cand
        return ans
'''

FILES["3407_substring_matching_pattern"] = r'''# LeetCode 3407 - Substring Matching Pattern
# https://leetcode.com/problems/substring-matching-pattern/


class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        i = p.find("*")
        left = p[:i]
        right = p[i + 1 :]
        li = s.find(left)
        if li < 0:
            return False
        return s.find(right, li + len(left)) >= 0
'''

FILES["3408_design_task_manager"] = r'''# LeetCode 3408 - Design Task Manager
# https://leetcode.com/problems/design-task-manager/

from typing import List


class TaskManager:
    def __init__(self, tasks: List[List[int]]) -> None:
        self.pri = {}
        self.user = {}
        self.h = []
        for t in tasks:
            self.add(t[0], t[1], t[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.pri[taskId] = priority
        self.user[taskId] = userId
        self.h.append([priority, taskId, userId])

    def edit(self, taskId: int, newPriority: int) -> None:
        self.pri[taskId] = newPriority
        self.h.append([newPriority, taskId, self.user[taskId]])

    def rmv(self, taskId: int) -> None:
        self.pri.pop(taskId, None)
        self.user.pop(taskId, None)

    def execTop(self) -> int:
        self.h.sort(key=lambda a: (a[0], a[1]))
        while self.h:
            top = self.h.pop()
            p = self.pri.get(top[1])
            if p is not None and p == top[0] and self.user.get(top[1]) == top[2]:
                del self.pri[top[1]]
                uid = self.user.get(top[1])
                del self.user[top[1]]
                return uid
        return -1
'''

FILES["3409_longest_subsequence_with_decreasing_adjacent_difference"] = r'''# LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
# https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        dp = [[0] * 301 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                d = abs(nums[i] - nums[j])
                best = 1
                for pd in range(d, 301):
                    if dp[j][pd] > best:
                        best = dp[j][pd]
                if best + 1 > dp[i][d]:
                    dp[i][d] = best + 1
                if dp[i][d] > ans:
                    ans = dp[i][d]
            if dp[i][0] < 1:
                dp[i][0] = 1
        return ans
'''

FILES["3410_maximize_subarray_sum_after_removing_all_occurrences_of_one_element"] = r'''# LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
# https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        def kadane(a: List[int]) -> int:
            best = -9007199254740991
            cur = 0
            for x in a:
                cur += x
                if cur > best:
                    best = cur
                if cur < 0:
                    cur = 0
            all_neg = True
            mx = a[0]
            for x in a:
                if x > mx:
                    mx = x
                if x >= 0:
                    all_neg = False
            if all_neg:
                return mx
            return best

        ans = kadane(nums)
        uniq = set()
        for x in nums:
            if x < 0:
                uniq.add(x)
        for v in uniq:
            b = [x for x in nums if x != v]
            if not b:
                continue
            cand = kadane(b)
            if cand > ans:
                ans = cand
        return ans
'''

FILES["3411_maximum_subarray_with_equal_products"] = r'''# LeetCode 3411 - Maximum Subarray With Equal Products
# https://leetcode.com/problems/maximum-subarray-with-equal-products/

from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        n = len(nums)
        ans = 1
        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                if prod > 1000000000 // nums[j]:
                    break
                prod *= nums[j]
                if g == 0:
                    g = nums[j]
                    l = nums[j]
                else:
                    g = gcd(g, nums[j])
                    l = l // gcd(l, nums[j]) * nums[j]
                if prod == l * g and j - i + 1 > ans:
                    ans = j - i + 1
        return ans
'''

FILES["3412_find_mirror_score_of_a_string"] = r'''# LeetCode 3412 - Find Mirror Score of a String
# https://leetcode.com/problems/find-mirror-score-of-a-string/


class Solution:
    def calculateScore(self, s: str) -> int:
        stacks = [[] for _ in range(26)]
        ans = 0
        for i, ch in enumerate(s):
            ci = ord(ch) - 97
            mir = 25 - ci
            if stacks[mir]:
                j = stacks[mir].pop()
                ans += i - j
            else:
                stacks[ci].append(i)
        return ans
'''

FILES["3413_maximum_coins_from_k_consecutive_bags"] = r'''# LeetCode 3413 - Maximum Coins From K Consecutive Bags
# https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

from typing import List


class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins = sorted(coins, key=lambda a: a[0])
        ans = 0
        n = len(coins)
        for i in range(n):
            s = 0
            start = coins[i][0]
            end = start + k - 1
            j = i
            while j < n and coins[j][0] <= end:
                l = coins[j][0]
                r = coins[j][1]
                if r > end:
                    r = end
                if l < start:
                    l = start
                if l <= r:
                    s += (r - l + 1) * coins[j][2]
                j += 1
            if s > ans:
                ans = s
        for i in range(n):
            s = 0
            end = coins[i][1]
            start = end - k + 1
            for j in range(i + 1):
                l = coins[j][0]
                r = coins[j][1]
                if l < start:
                    l = start
                if r > end:
                    r = end
                if l <= r:
                    s += (r - l + 1) * coins[j][2]
            if s > ans:
                ans = s
        return ans
'''

FILES["3414_maximum_score_of_non_overlapping_intervals"] = r'''# LeetCode 3414 - Maximum Score of Non-overlapping Intervals
# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

from typing import Dict, List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [{"l": it[0], "r": it[1], "w": it[2], "i": i} for i, it in enumerate(intervals)]
        arr.sort(key=lambda a: a["r"])

        def copyState(s: Dict) -> Dict:
            return {"score": s["score"], "idx": s["idx"][:]}

        def better(a: Dict, b: Dict) -> Dict:
            if a["score"] != b["score"]:
                return a if a["score"] > b["score"] else b
            m = min(len(a["idx"]), len(b["idx"]))
            for i in range(m):
                if a["idx"][i] != b["idx"][i]:
                    return a if a["idx"][i] < b["idx"][i] else b
            return a if len(a["idx"]) <= len(b["idx"]) else b

        dp = [[{"score": 0, "idx": []} for _ in range(5)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            cur = arr[i - 1]
            for t in range(5):
                dp[i][t] = copyState(dp[i - 1][t])
            lo, hi = 0, i - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid]["r"] < cur["l"]:
                    lo = mid + 1
                else:
                    hi = mid
            prev = lo
            for t in range(1, 5):
                prev_state = dp[prev][t - 1]
                cand = copyState(prev_state)
                cand["score"] = prev_state["score"] + cur["w"]
                cand["idx"].append(cur["i"])
                cand["idx"].sort()
                dp[i][t] = better(dp[i][t], cand)
        best = dp[n][0]
        for t in range(1, 5):
            best = better(best, dp[n][t])
        return best["idx"]
'''

FILES["3416_subsequences_with_a_unique_middle_mode_ii"] = r'''# LeetCode 3416 - Subsequences with a Unique Middle Mode II
# https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-ii/

from typing import List


class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        mod = 1000000007
        n = len(nums)
        ans = 0

        def uniqueMode(a: List[int]) -> bool:
            freq = {}
            for x in a:
                freq[x] = freq.get(x, 0) + 1
            best = 0
            cnt = 0
            for f in freq.values():
                if f > best:
                    best = f
                    cnt = 1
                elif f == best:
                    cnt += 1
            return cnt == 1

        for mid in range(2, n - 2):
            for a in range(mid):
                for b in range(a + 1, mid):
                    for c in range(mid + 1, n):
                        for d in range(c + 1, n):
                            if uniqueMode([nums[a], nums[b], nums[mid], nums[c], nums[d]]):
                                ans = (ans + 1) % mod
        return ans
'''

FILES["3417_zigzag_grid_traversal_with_skip"] = r'''# LeetCode 3417 - Zigzag Grid Traversal With Skip
# https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

from typing import List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        ans = []
        skip = False
        for i, row in enumerate(grid):
            if i % 2 == 0:
                for v in row:
                    if not skip:
                        ans.append(v)
                    skip = not skip
            else:
                for j in range(len(row) - 1, -1, -1):
                    if not skip:
                        ans.append(row[j])
                    skip = not skip
        return ans
'''


def main() -> None:
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.py"
        path.write_text(content, encoding="utf-8", newline="\n")
        print("wrote", folder)
    print("part4", len(FILES))


if __name__ == "__main__":
    main()
