// LeetCode 3698 - Split Array With Minimum Difference
// https://leetcode.com/problems/split-array-with-minimum-difference/

object Solution {
  def splitArray(nums: Array[Int]): Long = {
    val n = nums.length
    val s = new Array[Long](n)
    val f = Array.fill(n)(true)
    val g = Array.fill(n)(true)
    s(0) = nums(0)
    var i = 1
    while (i < n) {
      s(i) = s(i - 1) + nums(i)
      f(i) = f(i - 1)
      if (nums(i) <= nums(i - 1)) f(i) = false
      i += 1
    }
    i = n - 2
    while (i >= 0) {
      g(i) = g(i + 1)
      if (nums(i) <= nums(i + 1)) g(i) = false
      i -= 1
    }
    val inf = Long.MaxValue / 4
    var ans = inf
    i = 0
    while (i < n - 1) {
      if (f(i) && g(i + 1)) {
        val s1 = s(i)
        val s2 = s(n - 1) - s(i)
        ans = math.min(ans, math.abs(s1 - s2))
      }
      i += 1
    }
    if (ans < inf) ans else -1L
  }
}
