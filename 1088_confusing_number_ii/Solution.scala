// LeetCode 1088 - Confusing Number II
// https://leetcode.com/problems/confusing-number-ii/

object Solution {
  def confusingNumberII(n: Int): Int = {
    val rotate = Map(0 -> 0, 1 -> 1, 6 -> 9, 8 -> 8, 9 -> 6)
    val digits = Array(0, 1, 6, 8, 9)
    var ans = 0

    def isConfusing(num: Int): Boolean = {
      var rotated = 0
      var cur = num
      while (cur > 0) {
        val d = cur % 10
        rotated = rotated * 10 + rotate(d)
        cur /= 10
      }
      rotated != num
    }

    def dfs(cur: Long): Unit = {
      if (cur > n) return
      if (cur > 0 && isConfusing(cur.toInt)) ans += 1
      if (cur == 0) {
        for (d <- Array(1, 6, 8, 9)) dfs(d)
      } else {
        for (d <- digits) dfs(cur * 10 + d)
      }
    }

    dfs(0)
    ans
  }
}
