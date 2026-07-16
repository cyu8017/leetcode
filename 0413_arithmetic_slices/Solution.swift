// LeetCode 0413 - Arithmetic Slices
// https://leetcode.com/problems/arithmetic-slices/

class Solution {
    func numberOfArithmeticSlices(_ nums: [Int]) -> Int {
        if nums.count < 3 {
            return 0
        }

        var total = 0
        var current = 0
        for index in 2..<nums.count {
            if nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2] {
                current += 1
                total += current
            } else {
                current = 0
            }
        }
        return total
    }
}
