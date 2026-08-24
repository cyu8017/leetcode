// LeetCode 3575 - Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/

class Solution {
    companion object { const val MOD = 1_000_000_007 }
    lateinit var g: Array<ArrayList<Int>>
    lateinit var vals: IntArray
    var ans = 0

    fun digitMask(x0: Int): IntArray {
        var x = x0
        val v = x
        var mask = 0
        if (x == 0) return intArrayOf(1, 1, 0)
        while (x > 0) {
            val d = x % 10
            if ((mask and (1 shl d)) != 0) return intArrayOf(0, 0, 0)
            mask = mask or (1 shl d)
            x /= 10
        }
        return intArrayOf(mask, 1, v)
    }

    fun dfs(u: Int): HashMap<Int, Int> {
        var dp = HashMap<Int, Int>()
        dp[0] = 0
        val dm = digitMask(vals[u])
        if (dm[1] == 1) dp[dm[0]] = dm[2]
        for (c in g[u]) {
            val child = dfs(c)
            val ndp = HashMap<Int, Int>()
            for ((k1, v1) in dp) {
                for ((k2, v2) in child) {
                    if ((k1 and k2) == 0) {
                        val nm = k1 or k2
                        ndp[nm] = maxOf(ndp.getOrDefault(nm, 0), v1 + v2)
                    }
                }
            }
            for ((k, v) in dp) ndp[k] = maxOf(ndp.getOrDefault(k, 0), v)
            for ((k, v) in child) ndp[k] = maxOf(ndp.getOrDefault(k, 0), v)
            dp = ndp
        }
        var best = 0
        for (s in dp.values) best = maxOf(best, s)
        ans = (ans + best) % MOD
        return dp
    }

    fun goodSubtreeSum(vals: IntArray, par: IntArray): Int {
        val n = vals.size
        this.vals = vals
        g = Array(n) { ArrayList() }
        for (i in 1 until n) g[par[i]].add(i)
        ans = 0
        dfs(0)
        return ans
    }
}
