// LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

class Solution {
    func maxProfit(_ prices: [Int], _ profits: [Int]) -> Int {
        let n = prices.count
        var ans = -1
        for j in 0..<n {
            var bestL = -1, bestR = -1
            for i in 0..<j where prices[i] < prices[j] {
                bestL = max(bestL, profits[i])
            }
            for k in (j + 1)..<n where prices[k] > prices[j] {
                bestR = max(bestR, profits[k])
            }
            if bestL >= 0 && bestR >= 0 {
                ans = max(ans, bestL + profits[j] + bestR)
            }
        }
        return ans
    }
}
