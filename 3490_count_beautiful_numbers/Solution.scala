// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

object Solution {
  private var s: String = _

  private def countBeautiful(n: Int): Int = {
    if (n <= 0) return 0
    s = n.toString
    dfs(0, tight = true, 0, 1, started = false)
  }

  private def dfs(pos: Int, tight: Boolean, sum: Int, prod: Int, started: Boolean): Int = {
    if (pos == s.length) {
      if (!started) return 0
      return if (sum > 0 && prod % sum == 0) 1 else 0
    }
    val up = if (tight) s.charAt(pos) - '0' else 9
    var ans = 0
    var d = 0
    while (d <= up) {
      val nt = tight && d == up
      if (!started && d == 0) ans += dfs(pos + 1, nt, 0, 1, started = false)
      else {
        val ns = sum + d
        val np = if (!started) d else prod * d
        ans += dfs(pos + 1, nt, ns, np, started = true)
      }
      d += 1
    }
    ans
  }

  def beautifulNumbers(l: Int, r: Int): Int = countBeautiful(r) - countBeautiful(l - 1)
}
