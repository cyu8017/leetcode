// LeetCode 1475 - Final Prices With a Special Discount in a Shop
// https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution {
    func finalPrices(_ prices: [Int]) -> [Int] {
        var ans = prices, stack = [Int]()
        for (i, price) in prices.enumerated() {
            while let last = stack.last, prices[last] >= price {
                ans[stack.removeLast()] -= price
            }
            stack.append(i)
        }
        return ans
    }
}
