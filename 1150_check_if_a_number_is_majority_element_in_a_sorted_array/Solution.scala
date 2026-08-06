// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

object Solution {
  def isMajorityElement(nums: Array[Int], target: Int): Boolean = {
    def lowerBound(x: Int): Int = {
      var lo = 0
      var hi = nums.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (nums(mid) < x) lo = mid + 1 else hi = mid
      }
      lo
    }
    def upperBound(x: Int): Int = {
      var lo = 0
      var hi = nums.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (nums(mid) <= x) lo = mid + 1 else hi = mid
      }
      lo
    }
    upperBound(target) - lowerBound(target) > nums.length / 2
  }
}
