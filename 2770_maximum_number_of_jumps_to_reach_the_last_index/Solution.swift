// LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

class Solution {
    func maximumJumps(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        var dp = Array(repeating: -1, count: n)
        dp[0] = 0
        for i in 0..<n where dp[i] >= 0 {
            for j in (i + 1)..<n where abs(nums[j] - nums[i]) <= target {
                dp[j] = max(dp[j], dp[i] + 1)
            }
        }
        return dp[n - 1]
    }
}
