// LeetCode 2931 - Maximum Spending After Buying Items
// https://leetcode.com/problems/maximum-spending-after-buying-items/

class Solution {
    fun maxSpending(values: Array<IntArray>): Long {
        val m = values.size
        val n = values[0].size
        val idx = IntArray(m) { n - 1 }
        var ans = 0L
        var day = 1L
        val total = m * n
        repeat(total) {
            var bestI = -1
            var bestV = 1L shl 60
            for (i in 0 until m) {
                if (idx[i] >= 0 && values[i][idx[i]] < bestV) {
                    bestV = values[i][idx[i]].toLong()
                    bestI = i
                }
            }
            ans += bestV * day
            idx[bestI]--
            day++
        }
        return ans
    }
}
