// LeetCode 3260 - Find the Largest Palindrome Divisible by K
// https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

object Solution {
  def largestPalindrome(n: Int, k: Int): String = {
    val digits = repeat('9', n)
    val half = (n + 1) / 2
    k match {
      case 1 | 3 | 9 => new String(digits)
      case 2 =>
        digits(0) = '8'; digits(n - 1) = '8'
        new String(digits)
      case 4 =>
        if (n == 1) "8"
        else {
          digits(0) = '8'; digits(1) = '8'; digits(n - 1) = '8'; digits(n - 2) = '8'
          new String(digits)
        }
      case 5 =>
        digits(0) = '5'; digits(n - 1) = '5'
        new String(digits)
      case 8 =>
        if (n <= 2) new String(repeat('8', n))
        else {
          digits(0) = '8'; digits(1) = '8'; digits(2) = '8'
          digits(n - 1) = '8'; digits(n - 2) = '8'; digits(n - 3) = '8'
          new String(digits)
        }
      case 6 =>
        if (n == 1) "6"
        else {
          digits(0) = '8'; digits(n - 1) = '8'
          val sum = 16 + 9 * (n - 2)
          val need = sum % 3
          if (need != 0) {
            val pos = half - 1
            digits(pos) = ('0' + (digits(pos) - '0') - need).toChar
            if (n % 2 == 0 || pos != n - 1 - pos) digits(n - 1 - pos) = digits(pos)
          }
          new String(digits)
        }
      case 7 => largestPal7(n)
      case _ => new String(digits)
    }
  }

  def repeat(c: Char, n: Int): Array[Char] = Array.fill(n)(c)

  def mod7(s: String): Int = {
    var r = 0
    var i = 0
    while (i < s.length) {
      r = (r * 10 + (s.charAt(i) - '0')) % 7
      i += 1
    }
    r
  }

  def largestPal7(n: Int): String = {
    val halfLen = (n + 1) / 2
    val half = repeat('9', halfLen)
    var cont = true
    var res = ""
    while (cont) {
      val pal = new Array[Char](n)
      var i = 0
      while (i < halfLen) { pal(i) = half(i); i += 1 }
      i = 0
      while (i < n / 2) { pal(n - 1 - i) = pal(i); i += 1 }
      if (mod7(new String(pal)) == 0) { res = new String(pal); cont = false }
      else {
        var idx = halfLen - 1
        while (idx >= 0 && half(idx) == '0') {
          half(idx) = '9'
          idx -= 1
        }
        if (idx < 0) cont = false
        else half(idx) = (half(idx) - 1).toChar
      }
    }
    res
  }
}
