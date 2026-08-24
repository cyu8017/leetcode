// LeetCode 3169 - Count Days Without Meetings
// https://leetcode.com/problems/count-days-without-meetings/

object Solution {
  def countDays(days: Int, meetings: Array[Array[Int]]): Int = {
    val ms = meetings.sortBy(_(0))
    var last = 0
    var ans = 0
    ms.foreach { e =>
      val st = e(0)
      val ed = e(1)
      if (last < st) ans += st - last - 1
      last = math.max(last, ed)
    }
    ans += days - last
    ans
  }
}
