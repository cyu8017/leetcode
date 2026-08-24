// LeetCode 2801 - Count Stepping Numbers in Range
// https://leetcode.com/problems/count-stepping-numbers-in-range/

object Solution {
  private val MOD = 1000000007

  def countSteppingNumbers(low: String, high: String): Int = {
    var ans = (countTo(high) - countTo(dec(low))) % MOD
    if (ans < 0) ans += MOD
    ans
  }

  private def countTo(s: String): Int = {
    val memo = Array.fill(85, 2, 11, 2)(-1)
    dfs(s, 0, 1, -1, 0, memo)
  }

  private def dfs(s: String, pos: Int, tight: Int, last: Int, started: Int, memo: Array[Array[Array[Array[Int]]]]): Int = {
    if (pos == s.length) return started
    if (memo(pos)(tight)(last + 1)(started) != -1) return memo(pos)(tight)(last + 1)(started)
    val up = if (tight == 1) s.charAt(pos) - '0' else 9
    var ans = 0L
    var d = 0
    while (d <= up) {
      val nt = if (tight == 1 && d == up) 1 else 0
      if (started == 0) {
        if (d == 0) ans += dfs(s, pos + 1, nt, -1, 0, memo)
        else ans += dfs(s, pos + 1, nt, d, 1, memo)
      } else if (math.abs(d - last) == 1) {
        ans += dfs(s, pos + 1, nt, d, 1, memo)
      }
      d += 1
    }
    memo(pos)(tight)(last + 1)(started) = (ans % MOD).toInt
    memo(pos)(tight)(last + 1)(started)
  }

  private def dec(s: String): String = {
    val arr = s.toCharArray
    var i = arr.length - 1
    while (i >= 0 && arr(i) == '0') {
      arr(i) = '9'
      i -= 1
    }
    if (i >= 0) arr(i) = (arr(i) - 1).toChar
    var j = 0
    while (j < arr.length - 1 && arr(j) == '0') j += 1
    new String(arr, j, arr.length - j)
  }
}
