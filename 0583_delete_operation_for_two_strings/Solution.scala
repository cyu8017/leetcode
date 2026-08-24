// LeetCode 0583 - Delete Operation for Two Strings
// https://leetcode.com/problems/delete-operation-for-two-strings/

object Solution {
  def minDistance(word1: String, word2: String): Int = {
    val m = word1.length
    val n = word2.length
    var prev = Array.fill(n + 1)(0)
    var curr = Array.fill(n + 1)(0)
    var i = 1
    while (i <= m) {
      var j = 1
      while (j <= n) {
        if (word1.charAt(i - 1) == word2.charAt(j - 1)) curr(j) = prev(j - 1) + 1
        else curr(j) = math.max(prev(j), curr(j - 1))
        j += 1
      }
      val tmp = prev
      prev = curr
      curr = tmp
      j = 0
      while (j <= n) { curr(j) = 0; j += 1 }
      i += 1
    }
    m + n - 2 * prev(n)
  }
}
