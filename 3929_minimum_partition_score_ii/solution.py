# LeetCode 3929 - Minimum Partition Score II
# https://leetcode.com/problems/minimum-partition-score-ii/

from typing import List


class Line:
    def __init__(self, slope: int = 0, intercept: int = 0, count: int = 0, valid: bool = False):
        self.slope = slope
        self.intercept = intercept
        self.count = count
        self.valid = valid


class State:
    def __init__(self, value: int = 0, count: int = 0, valid: bool = False):
        self.value = value
        self.count = count
        self.valid = valid


def better(a: State, b: State) -> State:
    if not a.valid:
        return b
    if not b.valid:
        return a
    if a.value != b.value:
        return a if a.value < b.value else b
    return a if a.count >= b.count else b


def evaluate(line: Line, x: int) -> State:
    if not line.valid:
        return State()
    return State(line.slope * x + line.intercept, line.count, True)


class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def insert(tree: List[Line], node: int, left: int, right: int, line: Line) -> None:
            if not tree[node].valid:
                tree[node] = line
                return
            mid = (left + right) // 2
            x_left = prefix[left]
            x_mid = prefix[mid]
            left_better = better(evaluate(line, x_left), evaluate(tree[node], x_left))
            mid_better = better(evaluate(line, x_mid), evaluate(tree[node], x_mid))
            line_wins_left = left_better.value == evaluate(line, x_left).value and left_better.count == line.count
            line_wins_mid = mid_better.value == evaluate(line, x_mid).value and mid_better.count == line.count
            if line_wins_mid:
                tmp = tree[node]
                tree[node] = line
                line = tmp
            if left == right:
                return
            if line_wins_left != line_wins_mid:
                insert(tree, node * 2, left, mid, line)
            else:
                insert(tree, node * 2 + 1, mid + 1, right, line)

        def query(tree: List[Line], node: int, left: int, right: int, index: int) -> State:
            result = evaluate(tree[node], prefix[index])
            if left == right:
                return result
            mid = (left + right) // 2
            if index <= mid:
                return better(result, query(tree, node * 2, left, mid, index))
            return better(result, query(tree, node * 2 + 1, mid + 1, right, index))

        def run(penalty: int) -> State:
            tree = [Line() for _ in range(4 * (n + 1))]
            insert(tree, 1, 0, n, Line(0, 0, 0, True))
            current = State()
            for i in range(1, n + 1):
                best = query(tree, 1, 0, n, i)
                x = prefix[i]
                current = State(best.value + x * x + x + penalty, best.count + 1, True)
                insert(tree, 1, 0, n, Line(-2 * x, current.value + x * x - x, current.count, True))
            return current

        bound = prefix[n] * prefix[n] + prefix[n] + 1
        low = 0
        high = bound
        while low < high:
            mid = low + (high - low + 1) // 2
            if run(mid).count >= k:
                low = mid
            else:
                high = mid - 1
        state = run(low)
        return (state.value - low * k) // 2
