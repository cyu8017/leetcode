// LeetCode 1593 - Split a String Into the Max Number of Unique Substrings
// https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

object Solution {
  def maxUniqueSplit(s: String): Int = {
    val used = scala.collection.mutable.Set.empty[String]
    var answer = 0
    def dfs(i: Int): Unit = {
      if (used.size + s.length - i <= answer) return
      if (i == s.length) {
        answer = math.max(answer, used.size)
        return
      }
      for (j <- i + 1 to s.length) {
        val part = s.substring(i, j)
        if (!used.contains(part)) {
          used += part
          dfs(j)
          used -= part
        }
      }
    }
    dfs(0)
    answer
  }
}
