// LeetCode 3929 - Minimum Partition Score II
// https://leetcode.com/problems/minimum-partition-score-ii/

class Solution {
    private class Line(
        var slope: Long = 0,
        var intercept: Long = 0,
        var count: Int = 0,
        var valid: Boolean = false
    )

    private class State(
        var value: Long = 0,
        var count: Int = 0,
        var valid: Boolean = false
    )

    private fun better(a: State, b: State): State {
        if (!a.valid) return b
        if (!b.valid) return a
        if (a.value != b.value) return if (a.value < b.value) a else b
        return if (a.count >= b.count) a else b
    }

    private fun evaluate(line: Line, x: Long): State {
        if (!line.valid) return State()
        return State(line.slope * x + line.intercept, line.count, true)
    }

    private lateinit var prefix: LongArray
    private var n = 0

    private fun insert(tree: Array<Line>, node: Int, left: Int, right: Int, line0: Line) {
        var line = line0
        if (!tree[node].valid) {
            tree[node] = line
            return
        }
        val mid = (left + right) / 2
        val xLeft = prefix[left]
        val xMid = prefix[mid]
        val leftBetter = better(evaluate(line, xLeft), evaluate(tree[node], xLeft))
        val midBetter = better(evaluate(line, xMid), evaluate(tree[node], xMid))
        val lineWinsLeft = leftBetter.value == evaluate(line, xLeft).value && leftBetter.count == line.count
        val lineWinsMid = midBetter.value == evaluate(line, xMid).value && midBetter.count == line.count
        if (lineWinsMid) {
            val tmp = tree[node]
            tree[node] = line
            line = tmp
        }
        if (left == right) return
        if (lineWinsLeft != lineWinsMid) insert(tree, node * 2, left, mid, line)
        else insert(tree, node * 2 + 1, mid + 1, right, line)
    }

    private fun query(tree: Array<Line>, node: Int, left: Int, right: Int, index: Int): State {
        val result = evaluate(tree[node], prefix[index])
        if (left == right) return result
        val mid = (left + right) / 2
        return if (index <= mid) better(result, query(tree, node * 2, left, mid, index))
        else better(result, query(tree, node * 2 + 1, mid + 1, right, index))
    }

    private fun run(penalty: Long): State {
        val tree = Array(4 * (n + 1)) { Line() }
        insert(tree, 1, 0, n, Line(0, 0, 0, true))
        var current = State()
        for (i in 1..n) {
            val best = query(tree, 1, 0, n, i)
            val x = prefix[i]
            current = State(best.value + x * x + x + penalty, best.count + 1, true)
            insert(tree, 1, 0, n, Line(-2 * x, current.value + x * x - x, current.count, true))
        }
        return current
    }

    fun minPartitionScore(nums: IntArray, k: Int): Long {
        n = nums.size
        prefix = LongArray(n + 1)
        for (i in 0 until n) prefix[i + 1] = prefix[i] + nums[i]
        val bound = prefix[n] * prefix[n] + prefix[n] + 1
        var low = 0L
        var high = bound
        while (low < high) {
            val mid = low + (high - low + 1) / 2
            if (run(mid).count >= k) low = mid else high = mid - 1
        }
        val state = run(low)
        return (state.value - low * k) / 2
    }
}
