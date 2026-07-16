// LeetCode 0309 - Best Time to Buy and Sell Stock with Cooldown
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        if prices.isEmpty {
            return 0
        }
        var free = 0
        var hold = -prices[0]
        var cooldown = 0
        for index in 1..<prices.count {
            let price = prices[index]
            let nextFree = max(free, cooldown)
            let nextHold = max(hold, free - price)
            let nextCooldown = hold + price
            free = nextFree
            hold = nextHold
            cooldown = nextCooldown
        }
        return max(free, cooldown)
    }
}
