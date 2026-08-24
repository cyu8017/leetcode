// LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
// https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

object Solution {
  def smallestValue(n0: Int): Int = {
    def sumPrimeFactors(x0: Int): Int = {
      var x = x0
      var s = 0
      var i = 2
      while (i.toLong * i <= x) {
        while (x % i == 0) {
          s += i
          x /= i
        }
        i += 1
      }
      if (x > 1) s += x
      s
    }
    var n = n0
    while (true) {
      val s = sumPrimeFactors(n)
      if (s == n) return n
      n = s
    }
    n
  }
}
