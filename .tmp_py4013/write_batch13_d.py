from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def write(folder: str, body: str) -> None:
    (ROOT / folder / "solution.py").write_text(body.lstrip("\n"), encoding="utf-8")


write(
    "3467_transform_array_by_parity",
    '''
# LeetCode 3467 - Transform Array by Parity
# https://leetcode.com/problems/transform-array-by-parity/

from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] %= 2
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
''',
)

write(
    "3468_find_the_number_of_copy_arrays",
    '''
# LeetCode 3468 - Find the Number of Copy Arrays
# https://leetcode.com/problems/find-the-number-of-copy-arrays/

from typing import List


class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        n = len(original)
        lo, hi = bounds[0][0], bounds[0][1]
        for i in range(1, n):
            diff = original[i] - original[i - 1]
            lo2, hi2 = bounds[i][0], bounds[i][1]
            nlo, nhi = lo + diff, hi + diff
            if nlo < lo2:
                nlo = lo2
            if nhi > hi2:
                nhi = hi2
            if nlo > nhi:
                return 0
            lo, hi = nlo, nhi
        return hi - lo + 1
''',
)

write(
    "3469_find_minimum_cost_to_remove_array_elements",
    '''
# LeetCode 3469 - Find Minimum Cost to Remove Array Elements
# https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

from typing import List


class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def max2(a: int, b: int) -> int:
            return a if a > b else b

        def min3(a: int, b: int, c: int) -> int:
            return min(a, b, c)

        def key(i: int, prev: int) -> int:
            return (i << 32) | (prev & 0xFFFFFFFF)

        def dfs(i: int, prev: int) -> int:
            if i >= n:
                return 0 if prev == -1 else nums[prev]
            k = key(i, prev)
            if k in memo:
                return memo[k]
            if prev == -1:
                if i + 1 >= n:
                    res = nums[i]
                elif i + 2 >= n:
                    res = max2(nums[i], nums[i + 1])
                else:
                    a, b, c = nums[i], nums[i + 1], nums[i + 2]
                    res = min3(
                        max2(b, c) + dfs(i + 3, i),
                        max2(a, c) + dfs(i + 3, i + 1),
                        max2(a, b) + dfs(i + 3, i + 2),
                    )
            else:
                if i + 1 >= n:
                    res = max2(nums[prev], nums[i])
                else:
                    a, b, c = nums[prev], nums[i], nums[i + 1]
                    res = min3(
                        max2(b, c) + dfs(i + 2, prev),
                        max2(a, c) + dfs(i + 2, i),
                        max2(a, b) + dfs(i + 2, i + 1),
                    )
            memo[k] = res
            return res

        return dfs(0, -1)
''',
)

write(
    "3470_permutations_iv",
    '''
# LeetCode 3470 - Permutations IV
# https://leetcode.com/problems/permutations-iv/

from typing import List


class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        fact = [0] * (n + 1)
        fact[0] = 1
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i
            if fact[i] > 10**18:
                fact[i] = 10**18 + 1
        used = [False] * (n + 1)
        ans: List[int] = []
        kk = k

        def dfs(pos: int) -> bool:
            nonlocal kk
            if pos == n:
                return True
            for x in range(1, n + 1):
                if used[x]:
                    continue
                if pos > 0 and (ans[pos - 1] % 2 == x % 2):
                    continue
                rem = n - pos - 1
                cnt = fact[rem]
                if cnt >= kk:
                    used[x] = True
                    ans.append(x)
                    if dfs(pos + 1):
                        return True
                    ans.pop()
                    used[x] = False
                else:
                    kk -= cnt
            return False

        if not dfs(0):
            return []
        return ans
''',
)

write(
    "3471_find_the_largest_almost_missing_integer",
    '''
# LeetCode 3471 - Find the Largest Almost Missing Integer
# https://leetcode.com/problems/find-the-largest-almost-missing-integer/

from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = {}
        for i in range(n - k + 1):
            seen = set()
            for j in range(i, i + k):
                seen.add(nums[j])
            for x in seen:
                cnt[x] = cnt.get(x, 0) + 1
        ans = -1
        for key, value in cnt.items():
            if value == 1 and key > ans:
                ans = key
        return ans
''',
)

write(
    "3472_longest_palindromic_subsequence_after_at_most_k_operations",
    '''
# LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
# https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/


class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(n)]

        def dist_circ(a: str, b: str) -> int:
            d = abs(ord(a) - ord(b))
            return min(d, 26 - d)

        def dfs(i: int, j: int, ops: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1
            if dp[i][j][ops] != -1:
                return dp[i][j][ops]
            best = dfs(i + 1, j, ops)
            best = max(best, dfs(i, j - 1, ops))
            cost = dist_circ(s[i], s[j])
            if cost <= ops:
                best = max(best, 2 + dfs(i + 1, j - 1, ops - cost))
            dp[i][j][ops] = best
            return best

        return dfs(0, n - 1, k)
''',
)

write(
    "3473_sum_of_k_subarrays_with_length_at_least_m",
    '''
# LeetCode 3473 - Sum of K Subarrays With Length at Least M
# https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        neg = -(10**18)
        dp = [[neg] * (n + 1) for _ in range(k + 1)]
        for i in range(n + 1):
            dp[0][i] = 0
        for t in range(1, k + 1):
            best = neg
            for i in range(t * m, n + 1):
                j = i - m
                best = max(best, dp[t - 1][j] - pref[j])
                dp[t][i] = best + pref[i]
            for i in range(1, n + 1):
                dp[t][i] = max(dp[t][i], dp[t][i - 1])
        return dp[k][n]
''',
)

write(
    "3474_lexicographically_smallest_generated_string",
    '''
# LeetCode 3474 - Lexicographically Smallest Generated String
# https://leetcode.com/problems/lexicographically-smallest-generated-string/


class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        L = n + m - 1
        ans = ["?"] * L
        for i in range(n):
            if str1[i] == "T":
                for j in range(m):
                    if ans[i + j] != "?" and ans[i + j] != str2[j]:
                        return ""
                    ans[i + j] = str2[j]
        for i in range(L):
            if ans[i] == "?":
                ans[i] = "a"
        for i in range(n):
            if str1[i] == "F":
                match = True
                for j in range(m):
                    if ans[i + j] != str2[j]:
                        match = False
                        break
                if match:
                    changed = False
                    for j in range(m - 1, -1, -1):
                        pos = i + j
                        forced = False
                        for t in range(n):
                            if str1[t] == "T" and pos >= t and pos < t + m:
                                forced = True
                                break
                        if not forced:
                            ans[pos] = "b"
                            changed = True
                            break
                    if not changed:
                        return ""
        for i in range(n):
            match = True
            for j in range(m):
                if ans[i + j] != str2[j]:
                    match = False
                    break
            if str1[i] == "T" and not match:
                return ""
            if str1[i] == "F" and match:
                return ""
        return "".join(ans)
''',
)

write(
    "3476_maximize_profit_from_task_assignment",
    '''
# LeetCode 3476 - Maximize Profit from Task Assignment
# https://leetcode.com/problems/maximize-profit-from-task-assignment/

from typing import List


class Solution:
    def maxProfit(self, workers: List[int], tasks: List[List[int]]) -> int:
        workers = sorted(workers)
        tasks = sorted(tasks, key=lambda t: t[0])
        ans = 0
        used = [False] * len(tasks)
        for w in workers:
            best, bi = -1, -1
            for i in range(len(tasks)):
                if used[i]:
                    continue
                if tasks[i][0] > w:
                    break
                if tasks[i][1] > best:
                    best = tasks[i][1]
                    bi = i
            if bi >= 0:
                used[bi] = True
                ans += best
        return ans
''',
)

write(
    "3477_fruits_into_baskets_ii",
    '''
# LeetCode 3477 - Fruits Into Baskets II
# https://leetcode.com/problems/fruits-into-baskets-ii/

from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = [False] * len(baskets)
        unplaced = 0
        for f in fruits:
            placed = False
            for j in range(len(baskets)):
                if not used[j] and baskets[j] >= f:
                    used[j] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1
        return unplaced
''',
)

write(
    "3478_choose_k_elements_with_maximum_sum",
    '''
# LeetCode 3478 - Choose K Elements With Maximum Sum
# https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

from typing import List


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        arr = [[nums1[i], nums2[i], i] for i in range(n)]
        arr.sort(key=lambda x: x[0])
        ans = [0] * n
        h: List[int] = []
        s = 0

        def push(v: int) -> None:
            h.append(v)
            h.sort()

        def poll() -> int:
            return h.pop(0)

        i = 0
        while i < n:
            v = arr[i][0]
            start = i
            while i < n and arr[i][0] == v:
                i += 1
            for t in range(start, i):
                ans[arr[t][2]] = s
            for t in range(start, i):
                push(arr[t][1])
                s += arr[t][1]
                if len(h) > k:
                    s -= poll()
        return ans
''',
)

write(
    "3479_fruits_into_baskets_iii",
    '''
# LeetCode 3479 - Fruits Into Baskets III
# https://leetcode.com/problems/fruits-into-baskets-iii/

from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        size = 1
        while size < n:
            size <<= 1
        tree = [0] * (size * 2)
        for i in range(n):
            tree[size + i] = baskets[i]
        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[i * 2], tree[i * 2 + 1])

        def find(node: int, nl: int, nr: int, need: int) -> int:
            if tree[node] < need:
                return -1
            if nl == nr:
                return nl
            mid = (nl + nr) // 2
            left = find(node * 2, nl, mid, need)
            if left != -1:
                return left
            return find(node * 2 + 1, mid + 1, nr, need)

        def update(idx: int) -> None:
            p = size + idx
            tree[p] = -1
            p >>= 1
            while p > 0:
                tree[p] = max(tree[p * 2], tree[p * 2 + 1])
                p >>= 1

        unplaced = 0
        for f in fruits:
            idx = find(1, 0, size - 1, f)
            if idx == -1 or idx >= n:
                unplaced += 1
            else:
                update(idx)
        return unplaced
''',
)

write(
    "3480_maximize_subarrays_after_removing_one_conflicting_pair",
    '''
# LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

from typing import List


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        m = len(conflictingPairs)
        best = 0
        for skip in range(m):
            right_limit = [n + 1] * (n + 2)
            for i in range(m):
                if i == skip:
                    continue
                a, b = conflictingPairs[i][0], conflictingPairs[i][1]
                if a > b:
                    a, b = b, a
                if b < right_limit[a]:
                    right_limit[a] = b
            min_right = n + 1
            cnt = 0
            for l in range(n, 0, -1):
                if right_limit[l] < min_right:
                    min_right = right_limit[l]
                cnt += min_right - l
            if cnt > best:
                best = cnt
        return best
''',
)

write(
    "3481_apply_substitutions",
    '''
# LeetCode 3481 - Apply Substitutions
# https://leetcode.com/problems/apply-substitutions/

from typing import List


class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        mp = {r[0]: r[1] for r in replacements}

        def resolve(s: str) -> str:
            out = []
            i = 0
            while i < len(s):
                if s[i] == "%":
                    j = i + 1
                    while j < len(s) and s[j] != "%":
                        j += 1
                    key = s[i + 1 : j]
                    out.append(resolve(mp[key]))
                    i = j + 1
                else:
                    out.append(s[i])
                    i += 1
            return "".join(out)

        return resolve(text)
''',
)

write(
    "3483_unique_3_digit_even_numbers",
    '''
# LeetCode 3483 - Unique 3-Digit Even Numbers
# https://leetcode.com/problems/unique-3-digit-even-numbers/

from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        seen = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if digits[i] == 0:
                        continue
                    if digits[k] % 2 != 0:
                        continue
                    seen.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        return len(seen)
''',
)

print("wrote group d (15)")
