// LeetCode 1819 - Number of Different Subsequences GCDs
// https://leetcode.com/problems/number-of-different-subsequences-gcds/

object Solution {
  def countDifferentSubsequenceGCDs(nums: Array[Int]): Int = {
    val maxVal = nums.max
    val present = Array.fill(maxVal + 1)(false)
    for (num <- nums) present(num) = true
    var ans = 0
    for (g <- 1 to maxVal) {
      var has = false
      var gcdVal = 0
      var multiple = g
      while (multiple <= maxVal) {
        if (present(multiple)) {
          has = true
          gcdVal = gcd(gcdVal, multiple / g)
          if (gcdVal == 1) { multiple = maxVal + 1 }
          else multiple += g
        } else multiple += g
      }
      if (has && gcdVal == 1) ans += 1
    }
    ans
  }

  private def gcd(a: Int, b: Int): Int = {
    var x = a
    var y = b
    while (y != 0) {
      val t = x % y
      x = y
      y = t
    }
    x
  }
}
