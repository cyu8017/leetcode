#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["3931_check_adjacent_digit_differences"] = r'''# LeetCode 3931 - Check Adjacent Digit Differences
# https://leetcode.com/problems/check-adjacent-digit-differences/


class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for i in range(1, len(s)):
            if abs(ord(s[i - 1]) - ord(s[i])) > 2:
                return False
        return True
'''

FILES["3932_count_k_th_roots_in_a_range"] = r'''# LeetCode 3932 - Count K Th Roots In A Range
# https://leetcode.com/problems/count-k-th-roots-in-a-range/


class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if k == 1:
            return r - l + 1
        ans = 0
        x = 0
        while True:
            y = 1
            too_big = False
            for _i in range(k):
                if x != 0 and y > r // x:
                    too_big = True
                    break
                y *= x
                if y > r:
                    break
            if too_big or y > r:
                break
            if l <= y <= r:
                ans += 1
            x += 1
        return ans
'''

FILES["3933_largest_local_values_in_a_matrix_ii"] = r'''# LeetCode 3933 - Largest Local Values in a Matrix II
# https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

from typing import List


class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        positions: List[List[List[int]]] = [[] for _ in range(201)]
        for row in range(rows):
            for col in range(cols):
                value = matrix[row][col]
                if value > 0:
                    positions[value].append([row, col])
        answer = 0
        for value in range(1, 201):
            if not positions[value]:
                continue
            prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
            for row in range(rows):
                for col in range(cols):
                    add = 1 if matrix[row][col] > value else 0
                    prefix[row + 1][col + 1] = (
                        prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + add
                    )
            for pos in positions[value]:
                row, col = pos[0], pos[1]
                top = max(0, row - value)
                bottom = min(rows - 1, row + value)
                left = max(0, col - value)
                right = min(cols - 1, col + value)
                greater = (
                    prefix[bottom + 1][right + 1]
                    - prefix[top][right + 1]
                    - prefix[bottom + 1][left]
                    + prefix[top][left]
                )
                for dr in (-value, value):
                    for dc in (-value, value):
                        rr = row + dr
                        cc = col + dc
                        if 0 <= rr < rows and 0 <= cc < cols and matrix[rr][cc] > value:
                            greater -= 1
                if greater == 0:
                    answer += 1
        return answer
'''

FILES["3935_power_update_after_k_th_largest_insertion_i"] = r'''# LeetCode 3935 - Power Update After K Th Largest Insertion I
# https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

from typing import Dict, List, Optional


def merge(st: Dict[int, int], x: int, v: int) -> None:
    c = st.get(x, 0)
    if c + v == 0:
        st.pop(x, None)
    else:
        st[x] = c + v


def firstKey(st: Dict[int, int]) -> Optional[int]:
    best = None
    for k in st:
        if best is None or k < best:
            best = k
    return best


def lastKey(st: Dict[int, int]) -> Optional[int]:
    best = None
    for k in st:
        if best is None or k > best:
            best = k
    return best


def qpow(a: int, b: int, mod: int) -> int:
    ans = 1
    a = int(a)
    while b > 0:
        if (b & 1) != 0:
            ans = (ans * a) % mod
        a = (a * a) % mod
        b >>= 1
    return ans


class Solution:
    def powerUpdate(self, nums: List[int], p: int, queries: List[List[int]]) -> List[int]:
        L: Dict[int, int] = {}
        R: Dict[int, int] = {}
        sz1 = 0
        sz2 = len(nums)
        for x in nums:
            merge(R, x, 1)
        mod = 1000000007
        ans = [0] * len(queries)
        for qi in range(len(queries)):
            val, k = queries[qi][0], queries[qi][1]
            merge(R, val, 1)
            sz2 += 1
            node = firstKey(R)
            merge(R, node, -1)
            sz2 -= 1
            merge(L, node, 1)
            sz1 += 1
            while sz2 < k:
                node = lastKey(L)
                merge(L, node, -1)
                sz1 -= 1
                merge(R, node, 1)
                sz2 += 1
            while sz2 > k:
                node = firstKey(R)
                merge(R, node, -1)
                sz2 -= 1
                merge(L, node, 1)
                sz1 += 1
            x = firstKey(R)
            p = qpow(p, x, mod)
            ans[qi] = p
        return ans
'''

FILES["3936_minimum_swaps_to_move_zeros_to_end"] = r'''# LeetCode 3936 - Minimum Swaps To Move Zeros To End
# https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/

from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        i = 0
        j = n - 1
        while i < j:
            while i < n and nums[i] != 0:
                i += 1
            while j > 0 and nums[j] == 0:
                j -= 1
            if i >= j:
                break
            ans += 1
            i += 1
            j -= 1
        return ans
'''

FILES["3937_minimum_operations_to_make_array_modulo_alternating_i"] = r'''# LeetCode 3937 - Minimum Operations To Make Array Modulo Alternating I
# https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] %= k
        ans = 2147483647
        for x in range(k):
            for y in range(k):
                if x == y:
                    continue
                cnt = 0
                for i in range(len(nums)):
                    target = y if (i & 1) != 0 else x
                    diff = abs(target - nums[i])
                    cnt += min(diff, k - diff)
                ans = min(ans, cnt)
        return ans
'''

FILES["3938_maximum_path_intersection_sum_in_a_grid"] = r'''# LeetCode 3938 - Maximum Path Intersection Sum in a Grid
# https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

from typing import Callable, List


def checkLine(length: int, value: Callable[[int], int]) -> int:
    answer = -2147483648
    best_ending = value(0) + value(1)
    if best_ending > answer:
        answer = best_ending
    for i in range(2, length):
        if value(i - 1) + value(i) > best_ending + value(i):
            best_ending = value(i - 1) + value(i)
        else:
            best_ending += value(i)
        if best_ending > answer:
            answer = best_ending
    return answer


class Solution:
    def maxPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        answer = -2147483648
        for row in range(rows):
            r = row
            answer = max(answer, checkLine(cols, lambda col, r=r: grid[r][col]))
        for col in range(cols):
            c = col
            answer = max(answer, checkLine(rows, lambda row, c=c: grid[row][c]))
        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if grid[row][col] > answer:
                    answer = grid[row][col]
        return answer
'''

FILES["3939_count_non_adjacent_subsets_in_a_rooted_tree"] = r'''# LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
# https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

from typing import List


class Solution:
    def countNonAdjacentSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        mod = 1000000007
        n = len(parent)
        children: List[List[int]] = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        dp0: List[List[int]] = [None] * n
        dp1: List[List[int]] = [None] * n
        for u in range(n - 1, -1, -1):
            a = [0] * k
            b = [0] * k
            a[0] = 1
            b[(((nums[u] % k) + k) % k)] = 1
            for v in children[u]:
                na = [0] * k
                nb = [0] * k
                for x in range(k):
                    for y in range(k):
                        all_child = (dp0[v][y] + dp1[v][y]) % mod
                        na[(x + y) % k] = (na[(x + y) % k] + a[x] * all_child) % mod
                        nb[(x + y) % k] = (nb[(x + y) % k] + b[x] * dp0[v][y]) % mod
                a = na
                b = nb
            dp0[u] = a
            dp1[u] = b
        ans = (dp0[0][0] + dp1[0][0] - 1) % mod
        if ans < 0:
            ans += mod
        return ans
'''

FILES["3940_limit_occurrences_in_sorted_array"] = r'''# LeetCode 3940 - Limit Occurrences In Sorted Array
# https://leetcode.com/problems/limit-occurrences-in-sorted-array/

from typing import List


class Solution:
    def limitOccurrences(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        cnt = 1
        l = 1
        for r in range(1, n):
            if nums[r] != nums[r - 1]:
                cnt = 1
            else:
                cnt += 1
            if cnt <= k:
                nums[l] = nums[r]
                l += 1
        return nums[:l]
'''

FILES["3941_password_strength"] = r'''# LeetCode 3941 - Password Strength
# https://leetcode.com/problems/password-strength/


class Solution:
    def passwordStrength(self, password: str) -> int:
        st = set(password)
        ans = 0
        for ch in st:
            if ch.islower():
                ans += 1
            elif ch.isupper():
                ans += 2
            elif ch.isdigit():
                ans += 3
            else:
                ans += 5
        return ans
'''

FILES["3942_minimum_operations_to_sort_a_permutation"] = r'''# LeetCode 3942 - Minimum Operations To Sort A Permutation
# https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

from typing import List


def check(nums: List[int], zero: int, step: int) -> bool:
    n = len(nums)
    for i in range(1, n):
        prev = ((zero + (i - 1) * step) % n + n) % n
        curr = ((zero + i * step) % n + n) % n
        if nums[prev] > nums[curr]:
            return False
    return True


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = 0
        for i in range(n):
            if nums[i] == 0:
                zero = i
                break
        ans = 2147483647
        if check(nums, zero, 1):
            ans = min(ans, zero)
            ans = min(ans, n - zero + 2)
        if check(nums, zero, -1):
            ans = min(ans, zero + 2)
            ans = min(ans, n - zero)
        return -1 if ans == 2147483647 else ans
'''

FILES["3943_number_of_pairs_after_increment"] = r'''# LeetCode 3943 - Number of Pairs After Increment
# https://leetcode.com/problems/number-of-pairs-after-increment/

from typing import Dict, List


def rebuild(freq: List[Dict[int, int]], nums2: List[int], b: int, blockSize: int, n: int) -> None:
    freq[b].clear()
    end = min((b + 1) * blockSize, n)
    for i in range(b * blockSize, end):
        freq[b][nums2[i]] = freq[b].get(nums2[i], 0) + 1


def push(lazy: List[int], nums2: List[int], b: int, blockSize: int, n: int) -> None:
    if lazy[b] != 0:
        end = min((b + 1) * blockSize, n)
        for i in range(b * blockSize, end):
            nums2[i] += lazy[b]
        lazy[b] = 0


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        block_size = 225
        n = len(nums2)
        blocks = (n + block_size - 1) // block_size
        lazy = [0] * blocks
        freq: List[Dict[int, int]] = [{} for _ in range(blocks)]
        for b in range(blocks):
            rebuild(freq, nums2, b, block_size, n)
        fixed: Dict[int, int] = {}
        for x in nums1:
            fixed[x] = fixed.get(x, 0) + 1
        answer: List[int] = []
        for q in queries:
            if q[0] == 1:
                l, r, delta = q[1], q[2], q[3]
                first = l // block_size
                last = r // block_size
                if first == last:
                    push(lazy, nums2, first, block_size, n)
                    for i in range(l, r + 1):
                        nums2[i] += delta
                    rebuild(freq, nums2, first, block_size, n)
                    continue
                push(lazy, nums2, first, block_size, n)
                for i in range(l, (first + 1) * block_size):
                    nums2[i] += delta
                rebuild(freq, nums2, first, block_size, n)
                push(lazy, nums2, last, block_size, n)
                for i in range(last * block_size, r + 1):
                    nums2[i] += delta
                rebuild(freq, nums2, last, block_size, n)
                for b in range(first + 1, last):
                    lazy[b] += delta
            else:
                total = 0
                for a, count_a in fixed.items():
                    target = q[1] - a
                    for b in range(blocks):
                        c = freq[b].get(target - lazy[b])
                        if c is not None:
                            total += count_a * c
                answer.append(total)
        return answer
'''

FILES["3944_minimum_operations_to_make_array_modulo_alternating_ii"] = r'''# LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
# https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

from typing import List


def costs(freq: List[int], k: int) -> List[int]:
    dbl = [0] * (2 * k)
    for i in range(2 * k):
        dbl[i] = freq[i % k]
    count_prefix = [0] * (2 * k + 1)
    weighted_prefix = [0] * (2 * k + 1)
    for i in range(2 * k):
        count_prefix[i + 1] = count_prefix[i] + dbl[i]
        weighted_prefix[i + 1] = weighted_prefix[i] + i * dbl[i]
    res = [0] * k
    cw = k // 2
    cc = (k - 1) // 2
    for t in range(k):
        cnt = count_prefix[t + cw + 1] - count_prefix[t]
        s = weighted_prefix[t + cw + 1] - weighted_prefix[t]
        res[t] += s - t * cnt
        if cc > 0:
            cnt2 = count_prefix[t + k] - count_prefix[t + k - cc]
            sum2 = weighted_prefix[t + k] - weighted_prefix[t + k - cc]
            res[t] += (t + k) * cnt2 - sum2
    return res


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        even_freq = [0] * k
        odd_freq = [0] * k
        for i in range(len(nums)):
            if i % 2 == 0:
                even_freq[nums[i] % k] += 1
            else:
                odd_freq[nums[i] % k] += 1
        even_cost = costs(even_freq, k)
        odd_cost = costs(odd_freq, k)
        best1 = 1 << 62
        best2 = 1 << 62
        best_index = -1
        for i in range(k):
            x = odd_cost[i]
            if x < best1:
                best2 = best1
                best1 = x
                best_index = i
            elif x < best2:
                best2 = x
        ans = 1 << 62
        for x in range(k):
            other = best2 if x == best_index else best1
            ans = min(ans, even_cost[x] + other)
        return ans
'''

FILES["3945_digit_frequency_score"] = r'''# LeetCode 3945 - Digit Frequency Score
# https://leetcode.com/problems/digit-frequency-score/


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += n % 10
            n //= 10
        return ans
'''

FILES["3946_maximum_number_of_items_from_sale_i"] = r'''# LeetCode 3946 - Maximum Number Of Items From Sale I
# https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        f = [0] * (budget + 1)
        mn = 2147483647
        for item in items:
            factor, price = item[0], item[1]
            mn = min(mn, price)
            cnt = 0
            for j_item in items:
                if j_item[0] % factor == 0:
                    cnt += 1
            for j in range(budget, price - 1, -1):
                f[j] = max(f[j], f[j - price] + cnt)
        ans = 0
        for i in range(budget + 1):
            extra = (budget - i) // mn
            ans = max(ans, f[i] + extra)
        return ans
'''


def main() -> None:
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.py"
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"wrote {folder}")
    print(f"done {len(FILES)}")


if __name__ == "__main__":
    main()
