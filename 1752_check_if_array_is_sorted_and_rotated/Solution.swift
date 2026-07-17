// LeetCode 1752 - Check if Array Is Sorted and Rotated
// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution {
    func check(_ nums: [Int]) -> Bool {
        let n = nums.count
        var drops = 0
        for i in 0..<n where nums[i] > nums[(i + 1) % n] {
            drops += 1
        }
        return drops <= 1
    }
}
