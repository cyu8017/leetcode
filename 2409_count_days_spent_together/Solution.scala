// LeetCode 2409 - Count Days Spent Together
// https://leetcode.com/problems/count-days-spent-together/

object Solution {
  private val DAYS = Array(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

  def countDaysTogether(arriveAlice: String, leaveAlice: String, arriveBob: String, leaveBob: String): Int = {
    val a1 = toDay(arriveAlice)
    val a2 = toDay(leaveAlice)
    val b1 = toDay(arriveBob)
    val b2 = toDay(leaveBob)
    val start = math.max(a1, b1)
    val end = math.min(a2, b2)
    if (end < start) 0 else end - start + 1
  }

  private def toDay(s: String): Int = {
    val m = (s.charAt(0) - '0') * 10 + (s.charAt(1) - '0')
    val d = (s.charAt(3) - '0') * 10 + (s.charAt(4) - '0')
    var res = d
    var i = 0
    while (i < m - 1) {
      res += DAYS(i)
      i += 1
    }
    res
  }
}
