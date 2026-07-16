// LeetCode 0123 - Best Time to Buy and Sell Stock III
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var buyOne = Int.max
        var buyTwo = Int.max
        var sellOne = 0
        var sellTwo = 0
        for price in prices {
            buyOne = min(buyOne, price)
            sellOne = max(sellOne, price - buyOne)
            buyTwo = min(buyTwo, price - sellOne)
            sellTwo = max(sellTwo, price - buyTwo)
        }
        return sellTwo
    }
}