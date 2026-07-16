// LeetCode 0396 - Rotate Function
// https://leetcode.com/problems/rotate-function/

class Solution {
    func maxRotateFunction(_ nums: [Int]) -> Int {
        let total = nums.reduce(0, +)
        var current = 0
        for (index, value) in nums.enumerated() {
            current += index * value
        }
        var best = current

        if nums.count > 1 {
            for index in stride(from: nums.count - 1, through: 1, by: -1) {
                current += total - nums.count * nums[index]
                best = max(best, current)
            }
        }

        return best
    }
}
