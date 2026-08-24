// LeetCode 3694 - Distinct Points Reachable After Substring Removal
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

object Solution {
  def distinctPoints(s: String, k: Int): Int = {
    val n = s.length
    val f = new Array[Int](n + 1)
    val g = new Array[Int](n + 1)
    var x = 0
    var y = 0
    var i = 1
    while (i <= n) {
      val c = s.charAt(i - 1)
      if (c == 'U') y += 1
      else if (c == 'D') y -= 1
      else if (c == 'L') x -= 1
      else x += 1
      f(i) = x
      g(i) = y
      i += 1
    }
    val st = new java.util.HashSet[java.lang.Long]()
    i = k
    while (i <= n) {
      val a = f(n) - (f(i) - f(i - k))
      val b = g(n) - (g(i) - g(i - k))
      val key = a.toLong * n + b
      st.add(key)
      i += 1
    }
    st.size()
  }
}
