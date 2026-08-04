// LeetCode 1504 - Count Submatrices With All Ones
// https://leetcode.com/problems/count-submatrices-with-all-ones/

class Solution {
    fun numSubmat(mat: Array<IntArray>): Int {
        val n = mat[0].size
        val heights = IntArray(n)
        var ans = 0
        for (row in mat) {
            for (j in 0 until n) {
                heights[j] = if (row[j] == 1) heights[j] + 1 else 0
            }
            var running = 0
            val stack = Array(n) { IntArray(2) }
            var top = -1
            for (h in heights) {
                var count = 1
                while (top >= 0 && stack[top][0] >= h) {
                    val prev = stack[top--]
                    running -= prev[0] * prev[1]
                    count += prev[1]
                }
                stack[++top] = intArrayOf(h, count)
                running += h * count
                ans += running
            }
        }
        return ans
    }
}
