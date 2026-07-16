// LeetCode 0072 - Edit Distance
// https://leetcode.com/problems/edit-distance/

object Solution {
  def minDistance(word1: String, word2: String): Int = {
    val m = word1.length
    val n = word2.length
    var prev = Array.tabulate(n + 1)(identity)
    var curr = Array.ofDim[Int](n + 1)

    for (i <- 1 to m) {
      curr(0) = i
      for (j <- 1 to n) {
        curr(j) = if (word1(i - 1) == word2(j - 1)) {
          prev(j - 1)
        } else {
          1 + math.min(prev(j), math.min(curr(j - 1), prev(j - 1)))
        }
      }
      val tmp = prev
      prev = curr
      curr = tmp
    }

    prev(n)
  }
}
