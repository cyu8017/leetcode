// LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

object Solution {
  def maxDifference(s: String, k: Int): Int = {
    val n = s.length
    var ans = -1000000000
    var a = 0
    while (a < 5) {
      var b = 0
      while (b < 5) {
        if (a != b) {
          val prefA = new Array[Int](n + 1)
          val prefB = new Array[Int](n + 1)
          var i = 0
          while (i < n) {
            prefA(i + 1) = prefA(i)
            prefB(i + 1) = prefB(i)
            if (s.charAt(i) - '0' == a) prefA(i + 1) += 1
            if (s.charAt(i) - '0' == b) prefB(i + 1) += 1
            i += 1
          }
          i = 0
          while (i < n) {
            var j = i + k - 1
            while (j < n) {
              val fa = prefA(j + 1) - prefA(i)
              val fb = prefB(j + 1) - prefB(i)
              if (fa % 2 == 1 && fb % 2 == 0 && fb > 0) {
                if (fa - fb > ans) ans = fa - fb
              }
              j += 1
            }
            i += 1
          }
        }
        b += 1
      }
      a += 1
    }
    ans
  }
}
