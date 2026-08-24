// LeetCode 2315 - Count Asterisks
// https://leetcode.com/problems/count-asterisks/

object Solution {
  def countAsterisks(s: String): Int = {
    var ans = 0
    var inside = false
    s.foreach { c =>
      if (c == '|') inside = !inside
      else if (c == '*' && !inside) ans += 1
    }
    ans
  }
}
