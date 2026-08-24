// LeetCode 2547 - Minimum Cost to Split an Array
// https://leetcode.com/problems/minimum-cost-to-split-an-array/

class Solution {
    func minCost(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let INF = Int.max / 4
        var dp = [Int](repeating: INF, count: n + 1)
        dp[0] = 0
        for i in 0..<n {
            var freq = [Int: Int]()
            var trimmed = 0
            for j in i..<n {
                let c = freq[nums[j], default: 0] + 1
                freq[nums[j]] = c
                if c == 2 { trimmed += 2 }
                else if c > 2 { trimmed += 1 }
                dp[j + 1] = min(dp[j + 1], dp[i] + k + trimmed)
            }
        }
        return dp[n]
    }
}
