// LeetCode 0154 - Find Minimum in Rotated Sorted Array II
// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var left = 0
        var right = nums.count - 1
        while left < right {
            let middle = (left + right) / 2
            if nums[middle] > nums[right] {
                left = middle + 1
            } else if nums[middle] < nums[right] {
                right = middle
            } else {
                right -= 1
            }
        }
        return nums[left]
    }
}