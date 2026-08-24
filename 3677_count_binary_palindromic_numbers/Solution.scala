// LeetCode 3677 - Count Binary Palindromic Numbers
// https://leetcode.com/problems/count-binary-palindromic-numbers/

object Solution {
  def countBinaryPalindromes(n: Long): Int = {
    if (n == 0) return 1
    var ans = 1
    val sb = new StringBuilder
    var x = n
    while (x > 0) {
      sb.append(('0' + (x & 1).toInt).toChar)
      x >>= 1
    }
    val s = sb.reverse().toString
    val L = s.length
    var len = 1
    while (len < L) {
      val half = (len + 1) / 2
      ans += 1 << (half - 1)
      len += 1
    }
    val half = (L + 1) / 2
    val prefix = s.substring(0, half)
    val start = 1 << (half - 1)
    var prefVal = 0L
    for (c <- prefix) prefVal = (prefVal << 1) | (c - '0')
    ans += (prefVal - start).toInt
    val pal = new StringBuilder(prefix)
    var i = half - 1 - (L % 2)
    while (i >= 0) {
      pal.append(prefix.charAt(i))
      i -= 1
    }
    var pval = 0L
    for (c <- pal.toString) pval = (pval << 1) | (c - '0')
    if (pval <= n) ans += 1
    ans
  }
}
