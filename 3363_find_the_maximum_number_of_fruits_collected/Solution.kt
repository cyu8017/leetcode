// LeetCode 3363 - Find the Maximum Number of Fruits Collected
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

class Solution {
    fun maxCollectedFruits(fruits: Array<IntArray>): Int {
        val n = fruits.size
        var ans = 0
        for (i in 0 until n) {
            ans += fruits[i][i]
            fruits[i][i] = 0
        }
        val neg = -(1 shl 30)
        val dp2 = Array(n) { IntArray(n) { neg } }
        val dp3 = Array(n) { IntArray(n) { neg } }
        dp2[0][n - 1] = fruits[0][n - 1]
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (dp2[i][j] == neg) continue
                for (dj in intArrayOf(-1, 0, 1)) {
                    val ni = i + 1
                    val nj = j + dj
                    if (ni < n && nj in 0 until n && nj > ni) {
                        val v = dp2[i][j] + fruits[ni][nj]
                        if (v > dp2[ni][nj]) dp2[ni][nj] = v
                    }
                }
            }
        }
        dp3[n - 1][0] = fruits[n - 1][0]
        for (j in 0 until n) {
            for (i in 0 until n) {
                if (dp3[i][j] == neg) continue
                for (di in intArrayOf(-1, 0, 1)) {
                    val ni = i + di
                    val nj = j + 1
                    if (ni in 0 until n && nj < n && ni > nj) {
                        val v = dp3[i][j] + fruits[ni][nj]
                        if (v > dp3[ni][nj]) dp3[ni][nj] = v
                    }
                }
            }
        }
        ans += dp2[n - 1][n - 1] + dp3[n - 1][n - 1]
        return ans
    }
}
