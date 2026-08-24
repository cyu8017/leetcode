// LeetCode 2531 - Make Number of Distinct Characters Equal
// https://leetcode.com/problems/make-number-of-distinct-characters-equal/

object Solution {
  def isItPossible(word1: String, word2: String): Boolean = {
    val c1 = Array.fill(26)(0)
    val c2 = Array.fill(26)(0)
    word1.foreach(c => c1(c - 'a') += 1)
    word2.foreach(c => c2(c - 'a') += 1)
    var d1 = 0
    var d2 = 0
    var i = 0
    while (i < 26) {
      if (c1(i) > 0) d1 += 1
      if (c2(i) > 0) d2 += 1
      i += 1
    }
    var a = 0
    while (a < 26) {
      if (c1(a) != 0) {
        var b = 0
        while (b < 26) {
          if (c2(b) != 0) {
            var nd1 = d1
            var nd2 = d2
            if (a == b) {
              if (nd1 == nd2) return true
            } else {
              if (c1(a) == 1) nd1 -= 1
              if (c1(b) == 0) nd1 += 1
              if (c2(b) == 1) nd2 -= 1
              if (c2(a) == 0) nd2 += 1
              if (nd1 == nd2) return true
            }
          }
          b += 1
        }
      }
      a += 1
    }
    false
  }
}
