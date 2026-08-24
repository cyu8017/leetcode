// LeetCode 2246 - Longest Path With Different Adjacent Characters
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

object Solution {
  def longestPath(parent: Array[Int], s: String): Int = {
    val n = parent.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 1
    while (i < n) {
      g(parent(i)) += i
      i += 1
    }
    var ans = 1
    def dfs(u: Int): Int = {
      var best1 = 0
      var best2 = 0
      for (v <- g(u)) {
        val lenV = dfs(v)
        if (s.charAt(v) != s.charAt(u)) {
          if (lenV > best1) {
            best2 = best1
            best1 = lenV
          } else if (lenV > best2) best2 = lenV
        }
      }
      ans = math.max(ans, 1 + best1 + best2)
      1 + best1
    }
    dfs(0)
    ans
  }
}
