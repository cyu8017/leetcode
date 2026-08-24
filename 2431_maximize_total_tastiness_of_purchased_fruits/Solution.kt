// LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
// https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

class Solution {
    fun maxTastiness(price: IntArray, tastiness: IntArray, maxAmount: Int, maxCoupons: Int): Int {
        val n = price.size
        val dp = Array(maxAmount + 1) { IntArray(maxCoupons + 1) { Int.MIN_VALUE / 2 } }
        dp[0][0] = 0
        for (i in 0 until n) {
            val p = price[i]
            val t = tastiness[i]
            for (a in maxAmount downTo 0) {
                for (c in maxCoupons downTo 0) {
                    if (dp[a][c] < 0) continue
                    if (a + p <= maxAmount) dp[a + p][c] = maxOf(dp[a + p][c], dp[a][c] + t)
                    if (c + 1 <= maxCoupons && a + p / 2 <= maxAmount) {
                        dp[a + p / 2][c + 1] = maxOf(dp[a + p / 2][c + 1], dp[a][c] + t)
                    }
                }
            }
        }
        var ans = 0
        for (a in 0..maxAmount) for (c in 0..maxCoupons) ans = maxOf(ans, dp[a][c])
        return ans
    }
}
