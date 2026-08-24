// LeetCode 1536 - Minimum Swaps to Arrange a Binary Grid
// https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

class Solution {
    fun minSwaps(grid: Array<IntArray>): Int {
        val n = grid.size
        val zeros = IntArray(n)
        for (i in 0 until n) {
            var count = 0
            for (j in n - 1 downTo 0) {
                if (grid[i][j] != 0) break
                count++
            }
            zeros[i] = count
        }
        var answer = 0
        for (i in 0 until n) {
            val required = n - i - 1
            var j = i
            while (j < n && zeros[j] < required) j++
            if (j == n) return -1
            answer += j - i
            val value = zeros[j]
            for (row in j downTo i + 1) {
                zeros[row] = zeros[row - 1]
            }
            zeros[i] = value
        }
        return answer
    }
}
