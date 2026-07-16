// LeetCode 0080 - Remove Duplicates from Sorted Array II
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        if nums.count <= 2 {
            return nums.count
        }

        var write = 2
        for i in 2..<nums.count {
            if nums[i] != nums[write - 2] {
                nums[write] = nums[i]
                write += 1
            }
        }

        return write
    }
}
