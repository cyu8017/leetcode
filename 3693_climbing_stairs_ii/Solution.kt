// LeetCode 3693 - Climbing Stairs II
// https://leetcode.com/problems/climbing-stairs-ii/

class Solution {
    fun climbStairs(n: Int, costs: IntArray): Int {
        val inf = 1e9.toInt()
        val f = IntArray(n + 1) { inf }
        f[0] = 0
        for (i in 1..n) {
            val x = costs[i - 1]
            for (j in maxOf(0, i - 3) until i) {
                f[i] = minOf(f[i], f[j] + x + (i - j) * (i - j))
            }
        }
        return f[n]
    }
}
