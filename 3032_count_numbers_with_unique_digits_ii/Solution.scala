// LeetCode 3032 - Count Numbers With Unique Digits II
// https://leetcode.com/problems/count-numbers-with-unique-digits-ii/

object Solution {
  def numberCount(a: Int, b: Int): Int = {
    var num = ""
    var f: Array[Array[Int]] = null
    def reset(): Unit = {
      f = Array.fill(num.length, 1 << 10)(-1)
    }
    def dfs(pos: Int, mask: Int, limit: Boolean): Int = {
      if (pos >= num.length) return if (mask != 0) 1 else 0
      if (!limit && f(pos)(mask) != -1) return f(pos)(mask)
      val up = if (limit) num.charAt(pos) - '0' else 9
      var ans = 0
      var i = 0
      while (i <= up) {
        if (((mask >> i) & 1) == 0) {
          var nxt = mask | (1 << i)
          if (mask == 0 && i == 0) nxt = 0
          ans += dfs(pos + 1, nxt, limit && i == up)
        }
        i += 1
      }
      if (!limit) f(pos)(mask) = ans
      ans
    }
    num = b.toString
    reset()
    val y = dfs(0, 0, true)
    num = (a - 1).toString
    reset()
    val x = dfs(0, 0, true)
    y - x
  }
}
