// LeetCode 3765 - Complete Prime Number
// https://leetcode.com/problems/complete-prime-number/

object Solution {
  private def isPrime(x: Int): Boolean = {
    if (x < 2) return false
    var i = 2
    while (i * i <= x) {
      if (x % i == 0) return false
      i += 1
    }
    true
  }

  def completePrime(num: Int): Boolean = {
    val s = Integer.toString(num)
    var x = 0
    s.foreach { c =>
      x = x * 10 + (c - '0')
      if (!isPrime(x)) return false
    }
    x = 0
    var p = 1
    var i = s.length - 1
    while (i >= 0) {
      x = p * (s.charAt(i) - '0') + x
      p *= 10
      if (!isPrime(x)) return false
      i -= 1
    }
    true
  }
}
