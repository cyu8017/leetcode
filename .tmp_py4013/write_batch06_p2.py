from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
files = {}

files["2666_allow_one_function_call"] = '''# LeetCode 2666 - Allow One Function Call
# https://leetcode.com/problems/allow-one-function-call/

from typing import Any, Callable


class Solution:
    def once(self, fn: Callable) -> Callable:
        called = False
        res = None

        def wrapper(*args: Any) -> Any:
            nonlocal called, res
            if called:
                return None
            called = True
            res = fn(*args)
            return res

        return wrapper
'''

files["2667_create_hello_world_function"] = '''# LeetCode 2667 - Create Hello World Function
# https://leetcode.com/problems/create-hello-world-function/

from typing import Any, Callable


class Solution:
    def createHelloWorld(self) -> Callable:
        def hello(*args: Any) -> str:
            return "Hello World"

        return hello
'''

files["2670_find_the_distinct_difference_array"] = '''# LeetCode 2670 - Find the Distinct Difference Array
# https://leetcode.com/problems/find-the-distinct-difference-array/

from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf = [0] * (n + 1)
        seen = set()
        for i in range(n - 1, -1, -1):
            seen.add(nums[i])
            suf[i] = len(seen)
        seen.clear()
        ans = [0] * n
        for i in range(n):
            seen.add(nums[i])
            ans[i] = len(seen) - suf[i + 1]
        return ans
'''

files["2671_frequency_tracker"] = '''# LeetCode 2671 - Frequency Tracker
# https://leetcode.com/problems/frequency-tracker/

from collections import defaultdict


class FrequencyTracker:
    def __init__(self):
        self.freq = defaultdict(int)
        self.count = defaultdict(int)

    def add(self, number: int) -> None:
        old = self.freq[number]
        if old > 0:
            self.count[old] -= 1
        self.freq[number] = old + 1
        self.count[old + 1] += 1

    def deleteOne(self, number: int) -> None:
        old = self.freq[number]
        if old == 0:
            return
        self.count[old] -= 1
        self.freq[number] = old - 1
        if old - 1 > 0:
            self.count[old - 1] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.count[frequency] > 0
'''

files["2672_number_of_adjacent_elements_with_the_same_color"] = '''# LeetCode 2672 - Number of Adjacent Elements With the Same Color
# https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

from typing import List


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        ans = [0] * len(queries)
        same = 0
        for i, (idx, color) in enumerate(queries):
            if colors[idx] != 0:
                if idx > 0 and colors[idx] == colors[idx - 1]:
                    same -= 1
                if idx + 1 < n and colors[idx] == colors[idx + 1]:
                    same -= 1
            colors[idx] = color
            if idx > 0 and colors[idx] == colors[idx - 1]:
                same += 1
            if idx + 1 < n and colors[idx] == colors[idx + 1]:
                same += 1
            ans[i] = same
        return ans
'''

files["2673_make_costs_of_paths_equal_in_a_binary_tree"] = '''# LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
# https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        for i in range(n // 2 - 1, -1, -1):
            l, r = 2 * i + 1, 2 * i + 2
            ans += abs(cost[l] - cost[r])
            cost[i] += max(cost[l], cost[r])
        return ans
'''

files["2674_split_a_circular_linked_list"] = '''# LeetCode 2674 - Split a Circular Linked List
# https://leetcode.com/problems/split-a-circular-linked-list/

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitCircularLinkedList(self, list: Optional[ListNode]) -> List[Optional[ListNode]]:
        if not list:
            return [None, None]
        slow = list
        fast = list
        while fast.next is not list and fast.next.next is not list:
            slow = slow.next
            fast = fast.next.next
        if fast.next.next is list:
            fast = fast.next
        head2 = slow.next
        slow.next = list
        fast.next = head2
        return [list, head2]
'''

files["2675_array_of_objects_to_matrix"] = '''# LeetCode 2675 - Array of Objects to Matrix
# https://leetcode.com/problems/array-of-objects-to-matrix/

from typing import Any, Dict, List


class Solution:
    def jsonToMatrix(self, arr: List[Any]) -> List[List[Any]]:
        def is_obj(x: Any) -> bool:
            return isinstance(x, dict)

        def flatten(obj: Any, prefix: str, out: Dict[str, Any]) -> None:
            if not is_obj(obj) and not isinstance(obj, list):
                out[prefix] = obj
                return
            if isinstance(obj, list):
                if not obj:
                    return
                for i, item in enumerate(obj):
                    flatten(item, prefix + "." + str(i) if prefix else str(i), out)
                return
            keys = list(obj.keys())
            if not keys:
                return
            for k in keys:
                flatten(obj[k], prefix + "." + str(k) if prefix else str(k), out)

        maps = []
        for o in arr:
            m = {}
            flatten(o, "", m)
            maps.append(m)
        key_set = set()
        for m in maps:
            key_set.update(m.keys())
        keys = sorted(key_set)
        mat = [keys]
        for m in maps:
            mat.append([m[k] if k in m else "" for k in keys])
        return mat
'''

files["2676_throttle"] = '''# LeetCode 2676 - Throttle
# https://leetcode.com/problems/throttle/

import threading
import time
from typing import Any, Callable


class Solution:
    def throttle(self, fn: Callable, t: int) -> Callable:
        last = float("-inf")
        pending = None
        timer = None
        lock = threading.Lock()

        def run(*args: Any) -> None:
            nonlocal last
            last = time.time() * 1000
            fn(*args)

        def wrapper(*args: Any) -> None:
            nonlocal pending, timer
            with lock:
                now = time.time() * 1000
                remaining = t - (now - last)
                if remaining <= 0:
                    if timer is not None:
                        timer.cancel()
                        timer = None
                    run(*args)
                else:
                    pending = args
                    if timer is None:
                        def later() -> None:
                            nonlocal timer, pending
                            with lock:
                                timer = None
                                if pending is not None:
                                    a = pending
                                    pending = None
                                    run(*a)

                        timer = threading.Timer(remaining / 1000.0, later)
                        timer.daemon = True
                        timer.start()

        return wrapper
'''

files["2677_chunk_array"] = '''# LeetCode 2677 - Chunk Array
# https://leetcode.com/problems/chunk-array/

from typing import Any, List


class Solution:
    def chunk(self, arr: List[Any], size: int) -> List[List[Any]]:
        ans = []
        for i in range(0, len(arr), size):
            ans.append(arr[i:i + size])
        return ans
'''

files["2678_number_of_senior_citizens"] = '''# LeetCode 2678 - Number of Senior Citizens
# https://leetcode.com/problems/number-of-senior-citizens/

from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for d in details:
            age = (ord(d[11]) - 48) * 10 + (ord(d[12]) - 48)
            if age > 60:
                ans += 1
        return ans
'''

files["2679_sum_in_a_matrix"] = '''# LeetCode 2679 - Sum in a Matrix
# https://leetcode.com/problems/sum-in-a-matrix/

from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        ans = 0
        n = len(nums[0])
        for j in range(n):
            mx = 0
            for row in nums:
                mx = max(mx, row[j])
            ans += mx
        return ans
'''

files["2680_maximum_or"] = '''# LeetCode 2680 - Maximum OR
# https://leetcode.com/problems/maximum-or/

from typing import List


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        suf = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] | nums[i]
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] | nums[i]
        ans = 0
        for i in range(n):
            cur = pref[i] | (nums[i] * (2 ** k)) | suf[i + 1]
            if cur > ans:
                ans = cur
        return ans
'''

files["2681_power_of_heroes"] = '''# LeetCode 2681 - Power of Heroes
# https://leetcode.com/problems/power-of-heroes/

from typing import List


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 1000000007
        nums = sorted(nums)
        ans, s = 0, 0
        for x in nums:
            ans = (ans + ((s + x) % MOD) * x % MOD * x) % MOD
            s = (s * 2 + x) % MOD
        return ans
'''

files["2682_find_the_losers_of_the_circular_game"] = '''# LeetCode 2682 - Find the Losers of the Circular Game
# https://leetcode.com/problems/find-the-losers-of-the-circular-game/

from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        seen = [False] * (n + 1)
        cur, step = 1, 1
        while not seen[cur]:
            seen[cur] = True
            cur = (cur - 1 + step * k) % n + 1
            step += 1
        return [i for i in range(1, n + 1) if not seen[i]]
'''

files["2683_neighboring_bitwise_xor"] = '''# LeetCode 2683 - Neighboring Bitwise XOR
# https://leetcode.com/problems/neighboring-bitwise-xor/

from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        x = 0
        for v in derived:
            x ^= v
        return x == 0
'''

files["2684_maximum_number_of_moves_in_a_grid"] = '''# LeetCode 2684 - Maximum Number of Moves in a Grid
# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * m
        for c in range(n - 2, -1, -1):
            ndp = [0] * m
            for r in range(m):
                best = 0
                for dr in (-1, 0, 1):
                    nr = r + dr
                    if 0 <= nr < m and grid[nr][c + 1] > grid[r][c]:
                        best = max(best, 1 + dp[nr])
                ndp[r] = best
            dp = ndp
        return max(dp)
'''

files["2685_count_the_number_of_complete_components"] = '''# LeetCode 2685 - Count the Number of Complete Components
# https://leetcode.com/problems/count-the-number-of-complete-components/

from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        vis = [False] * n
        ans = 0

        def dfs(u: int, nodes: List[int]) -> None:
            vis[u] = True
            nodes.append(u)
            for v in g[u]:
                if not vis[v]:
                    dfs(v, nodes)

        for i in range(n):
            if vis[i]:
                continue
            nodes = []
            dfs(i, nodes)
            ecount = 0
            for u in nodes:
                ecount += len(g[u])
            ecount //= 2
            sz = len(nodes)
            if ecount == sz * (sz - 1) // 2:
                ans += 1
        return ans
'''

files["2689_extract_kth_character_from_the_rope_tree"] = '''# LeetCode 2689 - Extract Kth Character From The Rope Tree
# https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

from typing import Optional


class RopeTreeNode:
    def __init__(self, len: int = 0, val: str = "", left=None, right=None):
        self.len = len
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getKthCharacter(self, root: Optional[RopeTreeNode], k: int) -> str:
        def dfs(node: RopeTreeNode, kk: int) -> str:
            if not node.left and not node.right:
                return node.val
            left_len = 0
            if node.left:
                left_len = node.left.len if node.left.len > 0 else 1
            if kk <= left_len:
                return dfs(node.left, kk)
            return dfs(node.right, kk - left_len)

        return dfs(root, k)
'''

files["2690_infinite_method_object"] = '''# LeetCode 2690 - Infinite Method Object
# https://leetcode.com/problems/infinite-method-object/

from typing import Any, Callable


class _InfiniteObject:
    def __getattr__(self, name: str) -> Callable[..., str]:
        return lambda *args, **kwargs: "Hello World"


class Solution:
    def createInfiniteObject(self) -> Any:
        return _InfiniteObject()
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
