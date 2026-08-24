// LeetCode 3872 - Longest Arithmetic Sequence After Changing At Most One Element
// https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

object Solution {
  def longestArithmetic(nums: Array[Int]): Int = {
    val n = nums.length
    val d = new Array[Int](n)
    var i = 1
    while (i < n) {
      d(i) = nums(i) - nums(i - 1)
      i += 1
    }
    val f = Array.fill(n)(2)
    val g = Array.fill(n)(2)
    f(0) = 1
    g(n - 1) = 1
    i = 2
    while (i < n) {
      if (d(i) == d(i - 1)) f(i) = f(i - 1) + 1
      i += 1
    }
    i = n - 3
    while (i >= 0) {
      if (d(i + 1) == d(i + 2)) g(i) = g(i + 1) + 1
      i -= 1
    }
    var ans = 3
    i = 0
    while (i < n) {
      ans = math.max(ans, math.max(f(i), g(i)))
      if (i > 0) ans = math.max(ans, f(i - 1) + 1)
      if (i + 1 < n) ans = math.max(ans, g(i + 1) + 1)
      if (i > 0 && i < n - 1) {
        var diff = nums(i + 1) - nums(i - 1)
        if (diff % 2 == 0) {
          diff /= 2
          var k = 3
          if (i > 1 && diff == d(i - 1)) k += f(i - 1) - 1
          if (i < n - 2 && diff == d(i + 2)) k += g(i + 1) - 1
          ans = math.max(ans, k)
        }
      }
      i += 1
    }
    ans
  }
}
