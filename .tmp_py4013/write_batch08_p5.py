from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
files = {}

files["2937_make_three_strings_equal"] = '''# LeetCode 2937 - Make Three Strings Equal
# https://leetcode.com/problems/make-three-strings-equal/


class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n = min(len(s1), len(s2), len(s3))
        i = 0
        while i < n and s1[i] == s2[i] == s3[i]:
            i += 1
        if i == 0:
            return -1
        return len(s1) + len(s2) + len(s3) - 3 * i
'''

files["2938_separate_black_and_white_balls"] = '''# LeetCode 2938 - Separate Black and White Balls
# https://leetcode.com/problems/separate-black-and-white-balls/


class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        zeros = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                zeros += 1
            else:
                ans += zeros
        return ans
'''

files["2939_maximum_xor_product"] = '''# LeetCode 2939 - Maximum Xor Product
# https://leetcode.com/problems/maximum-xor-product/


class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        mod = 1000000007
        A, B = a, b
        for i in range(n - 1, -1, -1):
            bit = 1 << i
            abit, bbit = A & bit, B & bit
            if abit == bbit:
                A |= bit
                B |= bit
            elif A > B:
                B |= bit
                A &= ~bit
            else:
                A |= bit
                B &= ~bit
        return ((A % mod) * (B % mod)) % mod
'''

files["2940_find_building_where_alice_and_bob_can_meet"] = '''# LeetCode 2940 - Find Building Where Alice and Bob Can Meet
# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

from typing import List


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        qn = len(queries)
        ans = [-1] * qn
        buckets = [[] for _ in range(len(heights))]
        for qi in range(qn):
            a, b = queries[qi][0], queries[qi][1]
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans[qi] = b
                continue
            buckets[b].append((heights[a], qi))
        st = []
        for i in range(len(heights) - 1, -1, -1):
            for h, qi in buckets[i]:
                lo, hi = 0, len(st) - 1
                pos = -1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if st[mid][0] > h:
                        pos = st[mid][1]
                        lo = mid + 1
                    else:
                        hi = mid - 1
                ans[qi] = pos
            while st and st[-1][0] <= heights[i]:
                st.pop()
            st.append((heights[i], i))
        return ans
'''

files["2941_maximum_gcd_sum_of_a_subarray"] = '''# LeetCode 2941 - Maximum GCD-Sum of a Subarray
# https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

from typing import List


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


class Solution:
    def maxGcdSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        ans = 0
        st = []
        for i in range(n):
            nst = [[nums[i], i]]
            for p in st:
                g = gcd(p[0], nums[i])
                if nst[-1][0] == g:
                    continue
                nst.append([g, p[1]])
            st = nst
            for g, idx in st:
                if i - idx + 1 >= k:
                    cand = (pref[i + 1] - pref[idx]) * g
                    if cand > ans:
                        ans = cand
        return ans
'''

files["2942_find_words_containing_character"] = '''# LeetCode 2942 - Find Words Containing Character
# https://leetcode.com/problems/find-words-containing-character/

from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i, w in enumerate(words):
            if x in w:
                ans.append(i)
        return ans
'''

files["2943_maximize_area_of_square_hole_in_grid"] = '''# LeetCode 2943 - Maximize Area of Square Hole in Grid
# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

from typing import List


def maxGap(bars: List[int]) -> int:
    if not bars:
        return 1
    bars.sort()
    best = 1
    cur = 1
    for i in range(1, len(bars)):
        if bars[i] == bars[i - 1] + 1:
            cur += 1
        else:
            cur = 1
        if cur > best:
            best = cur
    return best + 1


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        side = maxGap(hBars[:])
        vs = maxGap(vBars[:])
        if vs < side:
            side = vs
        return side * side
'''

files["2944_minimum_number_of_coins_for_fruits"] = '''# LeetCode 2944 - Minimum Number of Coins for Fruits
# https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

from typing import List


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [1 << 30] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = i
            while j <= n and j <= i + i:
                cand = dp[i - 1] + prices[i - 1]
                if cand < dp[j]:
                    dp[j] = cand
                j += 1
        return dp[n]
'''

files["2945_find_maximum_non_decreasing_array_length"] = '''# LeetCode 2945 - Find Maximum Non-decreasing Array Length
# https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

from typing import List


class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        last = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        dp = [0] * (n + 1)
        dq = [[0, 0]]
        for i in range(1, n + 1):
            while len(dq) > 1 and dq[1][1] <= pref[i]:
                dq.pop(0)
            j = dq[0][0]
            dp[i] = dp[j] + 1
            last[i] = pref[i] - pref[j]
            val = pref[i] + last[i]
            while dq and dq[-1][1] >= val:
                dq.pop()
            dq.append([i, val])
        return dp[n]
'''

files["2946_matrix_similarity_after_cyclic_shifts"] = '''# LeetCode 2946 - Matrix Similarity After Cyclic Shifts
# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            if i % 2 == 0:
                shift = n - (k % n)
                if shift == n:
                    shift = 0
            else:
                shift = k % n
            for j in range(n):
                if mat[i][j] != mat[i][(j + shift) % n]:
                    return False
        return True
'''

files["2947_count_beautiful_substrings_i"] = '''# LeetCode 2947 - Count Beautiful Substrings I
# https://leetcode.com/problems/count-beautiful-substrings-i/


def isVowel(c: str) -> bool:
    return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            v = c = 0
            for j in range(i, n):
                if isVowel(s[j]):
                    v += 1
                else:
                    c += 1
                if v == c and (v * c) % k == 0:
                    ans += 1
        return ans
'''

files["2948_make_lexicographically_smallest_array_by_swapping_elements"] = '''# LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        idx = list(range(n))
        idx.sort(key=lambda i: nums[i])
        ans = [0] * n
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[idx[j]] - nums[idx[j - 1]] <= limit:
                j += 1
            group_idx = idx[i:j]
            group_idx.sort()
            for t in range(j - i):
                ans[group_idx[t]] = nums[idx[i + t]]
            i = j
        return ans
'''

files["2949_count_beautiful_substrings_ii"] = '''# LeetCode 2949 - Count Beautiful Substrings II
# https://leetcode.com/problems/count-beautiful-substrings-ii/


def isVowel(c: str) -> bool:
    return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        x = 1
        while (x * x) % k != 0:
            x += 1
        freq = {0: 1}
        bal = 0
        vowels = 0
        ans = 0
        for ch in s:
            if isVowel(ch):
                bal += 1
                vowels += 1
            else:
                bal -= 1
            key = (bal, vowels % x)
            f = freq.get(key, 0)
            ans += f
            freq[key] = f + 1
        return ans
'''

files["2950_number_of_divisible_substrings"] = '''# LeetCode 2950 - Number of Divisible Substrings
# https://leetcode.com/problems/number-of-divisible-substrings/


class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        vals = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]
        ans = 0
        n = len(word)
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += vals[ord(word[j]) - 97]
                if s % (j - i + 1) == 0:
                    ans += 1
        return ans
'''

files["2951_find_the_peaks"] = '''# LeetCode 2951 - Find the Peaks
# https://leetcode.com/problems/find-the-peaks/

from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                ans.append(i)
        return ans
'''

files["2952_minimum_number_of_coins_to_be_added"] = '''# LeetCode 2952 - Minimum Number of Coins to be Added
# https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

from typing import List


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        ans = 0
        reach = 0
        i = 0
        while reach < target:
            if i < len(coins) and coins[i] <= reach + 1:
                reach += coins[i]
                i += 1
            else:
                reach += reach + 1
                ans += 1
        return ans
'''

files["2953_count_complete_substrings"] = '''# LeetCode 2953 - Count Complete Substrings
# https://leetcode.com/problems/count-complete-substrings/


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        ans = 0
        i = 0
        while i < n:
            j = i
            while j + 1 < n and abs(ord(word[j + 1]) - ord(word[j])) <= 2:
                j += 1
            seg = word[i : j + 1]
            m = len(seg)
            for chars in range(1, 27):
                length = chars * k
                if length > m:
                    break
                freq = [0] * 26
                unique = 0
                for r in range(m):
                    c = ord(seg[r]) - 97
                    freq[c] += 1
                    if freq[c] == 1:
                        unique += 1
                    if r >= length:
                        c2 = ord(seg[r - length]) - 97
                        freq[c2] -= 1
                        if freq[c2] == 0:
                            unique -= 1
                    if r >= length - 1 and unique == chars:
                        ok = True
                        for f in freq:
                            if f != 0 and f != k:
                                ok = False
                                break
                        if ok:
                            ans += 1
            i = j + 1
        return ans
'''

files["2954_count_the_number_of_infection_sequences"] = '''# LeetCode 2954 - Count the Number of Infection Sequences
# https://leetcode.com/problems/count-the-number-of-infection-sequences/

from typing import List

MOD = 1000000007


def modPow(a: int, b: int) -> int:
    res = 1
    a %= MOD
    while b > 0:
        if b & 1:
            res = res * a % MOD
        a = a * a % MOD
        b >>= 1
    return res


class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        fact = [0] * (n + 1)
        inv_fact = [0] * (n + 1)
        fact[0] = 1
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[n] = modPow(fact[n], MOD - 2)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        m = len(sick)
        total_empty = n - m
        ans = fact[total_empty]
        prev = -1
        for s in sick:
            gap = s - prev - 1
            if prev == -1:
                ans = ans * inv_fact[gap] % MOD
            elif gap > 0:
                ans = ans * inv_fact[gap] % MOD * modPow(2, gap - 1) % MOD
            prev = s
        gap2 = n - prev - 1
        ans = ans * inv_fact[gap2] % MOD
        return ans
'''

files["2955_number_of_same_end_substrings"] = '''# LeetCode 2955 - Number of Same-End Substrings
# https://leetcode.com/problems/number-of-same-end-substrings/

from typing import List


class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        pref = [[0] * 26 for _ in range(n + 1)]
        for i in range(n):
            for c in range(26):
                pref[i + 1][c] = pref[i][c]
            pref[i + 1][ord(s[i]) - 97] += 1
        ans = [0] * len(queries)
        for qi, (l, r) in enumerate(queries):
            total = 0
            for c in range(26):
                cnt = pref[r + 1][c] - pref[l][c]
                total += cnt * (cnt + 1) // 2
            ans[qi] = total
        return ans
'''

files["2956_find_common_elements_between_two_arrays"] = '''# LeetCode 2956 - Find Common Elements Between Two Arrays
# https://leetcode.com/problems/find-common-elements-between-two-arrays/

from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        a = sum(1 for v in nums1 if v in s2)
        b = sum(1 for v in nums2 if v in s1)
        return [a, b]
'''

files["2957_remove_adjacent_almost_equal_characters"] = '''# LeetCode 2957 - Remove Adjacent Almost-Equal Characters
# https://leetcode.com/problems/remove-adjacent-almost-equal-characters/


class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        ans = 0
        i = 1
        n = len(word)
        while i < n:
            if abs(ord(word[i]) - ord(word[i - 1])) <= 1:
                ans += 1
                i += 2
            else:
                i += 1
        return ans
'''

written = 0
for folder, content in files.items():
    path = root / folder / "solution.py"
    path.write_text(content, encoding="utf-8", newline="\n")
    written += 1
    print("wrote", folder)
print("p5 written", written)
