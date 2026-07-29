// LeetCode 1027 - Longest Arithmetic Subsequence
// https://leetcode.com/problems/longest-arithmetic-subsequence/

class Solution {
    func longestArithSeqLength(_ nums: [Int]) -> Int {
        var dp = Array(repeating: [Int: Int](), count: nums.count)
        var ans = 1
        for j in 1..<nums.count {
            for i in 0..<j {
                let d = nums[j] - nums[i]
                let len = (dp[i][d] ?? 1) + 1
                dp[j][d] = len
                ans = max(ans, len)
            }
        }
        return ans
    }
}
