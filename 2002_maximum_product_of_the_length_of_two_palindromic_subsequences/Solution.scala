// LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

object Solution {
  def maxProduct(s: String): Int = {
    val n = s.length
    val total = 1 << n
    def palLen(mask: Int): Int = {
      val chars = new StringBuilder
      var i = 0
      while (i < n) {
        if ((mask & (1 << i)) != 0) chars.append(s.charAt(i))
        i += 1
      }
      var l = 0
      var r = chars.length - 1
      while (l < r) {
        if (chars.charAt(l) != chars.charAt(r)) return 0
        l += 1
        r -= 1
      }
      chars.length
    }
    var best = 0
    var mask1 = 1
    while (mask1 < total) {
      val len1 = palLen(mask1)
      if (len1 > 0) {
        val remain = (total - 1) ^ mask1
        var mask2 = remain
        while (mask2 > 0) {
          val len2 = palLen(mask2)
          if (len2 > 0 && len1 * len2 > best) best = len1 * len2
          mask2 = (mask2 - 1) & remain
        }
      }
      mask1 += 1
    }
    best
  }
}
