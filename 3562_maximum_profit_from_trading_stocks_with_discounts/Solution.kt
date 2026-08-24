// LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
// https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

class Solution {
    lateinit var g: Array<ArrayList<Int>>
    lateinit var present: IntArray
    lateinit var future: IntArray
    var budget = 0

    fun dfs(u: Int): Array<IntArray> {
        val nxt = Array(budget + 1) { IntArray(2) }
        for (v in g[u]) {
            val fv = dfs(v)
            for (j in budget downTo 0) {
                for (jv in 0..j) {
                    for (pre in 0 until 2) {
                        nxt[j][pre] = maxOf(nxt[j][pre], nxt[j - jv][pre] + fv[jv][pre])
                    }
                }
            }
        }
        val f = Array(budget + 1) { IntArray(2) }
        val price = future[u - 1]
        for (j in 0..budget) {
            for (pre in 0 until 2) {
                val cost = present[u - 1] / (pre + 1)
                if (j >= cost) {
                    val buyProfit = nxt[j - cost][1] + (price - cost)
                    f[j][pre] = maxOf(nxt[j][0], buyProfit)
                } else {
                    f[j][pre] = nxt[j][0]
                }
            }
        }
        return f
    }

    fun maxProfit(n: Int, present: IntArray, future: IntArray, hierarchy: Array<IntArray>, budget: Int): Int {
        this.present = present
        this.future = future
        this.budget = budget
        g = Array(n + 1) { ArrayList() }
        for (e in hierarchy) g[e[0]].add(e[1])
        return dfs(1)[budget][0]
    }
}
