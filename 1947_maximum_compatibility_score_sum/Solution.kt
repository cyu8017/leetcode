// LeetCode 1947
// https://leetcode.com/problems/maximum-compatibility-score-sum/

class Solution {
    fun maxCompatibilitySum(students: Array<IntArray>, mentors: Array<IntArray>): Int {
        val m = students.size
        val score = Array(m) { IntArray(m) }
        for (i in 0 until m) for (j in 0 until m) {
            score[i][j] = students[i].indices.count { students[i][it] == mentors[j][it] }
        }
        val memo = IntArray(1 shl m) { -1 }
        fun dp(i: Int, mask: Int): Int {
            if (i == m) return 0
            if (memo[mask] != -1) return memo[mask]
            var best = 0
            for (j in 0 until m) if (mask and (1 shl j) == 0) {
                best = maxOf(best, score[i][j] + dp(i + 1, mask or (1 shl j)))
            }
            memo[mask] = best
            return best
        }
        return dp(0, 0)
    }
}
