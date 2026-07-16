// LeetCode 0324 - Wiggle Sort II
// https://leetcode.com/problems/wiggle-sort-ii/

class Solution {
    func wiggleSort(_ nums: inout [Int]) {
        let sortedNums = nums.sorted()
        var left = (nums.count - 1) / 2
        var right = nums.count - 1
        for index in 0..<nums.count {
            if index % 2 == 0 {
                nums[index] = sortedNums[left]
                left -= 1
            } else {
                nums[index] = sortedNums[right]
                right -= 1
            }
        }
    }
}
