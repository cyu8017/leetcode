#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}


def add(folder, body):
    SOLUTIONS[folder] = body if body.endswith("\n") else body + "\n"


add("2621_sleep", r'''# LeetCode 2621 - Sleep
# https://leetcode.com/problems/sleep/

import time


class Solution:
    def sleep(self, millis: int):
        time.sleep(millis / 1000.0)
        return None
''')

add("2622_cache_with_time_limit", r'''# LeetCode 2622 - Cache With Time Limit
# https://leetcode.com/problems/cache-with-time-limit/

import time
from typing import Any


class TimeLimitedCache:
    def __init__(self):
        self.data = {}

    def set(self, key: int, value: int, duration: int) -> bool:
        now = int(time.time() * 1000)
        e = self.data.get(key)
        alive = e is not None and e["expire"] > now
        self.data[key] = {"value": value, "expire": now + duration}
        return alive

    def get(self, key: int) -> int:
        now = int(time.time() * 1000)
        e = self.data.get(key)
        if e is None or e["expire"] <= now:
            return -1
        return e["value"]

    def count(self) -> int:
        now = int(time.time() * 1000)
        cnt = 0
        dead = []
        for k, e in self.data.items():
            if e["expire"] > now:
                cnt += 1
            else:
                dead.append(k)
        for k in dead:
            del self.data[k]
        return cnt


class Solution:
    def TimeLimitedCache(self, actions: Any = None) -> TimeLimitedCache:
        return TimeLimitedCache()
''')

add("2623_memoize", r'''# LeetCode 2623 - Memoize
# https://leetcode.com/problems/memoize/

from typing import Any, Callable


class Solution:
    def memoize(self, fn: Callable) -> Callable:
        cache = {}

        def wrapped(x: Any) -> Any:
            if x in cache:
                return cache[x]
            r = fn(x)
            cache[x] = r
            return r

        return wrapped
''')

add("2624_snail_traversal", r'''# LeetCode 2624 - Snail Traversal
# https://leetcode.com/problems/snail-traversal/

from typing import List


class Solution:
    def snail(self, nums: List[int], rowsCount: int, colsCount: int) -> List[List[int]]:
        if rowsCount * colsCount != len(nums):
            return []
        ans = [[0] * colsCount for _ in range(rowsCount)]
        idx = 0
        for c in range(colsCount):
            if c % 2 == 0:
                for r in range(rowsCount):
                    ans[r][c] = nums[idx]
                    idx += 1
            else:
                for r in range(rowsCount - 1, -1, -1):
                    ans[r][c] = nums[idx]
                    idx += 1
        return ans
''')

add("2625_flatten_deeply_nested_array", r'''# LeetCode 2625 - Flatten Deeply Nested Array
# https://leetcode.com/problems/flatten-deeply-nested-array/

from typing import Any, List


class Solution:
    def flat(self, arr: List[Any], n: int) -> List[Any]:
        res = []

        def dfs(a: List[Any], depth: int) -> None:
            for x in a:
                if isinstance(x, list) and depth < n:
                    dfs(x, depth + 1)
                else:
                    res.append(x)

        dfs(arr, 0)
        return res
''')

add("2626_array_reduce_transformation", r'''# LeetCode 2626 - Array Reduce Transformation
# https://leetcode.com/problems/array-reduce-transformation/

from typing import Any, Callable, List


class Solution:
    def reduce(self, nums: List[int], fn: Callable, init: Any) -> Any:
        acc = init
        for x in nums:
            acc = fn(acc, x)
        return acc
''')

add("2627_debounce", r'''# LeetCode 2627 - Debounce
# https://leetcode.com/problems/debounce/

from typing import Any, Callable, List


class Solution:
    def debounce(self, fn: Callable, t: int) -> Callable:
        timer = {"id": None}

        def wrapped(*args: Any) -> Any:
            timer["id"] = {"args": args, "t": t}
            return fn(*args)

        return wrapped
''')

add("2628_json_deep_equal", r'''# LeetCode 2628 - JSON Deep Equal
# https://leetcode.com/problems/json-deep-equal/

from typing import Any


class Solution:
    def areDeeplyEqual(self, o1: Any, o2: Any) -> bool:
        if o1 is o2 or o1 == o2 and not isinstance(o1, (list, dict)):
            if o1 == o2 and type(o1) is type(o2) and not isinstance(o1, (list, dict)):
                return True
            if o1 is o2:
                return True
        if type(o1) is not type(o2):
            return False
        if o1 is None or o2 is None:
            return False
        if not isinstance(o1, (list, dict)):
            return o1 == o2
        if isinstance(o1, list) != isinstance(o2, list):
            return False
        if isinstance(o1, list):
            if len(o1) != len(o2):
                return False
            for i in range(len(o1)):
                if not self.areDeeplyEqual(o1[i], o2[i]):
                    return False
            return True
        if len(o1) != len(o2):
            return False
        for k in o1:
            if k not in o2 or not self.areDeeplyEqual(o1[k], o2[k]):
                return False
        return True
''')

add("2629_function_composition", r'''# LeetCode 2629 - Function Composition
# https://leetcode.com/problems/function-composition/

from typing import Callable, List


class Solution:
    def compose(self, functions: List[Callable]) -> Callable:
        def wrapped(x):
            for i in range(len(functions) - 1, -1, -1):
                x = functions[i](x)
            return x

        return wrapped
''')

add("2630_memoize_ii", r'''# LeetCode 2630 - Memoize II
# https://leetcode.com/problems/memoize-ii/

from typing import Any, Callable


class Solution:
    def memoize(self, fn: Callable) -> Callable:
        root = {}
        RES = object()

        def wrapped(*args: Any) -> Any:
            node = root
            for a in args:
                if a not in node:
                    node[a] = {}
                node = node[a]
            if RES in node:
                return node[RES]
            v = fn(*args)
            node[RES] = v
            return v

        return wrapped
''')

add("2631_group_by", r'''# LeetCode 2631 - Group By
# https://leetcode.com/problems/group-by/

from typing import Any, Callable, Dict, List


class Solution:
    def groupBy(self, array: List[Any], fn: Callable) -> Dict[Any, List[Any]]:
        out = {}
        for x in array:
            k = fn(x)
            if k not in out:
                out[k] = []
            out[k].append(x)
        return out
''')

add("2632_curry", r'''# LeetCode 2632 - Curry
# https://leetcode.com/problems/curry/

from typing import Any, Callable


class Solution:
    def curry(self, fn: Callable) -> Callable:
        arity = fn.__code__.co_argcount

        def curried(*args: Any):
            if len(args) >= arity:
                return fn(*args)

            def nxt(*next_args: Any):
                return curried(*args, *next_args)

            return nxt

        return curried
''')

add("2633_convert_object_to_json_string", r'''# LeetCode 2633 - Convert Object to JSON String
# https://leetcode.com/problems/convert-object-to-json-string/

from typing import Any


class Solution:
    def jsonStringify(self, object: Any) -> str:
        if object is None:
            return "null"
        t = type(object)
        if t is str:
            return '"' + object + '"'
        if t is bool:
            return "true" if object else "false"
        if t is int or t is float:
            return str(object)
        if isinstance(object, list):
            return "[" + ",".join(self.jsonStringify(x) for x in object) + "]"
        keys = list(object.keys())
        return "{" + ",".join('"' + str(k) + '":' + self.jsonStringify(object[k]) for k in keys) + "}"
''')

add("2634_filter_elements_from_array", r'''# LeetCode 2634 - Filter Elements from Array
# https://leetcode.com/problems/filter-elements-from-array/

from typing import Any, Callable, List


class Solution:
    def filter(self, arr: List[Any], fn: Callable) -> List[Any]:
        out = []
        for i in range(len(arr)):
            if fn(arr[i], i):
                out.append(arr[i])
        return out
''')

add("2635_apply_transform_over_each_element_in_array", r'''# LeetCode 2635 - Apply Transform Over Each Element in Array
# https://leetcode.com/problems/apply-transform-over-each-element-in-array/

from typing import Any, Callable, List


class Solution:
    def map(self, arr: List[Any], fn: Callable) -> List[Any]:
        out = [None] * len(arr)
        for i in range(len(arr)):
            out[i] = fn(arr[i], i)
        return out
''')

add("2636_promise_pool", r'''# LeetCode 2636 - Promise Pool
# https://leetcode.com/problems/promise-pool/

from typing import Callable, List


class Solution:
    def promisePool(self, functions: List[Callable], n: int = 1):
        i = 0

        def worker() -> None:
            nonlocal i
            while i < len(functions):
                cur = i
                i += 1
                functions[cur]()

        limit = min(n, len(functions))
        for _ in range(limit):
            worker()
        return None
''')

add("2637_promise_time_limit", r'''# LeetCode 2637 - Promise Time Limit
# https://leetcode.com/problems/promise-time-limit/

import time
from typing import Any, Callable


class Solution:
    def timeLimit(self, fn: Callable, t: int) -> Callable:
        def wrapped(*args: Any):
            start = time.time()
            res = fn(*args)
            if (time.time() - start) * 1000 > t:
                raise TimeoutError("Time Limit Exceeded")
            return res

        return wrapped
''')

add("2638_count_the_number_of_k_free_subsets", r'''# LeetCode 2638 - Count the Number of K-Free Subsets
# https://leetcode.com/problems/count-the-number-of-k-free-subsets/

from typing import List


class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        groups = {}
        for x in nums:
            key = x % k
            if key not in groups:
                groups[key] = []
            groups[key].append(x)
        ans = 1
        for g in groups.values():
            prev_val = -1
            prev_take = 0
            prev_skip = 1
            for v in g:
                skip = prev_take + prev_skip
                take = prev_skip if prev_val + k == v else prev_take + prev_skip
                prev_take = take
                prev_skip = skip
                prev_val = v
            ans *= prev_take + prev_skip
        return ans
''')

add("2639_find_the_width_of_columns_of_a_grid", r'''# LeetCode 2639 - Find the Width of Columns of a Grid
# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = [0] * n

        def width(x: int) -> int:
            if x == 0:
                return 1
            w = 0
            if x < 0:
                w += 1
                x = -x
            while x > 0:
                w += 1
                x //= 10
            return w

        for row in grid:
            for j in range(n):
                ans[j] = max(ans[j], width(row[j]))
        return ans
''')

add("2640_find_the_score_of_all_prefixes_of_an_array", r'''# LeetCode 2640 - Find the Score of All Prefixes of an Array
# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        mx = 0
        s = 0
        for i, x in enumerate(nums):
            if x > mx:
                mx = x
            s += x + mx
            ans[i] = s
        return ans
''')


def main():
    written = 0
    for folder, body in SOLUTIONS.items():
        path = ROOT / folder / "solution.py"
        path.write_text(body, encoding="utf-8")
        if body.startswith("\ufeff"):
            raise SystemExit(f"BOM in {folder}")
        written += 1
    print(f"wrote {written}")


if __name__ == "__main__":
    main()
