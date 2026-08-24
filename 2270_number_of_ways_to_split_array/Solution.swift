// LeetCode 2270 - Number of Ways to Split Array
// https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution {
    func waysToSplitArray(_ nums: [Int]) -> Int {
        let total = nums.reduce(0, +)
        var left = 0, ans = 0
        for i in 0..<(nums.count - 1) {
            left += nums[i]
            if left >= total - left { ans += 1 }
        }
        return ans
    }
}
