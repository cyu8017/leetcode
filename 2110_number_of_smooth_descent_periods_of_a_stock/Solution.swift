// LeetCode 2110 - Number of Smooth Descent Periods of a Stock
// https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution {
    func getDescentPeriods(_ prices: [Int]) -> Int {
        var ans = 1, cur = 1
        for i in 1..<prices.count {
            if prices[i] == prices[i - 1] - 1 { cur += 1 }
            else { cur = 1 }
            ans += cur
        }
        return ans
    }
}
