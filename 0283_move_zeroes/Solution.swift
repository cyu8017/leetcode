// LeetCode 0283 - Move Zeroes
// https://leetcode.com/problems/move-zeroes/

class Solution {
    func moveZeroes(_ nums: inout [Int]) {
        var insert = 0
        for num in nums {
            if num != 0 {
                nums[insert] = num
                insert += 1
            }
        }
        for index in insert..<nums.count {
            nums[index] = 0
        }
    }
}
