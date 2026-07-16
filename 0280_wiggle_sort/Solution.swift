// LeetCode 0280 - Wiggle Sort
// https://leetcode.com/problems/wiggle-sort/

class Solution {
    func wiggleSort(_ nums: inout [Int]) {
        for index in 1..<nums.count {
            if index % 2 == 1 && nums[index] < nums[index - 1] {
                nums.swapAt(index, index - 1)
            } else if index % 2 == 0 && nums[index] > nums[index - 1] {
                nums.swapAt(index, index - 1)
            }
        }
    }
}
