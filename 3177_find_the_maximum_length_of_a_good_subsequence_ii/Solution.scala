// LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

object Solution {
  def maximumLength(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val f = Array.ofDim[Int](n, k + 1)
    val mp = Array.fill(k + 1)(scala.collection.mutable.HashMap.empty[Int, Int])
    val g = Array.ofDim[Int](k + 1, 3)
    var ans = 0
    var i = 0
    while (i < n) {
      var h = 0
      while (h <= k) {
        f(i)(h) = mp(h).getOrElse(nums(i), 0)
        if (h > 0) {
          if (g(h - 1)(0) != nums(i)) f(i)(h) = math.max(f(i)(h), g(h - 1)(1))
          else f(i)(h) = math.max(f(i)(h), g(h - 1)(2))
        }
        f(i)(h) += 1
        mp(h)(nums(i)) = math.max(mp(h).getOrElse(nums(i), 0), f(i)(h))
        if (g(h)(0) != nums(i)) {
          if (f(i)(h) >= g(h)(1)) {
            g(h)(2) = g(h)(1)
            g(h)(1) = f(i)(h)
            g(h)(0) = nums(i)
          } else if (f(i)(h) > g(h)(2)) {
            g(h)(2) = f(i)(h)
          }
        } else if (f(i)(h) > g(h)(1)) {
          g(h)(1) = f(i)(h)
        }
        ans = math.max(ans, f(i)(h))
        h += 1
      }
      i += 1
    }
    ans
  }
}
