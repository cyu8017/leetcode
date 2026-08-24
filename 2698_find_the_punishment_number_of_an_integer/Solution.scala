// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

object Solution {
  def punishmentNumber(n: Int): Int = {
    var ans = 0
    var i = 1
    while (i <= n) {
      val sq = i * i
      if (can(sq, i)) ans += sq
      i += 1
    }
    ans
  }

  private def can(sq: Int, target: Int): Boolean = {
    val s = sq.toString
    dfs(s, 0, 0, target)
  }

  private def dfs(s: String, i: Int, sum: Int, target: Int): Boolean = {
    val m = s.length
    if (i == m) return sum == target
    var cur = 0
    var j = i
    while (j < m) {
      cur = cur * 10 + (s.charAt(j) - '0')
      if (sum + cur > target) return false
      if (dfs(s, j + 1, sum + cur, target)) return true
      j += 1
    }
    false
  }
}
