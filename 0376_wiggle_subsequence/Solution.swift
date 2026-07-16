// LeetCode 0376 - Wiggle Subsequence
// https://leetcode.com/problems/wiggle-subsequence/

class Solution {
    func wiggleMaxLength(_ nums: [Int]) -> Int {
        if nums.count < 2 {
            return nums.count
        }

        var up = 1
        var down = 1
        for index in 1..<nums.count {
            if nums[index] > nums[index - 1] {
                up = down + 1
            } else if nums[index] < nums[index - 1] {
                down = up + 1
            }
        }

        return max(up, down)
    }
}
