from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def write(folder: str, body: str) -> None:
    path = ROOT / folder / "solution.py"
    path.write_text(body.lstrip("\n"), encoding="utf-8")


write(
    "3434_maximum_frequency_after_subarray_operation",
    '''
# LeetCode 3434 - Maximum Frequency After Subarray Operation
# https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        base = 0
        for x in nums:
            if x == k:
                base += 1
        ans = base
        uniq = set(nums)
        for v in uniq:
            if v == k:
                continue
            best = cur = 0
            for x in nums:
                delta = 0
                if x == v:
                    delta = 1
                elif x == k:
                    delta = -1
                cur += delta
                if cur < 0:
                    cur = 0
                if cur > best:
                    best = cur
            if base + best > ans:
                ans = base + best
        return ans
''',
)

write(
    "3435_frequencies_of_shortest_supersequences",
    '''
# LeetCode 3435 - Frequencies of Shortest Supersequences
# https://leetcode.com/problems/frequencies-of-shortest-supersequences/

from typing import List


class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        used = [False] * 26
        for w in words:
            used[ord(w[0]) - 97] = True
            used[ord(w[1]) - 97] = True
        letters = [i for i in range(26) if used[i]]
        m = len(letters)
        freq = [0] * 26
        best = 10**9
        best_freqs: List[List[int]] = []

        def dfs(i: int) -> None:
            nonlocal best, best_freqs
            if i == m:
                for w in words:
                    a = ord(w[0]) - 97
                    b = ord(w[1]) - 97
                    if a == b:
                        if freq[a] < 2:
                            return
                    elif freq[a] < 1 or freq[b] < 1:
                        return
                s = sum(freq)
                f = freq[:]
                if s < best:
                    best = s
                    best_freqs = [f]
                elif s == best:
                    best_freqs.append(f)
                return
            L = letters[i]
            for c in range(1, 3):
                freq[L] = c
                dfs(i + 1)
            freq[L] = 0

        dfs(0)
        return best_freqs
''',
)

write(
    "3437_permutations_iii",
    '''
# LeetCode 3437 - Permutations III
# https://leetcode.com/problems/permutations-iii/

from typing import List


class Solution:
    def permute(self, n: int) -> List[List[int]]:
        ans: List[List[int]] = []
        used = [False] * (n + 1)
        cur: List[int] = []

        def dfs() -> None:
            if len(cur) == n:
                ans.append(cur[:])
                return
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cur and (cur[-1] % 2 == i % 2):
                    continue
                used[i] = True
                cur.append(i)
                dfs()
                cur.pop()
                used[i] = False

        dfs()
        return ans
''',
)

write(
    "3438_find_valid_pair_of_adjacent_digits_in_string",
    '''
# LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
# https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/


class Solution:
    def findValidPair(self, s: str) -> str:
        freq = [0] * 10
        for c in s:
            freq[ord(c) - 48] += 1
        for i in range(len(s) - 1):
            a = ord(s[i]) - 48
            b = ord(s[i + 1]) - 48
            if a != b and freq[a] == a and freq[b] == b:
                return s[i : i + 2]
        return ""
''',
)

write(
    "3439_reschedule_meetings_for_maximum_free_time_i",
    '''
# LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]
        gaps[n] = eventTime - endTime[n - 1]
        window = k + 1
        s = 0
        for i in range(min(window, len(gaps))):
            s += gaps[i]
        ans = s
        for i in range(window, len(gaps)):
            s += gaps[i] - gaps[i - window]
            if s > ans:
                ans = s
        return ans
''',
)

write(
    "3440_reschedule_meetings_for_maximum_free_time_ii",
    '''
# LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]
        gaps[n] = eventTime - endTime[n - 1]
        ans = 0
        for g in gaps:
            if g > ans:
                ans = g
        left_max = [0] * (n + 1)
        right_max = [0] * (n + 1)
        for i in range(n + 1):
            left_max[i] = gaps[i]
            if i > 0 and left_max[i - 1] > left_max[i]:
                left_max[i] = left_max[i - 1]
        for i in range(n, -1, -1):
            right_max[i] = gaps[i]
            if i < n and right_max[i + 1] > right_max[i]:
                right_max[i] = right_max[i + 1]
        for i in range(n):
            dur = endTime[i] - startTime[i]
            merged = gaps[i] + gaps[i + 1]
            best_other = 0
            if i > 0 and left_max[i - 1] > best_other:
                best_other = left_max[i - 1]
            if i + 2 <= n and right_max[i + 2] > best_other:
                best_other = right_max[i + 2]
            cand = merged
            if best_other >= dur:
                cand = merged + dur
            if cand > ans:
                ans = cand
        return ans
''',
)

write(
    "3441_minimum_cost_good_caption",
    '''
# LeetCode 3441 - Minimum Cost Good Caption
# https://leetcode.com/problems/minimum-cost-good-caption/


class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""
        ans = list(caption)
        i = 0
        while i < n:
            j = i
            while j < n and ans[j] == ans[i]:
                j += 1
            if j - i >= 3:
                i = j
                continue
            need = 3 - (j - i)
            if j + need <= n:
                for t in range(need):
                    ans[j + t] = ans[i]
                i = j + need
            else:
                ch = "a"
                if i > 0:
                    ch = ans[i - 1]
                elif j < n:
                    ch = caption[j]
                for t in range(i, n):
                    ans[t] = ch
                break
        i = 0
        while i < n:
            j = i
            while j < n and ans[j] == ans[i]:
                j += 1
            if j - i < 3:
                return ""
            i = j
        return "".join(ans)
''',
)

write(
    "3442_maximum_difference_between_even_and_odd_frequency_i",
    '''
# LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/


class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1
        max_odd, min_even = 0, 10**9
        for f in freq:
            if f == 0:
                continue
            if f % 2 == 1:
                if f > max_odd:
                    max_odd = f
            elif f < min_even:
                min_even = f
        return max_odd - min_even
''',
)

write(
    "3443_maximum_manhattan_distance_after_k_changes",
    '''
# LeetCode 3443 - Maximum Manhattan Distance After K Changes
# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        lat = lon = 0
        for i, c in enumerate(s):
            if c == "N":
                lat += 1
            elif c == "S":
                lat -= 1
            elif c == "E":
                lon += 1
            else:
                lon -= 1
            md = abs(lat) + abs(lon)
            steps = i + 1
            cur = md + 2 * k
            if cur > steps:
                cur = steps
            if cur > ans:
                ans = cur
        return ans
''',
)

write(
    "3444_minimum_increments_for_target_multiples_in_an_array",
    '''
# LeetCode 3444 - Minimum Increments for Target Multiples in an Array
# https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

from typing import List


class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        def lcm(a: int, b: int) -> int:
            return a // gcd(a, b) * b

        m = len(target)
        N = 1 << m
        inf = 10**18
        dp = [inf] * N
        dp[0] = 0
        for x in nums:
            ndp = dp[:]
            for mask in range(N):
                for sub in range(1, N):
                    L = 1
                    ok = True
                    for i in range(m):
                        if sub & (1 << i):
                            L = lcm(L, target[i])
                            if L > 1000000000:
                                ok = False
                                break
                    if not ok:
                        continue
                    cost = (L - x % L) % L
                    nmask = mask | sub
                    if dp[mask] + cost < ndp[nmask]:
                        ndp[nmask] = dp[mask] + cost
            dp = ndp
        return dp[N - 1]
''',
)

write(
    "3445_maximum_difference_between_even_and_odd_frequency_ii",
    '''
# LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/


class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        ans = -10**9
        for a in range(5):
            for b in range(5):
                if a == b:
                    continue
                pref_a = [0] * (n + 1)
                pref_b = [0] * (n + 1)
                for i in range(n):
                    pref_a[i + 1] = pref_a[i]
                    pref_b[i + 1] = pref_b[i]
                    if ord(s[i]) - 48 == a:
                        pref_a[i + 1] += 1
                    if ord(s[i]) - 48 == b:
                        pref_b[i + 1] += 1
                for i in range(n):
                    for j in range(i + k - 1, n):
                        fa = pref_a[j + 1] - pref_a[i]
                        fb = pref_b[j + 1] - pref_b[i]
                        if fa % 2 == 1 and fb % 2 == 0 and fb > 0:
                            if fa - fb > ans:
                                ans = fa - fb
        return ans
''',
)

write(
    "3446_sort_matrix_by_diagonals",
    '''
# LeetCode 3446 - Sort Matrix by Diagonals
# https://leetcode.com/problems/sort-matrix-by-diagonals/

from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diags = {}
        for i in range(n):
            for j in range(n):
                key = i - j
                if key not in diags:
                    diags[key] = []
                diags[key].append(grid[i][j])
        for key, lst in diags.items():
            if key >= 0:
                lst.sort(reverse=True)
            else:
                lst.sort()
        idx = {}
        for i in range(n):
            for j in range(n):
                k = i - j
                pos = idx.get(k, 0)
                grid[i][j] = diags[k][pos]
                idx[k] = pos + 1
        return grid
''',
)

write(
    "3447_assign_elements_to_groups_with_constraints",
    '''
# LeetCode 3447 - Assign Elements to Groups with Constraints
# https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

from typing import List


class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        max_v = 100001
        first = [-1] * max_v
        for i, e in enumerate(elements):
            if e < max_v and first[e] == -1:
                first[e] = i
        ans = [0] * len(groups)
        for gi, g in enumerate(groups):
            best = -1
            d = 1
            while d * d <= g:
                if g % d == 0:
                    if first[d] != -1 and (best == -1 or first[d] < best):
                        best = first[d]
                    other = g // d
                    if first[other] != -1 and (best == -1 or first[other] < best):
                        best = first[other]
                d += 1
            ans[gi] = best
        return ans
''',
)

write(
    "3448_count_substrings_divisible_by_last_digit",
    '''
# LeetCode 3448 - Count Substrings Divisible By Last Digit
# https://leetcode.com/problems/count-substrings-divisible-by-last-digit/


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for r in range(n):
            last = ord(s[r]) - 48
            if last == 0:
                continue
            mod = 0
            p = 1 % last
            for l in range(r, -1, -1):
                mod = (mod + (ord(s[l]) - 48) * p) % last
                p = (p * 10) % last
                if mod == 0:
                    ans += 1
        return ans
''',
)

write(
    "3449_maximize_the_minimum_game_score",
    '''
# LeetCode 3449 - Maximize the Minimum Game Score
# https://leetcode.com/problems/maximize-the-minimum-game-score/

from typing import List


class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def ok(mid: int) -> bool:
            need = extra = 0
            for p in points:
                req = (mid + p - 1) // p
                if req > extra:
                    visits = req - extra
                    need += 2 * visits - 1
                    extra = visits - 1
                else:
                    need += 1
                    extra = 0
                if need > m:
                    return False
            return need <= m

        lo, hi = 0, 10**18
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
''',
)

print("wrote group b (15)")
