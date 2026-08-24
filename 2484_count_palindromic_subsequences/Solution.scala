// LeetCode 2484 - Count Palindromic Subsequences
// https://leetcode.com/problems/count-palindromic-subsequences/

object Solution {
  def countPalindromes(s: String): Int = {
    val mod = 1000000007
    val n = s.length
    val pref = Array.ofDim[Int](n, 10, 10)
    val suf = Array.ofDim[Int](n, 10, 10)
    val cnt = new Array[Int](10)
    var i = 0
    while (i < n) {
      if (i > 0) {
        var a = 0
        while (a < 10) {
          var b = 0
          while (b < 10) {
            pref(i)(a)(b) = pref(i - 1)(a)(b)
            b += 1
          }
          a += 1
        }
      }
      val d = s.charAt(i) - '0'
      var a = 0
      while (a < 10) {
        pref(i)(a)(d) += cnt(a)
        a += 1
      }
      cnt(d) += 1
      i += 1
    }
    java.util.Arrays.fill(cnt, 0)
    i = n - 1
    while (i >= 0) {
      if (i + 1 < n) {
        var a = 0
        while (a < 10) {
          var b = 0
          while (b < 10) {
            suf(i)(a)(b) = suf(i + 1)(a)(b)
            b += 1
          }
          a += 1
        }
      }
      val d = s.charAt(i) - '0'
      var a = 0
      while (a < 10) {
        suf(i)(a)(d) += cnt(a)
        a += 1
      }
      cnt(d) += 1
      i -= 1
    }
    var ans = 0
    i = 2
    while (i < n - 2) {
      var a = 0
      while (a < 10) {
        var b = 0
        while (b < 10) {
          ans = ((ans + pref(i - 1)(a)(b).toLong * suf(i + 1)(a)(b)) % mod).toInt
          b += 1
        }
        a += 1
      }
      i += 1
    }
    ans
  }
}
