// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

object Solution {
  def shortestMatchingSubstring(s: String, p: String): Int = {
    val parts = new java.util.ArrayList[String]()
    val cur = new StringBuilder
    p.foreach { c =>
      if (c == '*') {
        parts.add(cur.toString)
        cur.setLength(0)
      } else cur.append(c)
    }
    parts.add(cur.toString)
    while (parts.size() < 3) parts.add("")
    val a = parts.get(0)
    val b = parts.get(1)
    val c = parts.get(2)
    val n = s.length
    val posA = findAll(s, a)
    val posB = findAll(s, b)
    val posC = findAll(s, c)
    var ans = n + 1
    val ita = posA.iterator()
    while (ita.hasNext) {
      val ia = ita.next()
      val endA = ia + a.length
      var bi = sortSearch(posB, endA)
      var done = false
      while (bi < posB.size() && !done) {
        val endB = posB.get(bi) + b.length
        val ci = sortSearch(posC, endB)
        if (ci < posC.size()) {
          val length = posC.get(ci) + c.length - ia
          if (length < ans) ans = length
        }
        done = true
        bi += 1
      }
    }
    if (ans == n + 1) -1 else ans
  }

  private def findAll(s: String, sub: String): java.util.ArrayList[Integer] = {
    val res = new java.util.ArrayList[Integer]()
    val n = s.length
    if (sub.isEmpty) {
      var i = 0
      while (i <= n) { res.add(i); i += 1 }
      return res
    }
    var i = 0
    while (i + sub.length <= n) {
      if (s.regionMatches(i, sub, 0, sub.length)) res.add(i)
      i += 1
    }
    res
  }

  private def sortSearch(arr: java.util.ArrayList[Integer], x: Int): Int = {
    val i = java.util.Collections.binarySearch(arr, Integer.valueOf(x))
    if (i >= 0) i else -i - 1
  }
}
