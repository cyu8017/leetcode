// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/


class Solution {
    fun sumRemoteness(grid: Array<IntArray>): Long {
        val m = grid.size
        val n = grid[0].size
        val seen = Array(m) { BooleanArray(n) }
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        var total = 0L
        for (i in 0 until m) for (j in 0 until n) if (grid[i][j] != -1) total += grid[i][j]
        var ans = 0L
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == -1 || seen[i][j]) continue
                val q = ArrayDeque<IntArray>()
                q.add(intArrayOf(i, j))
                seen[i][j] = true
                var sum = 0L
                var cnt = 0
                while (q.isNotEmpty()) {
                    val cur = q.removeFirst()
                    val x = cur[0]
                    val y = cur[1]
                    sum += grid[x][y]
                    cnt++
                    for (d in dirs) {
                        val ni = x + d[0]
                        val nj = y + d[1]
                        if (ni in 0 until m && nj in 0 until n && !seen[ni][nj] && grid[ni][nj] != -1) {
                            seen[ni][nj] = true
                            q.add(intArrayOf(ni, nj))
                        }
                    }
                }
                ans += (total - sum) * cnt
            }
        }
        return ans
    }
}
