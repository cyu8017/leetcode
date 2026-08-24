// LeetCode 3940 - Limit Occurrences in Sorted Array
// https://leetcode.com/problems/limit-occurrences-in-sorted-array/

object Solution {
  def limitOccurrences(nums: Array[Int], k: Int): Array[Int] = {
    val n = nums.length
    var cnt = 1
    var l = 1
    var r = 1
    while (r < n) {
      if (nums(r) != nums(r - 1)) cnt = 1
      else cnt += 1
      if (cnt <= k) {
        nums(l) = nums(r)
        l += 1
      }
      r += 1
    }
    nums.take(l)
  }
}
