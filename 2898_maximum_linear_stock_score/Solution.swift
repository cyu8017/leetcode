// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

class Solution {
    func maxScore(_ prices: [Int]) -> Int {
        var best: [Int: Int] = [:]
        var ans = 0
        for i in 0..<prices.count {
            let key = prices[i] - (i + 1)
            let cand = best[key, default: 0] + prices[i]
            if cand > best[key, default: 0] { best[key] = cand }
            ans = max(ans, best[key]!)
        }
        return ans
    }
}
