// LeetCode 2706 - Buy Two Chocolates
// https://leetcode.com/problems/buy-two-chocolates/

class Solution {
    func buyChoco(_ prices: [Int], _ money: Int) -> Int {
        let prices = prices.sorted()
        let cost = prices[0] + prices[1]
        return cost <= money ? money - cost : money
    }
}
