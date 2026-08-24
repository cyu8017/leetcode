// LeetCode 3571 - Find the Shortest Superstring II
// https://leetcode.com/problems/find-the-shortest-superstring-ii/

object Solution {
  def shortestSuperstring(s1: String, s2: String): String = {
    if (s1.length > s2.length) return shortestSuperstring(s2, s1)
    val m = s1.length
    if (s2.contains(s1)) return s2
    var i = 0
    while (i < m) {
      if (s2.startsWith(s1.substring(i))) return s1.substring(0, i) + s2
      val len = m - i
      if (s2.length >= len && s2.substring(s2.length - len) == s1.substring(0, len))
        return s2 + s1.substring(m - i)
      i += 1
    }
    s1 + s2
  }
}
