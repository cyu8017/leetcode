// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

class Solution {
    fun minArraySum(nums: IntArray, k: Int, op1: Int, op2: Int): Int {
        val inf = 1e18.toLong()
        var dp = Array(op1 + 1) { LongArray(op2 + 1) { inf } }
        dp[0][0] = 0L
        for (x in nums) {
            val ndp = Array(op1 + 1) { LongArray(op2 + 1) { inf } }
            for (a in 0..op1) {
                for (b in 0..op2) {
                    if (dp[a][b] == inf) continue
                    tryCand(ndp, dp[a][b], a, b, x)
                    if (a < op1) tryCand(ndp, dp[a][b], a + 1, b, (x + 1) / 2)
                    if (b < op2 && x >= k) tryCand(ndp, dp[a][b], a, b + 1, x - k)
                    if (a < op1 && b < op2) {
                        val v1 = (x + 1) / 2
                        if (v1 >= k) tryCand(ndp, dp[a][b], a + 1, b + 1, v1 - k)
                        if (x >= k) tryCand(ndp, dp[a][b], a + 1, b + 1, (x - k + 1) / 2)
                    }
                }
            }
            dp = ndp
        }
        var ans = inf
        for (a in 0..op1) {
            for (b in 0..op2) {
                if (dp[a][b] < ans) ans = dp[a][b]
            }
        }
        return ans.toInt()
    }

    private fun tryCand(ndp: Array<LongArray>, base: Long, na: Int, nb: Int, v: Int) {
        if (base + v < ndp[na][nb]) ndp[na][nb] = base + v
    }
}
