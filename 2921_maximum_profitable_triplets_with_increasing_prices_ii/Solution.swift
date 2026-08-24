// LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

class Solution {
    private var bit: [Int] = []

    func maxProfit(_ prices: [Int], _ profits: [Int]) -> Int {
        let n = prices.count
        var ans = -1
        var maxLeft = Array(repeating: 0, count: n)
        bit = Array(repeating: 0, count: 5002)
        for j in 0..<n {
            maxLeft[j] = query(prices[j] - 1)
            update(prices[j], profits[j])
        }
        for j in 0..<n {
            var bestR = -1
            for k in (j + 1)..<n where prices[k] > prices[j] {
                bestR = max(bestR, profits[k])
            }
            if maxLeft[j] >= 0 && bestR >= 0 {
                ans = max(ans, maxLeft[j] + profits[j] + bestR)
            }
        }
        return ans
    }

    private func update(_ i0: Int, _ val: Int) {
        var i = i0
        while i < bit.count {
            bit[i] = max(bit[i], val)
            i += i & -i
        }
    }

    private func query(_ i0: Int) -> Int {
        var i = i0, best = -1
        while i > 0 {
            best = max(best, bit[i])
            i -= i & -i
        }
        return best
    }
}
