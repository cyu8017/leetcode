// LeetCode 3276 - Select Cells in Grid With Maximum Score
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

class Solution {
    fun maxScore(grid: Array<IntArray>): Int {
        val m = grid.size
        val vals = HashMap<Int, MutableList<Int>>()
        for (i in 0 until m) {
            val seen = HashSet<Int>()
            for (v in grid[i]) {
                if (seen.add(v)) {
                    vals.getOrPut(v) { ArrayList() }.add(i)
                }
            }
        }
        val arr = ArrayList(vals.keys)
        arr.sortDescending()
        val N = 1 shl m
        var dp = IntArray(N)
        for (v in arr) {
            val ndp = dp.copyOf()
            for (r in vals[v]!!) {
                val bit = 1 shl r
                for (mask in 0 until N) {
                    if ((mask and bit) != 0) continue
                    val cand = dp[mask] + v
                    val nmask = mask or bit
                    if (cand > ndp[nmask]) ndp[nmask] = cand
                }
            }
            dp = ndp
        }
        var ans = 0
        for (x in dp) ans = maxOf(ans, x)
        return ans
    }
}
