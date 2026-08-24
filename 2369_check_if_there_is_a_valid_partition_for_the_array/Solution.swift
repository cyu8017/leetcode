// LeetCode 2369 - Check if There is a Valid Partition For The Array
// https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

class Solution {
    func validPartition(_ nums: [Int]) -> Bool {
        let n = nums.count
        var dp = [Bool](repeating: false, count: n + 1)
        dp[0] = true
        for i in 1...n {
            if i >= 2 && nums[i - 1] == nums[i - 2] && dp[i - 2] { dp[i] = true }
            if i >= 3 && nums[i - 1] == nums[i - 2] && nums[i - 2] == nums[i - 3] && dp[i - 3] { dp[i] = true }
            if i >= 3 && nums[i - 1] == nums[i - 2] + 1 && nums[i - 2] == nums[i - 3] + 1 && dp[i - 3] { dp[i] = true }
        }
        return dp[n]
    }
}
