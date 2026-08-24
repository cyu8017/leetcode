// LeetCode 3976 - Maximum Subarray Sum After Multiplier
// https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/


class Solution {
    func maxSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let inf = Int.min / 4
        var f = Array(repeating: Array(repeating: inf, count: 4), count: n + 1)
        f[0][0] = 0
        var ans = inf
        for i in 1...n {
            let x = nums[i - 1]
            f[i][0] = max(f[i - 1][0], 0) + x
            f[i][1] = max(max(f[i - 1][0], f[i - 1][1]), 0) + x * k
            f[i][2] = max(max(f[i - 1][0], f[i - 1][2]), 0) + x / k
            f[i][3] = max(max(f[i - 1][1], f[i - 1][2]), f[i - 1][3]) + x
            ans = max(ans, max(max(f[i][0], f[i][1]), max(f[i][2], f[i][3])))
        }
        return ans
    }
}
