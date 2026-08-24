// LeetCode 2100 - Find Good Days to Rob the Bank
// https://leetcode.com/problems/find-good-days-to-rob-the-bank/

object Solution {
  def goodDaysToRobBank(security: Array[Int], time: Int): List[Int] = {
    val n = security.length
    if (time == 0) return (0 until n).toList
    val left = Array.fill(n)(0)
    val right = Array.fill(n)(0)
    var i = 1
    while (i < n) {
      if (security(i) <= security(i - 1)) left(i) = left(i - 1) + 1
      i += 1
    }
    i = n - 2
    while (i >= 0) {
      if (security(i) <= security(i + 1)) right(i) = right(i + 1) + 1
      i -= 1
    }
    (time until n - time).filter(i => left(i) >= time && right(i) >= time).toList
  }
}
