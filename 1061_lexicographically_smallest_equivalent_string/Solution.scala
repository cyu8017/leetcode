// LeetCode 1061 - Lexicographically Smallest Equivalent String
// https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

object Solution {
  def smallestEquivalentString(s1: String, s2: String, baseStr: String): String = {
    val parent = Array.tabulate(26)(identity)

    def find(x: Int): Int = {
      var cur = x
      while (parent(cur) != cur) {
        parent(cur) = parent(parent(cur))
        cur = parent(cur)
      }
      cur
    }

    def union(a: Int, b: Int): Unit = {
      val ra = find(a)
      val rb = find(b)
      if (ra == rb) return
      if (ra < rb) parent(rb) = ra else parent(ra) = rb
    }

    for (i <- s1.indices) union(s1(i) - 'a', s2(i) - 'a')
    baseStr.map(c => (find(c - 'a') + 'a').toChar).mkString
  }
}
