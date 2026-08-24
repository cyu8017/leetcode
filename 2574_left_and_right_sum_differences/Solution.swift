// LeetCode 2574 - Left and Right Sum Differences
// https://leetcode.com/problems/left-and-right-sum-differences/

class Solution {
    func leftRightDifference(_ nums: [Int]) -> [Int] {
        let total = nums.reduce(0, +)
        var ans = [Int](repeating: 0, count: nums.count)
        var left = 0
        for i in 0..<nums.count {
            let right = total - left - nums[i]
            ans[i] = abs(left - right)
            left += nums[i]
        }
        return ans
    }
}
