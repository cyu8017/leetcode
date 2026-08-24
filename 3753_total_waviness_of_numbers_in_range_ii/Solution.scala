// LeetCode 3753 - Total Waviness Of Numbers In Range II
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

object Solution {
  private class Result(var count: Long = 0, var sum: Long = 0)

  private def wavinessUpTo(limit: Long): Long = {
    if (limit < 0) return 0
    val digits = new java.util.ArrayList[Integer]()
    if (limit == 0) digits.add(0)
    else {
      var value = limit
      while (value > 0) {
        digits.add((value % 10).toInt)
        value /= 10
      }
      java.util.Collections.reverse(digits)
    }
    val memo = new java.util.HashMap[String, Result]()
    dfs(0, 10, 10, started = false, tight = true, digits, memo).sum
  }

  private def dfs(
      position: Int,
      secondLast: Int,
      last: Int,
      started: Boolean,
      tight: Boolean,
      digits: java.util.List[Integer],
      memo: java.util.HashMap[String, Result]
  ): Result = {
    if (position == digits.size()) return new Result(1, 0)
    val key = position + "," + secondLast + "," + last + "," + started
    if (!tight && memo.containsKey(key)) return memo.get(key)
    val upper = if (tight) digits.get(position).intValue else 9
    val result = new Result()
    var digit = 0
    while (digit <= upper) {
      val nextTight = tight && digit == upper
      var nextSecondLast = secondLast
      var nextLast = last
      val nextStarted = started || digit != 0
      var add = 0L
      if (!nextStarted) {
        nextSecondLast = 10
        nextLast = 10
      } else if (!started) {
        nextSecondLast = 10
        nextLast = digit
      } else {
        if (secondLast != 10 &&
            ((last > secondLast && last > digit) || (last < secondLast && last < digit))) {
          add = 1
        }
        nextSecondLast = last
        nextLast = digit
      }
      val child = dfs(position + 1, nextSecondLast, nextLast, nextStarted, nextTight, digits, memo)
      result.count += child.count
      result.sum += child.sum + add * child.count
      digit += 1
    }
    if (!tight) memo.put(key, result)
    result
  }

  def totalWaviness(a: Long, b: Long): Long = wavinessUpTo(b) - wavinessUpTo(a - 1)
}
