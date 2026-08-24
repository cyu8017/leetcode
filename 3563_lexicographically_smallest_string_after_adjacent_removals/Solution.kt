// LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

class Solution {
    fun lexicographicallySmallestString(s: String): String {
        var n = s.length
        String[][] dp = arrayOfNulls<String>(n + 1)[n + 1]
        var i: Int = 0
while (i <= n) {

            for (j in 0..n) { dp[i][j] = "" }
        for (length in 1..n) {
            var i = 0
            while (i + length <= n) {
                var j = i + length
                var minStr = s[i] + dp[i + 1][j]
                for (k in i + 1 until j) {
                    if (isConsec(s[i], s[k]) && dp[i + 1][k].isEmpty()) {
                        var cand = dp[k + 1][j]
                        if (cand.compareTo(minStr) < 0) minStr = cand
                    }
                }
                dp[i][j] = minStr
                i = i + 1
            }
        }
        return dp[0][n]
    }

    fun isConsec(a: Char, b: Char): Boolean {
        var d = kotlin.math.abs(a - b)
        return d == 1 || d == 25
    }
}
i = i + 1
}
