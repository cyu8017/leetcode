// LeetCode 3995 - Minimum Cost to Convert String III
// https://leetcode.com/problems/minimum-cost-to-convert-string-iii/

class Solution {
    fun minCost(source: String, target: String, rules: Array<Array<String>>, costs: IntArray): Int {
        val n = source.length
        if (target.length != n) return -1
        val dp = IntArray(n + 1) { Int.MAX_VALUE }
        dp[0] = 0
        for (i in 0 until n) {
            if (dp[i] == Int.MAX_VALUE) continue
            if (source[i] == target[i] && dp[i] < dp[i + 1]) dp[i + 1] = dp[i]
            for (j in rules.indices) {
                val p = rules[j][0]
                val r = rules[j][1]
                val plen = p.length
                if (i + plen > n) continue
                var c = costs[j]
                var ok = true
                for (ki in 0 until plen) {
                    if (r[ki] != target[i + ki]) { ok = false; break }
                    if (p[ki] == '*') c++
                    else if (p[ki] != source[i + ki]) { ok = false; break }
                }
                if (ok && dp[i] <= Int.MAX_VALUE - c && dp[i] + c < dp[i + plen]) {
                    dp[i + plen] = dp[i] + c
                }
            }
        }
        return if (dp[n] == Int.MAX_VALUE) -1 else dp[n]
    }
}
