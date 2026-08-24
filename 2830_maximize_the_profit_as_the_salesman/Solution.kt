// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

class Solution {
    fun maximizeTheProfit(n: Int, offers: MutableList<MutableList<Int>>): Int {
        val byEnd = Array(n) { ArrayList<MutableList<Int>>() }
        for (o in offers) byEnd[o[1]].add(o)
        val dp = IntArray(n + 1)
        for (end in 0 until n) {
            dp[end + 1] = dp[end]
            for (o in byEnd[end]) {
                dp[end + 1] = maxOf(dp[end + 1], dp[o[0]] + o[2])
            }
        }
        return dp[n]
    }
}
