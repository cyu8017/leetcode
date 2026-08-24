// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

object Solution {
  private val MOD = 1000000007
  private var minSum = 0
  private var maxSum = 0

  def count(num1: String, num2: String, min_sum: Int, max_sum: Int): Int = {
    minSum = min_sum
    maxSum = max_sum
    (dp(num2) - dp(dec(num1)) + MOD) % MOD
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

  private def dp(s: String): Int = {
    val memo = scala.collection.mutable.HashMap.empty[String, Int]
    dfs(s, 0, 0, tight = true, memo)
  }

  private def dfs(
    s: String,
    pos: Int,
    sum: Int,
    tight: Boolean,
    memo: scala.collection.mutable.HashMap[String, Int]
  ): Int = {
    if (sum > maxSum) return 0
    if (pos == s.length) return if (sum >= minSum) 1 else 0
    val key = pos + "," + sum + "," + (if (tight) 1 else 0)
    memo.get(key) match {
      case Some(cached) => cached
      case None =>
        val up = if (tight) s.charAt(pos) - '0' else 9
        var res = 0
        var d = 0
        while (d <= up) {
          res = (res + dfs(s, pos + 1, sum + d, tight && d == up, memo)) % MOD
          d += 1
        }
        memo(key) = res
        res
    }
  }
}
