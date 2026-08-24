// LeetCode 3225 - Maximum Score From Grid Operations
// https://leetcode.com/problems/maximum-score-from-grid-operations/

class Solution {
    fun maximumScore(grid: Array<IntArray>): Long {
        var n = grid.size
        var prefix = LongArray(n)[]
        for (j in 0 until n) {
            prefix[j] = LongArray(n + 1)
            for (i in 0 until n) { prefix[j][i + 1] = prefix[j][i] + grid[i][j] }
        }
        var prevPick = LongArray(n + 1)
        var prevSkip = LongArray(n + 1)
        for (j in 1 until n) {
            var currPick = LongArray(n + 1)
        var currSkip = LongArray(n + 1)
            for (curr in 0 ..n) {
                for (prev in 0 ..n) {
                    if (curr > prev) {
                        var score = prefix[j - 1][curr] - prefix[j - 1][prev]
                        currPick[curr] = maxOf(currPick[curr], prevSkip[prev] + score)
                        currSkip[curr] = maxOf(currSkip[curr], prevSkip[prev] + score)
                    } else {
                        var score = prefix[j][prev] - prefix[j][curr]
                        currPick[curr] = maxOf(currPick[curr], prevPick[prev] + score)
                        currSkip[curr] = maxOf(currSkip[curr], prevPick[prev])
                    }
                }
            }
            prevPick = currPick
            prevSkip = currSkip
        }
        var ans = Long.MIN_VALUE
        for (v in prevPick) { ans = maxOf(ans, v) }
        return ans
    }
}
