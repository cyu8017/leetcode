// LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

object Solution {
  def findMaxK(nums: Array[Int]): Int = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var ans = -1
    var i = 0
    while (i < nums.length) {
      val x = nums(i)
      seen += x
      if (x > 0 && seen.contains(-x) && x > ans) ans = x
      if (x < 0 && seen.contains(-x) && -x > ans) ans = -x
      i += 1
    }
    ans
  }
}
