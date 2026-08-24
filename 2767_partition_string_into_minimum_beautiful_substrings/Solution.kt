// LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

class Solution {
    fun minimumBeautifulSubstrings(s: String): Int {
        var n = s.length
        var pow5 = HashSet<String>()
        var x = 1
        while () {
            var b = Long.toBinaryString(x)
            if (b.length > n) break
            pow5.add(b)
            x *= 5
        }
        val INF = 1  shl  30
        var dp = IntArray(n + 1)
        dp.fill(INF)
        dp[0] = 0
        for (i in 0 until n) {
            if (dp[i] == INF || s[i] == '0') continue
            for (j in i + 1 ..n) {
                if (pow5.contains(s.substring(i, j)))
                    dp[j] = minOf(dp[j], dp[i] + 1)
            }
        }
        return dp[n] ==if (INF) -1 else dp[n]
    }
}
