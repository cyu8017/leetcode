// LeetCode 3550 - Smallest Index With Digit Sum Equal to Index
// https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

object Solution {
  def smallestIndex(nums: Array[Int]): Int = {
    var i = 0
    while (i < nums.length) {
      var x = nums(i)
      var s = 0
      while (x > 0) { s += x % 10; x /= 10 }
      if (s == i) return i
      i += 1
    }
    -1
  }
}
