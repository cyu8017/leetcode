from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
files = {}

files["2897_apply_operations_on_array_to_maximize_sum_of_squares"] = '''# LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = 1000000007
        cnt = [0] * 32
        for v in nums:
            for b in range(32):
                if (v & (1 << b)) != 0:
                    cnt[b] += 1
        ans = 0
        for _ in range(k):
            cur = 0
            for b in range(32):
                if cnt[b] > 0:
                    cur |= 1 << b
                    cnt[b] -= 1
            ans = (ans + ((cur % mod) * (cur % mod)) % mod) % mod
        return ans
'''

files["2898_maximum_linear_stock_score"] = '''# LeetCode 2898 - Maximum Linear Stock Score
# https://leetcode.com/problems/maximum-linear-stock-score/

from typing import List


class Solution:
    def maxScore(self, prices: List[int]) -> int:
        best = {}
        ans = 0
        for i, price in enumerate(prices):
            key = price - (i + 1)
            cand = best.get(key, 0) + price
            if cand > best.get(key, 0):
                best[key] = cand
            if best[key] > ans:
                ans = best[key]
        return ans
'''

files["2899_last_visited_integers"] = '''# LeetCode 2899 - Last Visited Integers
# https://leetcode.com/problems/last-visited-integers/

from typing import List


class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k = 0
        for v in nums:
            if v != -1:
                seen.append(v)
                k = 0
            else:
                k += 1
                if k > len(seen):
                    ans.append(-1)
                else:
                    ans.append(seen[-k])
        return ans
'''

files["2900_longest_unequal_adjacent_groups_subsequence_i"] = '''# LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = [words[0]]
        last = groups[0]
        for i in range(1, len(words)):
            if groups[i] != last:
                ans.append(words[i])
                last = groups[i]
        return ans
'''

files["2901_longest_unequal_adjacent_groups_subsequence_ii"] = '''# LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        prev = [-1] * n

        def hamming(a: str, b: str) -> int:
            if len(a) != len(b):
                return 100
            return sum(1 for i in range(len(a)) if a[i] != b[i])

        best = 1
        best_i = 0
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and hamming(words[i], words[j]) == 1 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > best:
                best = dp[i]
                best_i = i
        path = []
        i = best_i
        while i != -1:
            path.append(words[i])
            i = prev[i]
        path.reverse()
        return path
'''

files["2902_count_of_sub_multisets_with_bounded_sum"] = '''# LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
# https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

from typing import List


class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        mod = 1000000007
        freq = {}
        total = 0
        for v in nums:
            freq[v] = freq.get(v, 0) + 1
            total += v
        if total < l:
            return 0
        if r > total:
            r = total
        dp = [0] * (r + 1)
        dp[0] = 1
        zeros = freq.get(0, 0)
        freq.pop(0, None)
        for v, c in freq.items():
            ndp = [0] * (r + 1)
            for s in range(r + 1):
                if dp[s] == 0:
                    continue
                k = 0
                while k <= c and s + k * v <= r:
                    ndp[s + k * v] = (ndp[s + k * v] + dp[s]) % mod
                    k += 1
            dp = ndp
        ans = 0
        for s in range(l, r + 1):
            ans = (ans + dp[s]) % mod
        ans = (ans * (zeros + 1)) % mod
        return ans
'''

files["2903_find_indices_with_index_and_value_difference_i"] = '''# LeetCode 2903 - Find Indices With Index and Value Difference I
# https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if abs(j - i) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]
'''

files["2904_shortest_and_lexicographically_smallest_beautiful_string"] = '''# LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        n = len(s)
        for i in range(n):
            ones = 0
            for j in range(i, n):
                if s[j] == "1":
                    ones += 1
                if ones == k:
                    cand = s[i : j + 1]
                    if not ans or len(cand) < len(ans) or (len(cand) == len(ans) and cand < ans):
                        ans = cand
                    break
                if ones > k:
                    break
        return ans
'''

files["2905_find_indices_with_index_and_value_difference_ii"] = '''# LeetCode 2905 - Find Indices With Index and Value Difference II
# https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        min_idx = 0
        max_idx = 0
        for j in range(indexDifference, n):
            i = j - indexDifference
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i
            if nums[j] - nums[min_idx] >= valueDifference:
                return [min_idx, j]
            if nums[max_idx] - nums[j] >= valueDifference:
                return [max_idx, j]
        return [-1, -1]
'''

files["2906_construct_product_matrix"] = '''# LeetCode 2906 - Construct Product Matrix
# https://leetcode.com/problems/construct-product-matrix/

from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        pref = 1
        for i in range(m):
            for j in range(n):
                ans[i][j] = pref
                pref = (pref * (grid[i][j] % mod)) % mod
        suf = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                ans[i][j] = (ans[i][j] * suf) % mod
                suf = (suf * (grid[i][j] % mod)) % mod
        return ans
'''

files["2907_maximum_profitable_triplets_with_increasing_prices_i"] = '''# LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
# https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        ans = -1
        for j in range(n):
            best_l = -1
            best_r = -1
            for i in range(j):
                if prices[i] < prices[j] and profits[i] > best_l:
                    best_l = profits[i]
            for k in range(j + 1, n):
                if prices[k] > prices[j] and profits[k] > best_r:
                    best_r = profits[k]
            if best_l >= 0 and best_r >= 0:
                cand = best_l + profits[j] + best_r
                if cand > ans:
                    ans = cand
        return ans
'''

files["2908_minimum_sum_of_mountain_triplets_i"] = '''# LeetCode 2908 - Minimum Sum of Mountain Triplets I
# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1 << 30
        for j in range(1, n - 1):
            left = 1 << 30
            right = 1 << 30
            for i in range(j):
                if nums[i] < nums[j] and nums[i] < left:
                    left = nums[i]
            for k in range(j + 1, n):
                if nums[k] < nums[j] and nums[k] < right:
                    right = nums[k]
            if left < (1 << 30) and right < (1 << 30):
                cand = left + nums[j] + right
                if cand < ans:
                    ans = cand
        return -1 if ans == (1 << 30) else ans
'''

files["2909_minimum_sum_of_mountain_triplets_ii"] = '''# LeetCode 2909 - Minimum Sum of Mountain Triplets II
# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        mn = 1 << 30
        for i in range(n):
            left[i] = mn
            if nums[i] < mn:
                mn = nums[i]
        mn = 1 << 30
        for i in range(n - 1, -1, -1):
            right[i] = mn
            if nums[i] < mn:
                mn = nums[i]
        ans = 1 << 30
        for j in range(1, n - 1):
            if left[j] < nums[j] and right[j] < nums[j]:
                cand = left[j] + nums[j] + right[j]
                if cand < ans:
                    ans = cand
        return -1 if ans == (1 << 30) else ans
'''

files["2910_minimum_number_of_groups_to_create_a_valid_assignment"] = '''# LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
# https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

from typing import List


class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        freq = {}
        for b in balls:
            freq[b] = freq.get(b, 0) + 1
        counts = list(freq.values())
        min_f = min(counts)
        for size in range(min_f, 0, -1):
            ok = True
            groups = 0
            for c in counts:
                rem = c % (size + 1)
                g2 = c // (size + 1)
                if rem == 0:
                    groups += g2
                elif size - rem <= g2:
                    groups += g2 + 1
                else:
                    ok = False
                    break
            if ok:
                return groups
        return len(balls)
'''

files["2911_minimum_changes_to_make_k_semi_palindromes"] = '''# LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
# https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/


class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        inf = 1 << 20
        cost = [[inf] * n for _ in range(n)]

        def semi_cost(l: int, r: int) -> int:
            length = r - l + 1
            best = inf
            for d in range(1, length):
                if length % d != 0:
                    continue
                chg = 0
                for start in range(d):
                    chars = [s[i] for i in range(l + start, r + 1, d)]
                    i, j = 0, len(chars) - 1
                    while i < j:
                        if chars[i] != chars[j]:
                            chg += 1
                        i += 1
                        j -= 1
                if chg < best:
                    best = chg
            return best

        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = semi_cost(i, j)
        dp = [[inf] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for i in range(1, n + 1):
                for t in range(i - 1):
                    cand = dp[p - 1][t] + cost[t][i - 1]
                    if cand < dp[p][i]:
                        dp[p][i] = cand
        return dp[k][n]
'''

files["2912_number_of_ways_to_reach_destination_in_the_grid"] = '''# LeetCode 2912 - Number of Ways to Reach Destination in the Grid
# https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/

from typing import List


class Solution:
    def numberOfWays(self, n: int, m: int, k: int, source: List[int], dest: List[int]) -> int:
        mod = 1000000007
        sx, sy = source[0], source[1]
        tx, ty = dest[0], dest[1]
        same = row = col = other = 0
        if sx == tx and sy == ty:
            same = 1
        elif sx == tx:
            row = 1
        elif sy == ty:
            col = 1
        else:
            other = 1
        for _ in range(k):
            ns = (row * (m - 1) + col * (n - 1)) % mod
            nr = (same + (row * (m - 2)) % mod + (other * (n - 1)) % mod) % mod
            nc = (same + (col * (n - 2)) % mod + (other * (m - 1)) % mod) % mod
            no = (row * (n - 1) + col * (m - 1) + (other * (n + m - 4)) % mod) % mod
            same, row, col, other = ns, nr, nc, no
        if sx == tx and sy == ty:
            return same
        if sx == tx:
            return row
        if sy == ty:
            return col
        return other
'''

files["2913_subarrays_distinct_element_sum_of_squares_i"] = '''# LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                d = len(seen)
                ans += d * d
        return ans
'''

files["2914_minimum_number_of_changes_to_make_binary_string_beautiful"] = '''# LeetCode 2914 - Minimum Number of Changes to Make Binary String Beautiful
# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/


class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                ans += 1
        return ans
'''

files["2915_length_of_the_longest_subsequence_that_sums_to_target"] = '''# LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
# https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)
        dp[0] = 0
        for v in nums:
            for s in range(target, v - 1, -1):
                if dp[s - v] >= 0 and dp[s - v] + 1 > dp[s]:
                    dp[s] = dp[s - v] + 1
        return dp[target]
'''

written = 0
for folder, content in files.items():
    path = root / folder / "solution.py"
    path.write_text(content, encoding="utf-8", newline="\n")
    written += 1
    print("wrote", folder)
print("p3 written", written)
