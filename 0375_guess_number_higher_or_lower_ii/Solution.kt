// LeetCode 0375 - Guess Number Higher or Lower II

// https://leetcode.com/problems/guess-number-higher-or-lower-ii/



class Solution {

    fun getMoneyAmount(n: Int): Int {

        val dp = Array(n + 2) { IntArray(n + 2) }



        for (length in 2..n) {

            for (left in 1..n - length + 1) {

                val right = left + length - 1

                dp[left][right] = Int.MAX_VALUE

                for (guess in left until right) {

                    val cost = guess + maxOf(dp[left][guess - 1], dp[guess + 1][right])

                    dp[left][right] = minOf(dp[left][right], cost)

                }

            }

        }



        return dp[1][n]

    }

}
