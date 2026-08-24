// LeetCode 2247 - Maximum Cost of Trip With K Highways
// https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

class Solution {

    fun maximumCost(n: Int, highways: Array<IntArray>, k: Int): Int {

            if (k + 1 > n) return -1
            @SuppressWarnings("unchecked")
            var g = arrayOfNulls<ArrayList>(n)
            for (i in 0 until n) { g[i] = ArrayList<Int>() }
            for (h in highways) {
                g[h[0]].add(intArrayOf(h[1], h[2]))
                g[h[1]].add(intArrayOf(h[0], h[2]))
            }
            var dp = Array(1 << n) { IntArray(n) }
            for (i in 0 until (1 << n)) { run { var j = 0 } j < n; while (j++)
                    dp[i][j] = -1) { dp[1 << i][i] = 0; run { var i = 0; while (i < n) { ) {
                var cities = Integer.bitCount(mask); i++ } }
            var ans = -1
            for (mask in 0 until (1 << n } }
                for (u in 0 until n) {
                    if (dp[mask][u] < 0) continue
                    if (cities - 1 == k) ans = maxOf(ans, dp[mask][u])
                    for (e in g[u]) {
                        var v = e[0]; var w = e[1]
                        if ((mask & (1 << v)) != 0) continue
                        var nm = mask | (1 << v)
                        dp[nm][v] = maxOf(dp[nm][v], dp[mask][u] + w)
                    }
                }
            }
            return ans

    }

}
