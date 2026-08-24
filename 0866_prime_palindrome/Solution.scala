// LeetCode 0866 - Prime Palindrome
// https://leetcode.com/problems/prime-palindrome/

object Solution {
  def primePalindrome(n: Int): Int = {
    if (n <= 2) return 2
    if (n <= 3) return 3
    if (n <= 5) return 5
    if (n <= 7) return 7
    if (n <= 11) return 11
    def isPrime(x: Int): Boolean = {
      if (x < 2) return false
      if (x % 2 == 0) return x == 2
      var d = 3
      while (d.toLong * d <= x) {
        if (x % d == 0) return false
        d += 2
      }
      true
    }
    var length = 1
    while (length <= 5) {
      val start = math.pow(10, length - 1).toInt
      val end = math.pow(10, length).toInt
      var root = start
      while (root < end) {
        val s = root.toString
        val pal = new StringBuilder(s)
        var i = s.length - 2
        while (i >= 0) {
          pal.append(s.charAt(i))
          i -= 1
        }
        val value = pal.toString.toInt
        if (value >= n && isPrime(value)) return value
        root += 1
      }
      length += 1
    }
    0
  }
}
