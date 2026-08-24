// LeetCode 2412 - Minimum Money Required Before Transactions
// https://leetcode.com/problems/minimum-money-required-before-transactions/

class Solution {
    fun minimumMoney(transactions: Array<IntArray>): Long {
        var totalLoss = 0L
        var maxCashback = 0L
        var maxCost = 0L
        for (t in transactions) {
            val cost = t[0].toLong()
            val cashback = t[1].toLong()
            if (cost > cashback) {
                totalLoss += cost - cashback
                maxCashback = maxOf(maxCashback, cashback)
            } else {
                maxCost = maxOf(maxCost, cost)
            }
        }
        return maxOf(totalLoss + maxCashback, totalLoss + maxCost)
    }
}
