// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

class Solution {
    fun isMajorityElement(nums: IntArray, target: Int): Boolean {
        fun lowerBound(): Int {
            var lo = 0
            var hi = nums.size
            while (lo < hi) {
                val mid = (lo + hi) / 2
                if (nums[mid] < target) lo = mid + 1 else hi = mid
            }
            return lo
        }
        fun upperBound(): Int {
            var lo = 0
            var hi = nums.size
            while (lo < hi) {
                val mid = (lo + hi) / 2
                if (nums[mid] <= target) lo = mid + 1 else hi = mid
            }
            return lo
        }
        return upperBound() - lowerBound() > nums.size / 2
    }
}
