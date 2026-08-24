// LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

object Solution {
  def maximumLength(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val f = Array.ofDim[Int](n, k + 1)
    var ans = 0
    var i = 0
    while (i < n) {
      var h = 0
      while (h <= k) {
        var j = 0
        while (j < i) {
          if (nums(i) == nums(j)) f(i)(h) = math.max(f(i)(h), f(j)(h))
          else if (h > 0) f(i)(h) = math.max(f(i)(h), f(j)(h - 1))
          j += 1
        }
        f(i)(h) += 1
        h += 1
      }
      ans = math.max(ans, f(i)(k))
      i += 1
    }
    ans
  }
}
