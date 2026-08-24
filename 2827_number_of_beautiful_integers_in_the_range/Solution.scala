// LeetCode 2827 - Number of Beautiful Integers in the Range
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

object Solution {
  def numberOfBeautifulIntegers(low: Int, high: Int, k: Int): Int =
    count(high, k) - count(low - 1, k)

  private def count(n: Int, k: Int): Int = {
    if (n < 0) return 0
    val s = n.toString
    val memo = Array.fill(12, 45, 22, 2, 2)(-1)
    dfs(s, k, 0, 0, 0, 1, 0, memo)
  }

  private def dfs(s: String, k: Int, pos: Int, diff: Int, mod: Int, tight: Int, started: Int, memo: Array[Array[Array[Array[Array[Int]]]]]): Int = {
    if (pos == s.length) return if (started == 1 && diff == 0 && mod == 0) 1 else 0
    if (memo(pos)(diff + 20)(mod)(tight)(started) != -1) return memo(pos)(diff + 20)(mod)(tight)(started)
    val up = if (tight == 1) s.charAt(pos) - '0' else 9
    var ans = 0
    var digit = 0
    while (digit <= up) {
      val nt = if (tight == 1 && digit == up) 1 else 0
      if (started == 0) {
        if (digit == 0) ans += dfs(s, k, pos + 1, diff, mod, nt, 0, memo)
        else {
          val nd = diff + (if (digit % 2 == 0) 1 else -1)
          ans += dfs(s, k, pos + 1, nd, digit % k, nt, 1, memo)
        }
      } else {
        val nd = diff + (if (digit % 2 == 0) 1 else -1)
        ans += dfs(s, k, pos + 1, nd, (mod * 10 + digit) % k, nt, 1, memo)
      }
      digit += 1
    }
    memo(pos)(diff + 20)(mod)(tight)(started) = ans
    ans
  }
}
