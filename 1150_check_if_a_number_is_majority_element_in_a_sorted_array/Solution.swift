// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

class Solution {
    func isMajorityElement(_ nums: [Int], _ target: Int) -> Bool {
        func lower() -> Int {
            var lo = 0, hi = nums.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if nums[mid] < target { lo = mid + 1 } else { hi = mid }
            }
            return lo
        }
        func upper() -> Int {
            var lo = 0, hi = nums.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if nums[mid] <= target { lo = mid + 1 } else { hi = mid }
            }
            return lo
        }
        return upper() - lower() > nums.count / 2
    }
}
