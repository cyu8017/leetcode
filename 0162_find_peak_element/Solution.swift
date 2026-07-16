// LeetCode 0162 - Find Peak Element
// https://leetcode.com/problems/find-peak-element/

class Solution {
    func findPeakElement(_ nums: [Int]) -> Int {
        var left = 0, right = nums.count - 1
        while left < right {
            let mid = left + (right - left) / 2
            if nums[mid] > nums[mid + 1] { right = mid } else { left = mid + 1 }
        }
        return left
    }
}