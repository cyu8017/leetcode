// LeetCode 3929 - Minimum Partition Score II
// https://leetcode.com/problems/minimum-partition-score-ii/


class Solution {
    private struct Line {
        var slope: Int
        var intercept: Int
        var count: Int
        var valid: Bool
        init() { slope = 0; intercept = 0; count = 0; valid = false }
        init(_ slope: Int, _ intercept: Int, _ count: Int, _ valid: Bool) {
            self.slope = slope; self.intercept = intercept; self.count = count; self.valid = valid
        }
    }
    private struct State {
        var value: Int
        var count: Int
        var valid: Bool
        init() { value = 0; count = 0; valid = false }
        init(_ value: Int, _ count: Int, _ valid: Bool) {
            self.value = value; self.count = count; self.valid = valid
        }
    }

    private var prefix: [Int] = []
    private var n = 0

    private func better(_ a: State, _ b: State) -> State {
        if !a.valid { return b }
        if !b.valid { return a }
        if a.value != b.value { return a.value < b.value ? a : b }
        return a.count >= b.count ? a : b
    }

    private func evaluate(_ line: Line, _ x: Int) -> State {
        if !line.valid { return State() }
        return State(line.slope * x + line.intercept, line.count, true)
    }

    private func insert(_ tree: inout [Line], _ node: Int, _ left: Int, _ right: Int, _ lineIn: Line) {
        var line = lineIn
        if !tree[node].valid {
            tree[node] = line
            return
        }
        let mid = (left + right) / 2
        let xLeft = prefix[left]
        let leftBetter = better(evaluate(line, xLeft), evaluate(tree[node], xLeft))
        let midBetter = better(evaluate(line, prefix[mid]), evaluate(tree[node], prefix[mid]))
        let lineWinsLeft = leftBetter.value == evaluate(line, xLeft).value && leftBetter.count == line.count
        let lineWinsMid = midBetter.value == evaluate(line, prefix[mid]).value && midBetter.count == line.count
        if lineWinsMid {
            let tmp = tree[node]
            tree[node] = line
            line = tmp
        }
        if left == right { return }
        if lineWinsLeft != lineWinsMid {
            insert(&tree, node * 2, left, mid, line)
        } else {
            insert(&tree, node * 2 + 1, mid + 1, right, line)
        }
    }

    private func query(_ tree: [Line], _ node: Int, _ left: Int, _ right: Int, _ index: Int) -> State {
        let result = evaluate(tree[node], prefix[index])
        if left == right { return result }
        let mid = (left + right) / 2
        if index <= mid { return better(result, query(tree, node * 2, left, mid, index)) }
        return better(result, query(tree, node * 2 + 1, mid + 1, right, index))
    }

    private func run(_ penalty: Int) -> State {
        var tree = Array(repeating: Line(), count: 4 * (n + 1))
        insert(&tree, 1, 0, n, Line(0, 0, 0, true))
        var current = State()
        for i in 1...n {
            let best = query(tree, 1, 0, n, i)
            let x = prefix[i]
            current = State(best.value + x * x + x + penalty, best.count + 1, true)
            insert(&tree, 1, 0, n, Line(-2 * x, current.value + x * x - x, current.count, true))
        }
        return current
    }

    func minPartitionScore(_ nums: [Int], _ k: Int) -> Int {
        n = nums.count
        prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + nums[i] }
        let bound = prefix[n] * prefix[n] + prefix[n] + 1
        var low = 0, high = bound
        while low < high {
            let mid = low + (high - low + 1) / 2
            if run(mid).count >= k { low = mid }
            else { high = mid - 1 }
        }
        let state = run(low)
        return (state.value - low * k) / 2
    }
}
