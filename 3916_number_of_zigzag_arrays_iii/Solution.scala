// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

object Solution {
  def zigZagArrays(n: Int, l: Int, r: Int): Int = {
    val mod = 1000000007L
    val points = n + 1
    val values = new Array[Long](points + 1)
    var mm = 1
    while (mm <= points) {
      var up = new Array[Long](mm)
      var down = new Array[Long](mm)
      var value = 0
      while (value < mm) {
        up(value) = value
        down(value) = mm - 1 - value
        value += 1
      }
      var length = 3
      while (length <= n) {
        val nextUp = new Array[Long](mm)
        val nextDown = new Array[Long](mm)
        var prefix = 0L
        value = 0
        while (value < mm) {
          nextUp(value) = prefix
          prefix = (prefix + down(value)) % mod
          value += 1
        }
        var suffix = 0L
        value = mm - 1
        while (value >= 0) {
          nextDown(value) = suffix
          suffix = (suffix + up(value)) % mod
          value -= 1
        }
        up = nextUp
        down = nextDown
        length += 1
      }
      value = 0
      while (value < mm) {
        values(mm) = (values(mm) + up(value) + down(value)) % mod
        value += 1
      }
      mm += 1
    }
    val x = (r.toLong - l + 1) % mod
    if (r.toLong - l + 1 <= points) return values(r - l + 1).toInt
    val prefixA = new Array[Long](points + 2)
    val suffixA = new Array[Long](points + 2)
    prefixA(0) = 1
    var i = 1
    while (i <= points) {
      prefixA(i) = prefixA(i - 1) * ((x - i + mod) % mod) % mod
      i += 1
    }
    suffixA(points + 1) = 1
    i = points
    while (i >= 1) {
      suffixA(i) = suffixA(i + 1) * ((x - i + mod) % mod) % mod
      i -= 1
    }
    val factorial = new Array[Long](points + 1)
    factorial(0) = 1
    i = 1
    while (i <= points) {
      factorial(i) = factorial(i - 1) * i % mod
      i += 1
    }
    var answer = 0L
    i = 1
    while (i <= points) {
      val numerator = prefixA(i - 1) * suffixA(i + 1) % mod
      val denominator = factorial(i - 1) * factorial(points - i) % mod
      val term = values(i) * numerator % mod * powm(denominator, mod - 2, mod) % mod
      if ((points - i) % 2 == 1) answer -= term
      else answer += term
      answer %= mod
      i += 1
    }
    if (answer < 0) answer += mod
    answer.toInt
  }

  private def powm(a0: Long, e0: Long, mod: Long): Long = {
    var a = a0
    var e = e0
    var res = 1L
    while (e > 0) {
      if ((e & 1) != 0) res = res * a % mod
      a = a * a % mod
      e >>= 1
    }
    res
  }
}
