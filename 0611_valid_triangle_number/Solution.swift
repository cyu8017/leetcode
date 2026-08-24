// LeetCode 0611 - Valid Triangle Number
// https://leetcode.com/problems/valid-triangle-number/

class Solution {
    func triangleNumber(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        let n = nums.count
        var count = 0
        for k in stride(from: n - 1, through: 2, by: -1) {
            var left = 0
            var right = k - 1
            while left < right {
                if nums[left] + nums[right] > nums[k] {
                    count += right - left
                    right -= 1
                } else {
                    left += 1
                }
            }
        }
        return count
    }
}
