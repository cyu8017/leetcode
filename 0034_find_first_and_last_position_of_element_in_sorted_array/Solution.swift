// LeetCode 0034 - Find First and Last Position of Element in Sorted Array
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution {
    func searchRange(_ nums: [Int], _ target: Int) -> [Int] {
        if nums.isEmpty {
            return [-1, -1]
        }

        let start = lowerBound(nums, target)
        if start == nums.count || nums[start] != target {
            return [-1, -1]
        }

        return [start, upperBound(nums, target) - 1]
    }

    private func lowerBound(_ nums: [Int], _ target: Int) -> Int {
        var left = 0
        var right = nums.count

        while left < right {
            let mid = (left + right) / 2
            if nums[mid] < target {
                left = mid + 1
            } else {
                right = mid
            }
        }

        return left
    }

    private func upperBound(_ nums: [Int], _ target: Int) -> Int {
        var left = 0
        var right = nums.count

        while left < right {
            let mid = (left + right) / 2
            if nums[mid] <= target {
                left = mid + 1
            } else {
                right = mid
            }
        }

        return left
    }
}
