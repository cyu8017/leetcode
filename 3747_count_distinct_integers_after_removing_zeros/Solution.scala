// LeetCode 3747 - Count Distinct Integers After Removing Zeros
// https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

object Solution {
  def countDistinct(n: Long): Long = {
    val s = java.lang.Long.toString(n)
    val m = s.length
    val f = Array.fill(20, 2, 2, 2)(-1L)

    def dfs(i: Int, zero: Int, lead: Int, limit: Int): Long = {
      if (i == m) return if (zero == 0 && lead == 0) 1 else 0
      if (limit == 0 && f(i)(zero)(lead)(limit) != -1) return f(i)(zero)(lead)(limit)
      val up = if (limit == 1) s.charAt(i) - '0' else 9
      var ans = 0L
      var d = 0
      while (d <= up) {
        var nxtZero = zero
        if (d == 0 && lead == 0) nxtZero = 1
        val nxtLead = if (lead == 1 && d == 0) 1 else 0
        val nxtLimit = if (limit == 1 && d == up) 1 else 0
        ans += dfs(i + 1, nxtZero, nxtLead, nxtLimit)
        d += 1
      }
      if (limit == 0) f(i)(zero)(lead)(limit) = ans
      ans
    }

    dfs(0, 0, 1, 1)
  }
}
