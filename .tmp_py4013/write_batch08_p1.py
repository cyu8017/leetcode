from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
files = {}

files["2856_minimum_array_length_after_pair_removals"] = '''# LeetCode 2856 - Minimum Array Length After Pair Removals
# https://leetcode.com/problems/minimum-array-length-after-pair-removals/

from typing import List


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        mx = 0
        for v in nums:
            c = freq.get(v, 0) + 1
            freq[v] = c
            if c > mx:
                mx = c
        if mx <= n // 2:
            return n % 2
        return 2 * mx - n
'''

files["2857_count_pairs_of_points_with_distance_k"] = '''# LeetCode 2857 - Count Pairs of Points With Distance k
# https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

from typing import List


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        freq = {}
        ans = 0
        for x, y in coordinates:
            for a in range(k + 1):
                b = k - a
                ans += freq.get((x ^ a, y ^ b), 0)
            key = (x, y)
            freq[key] = freq.get(key, 0) + 1
        return ans
'''

files["2858_minimum_edge_reversals_so_every_node_is_reachable"] = '''# LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
# https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

from typing import List


class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append((v, 0))
            g[v].append((u, 1))
        ans = [0] * n

        def dfs1(u: int, p: int) -> None:
            for v, ww in g[u]:
                if v == p:
                    continue
                ans[0] += ww
                dfs1(v, u)

        def dfs2(u: int, p: int) -> None:
            for v, ww in g[u]:
                if v == p:
                    continue
                ans[v] = ans[u] + 1 if ww == 0 else ans[u] - 1
                dfs2(v, u)

        dfs1(0, -1)
        dfs2(0, -1)
        return ans
'''

files["2859_sum_of_values_at_indices_with_k_set_bits"] = '''# LeetCode 2859 - Sum of Values at Indices With K Set Bits
# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i, val in enumerate(nums):
            x, bits = i, 0
            while x:
                bits += x & 1
                x >>= 1
            if bits == k:
                ans += val
        return ans
'''

files["2860_happy_students"] = '''# LeetCode 2860 - Happy Students
# https://leetcode.com/problems/happy-students/

from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        ans = 0
        if nums[0] > 0:
            ans += 1
        for i in range(n):
            selected = i + 1
            if selected > nums[i] and (i == n - 1 or selected < nums[i + 1]):
                ans += 1
        return ans
'''

files["2861_maximum_number_of_alloys"] = '''# LeetCode 2861 - Maximum Number of Alloys
# https://leetcode.com/problems/maximum-number-of-alloys/

from typing import List


class Solution:
    def maxNumberOfAlloys(
        self,
        n: int,
        k: int,
        budget: int,
        composition: List[List[int]],
        stock: List[int],
        cost: List[int],
    ) -> int:
        def ok(machines: int) -> bool:
            for comp in composition:
                spend = 0
                for i in range(n):
                    need = machines * comp[i] - stock[i]
                    if need > 0:
                        spend += need * cost[i]
                if spend <= budget:
                    return True
            return False

        lo, hi, ans = 0, 10**9, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
'''

files["2862_maximum_element_sum_of_a_complete_subset_of_indices"] = '''# LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
# https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def square_free(x: int) -> int:
            res = 1
            p = 2
            while p * p <= x:
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                if cnt % 2 == 1:
                    res *= p
                p += 1
            if x > 1:
                res *= x
            return res

        n = len(nums)
        groups = {}
        ans = 0
        for i in range(1, n + 1):
            sf = square_free(i)
            s = groups.get(sf, 0) + nums[i - 1]
            groups[sf] = s
            if s > ans:
                ans = s
        return ans
'''

files["2863_maximum_length_of_semi_decreasing_subarrays"] = '''# LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
# https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        st = []
        for i in range(n - 1, -1, -1):
            if not st or nums[i] > nums[st[-1]]:
                st.append(i)
        for i in range(n):
            while st and nums[i] > nums[st[-1]]:
                j = st.pop()
                if j - i + 1 > ans:
                    ans = j - i + 1
        return ans
'''

files["2864_maximum_odd_binary_number"] = '''# LeetCode 2864 - Maximum Odd Binary Number
# https://leetcode.com/problems/maximum-odd-binary-number/


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        zeros = len(s) - ones
        return "1" * (ones - 1) + "0" * zeros + "1"
'''

files["2865_beautiful_towers_i"] = '''# LeetCode 2865 - Beautiful Towers I
# https://leetcode.com/problems/beautiful-towers-i/

from typing import List


class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        for peak in range(n):
            s = heights[peak]
            mn = heights[peak]
            for i in range(peak - 1, -1, -1):
                if heights[i] < mn:
                    mn = heights[i]
                s += mn
            mn = heights[peak]
            for i in range(peak + 1, n):
                if heights[i] < mn:
                    mn = heights[i]
                s += mn
            if s > ans:
                ans = s
        return ans
'''

files["2866_beautiful_towers_ii"] = '''# LeetCode 2866 - Beautiful Towers II
# https://leetcode.com/problems/beautiful-towers-ii/

from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        left = [0] * n
        st = [-1]
        s = 0
        for i in range(n):
            while len(st) > 1 and maxHeights[st[-1]] >= maxHeights[i]:
                j = st.pop()
                s -= maxHeights[j] * (j - st[-1])
            s += maxHeights[i] * (i - st[-1])
            left[i] = s
            st.append(i)
        right = [0] * n
        st = [n]
        s = 0
        for i in range(n - 1, -1, -1):
            while len(st) > 1 and maxHeights[st[-1]] >= maxHeights[i]:
                j = st.pop()
                s -= maxHeights[j] * (st[-1] - j)
            s += maxHeights[i] * (st[-1] - i)
            right[i] = s
            st.append(i)
        ans = 0
        for i in range(n):
            cand = left[i] + right[i] - maxHeights[i]
            if cand > ans:
                ans = cand
        return ans
'''

files["2867_count_valid_paths_in_a_tree"] = '''# LeetCode 2867 - Count Valid Paths in a Tree
# https://leetcode.com/problems/count-valid-paths-in-a-tree/

from typing import List


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        i = 2
        while i * i <= n:
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
            i += 1
        g = [[] for _ in range(n + 1)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def dfs(u: int, p: int) -> int:
            if is_prime[u]:
                return 0
            sz = 1
            for v in g[u]:
                if v != p:
                    sz += dfs(v, u)
            return sz

        ans = 0
        for u in range(1, n + 1):
            if not is_prime[u]:
                continue
            total = 0
            for v in g[u]:
                c = dfs(v, u)
                ans += c
                ans += total * c
                total += c
        return ans
'''

files["2868_the_wording_game"] = '''# LeetCode 2868 - The Wording Game
# https://leetcode.com/problems/the-wording-game/

from typing import List


class Solution:
    def canAliceWin(self, a: List[str], b: List[str]) -> bool:
        i = j = 0
        last = chr(0)
        alice = True
        while True:
            if alice:
                while i < len(a) and a[i][0] <= last:
                    i += 1
                if i == len(a):
                    return False
                last = a[i][-1]
                i += 1
            else:
                while j < len(b) and b[j][0] <= last:
                    j += 1
                if j == len(b):
                    return True
                last = b[j][-1]
                j += 1
            alice = not alice
'''

files["2869_minimum_operations_to_collect_elements"] = '''# LeetCode 2869 - Minimum Operations to Collect Elements
# https://leetcode.com/problems/minimum-operations-to-collect-elements/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        need = set(range(1, k + 1))
        for i in range(len(nums) - 1, -1, -1):
            need.discard(nums[i])
            if not need:
                return len(nums) - i
        return len(nums)
'''

files["2870_minimum_number_of_operations_to_make_array_empty"] = '''# LeetCode 2870 - Minimum Number of Operations to Make Array Empty
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        for v in nums:
            freq[v] = freq.get(v, 0) + 1
        ans = 0
        for c in freq.values():
            if c == 1:
                return -1
            ans += (c + 2) // 3
        return ans
'''

files["2871_split_array_into_maximum_number_of_subarrays"] = '''# LeetCode 2871 - Split Array Into Maximum Number of Subarrays
# https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

from typing import List


class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        ans = 0
        cur = -1
        for v in nums:
            if cur == -1:
                cur = v
            else:
                cur &= v
            if cur == 0:
                ans += 1
                cur = -1
        return 1 if ans == 0 else ans
'''

files["2872_maximum_number_of_k_divisible_components"] = '''# LeetCode 2872 - Maximum Number of K-Divisible Components
# https://leetcode.com/problems/maximum-number-of-k-divisible-components/

from typing import List


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        ans = 0

        def dfs(u: int, p: int) -> int:
            nonlocal ans
            s = values[u] % k
            for v in g[u]:
                if v == p:
                    continue
                s = (s + dfs(v, u)) % k
            if s == 0:
                ans += 1
            return s

        dfs(0, -1)
        return ans
'''

files["2873_maximum_value_of_an_ordered_triplet_i"] = '''# LeetCode 2873 - Maximum Value of an Ordered Triplet I
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    cand = (nums[i] - nums[j]) * nums[k]
                    if cand > ans:
                        ans = cand
        return ans
'''

files["2874_maximum_value_of_an_ordered_triplet_ii"] = '''# LeetCode 2874 - Maximum Value of an Ordered Triplet II
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        max_i = 0
        max_diff = 0
        for v in nums:
            if max_diff * v > ans:
                ans = max_diff * v
            if max_i - v > max_diff:
                max_diff = max_i - v
            if v > max_i:
                max_i = v
        return ans
'''

files["2875_minimum_size_subarray_in_infinite_array"] = '''# LeetCode 2875 - Minimum Size Subarray in Infinite Array
# https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

from typing import List


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        ans = 1 << 30
        if total > 0:
            loops = target // total
            remain = target % total
            if remain == 0:
                return loops * n
            arr = nums + nums
            left = 0
            s = 0
            best = 1 << 30
            for right in range(len(arr)):
                s += arr[right]
                while s > remain and left <= right:
                    s -= arr[left]
                    left += 1
                if s == remain and right - left + 1 < best:
                    best = right - left + 1
            if best < (1 << 30):
                ans = loops * n + best
        return -1 if ans == (1 << 30) else ans
'''

written = 0
for folder, content in files.items():
    path = root / folder / "solution.py"
    path.write_text(content, encoding="utf-8", newline="\n")
    written += 1
    print("wrote", folder)
print("p1 written", written)
