// LeetCode 0576 - Out of Boundary Paths
// https://leetcode.com/problems/out-of-boundary-paths/


class Solution {
    fun findPaths(m: Int, n: Int, maxMove: Int, startRow: Int, startColumn: Int): Int {
        val MOD = 1_000_000_007
        var dp = Array(m) { IntArray(n) }
        dp[startRow][startColumn] = 1
        var result = 0
        val dirs = arrayOf(intArrayOf(0, 1), intArrayOf(0, -1), intArrayOf(1, 0), intArrayOf(-1, 0))
        repeat(maxMove) {
            val nxt = Array(m) { IntArray(n) }
            for (row in 0 until m) {
                for (col in 0 until n) {
                    val ways = dp[row][col]
                    if (ways == 0) continue
                    for (dir in dirs) {
                        val nr = row + dir[0]
                        val nc = col + dir[1]
                        if (nr in 0 until m && nc in 0 until n) {
                            nxt[nr][nc] = (nxt[nr][nc] + ways) % MOD
                        } else {
                            result = (result + ways) % MOD
                        }
                    }
                }
            }
            dp = nxt
        }
        return result
    }
}
