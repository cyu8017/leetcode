#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["3167_better_compression_of_string"] = r'''# LeetCode 3167 - Better Compression of String
# https://leetcode.com/problems/better-compression-of-string/


class Solution:
    def betterCompression(self, compressed: str) -> str:
        cnt = [0] * 26
        n = len(compressed)
        i = 0
        while i < n:
            c = compressed[i]
            j = i + 1
            x = 0
            while j < n:
                d = compressed[j]
                if d < "0" or d > "9":
                    break
                x = x * 10 + (ord(d) - 48)
                j += 1
            cnt[ord(c) - 97] += x
            i = j
        ans = []
        for c in range(26):
            if cnt[c] > 0:
                ans.append(chr(97 + c))
                ans.append(str(cnt[c]))
        return "".join(ans)
'''

FILES["3168_minimum_number_of_chairs_in_a_waiting_room"] = r'''# LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/


class Solution:
    def minimumChairs(self, s: str) -> int:
        cnt = 0
        left = 0
        for c in s:
            if c == "E":
                if left > 0:
                    left -= 1
                else:
                    cnt += 1
            else:
                left += 1
        return cnt
'''

FILES["3169_count_days_without_meetings"] = r'''# LeetCode 3169 - Count Days Without Meetings
# https://leetcode.com/problems/count-days-without-meetings/

from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda e: e[0])
        last = 0
        ans = 0
        for st, ed in meetings:
            if last < st:
                ans += st - last - 1
            last = max(last, ed)
        ans += days - last
        return ans
'''

FILES["3170_lexicographically_minimum_string_after_removing_stars"] = r'''# LeetCode 3170 - Lexicographically Minimum String After Removing Stars
# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/


class Solution:
    def clearStars(self, s: str) -> str:
        g = [[] for _ in range(26)]
        n = len(s)
        rem = [False] * n
        for i, ch in enumerate(s):
            if ch == "*":
                rem[i] = True
                for j in range(26):
                    if g[j]:
                        rem[g[j].pop()] = True
                        break
            else:
                g[ord(ch) - 97].append(i)
        return "".join(s[i] for i in range(n) if not rem[i])
'''

FILES["3171_find_subarray_with_bitwise_or_closest_to_k"] = r'''# LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
# https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

from typing import List


def leading_zero_count(x: int) -> int:
    if x == 0:
        return 32
    n = 0
    for bit in range(31, -1, -1):
        if ((x >> bit) & 1) != 0:
            break
        n += 1
    return n


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        mx = 0
        for v in nums:
            mx = max(mx, v)
        m = 1 if mx == 0 else 32 - leading_zero_count(mx)
        cnt = [0] * m
        ans = 10**18
        s = 0
        i = 0
        for j, x in enumerate(nums):
            s |= x
            ans = min(ans, abs(s - k))
            for h in range(m):
                if ((x >> h) & 1) != 0:
                    cnt[h] += 1
            while i < j and s > k:
                y = nums[i]
                for h in range(m):
                    if ((y >> h) & 1) != 0:
                        cnt[h] -= 1
                        if cnt[h] == 0:
                            s ^= 1 << h
                ans = min(ans, abs(s - k))
                i += 1
        return ans
'''

FILES["3173_bitwise_or_of_adjacent_elements"] = r'''# LeetCode 3173 - Bitwise OR of Adjacent Elements
# https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

from typing import List


class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            ans[i - 1] = nums[i] | nums[i - 1]
        return ans
'''

FILES["3174_clear_digits"] = r'''# LeetCode 3174 - Clear Digits
# https://leetcode.com/problems/clear-digits/


class Solution:
    def clearDigits(self, s: str) -> str:
        stk = []
        for c in s:
            if "0" <= c <= "9":
                stk.pop()
            else:
                stk.append(c)
        return "".join(stk)
'''

FILES["3175_find_the_first_player_to_win_k_games_in_a_row"] = r'''# LeetCode 3175 - Find The First Player to win K Games in a Row
# https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

from typing import List


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        k = min(k, n - 1)
        i = 0
        cnt = 0
        for j in range(1, n):
            if skills[i] < skills[j]:
                i = j
                cnt = 1
            else:
                cnt += 1
            if cnt == k:
                break
        return i
'''

FILES["3176_find_the_maximum_length_of_a_good_subsequence_i"] = r'''# LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [[0] * (k + 1) for _ in range(n)]
        ans = 0
        for i in range(n):
            for h in range(k + 1):
                for j in range(i):
                    if nums[i] == nums[j]:
                        f[i][h] = max(f[i][h], f[j][h])
                    elif h > 0:
                        f[i][h] = max(f[i][h], f[j][h - 1])
                f[i][h] += 1
            ans = max(ans, f[i][k])
        return ans
'''

FILES["3177_find_the_maximum_length_of_a_good_subsequence_ii"] = r'''# LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [[0] * (k + 1) for _ in range(n)]
        mp = [{} for _ in range(k + 1)]
        g = [[0, 0, 0] for _ in range(k + 1)]
        ans = 0
        for i in range(n):
            for h in range(k + 1):
                f[i][h] = mp[h].get(nums[i], 0)
                if h > 0:
                    if g[h - 1][0] != nums[i]:
                        f[i][h] = max(f[i][h], g[h - 1][1])
                    else:
                        f[i][h] = max(f[i][h], g[h - 1][2])
                f[i][h] += 1
                mp[h][nums[i]] = max(mp[h].get(nums[i], 0), f[i][h])
                if g[h][0] != nums[i]:
                    if f[i][h] >= g[h][1]:
                        g[h][2] = g[h][1]
                        g[h][1] = f[i][h]
                        g[h][0] = nums[i]
                    elif f[i][h] > g[h][2]:
                        g[h][2] = f[i][h]
                elif f[i][h] > g[h][1]:
                    g[h][1] = f[i][h]
                ans = max(ans, f[i][h])
        return ans
'''

FILES["3178_find_the_child_who_has_the_ball_after_k_seconds"] = r'''# LeetCode 3178 - Find the Child Who Has the Ball After K Seconds
# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        mod = k % (n - 1)
        k = k // (n - 1)
        if k % 2 == 1:
            return n - mod - 1
        return mod
'''

FILES["3179_find_the_n_th_value_after_k_seconds"] = r'''# LeetCode 3179 - Find the N-th Value After K Seconds
# https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/


class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod = 1000000007
        a = [1] * n
        while k > 0:
            for i in range(1, n):
                a[i] = (a[i] + a[i - 1]) % mod
            k -= 1
        return a[n - 1]
'''

FILES["3180_maximum_total_reward_using_operations_i"] = r'''# LeetCode 3180 - Maximum Total Reward Using Operations I
# https://leetcode.com/problems/maximum-total-reward-using-operations-i/

from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        n = len(rewardValues)
        f = [-1] * (rewardValues[n - 1] << 1)

        def upper_bound(a: List[int], x: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) >> 1
                if a[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def dfs(x: int) -> int:
            if f[x] != -1:
                return f[x]
            idx = upper_bound(rewardValues, x)
            f[x] = 0
            for it in range(idx, n):
                f[x] = max(f[x], rewardValues[it] + dfs(x + rewardValues[it]))
            return f[x]

        return dfs(0)
'''

FILES["3181_maximum_total_reward_using_operations_ii"] = r'''# LeetCode 3181 - Maximum Total Reward Using Operations II
# https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        uniq = 0
        for i in range(len(rewardValues)):
            if uniq == 0 or rewardValues[i] != rewardValues[uniq - 1]:
                rewardValues[uniq] = rewardValues[i]
                uniq += 1
        f = 1
        for i in range(uniq):
            v = rewardValues[i]
            mask = f & ((1 << v) - 1)
            f = f | (mask << v)
        for i in range(100000, -1, -1):
            if (f >> i) & 1:
                return i
        return 0
'''

FILES["3183_the_number_of_ways_to_make_the_sum"] = r'''# LeetCode 3183 - The Number of Ways to Make the Sum
# https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/


class Solution:
    def numberOfWays(self, n: int) -> int:
        mod = 1000000007
        coins = [1, 2, 6]
        f = [0] * (n + 1)
        f[0] = 1
        for x in coins:
            for j in range(x, n + 1):
                f[j] = (f[j] + f[j - x]) % mod
        ans = f[n]
        if n >= 4:
            ans = (ans + f[n - 4]) % mod
        if n >= 8:
            ans = (ans + f[n - 8]) % mod
        return ans
'''

FILES["3184_count_pairs_that_form_a_complete_day_i"] = r'''# LeetCode 3184 - Count Pairs That Form a Complete Day I
# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = [0] * 24
        ans = 0
        for x in hours:
            ans += cnt[(24 - x % 24) % 24]
            cnt[x % 24] += 1
        return ans
'''

FILES["3185_count_pairs_that_form_a_complete_day_ii"] = r'''# LeetCode 3185 - Count Pairs That Form a Complete Day II
# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/

from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = [0] * 24
        ans = 0
        for x in hours:
            ans += cnt[(24 - x % 24) % 24]
            cnt[x % 24] += 1
        return ans
'''

FILES["3186_maximum_total_damage_with_spell_casting"] = r'''# LeetCode 3186 - Maximum Total Damage With Spell Casting
# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        n = len(power)
        power.sort()
        cnt = {}
        nxt = [0] * n
        f = [0] * n

        def lower_bound(a: List[int], x: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) >> 1
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        for i in range(n):
            cnt[power[i]] = cnt.get(power[i], 0) + 1
            nxt[i] = lower_bound(power, power[i] + 3)

        def dfs(i: int) -> int:
            if i >= n:
                return 0
            if f[i] != 0:
                return f[i]
            a = dfs(i + cnt[power[i]])
            b = power[i] * cnt[power[i]] + dfs(nxt[i])
            f[i] = max(a, b)
            return f[i]

        return dfs(0)
'''

FILES["3187_peaks_in_array"] = r'''# LeetCode 3187 - Peaks in Array
# https://leetcode.com/problems/peaks-in-array/

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
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = BIT(n - 1)

        def update_peak(i: int, val: int) -> None:
            if i <= 0 or i >= n - 1:
                return
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                tree.update(i, val)

        for i in range(1, n - 1):
            update_peak(i, 1)
        ans = []
        for q in queries:
            if q[0] == 1:
                l, r = q[1] + 1, q[2] - 1
                t = 0
                if l <= r:
                    t = tree.query(r) - tree.query(l - 1)
                ans.append(t)
            else:
                idx, val = q[1], q[2]
                for i in range(idx - 1, idx + 2):
                    update_peak(i, -1)
                nums[idx] = val
                for i in range(idx - 1, idx + 2):
                    update_peak(i, 1)
        return ans
'''

FILES["3189_minimum_moves_to_get_a_peaceful_board"] = r'''# LeetCode 3189 - Minimum Moves to Get a Peaceful Board
# https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

from typing import List


class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        ans = 0
        rooks.sort(key=lambda a: a[0])
        for i in range(len(rooks)):
            ans += abs(rooks[i][0] - i)
        rooks.sort(key=lambda a: a[1])
        for j in range(len(rooks)):
            ans += abs(rooks[j][1] - j)
        return ans
'''

FILES["3190_find_minimum_operations_to_make_all_elements_divisible_by_three"] = r'''# LeetCode 3190 - Find Minimum Operations to Make All Elements Divisible by Three
# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if x % 3 != 0:
                ans += 1
        return ans
'''

FILES["3191_minimum_operations_to_make_binary_array_elements_equal_to_one_i"] = r'''# LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I
# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if i + 2 >= len(nums):
                    return -1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1
        return ans
'''

FILES["3192_minimum_operations_to_make_binary_array_elements_equal_to_one_ii"] = r'''# LeetCode 3192 - Minimum Operations to Make Binary Array Elements Equal to One II
# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        v = 0
        for raw in nums:
            x = raw ^ v
            if x == 0:
                v ^= 1
                ans += 1
        return ans
'''

FILES["3193_count_the_number_of_inversions"] = r'''# LeetCode 3193 - Count the Number of Inversions
# https://leetcode.com/problems/count-the-number-of-inversions/

from typing import List


class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        req = [-1] * n
        for r in requirements:
            req[r[0]] = r[1]
        if req[0] > 0:
            return 0
        req[0] = 0
        m = 0
        for v in req:
            m = max(m, v)
        mod = 1000000007
        f = [[0] * (m + 1) for _ in range(n)]
        f[0][0] = 1
        for i in range(1, n):
            l, r = 0, m
            if req[i] >= 0:
                l = r = req[i]
            for j in range(l, r + 1):
                for k in range(min(i, j) + 1):
                    f[i][j] = (f[i][j] + f[i - 1][j - k]) % mod
        return f[n - 1][req[n - 1]]
'''

FILES["3194_minimum_average_of_smallest_and_largest_elements"] = r'''# LeetCode 3194 - Minimum Average of Smallest and Largest Elements
# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        ans = 1 << 30
        for i in range(n // 2):
            ans = min(ans, nums[i] + nums[n - i - 1])
        return ans / 2.0
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
