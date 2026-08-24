// LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

class Solution {
    func minArraySum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = (prefix[i] + nums[i]) % k }
        let inf = Int.max / 4
        var dp = Array(repeating: 0, count: n + 1)
        var best = Array(repeating: inf, count: k)
        best[0] = 0
        for i in 1...n {
            dp[i] = dp[i - 1] + nums[i - 1]
            if best[prefix[i]] < dp[i] { dp[i] = best[prefix[i]] }
            if dp[i] < best[prefix[i]] { best[prefix[i]] = dp[i] }
        }
        return dp[n]
    }
}
