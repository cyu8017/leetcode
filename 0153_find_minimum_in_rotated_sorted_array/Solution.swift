// LeetCode 0153 - Find Minimum in Rotated Sorted Array
// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var left = 0
        var right = nums.count - 1
        while left < right {
            let middle = (left + right) / 2
            if nums[middle] > nums[right] {
                left = middle + 1
            } else {
                right = middle
            }
        }
        return nums[left]
    }
}