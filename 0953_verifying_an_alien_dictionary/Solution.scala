// LeetCode 0953 - Verifying an Alien Dictionary
// https://leetcode.com/problems/verifying-an-alien-dictionary/

object Solution {
  def isAlienSorted(words: Array[String], order: String): Boolean = {
    val rank = Array.ofDim[Int](26)
    var i = 0
    while (i < 26) {
      rank(order.charAt(i) - 'a') = i
      i += 1
    }
    def lessEq(a: String, b: String): Boolean = {
      val n = math.min(a.length, b.length)
      var j = 0
      while (j < n) {
        if (rank(a.charAt(j) - 'a') != rank(b.charAt(j) - 'a'))
          return rank(a.charAt(j) - 'a') < rank(b.charAt(j) - 'a')
        j += 1
      }
      a.length <= b.length
    }
    i = 0
    while (i + 1 < words.length) {
      if (!lessEq(words(i), words(i + 1))) return false
      i += 1
    }
    true
  }
}
