// LeetCode 0081 - Search in Rotated Sorted Array II
// https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution {
    func search(_ nums: [Int], _ target: Int) -> Bool {
        var left = 0
        var right = nums.count - 1

        while left <= right {
            let mid = (left + right) / 2
            if nums[mid] == target {
                return true
            }

            if nums[left] == nums[mid] && nums[mid] == nums[right] {
                left += 1
                right -= 1
            } else if nums[left] <= nums[mid] {
                if nums[left] <= target && target < nums[mid] {
                    right = mid - 1
                } else {
                    left = mid + 1
                }
            } else {
                if nums[mid] < target && target <= nums[right] {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
        }

        return false
    }
}
