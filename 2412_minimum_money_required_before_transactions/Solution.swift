// LeetCode 2412 - Minimum Money Required Before Transactions
// https://leetcode.com/problems/minimum-money-required-before-transactions/

class Solution {
    func minimumMoney(_ transactions: [[Int]]) -> Int {
        var totalLoss = 0, maxCashback = 0, maxCost = 0
        for t in transactions {
            let cost = t[0], cashback = t[1]
            if cost > cashback {
                totalLoss += cost - cashback
                maxCashback = max(maxCashback, cashback)
            } else {
                maxCost = max(maxCost, cost)
            }
        }
        return max(totalLoss + maxCashback, totalLoss + maxCost)
    }
}
