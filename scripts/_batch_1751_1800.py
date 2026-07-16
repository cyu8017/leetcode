from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]


def s(text: str) -> str:
    return dedent(text).lstrip()


SOLUTIONS = {
1751: s("""
    import bisect
    class Solution:
        def maxValue(self, events, k):
            events.sort(key=lambda x: x[1])
            ends = [e[1] for e in events]
            n = len(events)
            dp = [[0] * (k + 1) for _ in range(n + 1)]
            for i in range(n - 1, -1, -1):
                j = bisect.bisect_right(ends, events[i][0] - 1)
                for c in range(1, k + 1):
                    dp[i][c] = max(dp[i + 1][c], events[i][2] + dp[j][c - 1])
            return dp[0][k]
    """),
1752: s("""
    class Solution:
        def check(self, nums):
            drops = sum(nums[i] > nums[(i + 1) % len(nums)] for i in range(len(nums)))
            return drops <= 1
    """),
1753: s("""
    class Solution:
        def maximumScore(self, a, b, c):
            stones = sorted([a, b, c], reverse=True)
            score = 0
            while stones[0] > 0 and stones[1] > 0:
                stones[0] -= 1
                stones[1] -= 1
                score += 1
                stones.sort(reverse=True)
            return score
    """),
1754: s("""
    class Solution:
        def largestMerge(self, word1, word2):
            i = j = 0
            out = []
            while i < len(word1) and j < len(word2):
                if word1[i:] > word2[j:]:
                    out.append(word1[i]); i += 1
                else:
                    out.append(word2[j]); j += 1
            out.extend(word1[i:]); out.extend(word2[j:])
            return "".join(out)
    """),
1755: s("""
    class Solution:
        def minAbsDifference(self, nums, goal):
            n = len(nums)
            left = nums[:n // 2]
            right = nums[n // 2:]
            def sums(arr):
                vals = [0]
                for x in arr:
                    vals += [v + x for v in vals]
                return sorted(vals)
            a, b = sums(left), sums(right)
            best = float("inf")
            j = len(b) - 1
            for x in a:
                while j and abs(x + b[j] - goal) >= abs(x + b[j - 1] - goal):
                    j -= 1
                best = min(best, abs(x + b[j] - goal))
            return best
    """),
1756: s("""
    class MRUQueue:
        def __init__(self, n):
            self.q = list(range(1, n + 1))
        def fetch(self, k):
            val = self.q.pop(k - 1)
            self.q.append(val)
            return val
    """),
1757: s('''QUERY = """
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
"""
'''),
1758: s("""
    class Solution:
        def minOperations(self, s):
            alt1 = sum(s[i] != "01"[i & 1] for i in range(len(s)))
            return min(alt1, len(s) - alt1)
    """),
1759: s("""
    MOD = 1_000_000_007
    class Solution:
        def countHomogenous(self, s):
            ans = 0
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                length = j - i
                ans = (ans + length * (length + 1) // 2) % MOD
                i = j
            return ans
    """),
1760: s("""
    class Solution:
        def minimumSize(self, nums, maxOperations):
            lo, hi = 1, max(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                ops = sum((x - 1) // mid for x in nums)
                if ops <= maxOperations:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
    """),
1761: s("""
    class Solution:
        def minTrioDegree(self, n, edges):
            adj = [set() for _ in range(n)]
            for a, b in edges:
                adj[a - 1].add(b - 1); adj[b - 1].add(a - 1)
            best = float("inf")
            for i in range(n):
                for j in adj[i]:
                    if j <= i:
                        continue
                    for k in adj[i]:
                        if k <= j or k not in adj[j]:
                            continue
                        best = min(best, len(adj[i]) + len(adj[j]) + len(adj[k]) - 6)
            return -1 if best == float("inf") else best
    """),
1762: s("""
    class Solution:
        def findBuildings(self, heights):
            ans = []
            tallest = 0
            for i in range(len(heights) - 1, -1, -1):
                if heights[i] > tallest:
                    ans.append(i)
                    tallest = heights[i]
            return ans[::-1]
    """),
1763: s("""
    class Solution:
        def longestNiceSubstring(self, s):
            def nice(t):
                chars = set(t)
                return all(ch.swapcase() in chars for ch in chars)
            best = ""
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    if nice(s[i:j]) and j - i > len(best):
                        best = s[i:j]
            return best
    """),
1764: s("""
    class Solution:
        def canChoose(self, groups, nums):
            n = len(nums)
            def dfs(i, start):
                if i == len(groups):
                    return start == n
                g = groups[i]
                m = len(g)
                for j in range(start, n - m + 1):
                    if nums[j:j + m] == g and dfs(i + 1, j + m):
                        return True
                return False
            return dfs(0, 0)
    """),
1765: s("""
    class Solution:
        def highestPeak(self, isWater):
            from collections import deque
            m, n = len(isWater), len(isWater[0])
            dist = [[-1] * n for _ in range(m)]
            q = deque()
            for i in range(m):
                for j in range(n):
                    if isWater[i][j]:
                        dist[i][j] = 0
                        q.append((i, j))
            while q:
                i, j = q.popleft()
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and dist[x][y] == -1:
                        dist[x][y] = dist[i][j] + 1
                        q.append((x, y))
            return dist
    """),
1766: s("""
    class Solution:
        def getCoprimes(self, nums, edges):
            from math import gcd
            adj = [[] for _ in range(len(nums))]
            for a, b in edges:
                adj[a].append(b); adj[b].append(a)
            ans = [-1] * len(nums)
            path = [[] for _ in range(51)]
            def dfs(node, parent, depth):
                best = (-1, -1)
                val = nums[node]
                for d in range(1, 51):
                    if gcd(val, d) == 1 and path[d]:
                        cand = path[d][-1]
                        if cand[0] > best[0]:
                            best = cand
                ans[node] = best[1]
                path[val].append((depth, node))
                for nxt in adj[node]:
                    if nxt != parent:
                        dfs(nxt, node, depth + 1)
                path[val].pop()
            dfs(0, -1, 0)
            return ans
    """),
1767: s('''QUERY = """
WITH RECURSIVE subtasks AS (
    SELECT task_id, 1 AS subtask_id, subtasks_count FROM Tasks
    UNION ALL
    SELECT task_id, subtask_id + 1, subtasks_count
    FROM subtasks
    WHERE subtask_id < subtasks_count
)
SELECT s.task_id, s.subtask_id
FROM subtasks s
LEFT JOIN Executed e ON s.task_id = e.task_id AND s.subtask_id = e.subtask_id
WHERE e.task_id IS NULL;
"""
'''),
1768: s("""
    class Solution:
        def mergeAlternately(self, word1, word2):
            i = j = 0
            out = []
            while i < len(word1) or j < len(word2):
                if i < len(word1):
                    out.append(word1[i]); i += 1
                if j < len(word2):
                    out.append(word2[j]); j += 1
            return "".join(out)
    """),
1769: s("""
    class Solution:
        def minOperations(self, boxes):
            n = len(boxes)
            ans = [0] * n
            balls = ops = 0
            for i in range(1, n):
                balls += boxes[i - 1]
                ops += balls
                ans[i] = ops
            balls = ops = 0
            for i in range(n - 2, -1, -1):
                balls += boxes[i + 1]
                ops += balls
                ans[i] += ops
            return ans
    """),
1770: s("""
    class Solution:
        def maximumScore(self, nums, multipliers):
            from functools import lru_cache
            n, m = len(nums), len(multipliers)
            @lru_cache(None)
            def dp(i, left):
                if i == m:
                    return 0
                right = n - 1 - (i - left)
                take_left = nums[left] * multipliers[i] + dp(i + 1, left + 1)
                take_right = nums[right] * multipliers[i] + dp(i + 1, left)
                return max(take_left, take_right)
            return dp(0, 0)
    """),
1771: s("""
    class Solution:
        def longestPalindrome(self, word1, word2):
            n1, n2 = len(word1), len(word2)
            dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
            best = 0
            for i in range(1, n1 + 1):
                for j in range(1, n2 + 1):
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 2
                        best = max(best, dp[i][j])
            return best
    """),
1772: s("""
    class Solution:
        def sortFeatures(self, features, responses):
            from collections import Counter
            count = Counter()
            feature_set = set(features)
            for response in responses:
                seen = set()
                for word in response.split():
                    if word in feature_set:
                        seen.add(word)
                for word in seen:
                    count[word] += 1
            return sorted(features, key=lambda f: (-count[f], f))
    """),
1773: s("""
    class Solution:
        def countMatches(self, items, ruleKey, ruleValue):
            idx = {"type": 0, "color": 1, "name": 2}[ruleKey]
            return sum(item[idx] == ruleValue for item in items)
    """),
1774: s("""
    class Solution:
        def closestCost(self, baseCosts, toppingCosts, target):
            sums = {0}
            for cost in toppingCosts:
                nxt = set(sums)
                for s in sums:
                    x = s + cost
                    while x not in nxt:
                        nxt.add(x)
                        x += cost
                sums = nxt
            best = float("inf")
            for base in baseCosts:
                for top in sums:
                    total = base + top
                    if abs(total - target) < abs(best - target) or (
                        abs(total - target) == abs(best - target) and total < best
                    ):
                        best = total
            return best
    """),
1775: s("""
    class Solution:
        def minOperations(self, nums1, nums2):
            n, m = len(nums1), len(nums2)
            if n < m:
                nums1, nums2 = nums2, nums1
                n, m = m, n
            total = sum(nums1) + sum(nums2)
            if total % n:
                return -1
            target = total // n
            diff = [target - x for x in nums2 if x <= target]
            if len(diff) != m:
                return -1
            return sum(diff)
    """),
1776: s("""
    class Solution:
        def getCollisionTimes(self, cars):
            n = len(cars)
            ans = [-1.0] * n
            stack = []
            for i in range(n - 1, -1, -1):
                pos, speed = cars[i]
                while stack:
                    j = stack[-1]
                    if speed <= cars[j][1]:
                        stack.pop()
                        continue
                    t = (cars[j][0] - pos) / (speed - cars[j][1])
                    if ans[j] < 0 or t <= ans[j]:
                        ans[i] = t
                        break
                    stack.pop()
                stack.append(i)
            return ans
    """),
1777: s('''QUERY = """
SELECT product_id,
       MAX(CASE WHEN store = 'store1' THEN price END) AS store1,
       MAX(CASE WHEN store = 'store2' THEN price END) AS store2,
       MAX(CASE WHEN store = 'store3' THEN price END) AS store3
FROM Products
GROUP BY product_id;
"""
'''),
1778: s("""
    class GridMaster:
        DIR = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        OPP = {"U": "D", "D": "U", "L": "R", "R": "L"}

        def __init__(self, grid):
            self.grid = grid
            self.m, self.n = len(grid), len(grid[0])
            self.r = self.c = 0
            for i in range(self.m):
                for j in range(self.n):
                    if grid[i][j] == -1:
                        self.r, self.c = i, j

        def canMove(self, direction):
            dr, dc = self.DIR[direction]
            nr, nc = self.r + dr, self.c + dc
            return 0 <= nr < self.m and 0 <= nc < self.n and self.grid[nr][nc] != 0

        def move(self, direction):
            if self.canMove(direction):
                dr, dc = self.DIR[direction]
                self.r += dr
                self.c += dc

        def isTarget(self):
            return self.grid[self.r][self.c] == 2

    class Solution:
        def findShortestPath(self, master):
            if isinstance(master, list):
                master = GridMaster(master)
            from collections import deque

            world = {(0, 0): 1}
            target = None
            if master.isTarget():
                return 0

            def dfs(r, c):
                nonlocal target
                for d, (dr, dc) in GridMaster.DIR.items():
                    if not master.canMove(d):
                        continue
                    master.move(d)
                    nr, nc = r + dr, c + dc
                    if (nr, nc) not in world:
                        world[(nr, nc)] = 2 if master.isTarget() else 1
                        if master.isTarget():
                            target = (nr, nc)
                        dfs(nr, nc)
                    master.move(GridMaster.OPP[d])

            dfs(0, 0)
            if target is None:
                return -1
            q = deque([(0, 0, 0)])
            seen = {(0, 0)}
            while q:
                r, c, dist = q.popleft()
                if (r, c) == target:
                    return dist
                for dr, dc in GridMaster.DIR.values():
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in world and world[(nr, nc)] and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        q.append((nr, nc, dist + 1))
            return -1
    """),
1779: s("""
    class Solution:
        def nearestValidPoint(self, x, y, points):
            best = float("inf")
            ans = -1
            for i, (px, py) in enumerate(points):
                if px != x and py != y:
                    continue
                dist = abs(px - x) + abs(py - y)
                if dist < best:
                    best = dist
                    ans = i
            return ans
    """),
1780: s("""
    class Solution:
        def checkPowersOfThree(self, n):
            while n:
                if n % 3 == 2:
                    return False
                n //= 3
            return True
    """),
1781: s("""
    class Solution:
        def beautySum(self, s):
            ans = 0
            for i in range(len(s)):
                freq = [0] * 26
                for j in range(i, len(s)):
                    freq[ord(s[j]) - 97] += 1
                    lo = min(x for x in freq if x)
                    hi = max(freq)
                    ans += hi - lo
            return ans
    """),
1782: s("""
    class Solution:
        def countPairs(self, n, edges, queries):
            from collections import Counter
            deg = [0] * (n + 1)
            shared = Counter()
            for a, b in edges:
                if a > b:
                    a, b = b, a
                deg[a] += 1
                deg[b] += 1
                shared[(a, b)] += 1
            freq = Counter()
            for a in range(1, n + 1):
                for b in range(a + 1, n + 1):
                    freq[deg[a] + deg[b]] += 1
                    freq[deg[a] + deg[b] - shared[(a, b)]] -= 1
            total = [0] * (2 * len(edges) + 2)
            running = 0
            for k in range(len(total)):
                running += freq[k]
                total[k] = running
            return [total[q] for q in queries]
    """),
1783: s('''QUERY = """
SELECT p.player_id, p.player_name, COUNT(*) AS grand_slams_count
FROM Players p
JOIN (
    SELECT Wimbledon AS player_id FROM Championships
    UNION ALL SELECT Fr_open FROM Championships
    UNION ALL SELECT US_open FROM Championships
    UNION ALL SELECT Au_open FROM Championships
) w ON p.player_id = w.player_id
GROUP BY p.player_id, p.player_name;
"""
'''),
1784: s("""
    class Solution:
        def checkOnesSegment(self, s):
            return "01" not in s.strip("0")
    """),
1785: s("""
    class Solution:
        def minElements(self, nums, limit, goal):
            diff = abs(sum(nums) - goal)
            return (diff + limit - 1) // limit
    """),
1786: s("""
    class Solution:
        def countRestrictedPaths(self, n, edges):
            import heapq
            adj = [[] for _ in range(n + 1)]
            for a, b, w in edges:
                adj[a].append((b, w)); adj[b].append((a, w))
            dist = [float("inf")] * (n + 1)
            dist[n] = 0
            heap = [(0, n)]
            while heap:
                d, u = heapq.heappop(heap)
                if d != dist[u]:
                    continue
                for v, w in adj[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))
            MOD = 1_000_000_007
            dp = [0] * (n + 1)
            dp[n] = 1
            for u in sorted(range(1, n + 1), key=lambda x: dist[x]):
                for v, _ in adj[u]:
                    if dist[v] < dist[u]:
                        dp[v] = (dp[v] + dp[u]) % MOD
            return dp[1]
    """),
1787: s("""
    class Solution:
        def minChanges(self, nums, k):
            from collections import Counter
            freq = [Counter() for _ in range(k)]
            size = [0] * k
            for i, x in enumerate(nums):
                freq[i % k][x] += 1
                size[i % k] += 1
            dp = {0: 0}
            for i in range(k):
                ndp = {}
                for xv in range(256):
                    cost = size[i] - freq[i].get(xv, 0)
                    for xo, changes in dp.items():
                        key = xo ^ xv
                        ndp[key] = min(ndp.get(key, 10**9), changes + cost)
                dp = ndp
            return dp[0]
    """),
1788: s("""
    class Solution:
        def maximumBeauty(self, flowers):
            best = float("-inf")
            left_best = {}
            for cur in flowers:
                if cur in left_best:
                    best = max(best, left_best[cur] + cur)
                for val in list(left_best.keys()):
                    if val > cur:
                        left_best[val] = max(left_best[val], left_best[val] + cur)
                    else:
                        left_best.pop(val)
                left_best[cur] = max(left_best.get(cur, float("-inf")), cur)
            return best
    """),
1789: s('''QUERY = """
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'
   OR employee_id IN (
       SELECT employee_id FROM Employee GROUP BY employee_id HAVING COUNT(*) = 1
   );
"""
'''),
1790: s("""
    class Solution:
        def areAlmostEqual(self, s1, s2):
            diff = [(a, b) for a, b in zip(s1, s2) if a != b]
            return not diff or (len(diff) == 2 and diff[0] == diff[1][::-1])
    """),
1791: s("""
    class Solution:
        def findCenter(self, edges):
            a, b = edges[0]
            c, d = edges[1]
            return a if a in (c, d) else b
    """),
1792: s("""
    class Solution:
        def maxAverageRatio(self, classes, extraStudents):
            import heapq
            heap = []
            for p, t in classes:
                gain = (p + 1) / (t + 1) - p / t
                heapq.heappush(heap, (-gain, p, t))
            for _ in range(extraStudents):
                _, p, t = heapq.heappop(heap)
                p += 1; t += 1
                gain = (p + 1) / (t + 1) - p / t
                heapq.heappush(heap, (-gain, p, t))
            return sum(p / t for _, p, t in heap) / len(heap)
    """),
1793: s("""
    class Solution:
        def maximumScore(self, nums, k):
            n = len(nums)
            stack = []
            ans = 0
            for i in range(n + 1):
                while stack and (i == n or nums[i] < nums[stack[-1]]):
                    mid = stack.pop()
                    left = stack[-1] + 1 if stack else 0
                    right = i - 1
                    if left <= k <= right:
                        ans = max(ans, nums[mid] * (right - left + 1))
                stack.append(i)
            return ans
    """),
1794: s("""
    class Solution:
        def countQuadruples(self, firstString, secondString):
            first = {}
            last_f = {}
            last_s = {}
            for i, ch in enumerate(firstString):
                if ch not in first:
                    first[ch] = i
                last_f[ch] = i
            for i, ch in enumerate(secondString):
                last_s[ch] = i
            best = float("inf")
            for ch in first:
                if ch in last_s:
                    best = min(best, last_f[ch] - last_s[ch])
            if best == float("inf"):
                return 0
            ans = 0
            for ch in first:
                if ch not in last_s or last_f[ch] - last_s[ch] != best:
                    continue
                i_count = sum(1 for k in range(first[ch], last_f[ch] + 1) if firstString[k] == ch)
                a_count = sum(1 for k in range(0, last_s[ch] + 1) if secondString[k] == ch)
                ans += i_count * a_count
            return ans
    """),
1795: s('''QUERY = """
SELECT product_id, 'store1' AS store, store1 AS price FROM Products WHERE store1 IS NOT NULL
UNION ALL
SELECT product_id, 'store2', store2 FROM Products WHERE store2 IS NOT NULL
UNION ALL
SELECT product_id, 'store3', store3 FROM Products WHERE store3 IS NOT NULL;
"""
'''),
1796: s("""
    class Solution:
        def secondHighest(self, s):
            digits = sorted({int(ch) for ch in s if ch.isdigit()})
            return digits[-2] if len(digits) > 1 else -1
    """),
1797: s("""
    class AuthenticationManager:
        def __init__(self, timeToLive):
            self.ttl = timeToLive
            self.tokens = {}
        def generate(self, tokenId, currentTime):
            self.tokens[tokenId] = currentTime + self.ttl
        def renew(self, tokenId, currentTime):
            if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
                self.tokens[tokenId] = currentTime + self.ttl
        def countUnexpiredTokens(self, currentTime):
            return sum(exp > currentTime for exp in self.tokens.values())
    """),
1798: s("""
    class Solution:
        def getMaximumConsecutive(self, coins):
            coins.sort()
            reach = 0
            for coin in coins:
                if coin > reach + 1:
                    break
                reach += coin
            return reach + 1
    """),
1799: s("""
    class Solution:
        def maxScore(self, nums):
            from math import gcd
            n = len(nums)
            scores = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    scores[i][j] = scores[j][i] = i * gcd(nums[i], nums[j])
            @cache
            def dp(mask):
                if mask == (1 << n) - 1:
                    return 0
                k = mask.bit_count() // 2 + 1
                best = 0
                for i in range(n):
                    if mask >> i & 1:
                        continue
                    for j in range(i + 1, n):
                        if mask >> j & 1:
                            continue
                        best = max(best, k * scores[i][j] + dp(mask | (1 << i) | (1 << j)))
                return best
            from functools import cache
            return dp(0)
    """),
1800: s("""
    class Solution:
        def maxAscendingSum(self, nums):
            best = cur = nums[0]
            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    cur += nums[i]
                else:
                    cur = nums[i]
                best = max(best, cur)
            return best
    """),
}

SOLUTIONS[1799] = s("""
    from functools import cache
    from math import gcd
    class Solution:
        def maxScore(self, nums):
            n = len(nums)
            @cache
            def dp(mask):
                if mask == (1 << n) - 1:
                    return 0
                step = mask.bit_count() // 2 + 1
                best = 0
                for i in range(n):
                    if mask >> i & 1:
                        continue
                    for j in range(i + 1, n):
                        if mask >> j & 1:
                            continue
                        best = max(
                            best,
                            step * gcd(nums[i], nums[j]) + dp(mask | (1 << i) | (1 << j)),
                        )
                return best
            return dp(0)
    """)


METHODS = {
1751: ("Solution", "maxValue", ["events", "k"]),
1752: ("Solution", "check", ["nums"]),
1753: ("Solution", "maximumScore", ["a", "b", "c"]),
1754: ("Solution", "largestMerge", ["word1", "word2"]),
1755: ("Solution", "minAbsDifference", ["nums", "goal"]),
1756: ("MRUQueue", "", []),
1757: ("Solution", "query", []),
1758: ("Solution", "minOperations", ["s"]),
1759: ("Solution", "countHomogenous", ["s"]),
1760: ("Solution", "minimumSize", ["nums", "maxOperations"]),
1761: ("Solution", "minTrioDegree", ["n", "edges"]),
1762: ("Solution", "findBuildings", ["heights"]),
1763: ("Solution", "longestNiceSubstring", ["s"]),
1764: ("Solution", "canChoose", ["groups", "nums"]),
1765: ("Solution", "highestPeak", ["isWater"]),
1766: ("Solution", "getCoprimes", ["nums", "edges"]),
1767: ("Solution", "query", []),
1768: ("Solution", "mergeAlternately", ["word1", "word2"]),
1769: ("Solution", "minOperations", ["boxes"]),
1770: ("Solution", "maximumScore", ["nums", "multipliers"]),
1771: ("Solution", "longestPalindrome", ["word1", "word2"]),
1772: ("Solution", "sortFeatures", ["features", "responses"]),
1773: ("Solution", "countMatches", ["items", "ruleKey", "ruleValue"]),
1774: ("Solution", "closestCost", ["baseCosts", "toppingCosts", "target"]),
1775: ("Solution", "minOperations", ["nums1", "nums2"]),
1776: ("Solution", "getCollisionTimes", ["cars"]),
1777: ("Solution", "query", []),
1778: ("Solution", "findShortestPath", ["grid"]),
1779: ("Solution", "nearestValidPoint", ["x", "y", "points"]),
1780: ("Solution", "checkPowersOfThree", ["n"]),
1781: ("Solution", "beautySum", ["s"]),
1782: ("Solution", "countPairs", ["n", "edges", "queries"]),
1783: ("Solution", "query", []),
1784: ("Solution", "checkOnesSegment", ["s"]),
1785: ("Solution", "minElements", ["nums", "limit", "goal"]),
1786: ("Solution", "countRestrictedPaths", ["n", "edges"]),
1787: ("Solution", "minChanges", ["nums", "k"]),
1788: ("Solution", "maximumBeauty", ["flowers"]),
1789: ("Solution", "query", []),
1790: ("Solution", "areAlmostEqual", ["s1", "s2"]),
1791: ("Solution", "findCenter", ["edges"]),
1792: ("Solution", "maxAverageRatio", ["classes", "extraStudents"]),
1793: ("Solution", "maximumScore", ["nums", "k"]),
1794: ("Solution", "countQuadruples", ["firstString", "secondString"]),
1795: ("Solution", "query", []),
1796: ("Solution", "secondHighest", ["s"]),
1797: ("AuthenticationManager", "", []),
1798: ("Solution", "getMaximumConsecutive", ["coins"]),
1799: ("Solution", "maxScore", ["nums"]),
1800: ("Solution", "maxAscendingSum", ["nums"]),
}

SQL = {1757, 1767, 1777, 1783, 1789, 1795}
DESIGN = {1756, 1797}

EXPLANATIONS = {
1751: "Sort events by end day, then DP with binary search for the latest non-overlapping event.",
1755: "Meet-in-the-middle: enumerate subset sums of both halves and binary-search the closest to goal.",
1756: "Array-backed MRU queue: fetch removes the k-th element and appends it to the end.",
1762: "Scan heights from right to left, keeping buildings taller than everything seen so far.",
1766: "DFS the tree while tracking the deepest coprime ancestor for each value 1..50.",
1770: "Top-down DP over multiplier index and the remaining left boundary of nums.",
1771: "Concatenate word1 with reversed word2, then take the longest palindromic substring crossing the join.",
1772: "Count feature mentions in responses, then sort by descending count and ascending name.",
1778: "Mock GridMaster from the test grid, DFS to discover the maze, then BFS for shortest path.",
1782: "Count shared-edge frequencies, convert pair counts into prefix sums over total degrees.",
1786: "Dijkstra from node n, then count paths in increasing distance order.",
1787: "Group indices by i % k and DP over XOR totals with per-group replacement costs.",
1788: "For each right endpoint, track best left palindrome-capable prefix sums for taller flowers.",
1793: "Expand from index k, always adding the larger neighbor to maximize the good-subarray score.",
1794: "For each shared character, count index pairs achieving the minimum cross-string distance.",
1797: "Hash map tokenId -> expiry; renew only if still unexpired, count by comparing to currentTime.",
1799: "Precompute pair scores, then bitmask DP pairing unused indices.",
}


def folder(number: int) -> Path:
    matches = sorted(p for p in ROOT.glob(f"{number:04d}_*") if p.is_dir())
    if len(matches) != 1:
        raise RuntimeError(f"Expected one folder for {number}, found {matches}")
    return matches[0]


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def explanation_for(number: int, method: str, cls: str) -> str:
    title = folder(number).name.split("_", 1)[1].replace("_", " ").title()
    body = EXPLANATIONS.get(
        number,
        f"Standard solution for `{method or cls}` with the constraints handled directly.",
    )
    return f"# {number}. {title}\n\n{body}\n"


for number in range(1751, 1801):
    problem = folder(number)
    (problem / "solution.py").write_text(SOLUTIONS[number], encoding="utf-8")
    (problem / "EXPLANATION.md").write_text(
        explanation_for(number, METHODS[number][1], METHODS[number][0]),
        encoding="utf-8",
    )
    cls, method, params = METHODS[number]
    config = {"class": cls, "method": method, "paramOrder": params, "types": None}
    if number in SQL:
        config["kind"] = "sql"
        config["runnable"] = False
    if number in DESIGN:
        config["kind"] = "design"
        config["runnable"] = True
    write_json(problem / "tests" / "config.json", config)

# Repair corrupted expected value in 1772 case 2.
cases_1772 = json.loads((folder(1772) / "tests" / "cases.json").read_text(encoding="utf-8"))
for case in cases_1772["cases"]:
    if isinstance(case.get("expected"), str) and "Constraints" in case["expected"]:
        case["expected"] = ["a", "aa", "b", "c"]
write_json(folder(1772) / "tests" / "cases.json", cases_1772)

print("Wrote solution.py, EXPLANATION.md, and configs for problems 1751-1800.")
