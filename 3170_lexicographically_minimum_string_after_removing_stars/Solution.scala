// LeetCode 3170 - Lexicographically Minimum String After Removing Stars
// https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

object Solution {
  def clearStars(s: String): String = {
    val g = Array.fill(26)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val n = s.length
    val rem = new Array[Boolean](n)
    var i = 0
    while (i < n) {
      if (s.charAt(i) == '*') {
        rem(i) = true
        var j = 0
        var found = false
        while (j < 26 && !found) {
          if (g(j).nonEmpty) {
            rem(g(j).last) = true
            g(j).remove(g(j).length - 1)
            found = true
          }
          j += 1
        }
      } else {
        g(s.charAt(i) - 'a') += i
      }
      i += 1
    }
    val ans = new StringBuilder
    i = 0
    while (i < n) {
      if (!rem(i)) ans.append(s.charAt(i))
      i += 1
    }
    ans.toString
  }
}
