// LeetCode 3414 - Maximum Score of Non-overlapping Intervals
// https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

class Solution {
    private class It(val l: Int, val r: Int, val w: Int, val i: Int)
    private class State(var score: Long = 0L, var idx: MutableList<Int> = ArrayList()) {
        fun copy(): State = State(score, ArrayList(idx))
    }

    private fun better(a: State, b: State): State {
        if (a.score != b.score) return if (a.score > b.score) a else b
        val n = minOf(a.idx.size, b.idx.size)
        for (i in 0 until n) {
            if (a.idx[i] != b.idx[i]) return if (a.idx[i] < b.idx[i]) a else b
        }
        return if (a.idx.size <= b.idx.size) a else b
    }

    fun maximumWeight(intervals: Array<IntArray>): IntArray {
        val n = intervals.size
        val arr = Array(n) { i -> It(intervals[i][0], intervals[i][1], intervals[i][2], i) }
        arr.sortBy { it.r }
        val dp = Array(n + 1) { Array(5) { State() } }
        for (i in 1..n) {
            val cur = arr[i - 1]
            for (t in 0..4) dp[i][t] = dp[i - 1][t].copy()
            var lo = 0
            var hi = i - 1
            while (lo < hi) {
                val mid = (lo + hi) / 2
                if (arr[mid].r < cur.l) lo = mid + 1 else hi = mid
            }
            val prev = lo
            for (t in 1..4) {
                val prevState = dp[prev][t - 1]
                val cand = prevState.copy()
                cand.score = prevState.score + cur.w
                cand.idx.add(cur.i)
                cand.idx.sort()
                dp[i][t] = better(dp[i][t], cand)
            }
        }
        var best = dp[n][0]
        for (t in 1..4) best = better(best, dp[n][t])
        return best.idx.toIntArray()
    }
}
