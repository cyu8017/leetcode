// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

object Solution {
  def lexSmallest(s: String): String = {
    val n = s.length
    var best = s
    var i = 1
    while (i <= n) {
      val t = s.toCharArray
      reverse(t, 0, 0 + i)
      val ts = new String(t)
      if (ts.compareTo(best) < 0) best = ts
      i += 1
    }
    i = 0
    while (i < n) {
      val t = s.toCharArray
      reverse(t, i, i + n - i)
      val ts = new String(t)
      if (ts.compareTo(best) < 0) best = ts
      i += 1
    }
    best
  }

  private def reverse(a: Array[Char], l: Int, r: Int): Unit = {
    var i = l
    var j = r - 1
    while (i < j) {
      val t = a(i); a(i) = a(j); a(j) = t
      i += 1
      j -= 1
    }
  }
}
