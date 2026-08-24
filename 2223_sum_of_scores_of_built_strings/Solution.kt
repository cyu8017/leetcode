// LeetCode 2223 - Sum of Scores of Built Strings
// https://leetcode.com/problems/sum-of-scores-of-built-strings/

class Solution {

    fun sumScores(s: String): Long {

            var n = s.length
            var z = IntArray(n)
            var l = 0; var r = 0
            for (i in 1 until n) {
                if (i <= r) z[i] = minOf(r - i + 1, z[i - l])
                while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++
                if (i + z[i] - 1 > r) {
                    l = i
                    r = i + z[i] - 1
                }
            }
            var ans = n
            for (i in 1 until n) { ans += z[i] }
            return ans

    }

}
