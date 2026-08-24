// LeetCode 2189 - Number of Ways to Build House of Cards
// https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/

class Solution {
    fun houseOfCards(n: Int): Int {
        var dp: IntArray = IntArray(n + 1)
        dp[0] = 1
        var k = 1
        while (3 * k - 1 <= n) {
            var cost: Int = 3 * k - 1
            for (j in n downTo cost) dp[j] += dp[j - cost]
            k++
        }
        return dp[n]
    }
}
