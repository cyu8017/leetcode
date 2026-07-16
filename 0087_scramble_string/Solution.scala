// LeetCode 0087 - Scramble String
// https://leetcode.com/problems/scramble-string/

object Solution {
  def isScramble(s1: String, s2: String): Boolean = {
    val memo = scala.collection.mutable.Map.empty[String, Boolean]

    def dfs(a: String, b: String): Boolean = {
      val key = a + "#" + b
      if (memo.contains(key)) {
        return memo(key)
      }
      if (a == b) {
        memo(key) = true
        return true
      }
      if (a.sorted != b.sorted) {
        memo(key) = false
        return false
      }

      val n = a.length
      for (i <- 1 until n) {
        if (dfs(a.substring(0, i), b.substring(0, i))
            && dfs(a.substring(i), b.substring(i))) {
          memo(key) = true
          return true
        }
        if (dfs(a.substring(0, i), b.substring(n - i))
            && dfs(a.substring(i), b.substring(0, n - i))) {
          memo(key) = true
          return true
        }
      }
      memo(key) = false
      false
    }

    dfs(s1, s2)
  }
}
