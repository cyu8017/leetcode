// LeetCode 3579 - Minimum Steps to Convert String with Operations
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

object Solution {
  def calc(word1: String, word2: String, l: Int, r: Int, rev: Boolean): Int = {
    val cnt = Array.ofDim[Int](26, 26)
    var res = 0
    var i = l
    while (i <= r) {
      val j = if (rev) r - (i - l) else i
      val a = word1.charAt(j) - 'a'
      val b = word2.charAt(i) - 'a'
      if (a != b) {
        if (cnt(b)(a) > 0) cnt(b)(a) -= 1
        else { cnt(a)(b) += 1; res += 1 }
      }
      i += 1
    }
    res
  }

  def minOperations(word1: String, word2: String): Int = {
    val n = word1.length
    val f = Array.fill(n + 1)(Integer.MAX_VALUE / 2)
    f(0) = 0
    var i = 1
    while (i <= n) {
      var j = 0
      while (j < i) {
        val a = calc(word1, word2, j, i - 1, false)
        val b = 1 + calc(word1, word2, j, i - 1, true)
        f(i) = math.min(f(i), f(j) + math.min(a, b))
        j += 1
      }
      i += 1
    }
    f(n)
  }
}
