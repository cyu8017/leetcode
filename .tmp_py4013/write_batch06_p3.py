from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
files = {}

files["2691_immutability_helper"] = '''# LeetCode 2691 - Immutability Helper
# https://leetcode.com/problems/immutability-helper/

from typing import Any, Callable, Dict, List, Union


class ImmutableHelper:
    def __init__(self, obj: Any):
        self.obj = obj

    def produce(self, mutator: Callable[[Any], None]) -> Any:
        clones = {}

        def is_obj(v: Any) -> bool:
            return isinstance(v, (dict, list))

        def get_clone(original: Any) -> Any:
            oid = id(original)
            if oid in clones:
                return clones[oid]
            if isinstance(original, list):
                copy = original[:]
            else:
                copy = dict(original)
            clones[oid] = copy
            return copy

        class _Proxy:
            def __init__(self, node: Any, on_replace: Callable[[Any], None]):
                object.__setattr__(self, "_node", node)
                object.__setattr__(self, "_on_replace", on_replace)

            def __getitem__(self, prop: Any) -> Any:
                node = object.__getattribute__(self, "_node")
                on_replace = object.__getattribute__(self, "_on_replace")
                val = node[prop]
                if is_obj(val):
                    def child_replace(child_clone: Any, _prop=prop, _node=node, _on=on_replace) -> None:
                        clone = get_clone(_node)
                        clone[_prop] = child_clone
                        _on(clone)
                    return _Proxy(val, child_replace)
                return val

            def __setitem__(self, prop: Any, value: Any) -> None:
                node = object.__getattribute__(self, "_node")
                on_replace = object.__getattribute__(self, "_on_replace")
                clone = get_clone(node)
                clone[prop] = value
                on_replace(clone)

            def __delitem__(self, prop: Any) -> None:
                node = object.__getattribute__(self, "_node")
                on_replace = object.__getattribute__(self, "_on_replace")
                clone = get_clone(node)
                del clone[prop]
                on_replace(clone)

            def __getattr__(self, prop: str) -> Any:
                node = object.__getattribute__(self, "_node")
                if isinstance(node, dict) and prop in node:
                    return self[prop]
                raise AttributeError(prop)

            def __setattr__(self, prop: str, value: Any) -> None:
                if prop.startswith("_"):
                    object.__setattr__(self, prop, value)
                    return
                self[prop] = value

        root_result = [self.obj]

        def on_root(clone: Any) -> None:
            root_result[0] = clone

        mutator(_Proxy(self.obj, on_root))
        return root_result[0]


class Solution:
    def ImmutableHelper(self, obj: Any, mutators: Any = None) -> ImmutableHelper:
        return ImmutableHelper(obj)
'''

files["2692_make_object_immutable"] = '''# LeetCode 2692 - Make Object Immutable
# https://leetcode.com/problems/make-object-immutable/

from typing import Any


class _ImmutableList(list):
    _MUTATORS = {"pop", "append", "extend", "insert", "remove", "clear", "sort", "reverse"}

    def __setitem__(self, index: Any, value: Any) -> None:
        raise Exception(f"Error Modifying Index: {index}")

    def __delitem__(self, index: Any) -> None:
        raise Exception(f"Error Modifying Index: {index}")

    def __getattribute__(self, prop: str) -> Any:
        if prop in _ImmutableList._MUTATORS:
            def banned(*args: Any, **kwargs: Any) -> Any:
                raise Exception(f"Error Calling Method: {prop}")
            return banned
        return object.__getattribute__(self, prop)


class _ImmutableDict(dict):
    def __setitem__(self, key: Any, value: Any) -> None:
        raise Exception(f"Error Modifying: {key}")

    def __delitem__(self, key: Any) -> None:
        raise Exception(f"Error Modifying: {key}")


class Solution:
    def makeImmutable(self, obj: Any) -> Any:
        def wrap(val: Any) -> Any:
            if val is None or not isinstance(val, (dict, list)):
                return val
            if isinstance(val, list):
                return _ImmutableList(wrap(x) for x in val)
            return _ImmutableDict((k, wrap(v)) for k, v in val.items())

        return wrap(obj)
'''

files["2693_call_function_with_custom_context"] = '''# LeetCode 2693 - Call Function with Custom Context
# https://leetcode.com/problems/call-function-with-custom-context/

from typing import Any, Callable


class Solution:
    def callPolyfill(self, fn: Callable, obj: Any, *args: Any) -> Any:
        key = object()
        if isinstance(obj, dict):
            obj[key] = fn
            res = obj[key](*args)
            del obj[key]
            return res
        setattr(obj, "_call_polyfill_fn", fn)
        res = getattr(obj, "_call_polyfill_fn")(*args)
        delattr(obj, "_call_polyfill_fn")
        return res
'''

files["2694_event_emitter"] = '''# LeetCode 2694 - Event Emitter
# https://leetcode.com/problems/event-emitter/

from typing import Any, Callable, Dict, List


class EventEmitter:
    def __init__(self):
        self.handlers: Dict[str, List[Callable]] = {}

    def subscribe(self, eventName: str, callback: Callable) -> Dict[str, Callable]:
        if eventName not in self.handlers:
            self.handlers[eventName] = []
        lst = self.handlers[eventName]
        lst.append(callback)

        def unsubscribe() -> None:
            if callback in lst:
                lst.remove(callback)

        return {"unsubscribe": unsubscribe}

    def emit(self, eventName: str, args: List[Any] = None) -> List[Any]:
        if args is None:
            args = []
        lst = self.handlers.get(eventName, [])
        return [cb(*args) for cb in lst]


class Solution:
    def EventEmitter(self, actions: Any = None, values: Any = None) -> EventEmitter:
        return EventEmitter()
'''

files["2695_array_wrapper"] = '''# LeetCode 2695 - Array Wrapper
# https://leetcode.com/problems/array-wrapper/

from typing import List


class ArrayWrapper:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def valueOf(self) -> int:
        s = 0
        for x in self.nums:
            s += x
        return s

    def __add__(self, other: "ArrayWrapper") -> int:
        return self.valueOf() + other.valueOf()

    def __int__(self) -> int:
        return self.valueOf()

    def toString(self) -> str:
        return "[" + ",".join(str(x) for x in self.nums) + "]"

    def __str__(self) -> str:
        return self.toString()


class Solution:
    def ArrayWrapper(self, nums: List[int]) -> ArrayWrapper:
        return ArrayWrapper(nums)
'''

files["2696_minimum_string_length_after_removing_substrings"] = '''# LeetCode 2696 - Minimum String Length After Removing Substrings
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/


class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for c in s:
            last = st[-1] if st else None
            if st and ((last == "A" and c == "B") or (last == "C" and c == "D")):
                st.pop()
            else:
                st.append(c)
        return len(st)
'''

files["2697_lexicographically_smallest_palindrome"] = '''# LeetCode 2697 - Lexicographically Smallest Palindrome
# https://leetcode.com/problems/lexicographically-smallest-palindrome/


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        arr = list(s)
        n = len(arr)
        for i in range(n // 2):
            c = arr[i] if arr[i] < arr[n - 1 - i] else arr[n - 1 - i]
            arr[i] = arr[n - 1 - i] = c
        return "".join(arr)
'''

files["2698_find_the_punishment_number_of_an_integer"] = '''# LeetCode 2698 - Find the Punishment Number of an Integer
# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def dfs(s: str, i: int, sm: int, target: int) -> bool:
            if i == len(s):
                return sm == target
            cur = 0
            for j in range(i, len(s)):
                cur = cur * 10 + (ord(s[j]) - 48)
                if sm + cur > target:
                    break
                if dfs(s, j + 1, sm + cur, target):
                    return True
            return False

        ans = 0
        for i in range(1, n + 1):
            sq = i * i
            if dfs(str(sq), 0, 0, i):
                ans += sq
        return ans
'''

files["2699_modify_graph_edge_weights"] = '''# LeetCode 2699 - Modify Graph Edge Weights
# https://leetcode.com/problems/modify-graph-edge-weights/

import heapq
from typing import List


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        INF = 2000000000

        def dijkstra(ignore_neg: bool) -> List[int]:
            dist = [INF] * n
            dist[source] = 0
            pq = [(0, source)]
            while pq:
                d, u = heapq.heappop(pq)
                if d != dist[u]:
                    continue
                for e in edges:
                    a, b, w = e[0], e[1], e[2]
                    if a != u and b != u:
                        continue
                    to = b if a == u else a
                    if w == -1:
                        if ignore_neg:
                            continue
                        w = 1
                    if d + w < dist[to]:
                        dist[to] = d + w
                        heapq.heappush(pq, (dist[to], to))
            return dist

        d = dijkstra(True)
        if d[destination] < target:
            return []
        matched = d[destination] == target
        for i in range(len(edges)):
            if edges[i][2] != -1:
                continue
            if matched:
                edges[i][2] = INF
                continue
            edges[i][2] = 1
            d = dijkstra(False)
            if d[destination] <= target:
                edges[i][2] += target - d[destination]
                matched = True
        d = dijkstra(False)
        if d[destination] != target:
            return []
        return edges
'''

files["2700_differences_between_two_objects"] = '''# LeetCode 2700 - Differences Between Two Objects
# https://leetcode.com/problems/differences-between-two-objects/

from typing import Any, Dict


class Solution:
    def objDiff(self, obj1: Any, obj2: Any) -> Any:
        diff = {}
        if isinstance(obj1, dict):
            keys = obj1.keys()
        else:
            keys = range(len(obj1)) if isinstance(obj1, list) else []
        for k in keys:
            if isinstance(obj1, dict):
                if k not in obj2:
                    continue
                v1, v2 = obj1[k], obj2[k]
            else:
                if not isinstance(obj2, list) or k >= len(obj2):
                    continue
                v1, v2 = obj1[k], obj2[k]
            if isinstance(v1, dict) and isinstance(v2, dict):
                child = self.objDiff(v1, v2)
                if child:
                    diff[k] = child
            elif isinstance(v1, list) and isinstance(v2, list):
                child = self.objDiff(v1, v2)
                if child:
                    diff[k] = child
            elif v1 != v2:
                diff[k] = [v1, v2]
        return diff
'''

files["2702_minimum_operations_to_make_numbers_non_positive"] = '''# LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
# https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

from typing import List
import math


class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        lo, hi = 0, 0
        for v in nums:
            hi = max(hi, math.ceil(v / y), math.ceil(v / x))
        hi += len(nums)

        def ok(ops: int) -> bool:
            extra = 0
            for v in nums:
                remain = v - ops * y
                if remain > 0:
                    extra += math.ceil(remain / (x - y))
            return extra <= ops

        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
'''

files["2703_return_length_of_arguments_passed"] = '''# LeetCode 2703 - Return Length of Arguments Passed
# https://leetcode.com/problems/return-length-of-arguments-passed/

from typing import Any


class Solution:
    def argumentsLength(self, *args: Any) -> int:
        return len(args)
'''

files["2704_to_be_or_not_to_be"] = '''# LeetCode 2704 - To Be Or Not To Be
# https://leetcode.com/problems/to-be-or-not-to-be/

from typing import Any, Callable, Dict


class Solution:
    def expect(self, val: Any) -> Dict[str, Callable[[Any], bool]]:
        def toBe(other: Any) -> bool:
            if val == other:
                return True
            raise Exception("Not Equal")

        def notToBe(other: Any) -> bool:
            if val != other:
                return True
            raise Exception("Equal")

        return {"toBe": toBe, "notToBe": notToBe}
'''

files["2705_compact_object"] = '''# LeetCode 2705 - Compact Object
# https://leetcode.com/problems/compact-object/

from typing import Any


class Solution:
    def compactObject(self, obj: Any) -> Any:
        if isinstance(obj, list):
            out = []
            for x in obj:
                v = self.compactObject(x)
                if v:
                    out.append(v)
            return out
        if isinstance(obj, dict):
            out = {}
            for k, val in obj.items():
                v = self.compactObject(val)
                if v:
                    out[k] = v
            return out
        return obj
'''

files["2706_buy_two_chocolates"] = '''# LeetCode 2706 - Buy Two Chocolates
# https://leetcode.com/problems/buy-two-chocolates/

from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        cost = prices[0] + prices[1]
        return money - cost if cost <= money else money
'''

files["2707_extra_characters_in_a_string"] = '''# LeetCode 2707 - Extra Characters in a String
# https://leetcode.com/problems/extra-characters-in-a-string/

from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dct = set(dictionary)
        n = len(s)
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(n):
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
            for j in range(i + 1, n + 1):
                if s[i:j] in dct:
                    dp[j] = min(dp[j], dp[i])
        return dp[n]
'''

files["2708_maximum_strength_of_a_group"] = '''# LeetCode 2708 - Maximum Strength of a Group
# https://leetcode.com/problems/maximum-strength-of-a-group/

from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        if n == 1:
            return nums[0]
        prod, used, i = 1, False, 0
        while i + 1 < n and nums[i] < 0 and nums[i + 1] < 0:
            prod *= nums[i] * nums[i + 1]
            used = True
            i += 2
        neg_left = i < n and nums[i] < 0
        while i < n:
            if nums[i] > 0:
                prod *= nums[i]
                used = True
            i += 1
        if not used:
            if neg_left:
                for x in nums:
                    if x == 0:
                        return 0
                return nums[n - 1]
            return 0
        return prod
'''

files["2709_greatest_common_divisor_traversal"] = '''# LeetCode 2709 - Greatest Common Divisor Traversal
# https://leetcode.com/problems/greatest-common-divisor-traversal/

from typing import List


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        mx = nums[0]
        for x in nums:
            if x > mx:
                mx = x
        parent = list(range(mx + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        has = [False] * (mx + 1)
        for x in nums:
            if x == 1:
                return False
            has[x] = True
        sieve = [0] * (mx + 1)
        for i in range(2, mx + 1):
            if sieve[i] == 0:
                for j in range(i, mx + 1, i):
                    if sieve[j] == 0:
                        sieve[j] = i
                    if has[j]:
                        unite(i, j)
        root = find(nums[0])
        for x in nums:
            if find(x) != root:
                return False
        return True
'''

files["2710_remove_trailing_zeros_from_a_string"] = '''# LeetCode 2710 - Remove Trailing Zeros From a String
# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        end = len(num)
        while end > 0 and num[end - 1] == "0":
            end -= 1
        return num[:end]
'''

written = 0
for folder, content in files.items():
    if not content.endswith("\n"):
        content += "\n"
    path = root / folder / "solution.py"
    path.write_text(content, encoding="utf-8", newline="\n")
    written += 1
    text = path.read_text(encoding="utf-8")
    assert not text.startswith("\\ufeff"), folder
    assert "def solve(self) -> None:\\n        pass" not in text, folder

print(f"wrote {written}")
