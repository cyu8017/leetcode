// LeetCode 0753 - Cracking the Safe
// https://leetcode.com/problems/cracking-the-safe/

object Solution {
  def crackSafe(n: Int, k: Int): String = {
    val seen = scala.collection.mutable.HashSet.empty[String]
    val path = scala.collection.mutable.ArrayBuffer.empty[Char]
    val start = "0" * (n - 1)
    def dfs(node: String): Unit = {
      var d = 0
      while (d < k) {
        val digit = ('0' + d).toChar
        val edge = node + digit
        if (seen.add(edge)) {
          dfs(edge.substring(1))
          path += digit
        }
        d += 1
      }
    }
    dfs(start)
    path.mkString + start
  }
}
