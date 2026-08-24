from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
files = {}

files["2711_difference_of_number_of_distinct_values_on_diagonals"] = '''# LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
# https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

from typing import List


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                top, bot = set(), set()
                r, c = i - 1, j - 1
                while r >= 0 and c >= 0:
                    top.add(grid[r][c])
                    r -= 1
                    c -= 1
                r, c = i + 1, j + 1
                while r < m and c < n:
                    bot.add(grid[r][c])
                    r += 1
                    c += 1
                ans[i][j] = abs(len(top) - len(bot))
        return ans
'''

files["2712_minimum_cost_to_make_all_characters_equal"] = '''# LeetCode 2712 - Minimum Cost to Make All Characters Equal
# https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/


class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(1, n):
            if s[i] != s[i - 1]:
                ans += min(i, n - i)
        return ans
'''

files["2713_maximum_strictly_increasing_cells_in_a_matrix"] = '''# LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
# https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

from typing import List


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((mat[i][j], i, j))
        cells.sort()
        row_max = [0] * m
        col_max = [0] * n
        dp = [[0] * n for _ in range(m)]
        ans = 0
        i = 0
        while i < len(cells):
            j = i
            while j < len(cells) and cells[j][0] == cells[i][0]:
                j += 1
            buf = []
            for k in range(i, j):
                r, c = cells[k][1], cells[k][2]
                best = max(row_max[r], col_max[c])
                dp[r][c] = best + 1
                ans = max(ans, dp[r][c])
                buf.append((r, c, dp[r][c]))
            for r, c, v in buf:
                row_max[r] = max(row_max[r], v)
                col_max[c] = max(col_max[c], v)
            i = j
        return ans
'''

files["2714_find_shortest_path_with_k_hops"] = '''# LeetCode 2714 - Find Shortest Path With K Hops
# https://leetcode.com/problems/find-shortest-path-with-k-hops/

import heapq
from typing import List


class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        INF = 10**18
        dist = [[INF] * (k + 1) for _ in range(n)]
        dist[s][0] = 0
        pq = [(0, s, 0)]
        while pq:
            cd, u, hops = heapq.heappop(pq)
            if u == d:
                return cd
            if cd > dist[u][hops]:
                continue
            for to, w in g[u]:
                if cd + w < dist[to][hops]:
                    dist[to][hops] = cd + w
                    heapq.heappush(pq, (dist[to][hops], to, hops))
                if hops < k and cd < dist[to][hops + 1]:
                    dist[to][hops + 1] = cd
                    heapq.heappush(pq, (cd, to, hops + 1))
        return -1
'''

files["2715_timeout_cancellation"] = '''# LeetCode 2715 - Timeout Cancellation
# https://leetcode.com/problems/timeout-cancellation/

import threading
from typing import Any, Callable, List


class Solution:
    def cancellable(self, fn: Callable, args: List[Any], t: int) -> Callable[[], None]:
        timer = threading.Timer(t / 1000.0, lambda: fn(*args))
        timer.daemon = True
        timer.start()

        def cancel() -> None:
            timer.cancel()

        return cancel
'''

files["2716_minimize_string_length"] = '''# LeetCode 2716 - Minimize String Length
# https://leetcode.com/problems/minimize-string-length/


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
'''

files["2717_semi_ordered_permutation"] = '''# LeetCode 2717 - Semi-Ordered Permutation
# https://leetcode.com/problems/semi-ordered-permutation/

from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        p1 = pn = 0
        for i, x in enumerate(nums):
            if x == 1:
                p1 = i
            if x == n:
                pn = i
        ans = p1 + (n - 1 - pn)
        if p1 > pn:
            ans -= 1
        return ans
'''

files["2718_sum_of_matrix_after_queries"] = '''# LeetCode 2718 - Sum of Matrix After Queries
# https://leetcode.com/problems/sum-of-matrix-after-queries/

from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row_done = [False] * n
        col_done = [False] * n
        rows_left, cols_left = n, n
        ans = 0
        for i in range(len(queries) - 1, -1, -1):
            typ, idx, val = queries[i]
            if typ == 0:
                if not row_done[idx]:
                    ans += val * cols_left
                    row_done[idx] = True
                    rows_left -= 1
            else:
                if not col_done[idx]:
                    ans += val * rows_left
                    col_done[idx] = True
                    cols_left -= 1
        return ans
'''

files["2719_count_of_integers"] = '''# LeetCode 2719 - Count of Integers
# https://leetcode.com/problems/count-of-integers/


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 1000000007

        def dec(s: str) -> str:
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == "0":
                arr[i] = "9"
                i -= 1
            if i >= 0:
                arr[i] = chr(ord(arr[i]) - 1)
            j = 0
            while j < len(arr) - 1 and arr[j] == "0":
                j += 1
            return "".join(arr[j:])

        def dp(s: str) -> int:
            memo = {}

            def dfs(pos: int, sm: int, tight: bool) -> int:
                if sm > max_sum:
                    return 0
                if pos == len(s):
                    return 1 if sm >= min_sum else 0
                key = (pos, sm, tight)
                if key in memo:
                    return memo[key]
                up = ord(s[pos]) - 48 if tight else 9
                res = 0
                for d in range(up + 1):
                    res = (res + dfs(pos + 1, sm + d, tight and d == up)) % MOD
                memo[key] = res
                return res

            return dfs(0, 0, True)

        return (dp(num2) - dp(dec(num1)) + MOD) % MOD
'''

files["2721_execute_asynchronous_functions_in_parallel"] = '''# LeetCode 2721 - Execute Asynchronous Functions in Parallel
# https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

import asyncio
from typing import Any, Callable, List


class Solution:
    def promiseAll(self, functions: List[Callable]) -> Any:
        async def run() -> List[Any]:
            n = len(functions)
            if n == 0:
                return []
            ans = [None] * n
            done = 0

            async def one(i: int, fn: Callable) -> None:
                nonlocal done
                result = fn()
                if asyncio.iscoroutine(result) or hasattr(result, "__await__"):
                    ans[i] = await result
                else:
                    ans[i] = result
                done += 1

            await asyncio.gather(*(one(i, fn) for i, fn in enumerate(functions)))
            return ans

        return run()
'''

files["2722_join_two_arrays_by_id"] = '''# LeetCode 2722 - Join Two Arrays by ID
# https://leetcode.com/problems/join-two-arrays-by-id/

from typing import Any, Dict, List


class Solution:
    def join(self, arr1: List[Dict[str, Any]], arr2: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        by_id = {}
        for obj in arr1:
            by_id[obj["id"]] = dict(obj)
        for obj in arr2:
            if obj["id"] in by_id:
                by_id[obj["id"]].update(obj)
            else:
                by_id[obj["id"]] = dict(obj)
        return sorted(by_id.values(), key=lambda o: o["id"])
'''

files["2723_add_two_promises"] = '''# LeetCode 2723 - Add Two Promises
# https://leetcode.com/problems/add-two-promises/

import asyncio
from typing import Any, Awaitable, Union


class Solution:
    async def addTwoPromises(self, promise1: Union[Awaitable, Any], promise2: Union[Awaitable, Any]) -> Any:
        async def resolve(p: Any) -> Any:
            if asyncio.iscoroutine(p) or hasattr(p, "__await__"):
                return await p
            return p

        return (await resolve(promise1)) + (await resolve(promise2))
'''

files["2724_sort_by"] = '''# LeetCode 2724 - Sort By
# https://leetcode.com/problems/sort-by/

from typing import Any, Callable, List


class Solution:
    def sortBy(self, arr: List[Any], fn: Callable[[Any], Any]) -> List[Any]:
        return sorted(arr, key=fn)
'''

files["2725_interval_cancellation"] = '''# LeetCode 2725 - Interval Cancellation
# https://leetcode.com/problems/interval-cancellation/

import threading
from typing import Any, Callable, List


class Solution:
    def cancellable(self, fn: Callable, args: List[Any], t: int) -> Callable[[], None]:
        cancelled = False

        fn(*args)

        def loop() -> None:
            while not cancelled:
                if cancelled:
                    break
                timer = threading.Event()
                timer.wait(t / 1000.0)
                if not cancelled:
                    fn(*args)

        thread = threading.Thread(target=loop, daemon=True)
        thread.start()

        def cancel() -> None:
            nonlocal cancelled
            cancelled = True

        return cancel
'''

files["2726_calculator_with_method_chaining"] = '''# LeetCode 2726 - Calculator with Method Chaining
# https://leetcode.com/problems/calculator-with-method-chaining/


class Calculator:
    def __init__(self, value: float):
        self.val = value

    def add(self, value: float) -> "Calculator":
        self.val += value
        return self

    def subtract(self, value: float) -> "Calculator":
        self.val -= value
        return self

    def multiply(self, value: float) -> "Calculator":
        self.val *= value
        return self

    def divide(self, value: float) -> "Calculator":
        if value == 0:
            raise Exception("Division by zero is not allowed")
        self.val /= value
        return self

    def power(self, value: float) -> "Calculator":
        self.val = self.val ** value
        return self

    def getResult(self) -> float:
        return self.val


class Solution:
    def Calculator(self, value: float) -> Calculator:
        return Calculator(value)
'''

files["2727_is_object_empty"] = '''# LeetCode 2727 - Is Object Empty
# https://leetcode.com/problems/is-object-empty/

from typing import Any, Dict, List, Union


class Solution:
    def isEmpty(self, obj: Union[Dict[Any, Any], List[Any]]) -> bool:
        if isinstance(obj, list):
            return len(obj) == 0
        return len(obj) == 0
'''

files["2728_count_houses_in_a_circular_street"] = '''# LeetCode 2728 - Count Houses in a Circular Street
# https://leetcode.com/problems/count-houses-in-a-circular-street/

from typing import List, Union


class Street:
    def __init__(self, doors: List[int]):
        self.doors = doors
        self.i = 0

    def closeDoor(self) -> None:
        self.doors[self.i] = 0

    def openDoor(self) -> None:
        self.doors[self.i] = 1

    def isDoorOpen(self) -> bool:
        return self.doors[self.i] == 1

    def moveRight(self) -> None:
        self.i = (self.i + 1) % len(self.doors)


class Solution:
    def houseCount(self, street: Union[Street, List[int]], k: int) -> int:
        if isinstance(street, list):
            street = Street(street)
        for _ in range(k):
            street.closeDoor()
            street.moveRight()
        ans = 0
        while True:
            ans += 1
            street.openDoor()
            street.moveRight()
            if street.isDoorOpen():
                break
        return ans
'''

files["2729_check_if_the_number_is_fascinating"] = '''# LeetCode 2729 - Check if The Number is Fascinating
# https://leetcode.com/problems/check-if-the-number-is-fascinating/


class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(2 * n) + str(3 * n)
        if len(s) != 9:
            return False
        cnt = [0] * 10
        for c in s:
            cnt[ord(c) - 48] += 1
        if cnt[0] != 0:
            return False
        for i in range(1, 10):
            if cnt[i] != 1:
                return False
        return True
'''

files["2730_find_the_longest_semi_repetitive_substring"] = '''# LeetCode 2730 - Find the Longest Semi-Repetitive Substring
# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/


class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans, left, last_pair = 0, 0, -1
        for right in range(len(s)):
            if right > 0 and s[right] == s[right - 1]:
                if last_pair >= left:
                    left = last_pair + 1
                last_pair = right - 1
            ans = max(ans, right - left + 1)
        return ans
'''

files["2731_movement_of_robots"] = '''# LeetCode 2731 - Movement of Robots
# https://leetcode.com/problems/movement-of-robots/

from typing import List


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 1000000007
        n = len(nums)
        pos = [nums[i] + (d if s[i] == "R" else -d) for i in range(n)]
        pos.sort()
        ans, pref = 0, 0
        for i in range(n):
            ans = (ans + ((pos[i] * i - pref) % MOD + MOD) % MOD) % MOD
            pref += pos[i]
        return (ans % MOD + MOD) % MOD
'''

written = 0
for folder, content in files.items():
    if not content.endswith("\n"):
        content += "\n"
    path = root / folder / "solution.py"
    path.write_text(content, encoding="utf-8", newline="\n")
    written += 1
    text = path.read_text(encoding="utf-8")
    assert not text.startswith("\ufeff"), folder
    assert "def solve(self) -> None:\n        pass" not in text, folder

print(f"wrote {written}")
