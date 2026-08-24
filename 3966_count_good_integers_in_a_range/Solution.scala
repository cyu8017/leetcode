// LeetCode 3966 - Count Good Integers in a Range
// https://leetcode.com/problems/count-good-integers-in-a-range/

import scala.collection.mutable

object Solution {
  def countGoodIntegers(l: Long, r: Long, k: Int): Long =
    count(r, k) - count(l - 1, k)

  private def count(bound: Long, k: Int): Long = {
    if (bound <= 0) return 0
    val digits = bound.toString
    val memo = mutable.HashMap.empty[String, Long]
    dfs(0, 0, started = false, tight = true, digits, k, memo)
  }

  private def dfs(
      position: Int,
      previous: Int,
      started: Boolean,
      tight: Boolean,
      digits: String,
      k: Int,
      memo: mutable.HashMap[String, Long]
  ): Long = {
    if (position == digits.length) return if (started) 1 else 0
    val key = position + "," + previous + "," + started
    if (!tight && memo.contains(key)) return memo(key)
    val limit = if (tight) digits.charAt(position) - '0' else 9
    var result = 0L
    var digit = 0
    while (digit <= limit) {
      val nextStarted = started || digit != 0
      if (!(started && math.abs(previous - digit) > k)) {
        val nextPrevious = if (nextStarted) digit else previous
        result += dfs(position + 1, nextPrevious, nextStarted, tight && digit == limit, digits, k, memo)
      }
      digit += 1
    }
    if (!tight) memo(key) = result
    result
  }
}
