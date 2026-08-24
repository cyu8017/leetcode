// LeetCode 3999 - Minimum Number of String Groups Through Transformations
// https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

object Solution {
  private def leastRotation(s: String): Int = {
    val n = s.length
    var i = 0
    var j = 1
    var k = 0
    while (i < n && j < n && k < n) {
      val a = s.charAt((i + k) % n)
      val b = s.charAt((j + k) % n)
      if (a == b) k += 1
      else {
        if (a > b) i += k + 1
        else j += k + 1
        if (i == j) j += 1
        k = 0
      }
    }
    if (i < j) i else j
  }

  private def canonicalRotate(s: String): String = {
    val n = s.length
    if (n <= 1) return s
    val r = leastRotation(s)
    if (r == 0) s else s.substring(r) + s.substring(0, r)
  }

  def minimumGroups(words: Array[String]): Int = {
    val keys = words.map { w =>
      val n = w.length
      val even = new StringBuilder()
      val odd = new StringBuilder()
      var i = 0
      while (i < n) {
        if (i % 2 == 0) even.append(w.charAt(i))
        else odd.append(w.charAt(i))
        i += 1
      }
      canonicalRotate(even.toString) + "#" + canonicalRotate(odd.toString)
    }.sorted
    var groups = 0
    var i = 0
    while (i < keys.length) {
      if (i == 0 || keys(i) != keys(i - 1)) groups += 1
      i += 1
    }
    groups
  }
}
