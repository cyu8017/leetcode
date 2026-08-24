#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3307_find_the_k_th_character_in_string_game_ii"] = r'''# LeetCode 3307 - Find the K-th Character in String Game II
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        shift = 0
        ops = operations[:]
        while ops:
            op = ops.pop()
            half = 1 << len(ops)
            if k > half:
                k = k - half
                if op == 1:
                    shift += 1
        return chr(97 + (shift % 26))
'''

FILES["3309_maximum_possible_number_by_binary_concatenation"] = r'''# LeetCode 3309 - Maximum Possible Number by Binary Concatenation
# https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

from typing import List


def toBin(x: int) -> str:
    if x == 0:
        return "0"
    s = ""
    while x > 0:
        s = str(x & 1) + s
        x >>= 1
    return s


def perm(i: int, idx: List[int], bs: List[str], ans: List[int]) -> None:
    if i == 3:
        s = bs[idx[0]] + bs[idx[1]] + bs[idx[2]]
        v = 0
        for c in s:
            v = v * 2 + (ord(c) - 48)
        if v > ans[0]:
            ans[0] = v
        return
    for j in range(i, 3):
        idx[i], idx[j] = idx[j], idx[i]
        perm(i + 1, idx, bs, ans)
        idx[i], idx[j] = idx[j], idx[i]


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        bs = [toBin(nums[0]), toBin(nums[1]), toBin(nums[2])]
        idx = [0, 1, 2]
        ans = [0]
        perm(0, idx, bs, ans)
        return ans[0]
'''

FILES["3310_remove_methods_from_project"] = r'''# LeetCode 3310 - Remove Methods From Project
# https://leetcode.com/problems/remove-methods-from-project/

from typing import List


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for e in invocations:
            g[e[0]].append(e[1])
        sus = [False] * n

        def dfs(u: int) -> None:
            if sus[u]:
                return
            sus[u] = True
            for v in g[u]:
                dfs(v)

        dfs(k)
        for e in invocations:
            if (not sus[e[0]]) and sus[e[1]]:
                return list(range(n))
        return [i for i in range(n) if not sus[i]]
'''

FILES["3311_construct_2d_grid_matching_graph_layout"] = r'''# LeetCode 3311 - Construct 2D Grid Matching Graph Layout
# https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

from typing import List


class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        deg = [len(g[i]) for i in range(n)]
        start = 0
        for i in range(n):
            if deg[i] == 1:
                start = i
                break
            if deg[i] == 2:
                start = i
        vis = [False] * n
        row = []
        cur, prev = start, -1
        while True:
            row.append(cur)
            vis[cur] = True
            nxt = -1
            for v in g[cur]:
                if v != prev and (not vis[v]) and deg[v] <= 3:
                    nxt = v
                    if deg[v] < 4:
                        break
            if nxt == -1:
                break
            prev = cur
            cur = nxt
        width = len(row)
        height = n // width if width != 0 else n
        if width == 0 or width * height != n:
            for w in range(1, n + 1):
                if n % w == 0:
                    width = w
                    height = n // w
                    break
        grid = [[0] * width for _ in range(height)]
        for i in range(n):
            grid[i // width][i % width] = i
        return grid
'''

FILES["3312_sorted_gcd_pair_queries"] = r'''# LeetCode 3312 - Sorted GCD Pair Queries
# https://leetcode.com/problems/sorted-gcd-pair-queries/

from typing import List


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_v = 0
        for x in nums:
            if x > max_v:
                max_v = x
        cnt = [0] * (max_v + 1)
        for x in nums:
            cnt[x] += 1
        div_cnt = [0] * (max_v + 1)
        for g in range(1, max_v + 1):
            c = 0
            for m in range(g, max_v + 1, g):
                c += cnt[m]
            div_cnt[g] = c * (c - 1) // 2
        exact = [0] * (max_v + 1)
        for g in range(max_v, 0, -1):
            exact[g] = div_cnt[g]
            for m in range(2 * g, max_v + 1, g):
                exact[g] -= exact[m]
        pref = [0] * (max_v + 1)
        for g in range(1, max_v + 1):
            pref[g] = pref[g - 1] + exact[g]
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            lo, hi = 1, max_v
            while lo < hi:
                mid = (lo + hi) >> 1
                if pref[mid] > q:
                    hi = mid
                else:
                    lo = mid + 1
            ans[i] = lo
        return ans
'''

FILES["3313_find_the_last_marked_nodes_in_tree"] = r'''# LeetCode 3313 - Find the Last Marked Nodes in Tree
# https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

from typing import List, Tuple


class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        def bfs(start: int) -> Tuple[int, List[int]]:
            dist = [-1] * n
            q = [start]
            dist[start] = 0
            far = start
            qi = 0
            while qi < len(q):
                u = q[qi]
                qi += 1
                if dist[u] > dist[far]:
                    far = u
                for v in g[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return far, dist

        u = bfs(0)[0]
        v, du = bfs(u)
        dv = bfs(v)[1]
        return [u if du[i] >= dv[i] else v for i in range(n)]
'''

FILES["3314_construct_the_minimum_bitwise_array_i"] = r'''# LeetCode 3314 - Construct the Minimum Bitwise Array I
# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        for i, n in enumerate(nums):
            for x in range(n):
                if (x | (x + 1)) == n:
                    ans[i] = x
                    break
        return ans
'''

FILES["3315_construct_the_minimum_bitwise_array_ii"] = r'''# LeetCode 3315 - Construct the Minimum Bitwise Array II
# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        for i, n in enumerate(nums):
            if n == 2:
                continue
            for b in range(31):
                if ((n >> b) & 1) == 0:
                    continue
                x = n ^ (1 << b)
                if (x | (x + 1)) == n:
                    ans[i] = x
                    break
        return ans
'''

FILES["3316_find_maximum_removals_from_source_string"] = r'''# LeetCode 3316 - Find Maximum Removals From Source String
# https://leetcode.com/problems/find-maximum-removals-from-source-string/

from typing import List


def ok(removeFirst: int, source: str, pattern: str, targetIndices: List[int], n: int) -> bool:
    mark = [False] * n
    for i in range(removeFirst):
        mark[targetIndices[i]] = True
    j = 0
    i = 0
    while i < n and j < len(pattern):
        if not mark[i] and source[i] == pattern[j]:
            j += 1
        i += 1
    return j == len(pattern)


class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        n = len(source)
        lo, hi = 0, len(targetIndices)
        while lo < hi:
            mid = (lo + hi + 1) >> 1
            if ok(mid, source, pattern, targetIndices, n):
                lo = mid
            else:
                hi = mid - 1
        return lo
'''

FILES["3317_find_the_number_of_possible_ways_for_an_event"] = r'''# LeetCode 3317 - Find the Number of Possible Ways for an Event
# https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/


def modPow(a: int, e: int, mod: int) -> int:
    r = 1
    a %= mod
    while e > 0:
        if e & 1:
            r = r * a % mod
        a = a * a % mod
        e >>= 1
    return r


class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        mod = 1000000007
        dp = [[0] * (x + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, min(x, i) + 1):
                dp[i][j] = (dp[i - 1][j - 1] + j * dp[i - 1][j] % mod) % mod
        fact = [0] * (x + 1)
        fact[0] = 1
        for i in range(1, x + 1):
            fact[i] = fact[i - 1] * i % mod
        ans = 0
        ypow = 1
        for k in range(1, min(x, n) + 1):
            ypow = ypow * y % mod
            perm = fact[x] * modPow(fact[x - k], mod - 2, mod) % mod
            ans = (ans + dp[n][k] * perm % mod * ypow % mod) % mod
        return ans
'''

FILES["3318_find_x_sum_of_all_k_long_subarrays_i"] = r'''# LeetCode 3318 - Find X-Sum of All K-Long Subarrays I
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        for i in range(n - k + 1):
            freq = {}
            for j in range(i, i + k):
                freq[nums[j]] = freq.get(nums[j], 0) + 1
            arr = [[key, val] for key, val in freq.items()]
            arr.sort(key=lambda A: (-A[1], -A[0]))
            lim = min(x, len(arr))
            keep = set(arr[t][0] for t in range(lim))
            s = 0
            for j in range(i, i + k):
                if nums[j] in keep:
                    s += nums[j]
            ans[i] = s
        return ans
'''

FILES["3319_k_th_largest_perfect_subtree_size_in_binary_tree"] = r'''# LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
# https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        sizes = []

        def dfs(node):
            if not node:
                return [0, 0, 1]
            L = dfs(node.left)
            R = dfs(node.right)
            sz = L[1] + R[1] + 1
            perf = L[2] == 1 and R[2] == 1 and L[0] == R[0]
            if perf:
                sizes.append(sz)
            return [max(L[0], R[0]) + 1, sz, 1 if perf else 0]

        dfs(root)
        sizes.sort(reverse=True)
        if k > len(sizes):
            return -1
        return sizes[k - 1]
'''

FILES["3320_count_the_number_of_winning_sequences"] = r'''# LeetCode 3320 - Count the Number of Winning Sequences
# https://leetcode.com/problems/count-the-number-of-winning-sequences/


class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 1000000007
        n = len(s)
        mp = {"F": 0, "W": 1, "E": 2}
        beat = [2, 0, 1]
        score = [[0] * 3 for _ in range(3)]
        for a in range(3):
            for b in range(3):
                if a == b:
                    score[a][b] = 0
                elif beat[a] == b:
                    score[a][b] = 1
                else:
                    score[a][b] = -1
        offset = n
        dp = [[0] * (2 * n + 1) for _ in range(3)]
        b0 = mp[s[0]]
        for a in range(3):
            dp[a][score[a][b0] + offset] = 1
        for i in range(1, n):
            ndp = [[0] * (2 * n + 1) for _ in range(3)]
            b = mp[s[i]]
            for last in range(3):
                for d in range(2 * n + 1):
                    if dp[last][d] == 0:
                        continue
                    for a in range(3):
                        if a == last:
                            continue
                        nd = d + score[a][b]
                        if nd < 0 or nd > 2 * n:
                            continue
                        ndp[a][nd] = (ndp[a][nd] + dp[last][d]) % mod
            dp = ndp
        ans = 0
        for a in range(3):
            for d in range(offset + 1, 2 * n + 1):
                ans = (ans + dp[a][d]) % mod
        return ans
'''

FILES["3321_find_x_sum_of_all_k_long_subarrays_ii"] = r'''# LeetCode 3321 - Find X-Sum of All K-Long Subarrays II
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        for i in range(n - k + 1):
            freq = {}
            for j in range(i, i + k):
                freq[nums[j]] = freq.get(nums[j], 0) + 1
            arr = [[key, val] for key, val in freq.items()]
            arr.sort(key=lambda A: (-A[1], -A[0]))
            lim = min(x, len(arr))
            keep = set(arr[t][0] for t in range(lim))
            s = 0
            for j in range(i, i + k):
                if nums[j] in keep:
                    s += nums[j]
            ans[i] = s
        return ans
'''

FILES["3323_minimize_connected_groups_by_inserting_interval"] = r'''# LeetCode 3323 - Minimize Connected Groups by Inserting Interval
# https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

from typing import List


class Solution:
    def minConnectedGroups(self, intervals: List[List[int]], k: int) -> int:
        intervals.sort(key=lambda a: a[0])
        merged = []
        for it in intervals:
            if not merged or it[0] > merged[-1][1]:
                merged.append([it[0], it[1]])
            elif it[1] > merged[-1][1]:
                merged[-1][1] = it[1]
        m = len(merged)
        ans = m
        for i in range(m):
            end = merged[i][1] + k
            j = i
            while j < m and merged[j][0] <= end:
                j += 1
            groups = i + 1 + (m - j)
            if groups < ans:
                ans = groups
        return ans
'''

FILES["3324_find_the_sequence_of_strings_appeared_on_the_screen"] = r'''# LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
# https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        cur = ""
        for ch in target:
            cur += "a"
            ans.append(cur)
            while cur[-1] != ch:
                last = chr(ord(cur[-1]) + 1)
                cur = cur[:-1] + last
                ans.append(cur)
        return ans
'''

FILES["3325_count_substrings_with_k_frequency_characters_i"] = r'''# LeetCode 3325 - Count Substrings With K-Frequency Characters I
# https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - 97] += 1
                if any(f >= k for f in freq):
                    ans += n - j
                    break
        return ans
'''

FILES["3326_minimum_division_operations_to_make_array_non_decreasing"] = r'''# LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
# https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

from typing import List


def smallestProperDivisor(x: int) -> int:
    d = 2
    while d * d <= x:
        if x % d == 0:
            return d
        d += 1
    return x


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
            while nums[i] > nums[i + 1]:
                d = smallestProperDivisor(nums[i])
                if d == nums[i]:
                    return -1
                nums[i] = nums[i] // d
                ops += 1
                if nums[i] > nums[i + 1] and smallestProperDivisor(nums[i]) == nums[i]:
                    return -1
        return ops
'''

FILES["3327_check_if_dfs_strings_are_palindromes"] = r'''# LeetCode 3327 - Check DFS Strings Are Palindromes
# https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

from typing import List


class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
        ans = [False] * n

        def isPal(t: str) -> bool:
            i, j = 0, len(t) - 1
            while i < j:
                if t[i] != t[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfsStr(u: int) -> str:
            out = ""
            for v in g[u]:
                out += dfsStr(v)
            out += s[u]
            ans[u] = isPal(out)
            return out

        dfsStr(0)
        return ans
'''

FILES["3329_count_substrings_with_k_frequency_characters_ii"] = r'''# LeetCode 3329 - Count Substrings With K-Frequency Characters II
# https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - 97] += 1
                if any(f >= k for f in freq):
                    ans += n - j
                    break
        return ans
'''

FILES["3330_find_the_original_typed_string_i"] = r'''# LeetCode 3330 - Find the Original Typed String I
# https://leetcode.com/problems/find-the-original-typed-string-i/


class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                ans += 1
        return ans
'''

FILES["3331_find_subtree_sizes_after_changes"] = r'''# LeetCode 3331 - Find Subtree Sizes After Changes
# https://leetcode.com/problems/find-subtree-sizes-after-changes/

from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
        new_parent = parent[:]
        last = [-1] * 26

        def dfs1(u: int) -> None:
            c = ord(s[u]) - 97
            prev = last[c]
            if prev != -1:
                new_parent[u] = prev
            last[c] = u
            for v in g[u]:
                dfs1(v)
            last[c] = prev

        dfs1(0)
        ng = [[] for _ in range(n)]
        for i in range(1, n):
            ng[new_parent[i]].append(i)
        ans = [0] * n

        def dfs2(u: int) -> int:
            sz = 1
            for v in ng[u]:
                sz += dfs2(v)
            ans[u] = sz
            return sz

        dfs2(0)
        return ans
'''

FILES["3332_maximum_points_tourist_can_earn"] = r'''# LeetCode 3332 - Maximum Points Tourist Can Earn
# https://leetcode.com/problems/maximum-points-tourist-can-earn/

from typing import List


class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [0] * n
        for day in range(k):
            ndp = [-(1 << 30)] * n
            for dest in range(n):
                best = -(1 << 30)
                for src in range(n):
                    val = dp[src]
                    if src == dest:
                        val += stayScore[day][dest]
                    else:
                        val += travelScore[src][dest]
                    if val > best:
                        best = val
                ndp[dest] = best
            dp = ndp
        ans = dp[0]
        for i in range(1, n):
            if dp[i] > ans:
                ans = dp[i]
        return ans
'''

FILES["3333_find_the_original_typed_string_ii"] = r'''# LeetCode 3333 - Find the Original Typed String II
# https://leetcode.com/problems/find-the-original-typed-string-ii/


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 1000000007
        groups = []
        i = 0
        while i < len(word):
            j = i
            while j < len(word) and word[j] == word[i]:
                j += 1
            groups.append(j - i)
            i = j
        total = 1
        for g in groups:
            total = total * g % mod
        if k <= len(groups):
            return total
        need = k - 1
        dp = [0] * need
        dp[0] = 1
        for g in groups:
            ndp = [0] * need
            pref = [0] * (need + 1)
            for i in range(need):
                pref[i + 1] = (pref[i] + dp[i]) % mod
            for s in range(need):
                lo = s - g
                if lo < 0:
                    lo = 0
                hi = s - 1
                if hi >= 0:
                    ndp[s] = (pref[hi + 1] - pref[lo] + mod) % mod
            dp = ndp
        bad = 0
        for v in dp:
            bad = (bad + v) % mod
        return (total - bad + mod) % mod
'''

FILES["3334_find_the_maximum_factor_score_of_array"] = r'''# LeetCode 3334 - Find the Maximum Factor Score of Array
# https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

from typing import List


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        gcd_all = nums[0]
        lcm_all = nums[0]
        for i in range(1, n):
            gcd_all = gcd(gcd_all, nums[i])
            lcm_all = lcm(lcm_all, nums[i])
        ans = gcd_all * lcm_all
        for skip in range(n):
            g = 0
            l = 1
            first = True
            for i in range(n):
                if i == skip:
                    continue
                if first:
                    g = l = nums[i]
                    first = False
                else:
                    g = gcd(g, nums[i])
                    l = lcm(l, nums[i])
            if first:
                continue
            v = g * l
            if v > ans:
                ans = v
        return ans
'''


def main() -> None:
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.py"
        path.write_text(content, encoding="utf-8", newline="\n")
        print("wrote", folder)
    print("part1", len(FILES))


if __name__ == "__main__":
    main()
