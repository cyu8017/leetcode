// LeetCode 2266 - Count Number of Texts
// https://leetcode.com/problems/count-number-of-texts/

class Solution {

    fun countTexts(pressedKeys: String): Int {

            var mod = 1000000007
            var n = pressedKeys.length
            var dp = IntArray(n + 1)
            dp[0] = 1
            for (i in 1..n) {
                dp[i] = dp[i - 1]
                var maxPress = if ((pressedKeys[i - 1] == '7' || pressedKeys[i - 1] == '9')) 4 else 3
                run {
    var j = 2
    while (j <= maxPress && j <= i) {

                    if (pressedKeys[i - j] != pressedKeys[i - 1]) break
                    dp[i] = (dp[i] + dp[i - j]) % mod

    j++
    }
    }
            }
            return dp[n]

    }

}
