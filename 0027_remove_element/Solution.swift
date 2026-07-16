// LeetCode 0027 - Remove Element
// https://leetcode.com/problems/remove-element/

class Solution {
    func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
        var write = 0
        for read in nums.indices {
            if nums[read] != val {
                nums[write] = nums[read]
                write += 1
            }
        }
        return write
    }
}
