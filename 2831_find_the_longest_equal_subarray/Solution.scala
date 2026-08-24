// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

object Solution {
  def longestEqualSubarray(nums: List[Int], k: Int): Int = {
    val pos = scala.collection.mutable.LinkedHashMap.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    var i = 0
    while (i < nums.length) {
      pos.getOrElseUpdate(nums(i), scala.collection.mutable.ArrayBuffer.empty[Int]) += i
      i += 1
    }
    var ans = 0
    pos.values.foreach { p =>
      var left = 0
      var right = 0
      while (right < p.length) {
        while (p(right) - p(left) - (right - left) > k) left += 1
        ans = math.max(ans, right - left + 1)
        right += 1
      }
    }
    ans
  }
}
