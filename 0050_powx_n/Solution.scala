// LeetCode 0050 - Pow(x, n)
// https://leetcode.com/problems/powx-n/

object Solution {
  def myPow(x: Double, n: Int): Double = {
    if (n == 0) {
      return 1.0
    }

    var baseValue = x
    var exponent = n
    if (exponent < 0) {
      baseValue = 1.0 / baseValue
      exponent = -exponent
    }

    var result = 1.0
    var current = baseValue

    while (exponent != 0) {
      if ((exponent & 1) == 1) {
        result *= current
      }
      current *= current
      exponent >>= 1
    }

    result
  }
}
