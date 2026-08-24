// LeetCode 2361 - Minimum Costs Using the Train Line
// https://leetcode.com/problems/minimum-costs-using-the-train-line/

class Solution {
    fun minimumCosts(regular: IntArray, express: IntArray, expressCost: Int): LongArray {
        val n = regular.size
        val ans = LongArray(n)
        var reg = 0L
        var exp = expressCost.toLong()
        for (i in 0 until n) {
            val nextReg = minOf(reg + regular[i], exp + express[i])
            val nextExp = minOf(reg + regular[i] + expressCost, exp + express[i])
            reg = nextReg
            exp = nextExp
            ans[i] = minOf(reg, exp)
        }
        return ans
    }
}
