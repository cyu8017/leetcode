// LeetCode 3862 - Find The Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/

object Solution {
  def smallestBalancedIndex(nums: Array[Int]): Int = {
    var s = 0L
    var p = 1L
    nums.foreach { x => s += x }
    var i = nums.length - 1
    while (i >= 0) {
      s -= nums(i)
      if (s == p) return i
      p *= nums(i)
      if (p >= s) return -1
      i -= 1
    }
    -1
  }
}
