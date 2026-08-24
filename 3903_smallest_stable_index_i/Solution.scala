// LeetCode 3903 - Smallest Stable Index I
// https://leetcode.com/problems/smallest-stable-index-i/

object Solution {
  def firstStableIndex(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val right = new Array[Int](n)
    right(n - 1) = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      right(i) = math.min(right(i + 1), nums(i))
      i -= 1
    }
    var left = 0
    i = 0
    while (i < n) {
      left = math.max(left, nums(i))
      if (left - right(i) <= k) return i
      i += 1
    }
    -1
  }
}
