#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2749_minimum_operations_to_make_the_integer_zero"] = r'''# LeetCode 2749 - Minimum Operations to Make the Integer Zero
# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        def popcount(x: int) -> int:
            c = 0
            v = int(x)
            while v > 0:
                c += v & 1
                v >>= 1
            return c

        for k in range(1, 61):
            rem = num1 - k * num2
            if rem < k:
                continue
            if popcount(rem) <= k:
                return k
        return -1
'''

FILES["2750_ways_to_split_array_into_good_subarrays"] = r'''# LeetCode 2750 - Ways to Split Array Into Good Subarrays
# https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

from typing import List


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 1000000007
        ones = [i for i, v in enumerate(nums) if v == 1]
        if not ones:
            return 0
        ans = 1
        for i in range(1, len(ones)):
            ans = ans * (ones[i] - ones[i - 1]) % MOD
        return ans
'''

FILES["2751_robot_collisions"] = r'''# LeetCode 2751 - Robot Collisions
# https://leetcode.com/problems/robot-collisions/

from typing import List


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        n = len(positions)
        idx = list(range(n))
        idx.sort(key=lambda i: positions[i])
        stack = []
        for i in idx:
            cur = [i, healths[i], directions[i]]
            while stack and stack[-1][2] == "R" and cur[2] == "L":
                top = stack[-1]
                if top[1] == cur[1]:
                    stack.pop()
                    cur[1] = 0
                    break
                if top[1] > cur[1]:
                    top[1] -= 1
                    cur[1] = 0
                    break
                cur[1] -= 1
                stack.pop()
            if cur[1] > 0:
                stack.append(cur)
        alive = {i: h for i, h, _ in stack}
        return [alive[i] for i in range(n) if i in alive]
'''

FILES["2753_count_houses_in_a_circular_street_ii"] = r'''# LeetCode 2753 - Count Houses in a Circular Street II
# https://leetcode.com/problems/count-houses-in-a-circular-street-ii/


class Solution:
    def houseCount(self, street, k: int) -> int:
        while not street.isDoorOpen():
            street.moveRight()
        street.closeDoor()
        street.moveRight()
        ans = 1
        for _ in range(1, k):
            if street.isDoorOpen():
                street.closeDoor()
                ans = 0
            ans += 1
            street.moveRight()
        return ans
'''

FILES["2754_bind_function_to_context"] = r'''# LeetCode 2754 - Bind Function to Context
# https://leetcode.com/problems/bind-function-to-context/

from typing import Any, Callable


class Solution:
    def bindPolyfill(self, fn: Callable, obj: Any) -> Callable:
        def bound(*args):
            try:
                return fn.__get__(obj, type(obj))(*args)
            except Exception:
                return fn(*args)

        return bound
'''

FILES["2755_deep_merge_of_two_objects"] = r'''# LeetCode 2755 - Deep Merge of Two Objects
# https://leetcode.com/problems/deep-merge-of-two-objects/

from typing import Any


class Solution:
    def deepMerge(self, obj1: Any, obj2: Any) -> Any:
        def is_obj(x: Any) -> bool:
            return isinstance(x, dict)

        def is_arr(x: Any) -> bool:
            return isinstance(x, list)

        def merge(a: Any, b: Any) -> Any:
            if is_obj(a) and is_obj(b):
                res = dict(a)
                for k in b:
                    if k in res:
                        res[k] = merge(res[k], b[k])
                    else:
                        res[k] = b[k]
                return res
            if is_arr(a) and is_arr(b):
                n = max(len(a), len(b))
                res = [None] * n
                for i in range(n):
                    if i >= len(a):
                        res[i] = b[i]
                    elif i >= len(b):
                        res[i] = a[i]
                    else:
                        res[i] = merge(a[i], b[i])
                return res
            return b

        return merge(obj1, obj2)
'''

FILES["2756_query_batching"] = r'''# LeetCode 2756 - Query Batching
# https://leetcode.com/problems/query-batching/

import time
from typing import Callable, List


class QueryBatcher:
    def __init__(self, queryMultiple: Callable, t: int):
        self.queryMultiple = queryMultiple
        self.t = t
        self.pending = []
        self.busyUntil = 0.0
        self.timer = None

    async def getValue(self, key: str) -> str:
        import asyncio

        loop = asyncio.get_event_loop()
        fut = loop.create_future()
        now = time.time() * 1000
        self.pending.append({"key": key, "resolve": fut})
        if now >= self.busyUntil:
            self.flush()
        elif self.timer is None:
            delay = max(0.0, (self.busyUntil - now) / 1000.0)

            def fire():
                self.timer = None
                self.flush()

            self.timer = loop.call_later(delay, fire)
        return await fut

    def flush(self) -> None:
        if not self.pending:
            return
        batch = self.pending
        self.pending = []
        if self.timer is not None:
            self.timer.cancel()
            self.timer = None
        self.busyUntil = time.time() * 1000 + self.t
        keys = [b["key"] for b in batch]
        result = self.queryMultiple(keys)

        def apply(values: List[str]) -> None:
            for i, item in enumerate(batch):
                fut = item["resolve"]
                if not fut.done():
                    fut.set_result(values[i])

        if hasattr(result, "__await__"):
            import asyncio

            async def wait_and_apply():
                values = await result
                apply(values)

            asyncio.get_event_loop().create_task(wait_and_apply())
        else:
            apply(result)
'''

FILES["2757_generate_circular_array_values"] = r'''# LeetCode 2757 - Generate Circular Array Values
# https://leetcode.com/problems/generate-circular-array-values/

from typing import Any, Generator, List, Optional


class Solution:
    def cycleGenerator(
        self, arr: List[Any], startIndex: int
    ) -> Generator[Any, Optional[int], None]:
        i = startIndex
        jump = yield arr[i]
        while True:
            n = len(arr)
            i = ((i + (jump or 0)) % n + n) % n
            jump = yield arr[i]
'''

FILES["2758_next_day"] = r'''# LeetCode 2758 - Next Day
# https://leetcode.com/problems/next-day/

from datetime import datetime, timedelta


class Solution:
    def nextDay(self, date_value) -> str:
        if isinstance(date_value, datetime):
            d = date_value
        else:
            d = datetime.fromisoformat(str(date_value)[:10])
        nxt = d + timedelta(days=1)
        return f"{nxt.year:04d}-{nxt.month:02d}-{nxt.day:02d}"
'''

FILES["2759_convert_json_string_to_object"] = r'''# LeetCode 2759 - Convert JSON String to Object
# https://leetcode.com/problems/convert-json-string-to-object/

from typing import Any


class Solution:
    def jsonParse(self, s: str) -> Any:
        i = 0

        def parse() -> Any:
            nonlocal i
            if s[i] == '"':
                i += 1
                out = []
                while s[i] != '"':
                    out.append(s[i])
                    i += 1
                i += 1
                return "".join(out)
            if s[i] == "t":
                i += 4
                return True
            if s[i] == "f":
                i += 5
                return False
            if s[i] == "n":
                i += 4
                return None
            if s[i] == "[":
                i += 1
                arr = []
                if s[i] == "]":
                    i += 1
                    return arr
                while True:
                    arr.append(parse())
                    if s[i] == ",":
                        i += 1
                        continue
                    i += 1
                    return arr
            if s[i] == "{":
                i += 1
                obj = {}
                if s[i] == "}":
                    i += 1
                    return obj
                while True:
                    key = parse()
                    i += 1
                    obj[key] = parse()
                    if s[i] == ",":
                        i += 1
                        continue
                    i += 1
                    return obj
            start = i
            if s[i] == "-":
                i += 1
            while i < len(s) and (s[i].isdigit() or s[i] == "."):
                i += 1
            num = s[start:i]
            return float(num) if "." in num else int(num)

        return parse()
'''

FILES["2760_longest_even_odd_subarray_with_threshold"] = r'''# LeetCode 2760 - Longest Even Odd Subarray With Threshold
# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 != 0 or nums[i] > threshold:
                continue
            j = i
            while j + 1 < n and nums[j + 1] <= threshold and nums[j + 1] % 2 != nums[j] % 2:
                j += 1
            ans = max(ans, j - i + 1)
        return ans
'''

FILES["2761_prime_pairs_with_target_sum"] = r'''# LeetCode 2761 - Prime Pairs With Target Sum
# https://leetcode.com/problems/prime-pairs-with-target-sum/

from typing import List


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        i = 2
        while i * i <= n:
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
            i += 1
        ans = []
        for x in range(2, n // 2 + 1):
            y = n - x
            if is_prime[x] and is_prime[y]:
                ans.append([x, y])
        return ans
'''

FILES["2762_continuous_subarrays"] = r'''# LeetCode 2762 - Continuous Subarrays
# https://leetcode.com/problems/continuous-subarrays/

from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        min_q = []
        max_q = []
        for right, val in enumerate(nums):
            while min_q and nums[min_q[-1]] > val:
                min_q.pop()
            while max_q and nums[max_q[-1]] < val:
                max_q.pop()
            min_q.append(right)
            max_q.append(right)
            while nums[max_q[0]] - nums[min_q[0]] > 2:
                left += 1
                if min_q[0] < left:
                    min_q.pop(0)
                if max_q[0] < left:
                    max_q.pop(0)
            ans += right - left + 1
        return ans
'''

FILES["2763_sum_of_imbalance_numbers_of_all_subarrays"] = r'''# LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
# https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

from typing import List


class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            seen = set()
            sorted_vals = []
            imbalance = 0

            def ceil_idx(x: int) -> int:
                lo, hi = 0, len(sorted_vals)
                while lo < hi:
                    mid = (lo + hi) >> 1
                    if sorted_vals[mid] < x:
                        lo = mid + 1
                    else:
                        hi = mid
                return lo

            for j in range(i, n):
                x = nums[j]
                if x not in seen:
                    seen.add(x)
                    idx = ceil_idx(x)
                    nxt = sorted_vals[idx] if idx < len(sorted_vals) else None
                    prev = sorted_vals[idx - 1] if idx > 0 else None
                    if prev is not None and x - prev != 1:
                        imbalance += 1
                    if nxt is not None and nxt - x != 1:
                        imbalance += 1
                    if prev is not None and nxt is not None and nxt - prev > 1:
                        imbalance -= 1
                    sorted_vals.insert(idx, x)
                ans += imbalance
        return ans
'''

FILES["2764_is_array_a_preorder_of_some_binary_tree"] = r'''# LeetCode 2764 - Is Array a Preorder of Some Binary Tree
# https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

from typing import List


class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        if not nodes:
            return True
        stack = [nodes[0][0]]
        for i in range(1, len(nodes)):
            node_id, parent = nodes[i][0], nodes[i][1]
            while stack and stack[-1] != parent:
                stack.pop()
            if not stack:
                return False
            stack.append(node_id)
        return True
'''

FILES["2765_longest_alternating_subarray"] = r'''# LeetCode 2765 - Longest Alternating Subarray
# https://leetcode.com/problems/longest-alternating-subarray/

from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                expect = -1 if (j - i) % 2 == 0 else 1
                if nums[j] - nums[j - 1] != expect:
                    break
                if nums[i + 1] - nums[i] != 1:
                    break
                ans = max(ans, j - i + 1)
        return ans
'''

FILES["2766_relocate_marbles"] = r'''# LeetCode 2766 - Relocate Marbles
# https://leetcode.com/problems/relocate-marbles/

from typing import List


class Solution:
    def relocateMarbles(
        self, nums: List[int], moveFrom: List[int], moveTo: List[int]
    ) -> List[int]:
        pos = set(nums)
        for src, dst in zip(moveFrom, moveTo):
            pos.discard(src)
            pos.add(dst)
        return sorted(pos)
'''

FILES["2767_partition_string_into_minimum_beautiful_substrings"] = r'''# LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
# https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        pow5 = set()
        x = 1
        while True:
            b = bin(x)[2:]
            if len(b) > n:
                break
            pow5.add(b)
            x *= 5
        INF = 10**9
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == INF or s[i] == "0":
                continue
            for j in range(i + 1, n + 1):
                if s[i:j] in pow5:
                    dp[j] = min(dp[j], dp[i] + 1)
        return -1 if dp[n] == INF else dp[n]
'''

FILES["2768_number_of_black_blocks"] = r'''# LeetCode 2768 - Number of Black Blocks
# https://leetcode.com/problems/number-of-black-blocks/

from typing import List


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        cnt = {}
        for x, y in coordinates:
            for i in range(x - 1, x + 1):
                for j in range(y - 1, y + 1):
                    if 0 <= i < m - 1 and 0 <= j < n - 1:
                        key = (i, j)
                        cnt[key] = cnt.get(key, 0) + 1
        out = [0] * 5
        out[0] = (m - 1) * (n - 1)
        for v in cnt.values():
            out[v] += 1
            out[0] -= 1
        return out
'''

FILES["2769_find_the_maximum_achievable_number"] = r'''# LeetCode 2769 - Find the Maximum Achievable Number
# https://leetcode.com/problems/find-the-maximum-achievable-number/


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t
'''

FILES["2770_maximum_number_of_jumps_to_reach_the_last_index"] = r'''# LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0
        for i in range(n):
            if dp[i] < 0:
                continue
            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        return dp[n - 1]
'''

FILES["2771_longest_non_decreasing_subarray_from_two_arrays"] = r'''# LeetCode 2771 - Longest Non-decreasing Subarray From Two Arrays
# https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

from typing import List


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp1 = dp2 = 1
        ans = 1
        for i in range(1, n):
            nd1 = nd2 = 1
            if nums1[i] >= nums1[i - 1]:
                nd1 = max(nd1, dp1 + 1)
            if nums1[i] >= nums2[i - 1]:
                nd1 = max(nd1, dp2 + 1)
            if nums2[i] >= nums1[i - 1]:
                nd2 = max(nd2, dp1 + 1)
            if nums2[i] >= nums2[i - 1]:
                nd2 = max(nd2, dp2 + 1)
            dp1, dp2 = nd1, nd2
            ans = max(ans, dp1, dp2)
        return ans
'''

FILES["2772_apply_operations_to_make_all_array_elements_equal_to_zero"] = r'''# LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
# https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        cur = 0
        for i in range(n):
            cur += diff[i]
            need = nums[i] - cur
            if need < 0:
                return False
            if need > 0:
                if i + k > n:
                    return False
                cur += need
                diff[i + k] -= need
        return True
'''

FILES["2773_height_of_special_binary_tree"] = r'''# LeetCode 2773 - Height of Special Binary Tree
# https://leetcode.com/problems/height-of-special-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def heightOfTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            if node.left and node.left.right is node:
                return dfs(node.right) + 1
            if node.right and node.right.left is node:
                return dfs(node.left) + 1
            return max(dfs(node.left), dfs(node.right)) + 1

        return dfs(root)
'''

FILES["2774_array_upper_bound"] = r'''# LeetCode 2774 - Array Upper Bound
# https://leetcode.com/problems/array-upper-bound/

from typing import List


class Solution:
    def upperBound(self, arr: List[int], target: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) >> 1
            if arr[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        if lo == 0 or arr[lo - 1] != target:
            return -1
        return lo - 1
'''

FILES["2775_undefined_to_null"] = r'''# LeetCode 2775 - Undefined to Null
# https://leetcode.com/problems/undefined-to-null/

from typing import Any


UNDEFINED = object()


class Solution:
    def undefinedToNull(self, obj: Any) -> Any:
        if obj is UNDEFINED:
            return None
        if obj is None or not isinstance(obj, (dict, list)):
            return obj
        if isinstance(obj, list):
            for i in range(len(obj)):
                obj[i] = self.undefinedToNull(obj[i])
            return obj
        for k in list(obj.keys()):
            obj[k] = self.undefinedToNull(obj[k])
        return obj
'''

FILES["2776_convert_callback_based_function_to_promise_based_function"] = r'''# LeetCode 2776 - Convert Callback Based Function to Promise Based Function
# https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/

import asyncio
from typing import Callable


class Solution:
    def promisify(self, fn: Callable) -> Callable:
        def wrapped(*args):
            loop = asyncio.get_event_loop()
            fut = loop.create_future()

            def callback(err, result=None):
                if fut.done():
                    return
                if err:
                    fut.set_exception(err if isinstance(err, BaseException) else Exception(err))
                else:
                    fut.set_result(result)

            fn(callback, *args)
            return fut

        return wrapped
'''

FILES["2777_date_range_generator"] = r'''# LeetCode 2777 - Date Range Generator
# https://leetcode.com/problems/date-range-generator/

from datetime import datetime, timedelta
from typing import Generator


class Solution:
    def dateRangeGenerator(
        self, start: str, end: str, step: int
    ) -> Generator[str, None, None]:
        cur = datetime.fromisoformat(start)
        last = datetime.fromisoformat(end)
        while cur <= last:
            yield f"{cur.year:04d}-{cur.month:02d}-{cur.day:02d}"
            cur = cur + timedelta(days=step)
'''

FILES["2778_sum_of_squares_of_special_elements"] = r'''# LeetCode 2778 - Sum of Squares of Special Elements
# https://leetcode.com/problems/sum-of-squares-of-special-elements/

from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if n % (i + 1) == 0:
                ans += nums[i] * nums[i]
        return ans
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
