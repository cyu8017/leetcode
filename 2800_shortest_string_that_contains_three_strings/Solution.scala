// LeetCode 2800 - Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

object Solution {
  def minimumString(a: String, b: String, c: String): String = {
    val perms = Array(
      Array(a, b, c), Array(a, c, b), Array(b, a, c),
      Array(b, c, a), Array(c, a, b), Array(c, b, a)
    )
    var ans = ""
    perms.foreach { p =>
      val cur = merge(merge(p(0), p(1)), p(2))
      if (ans.isEmpty || cur.length < ans.length || (cur.length == ans.length && cur < ans))
        ans = cur
    }
    ans
  }

  private def merge(x: String, y: String): String = {
    if (x.contains(y)) return x
    var best = x + y
    val n = math.min(x.length, y.length)
    var i = n
    var found = false
    while (i > 0 && !found) {
      if (x.substring(x.length - i) == y.substring(0, i)) {
        val cand = x + y.substring(i)
        if (cand.length < best.length || (cand.length == best.length && cand < best)) best = cand
        found = true
      }
      i -= 1
    }
    best
  }
}
