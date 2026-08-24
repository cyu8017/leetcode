// LeetCode 3253 - Construct String with Minimum Cost (Easy)
// https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

class Solution {
    fun minimumCost(target: String, words: Array<String>, costs: IntArray): Int {
        val inf = 1e18
        var n = target.length
        var dp = LongArray(n + 1)
        for (i in 0 ..n) { dp[i] = inf }
        dp[0] = 0
        var best = HashMap<String, Int>()
        for (i in 0 until words.size) {
            var old = best[words[i]]
            if (old == null || costs[i] < old) best[words[i]] = costs[i]
        }
        for (i in 0 until n) {
            if (dp[i] == inf) continue
            for (Map.Entry<String, Integer> e : best.entrySet()) {
                var w = e.getKey()
                var c = e.getValue()
                var L = w.length
                if (i + L <= n && target.startsWith(w, i) && dp[i] + c < dp[i + L]) {
                    dp[i + L] = dp[i] + c
                }
            }
        }
        if (dp[n] == inf) return -1
        return dp[n]
    }
}
