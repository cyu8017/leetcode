// LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
// https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/

object Solution {
  def countWays(word1: String, word2: String, target: String): Int = {
    val mod = 1000000007
    val n1 = word1.length
    val n2 = word2.length
    val size = (n1 + 1) * (n2 + 1) * 4
    var dp = new Array[Int](size)
    var next = new Array[Int](size)
    dp(index(0, 0, 0, n2)) = 1
    var ti = 0
    while (ti < target.length) {
      val ch = target.charAt(ti)
      java.util.Arrays.fill(next, 0)
      var j = 0
      while (j <= n2) {
        val prefix = new Array[Int](4)
        var a = 0
        while (a < n1) {
          var mask = 0
          while (mask < 4) {
            prefix(mask) += dp(index(a, j, mask, n2))
            if (prefix(mask) >= mod) prefix(mask) -= mod
            mask += 1
          }
          if (word1.charAt(a) == ch) {
            mask = 0
            while (mask < 4) {
              val at = index(a + 1, j, mask | 1, n2)
              next(at) += prefix(mask)
              if (next(at) >= mod) next(at) -= mod
              mask += 1
            }
          }
          a += 1
        }
        j += 1
      }
      var i = 0
      while (i <= n1) {
        val prefix = new Array[Int](4)
        var b = 0
        while (b < n2) {
          var mask = 0
          while (mask < 4) {
            prefix(mask) += dp(index(i, b, mask, n2))
            if (prefix(mask) >= mod) prefix(mask) -= mod
            mask += 1
          }
          if (word2.charAt(b) == ch) {
            mask = 0
            while (mask < 4) {
              val at = index(i, b + 1, mask | 2, n2)
              next(at) += prefix(mask)
              if (next(at) >= mod) next(at) -= mod
              mask += 1
            }
          }
          b += 1
        }
        i += 1
      }
      val tmp = dp
      dp = next
      next = tmp
      ti += 1
    }
    var answer = 0
    var i = 0
    while (i <= n1) {
      var j = 0
      while (j <= n2) {
        answer += dp(index(i, j, 3, n2))
        if (answer >= mod) answer -= mod
        j += 1
      }
      i += 1
    }
    answer
  }

  private def index(i: Int, j: Int, mask: Int, n2: Int): Int =
    ((i * (n2 + 1) + j) * 4) + mask
}
