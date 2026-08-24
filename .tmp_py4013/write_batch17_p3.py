#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["3907_count_smaller_elements_with_opposite_parity"] = r'''# LeetCode 3907 - Count Smaller Elements With Opposite Parity
# https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

from typing import List


class BIT3907:
    def __init__(self, n_: int):
        self.n = n_
        self.c = [0] * (n_ + 1)

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
    def countSmallerOppositeParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sorted_nums = sorted(nums)
        m = 0
        for i in range(len(sorted_nums)):
            if i == 0 or sorted_nums[i] != sorted_nums[i - 1]:
                sorted_nums[m] = sorted_nums[i]
                m += 1
        sorted_nums = sorted_nums[:m]
        bits = [BIT3907(m), BIT3907(m)]
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            lo = 0
            hi = len(sorted_nums)
            while lo < hi:
                mid = (lo + hi) >> 1
                if sorted_nums[mid] < nums[i]:
                    lo = mid + 1
                else:
                    hi = mid
            x = lo + 1
            ans[i] = bits[(nums[i] & 1) ^ 1].query(x - 1)
            bits[nums[i] & 1].update(x, 1)
        return ans
'''

FILES["3908_valid_digit_number"] = r'''# LeetCode 3908 - Valid Digit Number
# https://leetcode.com/problems/valid-digit-number/


class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        has_x = False
        while n > 9:
            has_x = has_x or (n % 10 == x)
            n //= 10
        return has_x and (n != x)
'''

FILES["3909_compare_sums_of_bitonic_parts"] = r'''# LeetCode 3909 - Compare Sums Of Bitonic Parts
# https://leetcode.com/problems/compare-sums-of-bitonic-parts/

from typing import List


class Solution:
    def compareBitonicSums(self, nums: List[int]) -> int:
        l = nums[0]
        r = 0
        for x in nums:
            r += x
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                break
            l += nums[i]
            r -= nums[i - 1]
        if l == r:
            return -1
        if l > r:
            return 0
        return 1
'''

FILES["3910_count_connected_subgraphs_with_even_node_sum"] = r'''# LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
# https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

from typing import List


class Solution:
    def evenSumSubgraphs(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g: List[List[int]] = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        m = (1 << n) - 1
        vis = 0

        def dfs(u: int) -> None:
            nonlocal vis
            vis |= 1 << u
            for v in g[u]:
                if ((vis >> v) & 1) == 0:
                    dfs(v)

        ans = 0
        for sub in range(1, m + 1):
            s = 0
            for i in range(n):
                if ((sub >> i) & 1) != 0:
                    s += nums[i]
            if s % 2 != 0:
                continue
            vis = m ^ sub
            start = sub.bit_length() - 1
            if sub == 0:
                start = 0
            dfs(start)
            if vis == m:
                ans += 1
        return ans
'''

FILES["3911_k_th_smallest_remaining_even_integer_in_subarray_queries"] = r'''# LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
# https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

from typing import List


def UpperBound3911(a: List[int], x: int) -> int:
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def kthSmallestEven(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        even_prefix = [0] * (n + 1)
        for i in range(n):
            even_prefix[i + 1] = even_prefix[i] + (1 if nums[i] % 2 == 0 else 0)
        ans = [0] * len(queries)
        for qi in range(len(queries)):
            l, r = queries[qi][0], queries[qi][1]
            k = queries[qi][2]
            lo = 1
            hi = k + (r - l + 1)
            while lo < hi:
                mid = (lo + hi) // 2
                pos = UpperBound3911(nums, 2 * mid)
                if pos > r + 1:
                    pos = r + 1
                removed = 0
                if pos > l:
                    removed = even_prefix[pos] - even_prefix[l]
                if mid - removed >= k:
                    hi = mid
                else:
                    lo = mid + 1
            ans[qi] = 2 * lo
        return ans
'''

FILES["3912_valid_elements_in_an_array"] = r'''# LeetCode 3912 - Valid Elements In An Array
# https://leetcode.com/problems/valid-elements-in-an-array/

from typing import List


class Solution:
    def findValidElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], nums[i])
        left = 0
        ans: List[int] = []
        for i in range(n):
            x = nums[i]
            if x > left or i == n - 1 or x > right[i + 1]:
                ans.append(x)
            left = max(left, x)
        return ans
'''

FILES["3913_sort_vowels_by_frequency"] = r'''# LeetCode 3913 - Sort Vowels By Frequency
# https://leetcode.com/problems/sort-vowels-by-frequency/

from typing import Dict, List


class Solution:
    def sortVowels(self, s: str) -> str:
        st = set(["a", "e", "i", "o", "u"])
        vowels: List[str] = []
        cnt: Dict[str, int] = {}
        for c in s:
            if c not in st:
                continue
            if c not in cnt:
                vowels.append(c)
                cnt[c] = 0
            cnt[c] += 1
        vowels.sort(key=lambda ch: -cnt[ch])
        ans = list(s)
        i = 0
        for k in range(len(s)):
            if s[k] not in st:
                continue
            ch = vowels[i]
            ans[k] = ch
            cnt[ch] -= 1
            if cnt[ch] == 0:
                i += 1
        return "".join(ans)
'''

FILES["3914_minimum_operations_to_make_array_non_decreasing"] = r'''# LeetCode 3914 - Minimum Operations To Make Array Non Decreasing
# https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            ans += max(0, nums[i - 1] - nums[i])
        return ans
'''

FILES["3915_maximum_sum_of_alternating_subsequence_with_distance_at_least_k"] = r'''# LeetCode 3915 - Maximum Sum Of Alternating Subsequence With Distance At Least K
# https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

from typing import List


class Fenwick3915:
    def __init__(self, n: int):
        self.f = [0] * n

    def update(self, i: int, val: int) -> None:
        while i < len(self.f):
            self.f[i] = max(self.f[i], val)
            i += i & -i

    def preMax(self, i: int) -> int:
        res = 0
        while i > 0:
            res = max(res, self.f[i])
            i &= i - 1
        return res


class Solution:
    def maxAlternatingSum(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        m = 0
        for i in range(len(sorted_nums)):
            if i == 0 or sorted_nums[i] != sorted_nums[i - 1]:
                sorted_nums[m] = sorted_nums[i]
                m += 1
        sorted_nums = sorted_nums[:m]
        n = len(nums)
        f_inc = [0] * n
        f_dec = [0] * n
        inc = Fenwick3915(m + 1)
        dec = Fenwick3915(m + 1)
        ans = 0
        ranks = [0] * n
        for i in range(n):
            x = nums[i]
            if i >= k:
                j = ranks[i - k]
                inc.update(m - j, f_inc[i - k])
                dec.update(j + 1, f_dec[i - k])
            lo = 0
            hi = len(sorted_nums)
            while lo < hi:
                mid = (lo + hi) >> 1
                if sorted_nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            ranks[i] = lo
            f_inc[i] = dec.preMax(lo) + x
            f_dec[i] = inc.preMax(m - 1 - lo) + x
            ans = max(ans, max(f_inc[i], f_dec[i]))
        return ans
'''

FILES["3916_number_of_zigzag_arrays_iii"] = r'''# LeetCode 3916 - Number of ZigZag Arrays III
# https://leetcode.com/problems/number-of-zigzag-arrays-iii/

from typing import List


def powm3916(a: int, e: int, mod: int) -> int:
    res = 1
    A = a
    E = e
    MOD = mod
    while E > 0:
        if (E & 1) != 0:
            res = res * A % MOD
        A = A * A % MOD
        E >>= 1
    return res


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 1000000007
        points = n + 1
        values = [0] * (points + 1)
        for m in range(1, points + 1):
            up = [0] * m
            down = [0] * m
            for value in range(m):
                up[value] = value
                down[value] = m - 1 - value
            for _length in range(3, n + 1):
                next_up = [0] * m
                next_down = [0] * m
                prefix = 0
                for value in range(m):
                    next_up[value] = prefix
                    prefix = (prefix + down[value]) % mod
                suffix = 0
                for value in range(m - 1, -1, -1):
                    next_down[value] = suffix
                    suffix = (suffix + up[value]) % mod
                up = next_up
                down = next_down
            for value in range(m):
                values[m] = (values[m] + up[value] + down[value]) % mod
        x = (r - l + 1) % mod
        if r - l + 1 <= points:
            return values[r - l + 1]
        prefix_a = [0] * (points + 2)
        suffix_a = [0] * (points + 2)
        prefix_a[0] = 1
        for i in range(1, points + 1):
            prefix_a[i] = prefix_a[i - 1] * ((x - i + mod) % mod) % mod
        suffix_a[points + 1] = 1
        for i in range(points, 0, -1):
            suffix_a[i] = suffix_a[i + 1] * ((x - i + mod) % mod) % mod
        factorial = [0] * (points + 1)
        factorial[0] = 1
        for i in range(1, points + 1):
            factorial[i] = factorial[i - 1] * i % mod
        answer = 0
        for i in range(1, points + 1):
            numerator = prefix_a[i - 1] * suffix_a[i + 1] % mod
            denominator = factorial[i - 1] * factorial[points - i] % mod
            term = values[i] * numerator % mod * powm3916(denominator, mod - 2, mod) % mod
            if (points - i) % 2 == 1:
                answer -= term
            else:
                answer += term
            answer %= mod
        if answer < 0:
            answer += mod
        return answer
'''

FILES["3917_count_indices_with_opposite_parity"] = r'''# LeetCode 3917 - Count Indices With Opposite Parity
# https://leetcode.com/problems/count-indices-with-opposite-parity/

from typing import List


class Solution:
    def countOppositeParity(self, nums: List[int]) -> List[int]:
        cnt = [0, 0]
        for x in nums:
            cnt[x & 1] += 1
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            x = nums[i]
            cnt[x & 1] -= 1
            ans[i] = cnt[(x & 1) ^ 1]
        return ans
'''

FILES["3918_sum_of_primes_between_number_and_its_reverse"] = r'''# LeetCode 3918 - Sum Of Primes Between Number And Its Reverse
# https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

from typing import List, Optional

isPrime3918: Optional[List[bool]] = None


def Init3918() -> None:
    global isPrime3918
    if isPrime3918 is not None:
        return
    isPrime3918 = [True] * 1001
    isPrime3918[0] = isPrime3918[1] = False
    i = 2
    while i * i <= 1000:
        if isPrime3918[i]:
            j = i * i
            while j <= 1000:
                isPrime3918[j] = False
                j += i
        i += 1


class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        Init3918()
        r = 0
        x = n
        while x > 0:
            r = r * 10 + x % 10
            x //= 10
        low = min(n, r)
        high = max(n, r)
        ans = 0
        for v in range(low, high + 1):
            if isPrime3918[v]:
                ans += v
        return ans
'''

FILES["3919_minimum_cost_to_move_between_indices"] = r'''# LeetCode 3919 - Minimum Cost To Move Between Indices
# https://leetcode.com/problems/minimum-cost-to-move-between-indices/

from typing import List


class Solution:
    def minCost(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        s1 = [0] * n
        s2 = [0] * n
        for i in range(1, n):
            c1 = 1
            if i > 1 and nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1]:
                c1 = nums[i] - nums[i - 1]
            c2 = 1
            if i < n - 1 and nums[i] - nums[i - 1] > nums[i + 1] - nums[i]:
                c2 = nums[i] - nums[i - 1]
            s1[i] = s1[i - 1] + c1
            s2[i] = s2[i - 1] + c2
        ans = [0] * len(queries)
        for i in range(len(queries)):
            l, r = queries[i][0], queries[i][1]
            ans[i] = (s1[r] - s1[l]) if l < r else (s2[l] - s2[r])
        return ans
'''

FILES["3920_maximize_fixed_points_after_deletions"] = r'''# LeetCode 3920 - Maximize Fixed Points After Deletions
# https://leetcode.com/problems/maximize-fixed-points-after-deletions/

from typing import List


class Solution:
    def maxFixedPoints(self, nums: List[int]) -> int:
        tails: List[int] = []
        for i in range(len(nums)):
            if i < nums[i]:
                continue
            d = i - nums[i]
            lo = 0
            hi = len(tails)
            while lo < hi:
                mid = (lo + hi) >> 1
                if tails[mid] < d:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == len(tails):
                tails.append(d)
            else:
                tails[lo] = d
        return len(tails)
'''

FILES["3921_score_validator"] = r'''# LeetCode 3921 - Score Validator
# https://leetcode.com/problems/score-validator/

from typing import List


class Solution:
    def scoreValidator(self, events: List[str]) -> List[int]:
        score = 0
        counter = 0
        for event_str in events:
            is_num = len(event_str) > 0
            num = 0
            start = 0
            if is_num and event_str[0] == "-":
                start = 1
            for i in range(start, len(event_str)):
                if event_str[i] < "0" or event_str[i] > "9":
                    is_num = False
                    break
                num = num * 10 + (ord(event_str[i]) - 48)
            if is_num and not (start == 1 and len(event_str) == 1):
                if start == 1:
                    num = -num
                score += num
            elif event_str == "W":
                counter += 1
                if counter == 10:
                    break
            else:
                score += 1
        return [score, counter]
'''

FILES["3922_minimum_flips_to_make_binary_string_coherent"] = r'''# LeetCode 3922 - Minimum Flips to Make Binary String Coherent
# https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/


class Solution:
    def minFlips(self, s: str) -> int:
        ones = 0
        for c in s:
            if c == "1":
                ones += 1
        answer = ones
        if ones > 0:
            answer = ones - 1
        zeros = len(s) - ones
        answer = min(answer, zeros)
        if len(s) >= 2:
            cost = 0
            for i in range(len(s)):
                want = "1" if (i == 0 or i == len(s) - 1) else "0"
                if s[i] != want:
                    cost += 1
            answer = min(answer, cost)
        return answer
'''

FILES["3923_minimum_generations_to_target_point"] = r'''# LeetCode 3923 - Minimum Generations to Target Point
# https://leetcode.com/problems/minimum-generations-to-target-point/

from typing import Dict, List


class P:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def key(self) -> str:
        return f"{self.a},{self.b},{self.c}"


class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        target_key = f"{target[0]},{target[1]},{target[2]}"
        generation: Dict[str, int] = {}
        all_pts: List[P] = []
        for values in points:
            p = P(values[0], values[1], values[2])
            generation[p.key()] = 0
            all_pts.append(p)
        if target_key in generation:
            return generation[target_key]
        current = 1
        while True:
            limit = len(all_pts)
            added: List[P] = []
            for i in range(limit):
                for j in range(i + 1, limit):
                    pi = all_pts[i]
                    pj = all_pts[j]
                    if pi.a == pj.a and pi.b == pj.b and pi.c == pj.c:
                        continue
                    p = P((pi.a + pj.a) // 2, (pi.b + pj.b) // 2, (pi.c + pj.c) // 2)
                    key = p.key()
                    if key not in generation:
                        generation[key] = current
                        added.append(p)
            if target_key in generation:
                return generation[target_key]
            if len(added) == 0:
                return -1
            for p in added:
                all_pts.append(p)
            current += 1
'''

FILES["3924_minimum_threshold_path_with_limited_heavy_edges"] = r'''# LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
# https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

from typing import List


def can(n: int, g: List[List[List[int]]], source: int, target: int, k: int, threshold: int) -> bool:
    inf = 1000000000
    dist = [inf] * n
    dist[source] = 0
    dq: List[int] = [source]
    while dq:
        u = dq.pop(0)
        for e in g[u]:
            to, weight = e[0], e[1]
            cost = 1 if weight > threshold else 0
            if dist[u] + cost >= dist[to] or dist[u] + cost > k:
                continue
            dist[to] = dist[u] + cost
            if cost == 0:
                dq.insert(0, to)
            else:
                dq.append(to)
    return dist[target] <= k


class Solution:
    def minThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        if source == target:
            return 0
        g: List[List[List[int]]] = [[] for _ in range(n)]
        max_weight = 0
        for e in edges:
            g[e[0]].append([e[1], e[2]])
            g[e[1]].append([e[0], e[2]])
            max_weight = max(max_weight, e[2])
        if not can(n, g, source, target, k, max_weight):
            return -1
        lo = 0
        hi = max_weight
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if can(n, g, source, target, k, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
'''

FILES["3925_concatenate_array_with_reverse"] = r'''# LeetCode 3925 - Concatenate Array With Reverse
# https://leetcode.com/problems/concatenate-array-with-reverse/

from typing import List


class Solution:
    def concatWithReverse(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[n - i - 1]
        return ans
'''

FILES["3926_count_valid_word_occurrences"] = r'''# LeetCode 3926 - Count Valid Word Occurrences
# https://leetcode.com/problems/count-valid-word-occurrences/

from typing import Dict, List


class Solution:
    def countWordOccurrences(self, chunks: List[str], queries: List[str]) -> List[int]:
        sb = ""
        for c in chunks:
            sb += c
        s = sb
        n = len(s)
        cnt: Dict[str, int] = {}
        i = 0
        while i < n:
            if s[i] == " " or s[i] == "-":
                i += 1
                continue
            j = i
            while j < n and s[j] != " " and (s[j] != "-" or (j + 1 < n and s[j + 1] != " " and s[j + 1] != "-")):
                j += 1
            word = s[i:j]
            cnt[word] = cnt.get(word, 0) + 1
            i = j
        ans = [0] * len(queries)
        for k in range(len(queries)):
            ans[k] = cnt.get(queries[k], 0)
        return ans
'''

FILES["3927_minimize_array_sum_using_divisible_replacements"] = r'''# LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
# https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

from typing import List


class Solution:
    def minArraySum(self, nums: List[int]) -> int:
        maximum = 0
        present = [False] * 100001
        for value in nums:
            present[value] = True
            if value > maximum:
                maximum = value
        best = [0] * (maximum + 1)
        for divisor in range(1, maximum + 1):
            if not present[divisor]:
                continue
            multiple = divisor
            while multiple <= maximum:
                if best[multiple] == 0:
                    best[multiple] = divisor
                multiple += divisor
        answer = 0
        for value in nums:
            answer += best[value]
        return answer
'''

FILES["3928_minimum_cost_to_buy_apples_ii"] = r'''# LeetCode 3928 - Minimum Cost to Buy Apples II
# https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

from typing import Dict, List


def dijkstra(n: int, g: List[List[Dict]], source: int, carrying: bool, inf: int) -> List[int]:
    dist = [inf] * n
    dist[source] = 0
    pq = [[0, source]]
    while pq:
        pq.sort(key=lambda a: a[0])
        cur = pq.pop(0)
        d, node = cur[0], cur[1]
        if d != dist[node]:
            continue
        for e in g[node]:
            weight = e["full"] if carrying else e["empty"]
            nxt = d + weight
            if nxt < dist[e["to"]]:
                dist[e["to"]] = nxt
                pq.append([nxt, e["to"]])
    return dist


class Solution:
    def minCostToBuyApples(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        g: List[List[Dict]] = [[] for _ in range(n)]
        for road in roads:
            empty = road[2]
            full = road[2] * road[3]
            g[road[0]].append({"to": road[1], "empty": empty, "full": full})
            g[road[1]].append({"to": road[0], "empty": empty, "full": full})
        inf = 2 ** 62
        answer = [0] * n
        for source in range(n):
            empty_dist = dijkstra(n, g, source, False, inf)
            full_dist = dijkstra(n, g, source, True, inf)
            best = prices[source]
            for shop in range(n):
                if empty_dist[shop] == inf or full_dist[shop] == inf:
                    continue
                total = empty_dist[shop] + full_dist[shop] + prices[shop]
                if total < best:
                    best = total
            answer[source] = best
        return answer
'''

FILES["3929_minimum_partition_score_ii"] = r'''# LeetCode 3929 - Minimum Partition Score II
# https://leetcode.com/problems/minimum-partition-score-ii/

from typing import List


class Line:
    def __init__(self, slope: int = 0, intercept: int = 0, count: int = 0, valid: bool = False):
        self.slope = slope
        self.intercept = intercept
        self.count = count
        self.valid = valid


class State:
    def __init__(self, value: int = 0, count: int = 0, valid: bool = False):
        self.value = value
        self.count = count
        self.valid = valid


def better(a: State, b: State) -> State:
    if not a.valid:
        return b
    if not b.valid:
        return a
    if a.value != b.value:
        return a if a.value < b.value else b
    return a if a.count >= b.count else b


def evaluate(line: Line, x: int) -> State:
    if not line.valid:
        return State()
    return State(line.slope * x + line.intercept, line.count, True)


class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def insert(tree: List[Line], node: int, left: int, right: int, line: Line) -> None:
            if not tree[node].valid:
                tree[node] = line
                return
            mid = (left + right) // 2
            x_left = prefix[left]
            x_mid = prefix[mid]
            left_better = better(evaluate(line, x_left), evaluate(tree[node], x_left))
            mid_better = better(evaluate(line, x_mid), evaluate(tree[node], x_mid))
            line_wins_left = left_better.value == evaluate(line, x_left).value and left_better.count == line.count
            line_wins_mid = mid_better.value == evaluate(line, x_mid).value and mid_better.count == line.count
            if line_wins_mid:
                tmp = tree[node]
                tree[node] = line
                line = tmp
            if left == right:
                return
            if line_wins_left != line_wins_mid:
                insert(tree, node * 2, left, mid, line)
            else:
                insert(tree, node * 2 + 1, mid + 1, right, line)

        def query(tree: List[Line], node: int, left: int, right: int, index: int) -> State:
            result = evaluate(tree[node], prefix[index])
            if left == right:
                return result
            mid = (left + right) // 2
            if index <= mid:
                return better(result, query(tree, node * 2, left, mid, index))
            return better(result, query(tree, node * 2 + 1, mid + 1, right, index))

        def run(penalty: int) -> State:
            tree = [Line() for _ in range(4 * (n + 1))]
            insert(tree, 1, 0, n, Line(0, 0, 0, True))
            current = State()
            for i in range(1, n + 1):
                best = query(tree, 1, 0, n, i)
                x = prefix[i]
                current = State(best.value + x * x + x + penalty, best.count + 1, True)
                insert(tree, 1, 0, n, Line(-2 * x, current.value + x * x - x, current.count, True))
            return current

        bound = prefix[n] * prefix[n] + prefix[n] + 1
        low = 0
        high = bound
        while low < high:
            mid = low + (high - low + 1) // 2
            if run(mid).count >= k:
                low = mid
            else:
                high = mid - 1
        state = run(low)
        return (state.value - low * k) // 2
'''


def main() -> None:
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.py"
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"wrote {folder}")
    print(f"done {len(FILES)}")


if __name__ == "__main__":
    main()
