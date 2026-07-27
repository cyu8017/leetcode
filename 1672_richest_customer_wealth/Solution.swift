// LeetCode 1672 - Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/

class Solution {
    func maximumWealth(_ accounts: [[Int]]) -> Int {
        var best = 0
        for row in accounts {
            best = max(best, row.reduce(0, +))
        }
        return best
    }
}
