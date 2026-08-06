// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

object Solution {
  def minAvailableDuration(slots1: Array[Array[Int]], slots2: Array[Array[Int]], duration: Int): List[Int] = {
    val a = slots1.sortBy(_(0))
    val b = slots2.sortBy(_(0))
    var i = 0
    var j = 0
    while (i < a.length && j < b.length) {
      val start = math.max(a(i)(0), b(j)(0))
      val end = math.min(a(i)(1), b(j)(1))
      if (end - start >= duration) return List(start, start + duration)
      if (a(i)(1) < b(j)(1)) i += 1 else j += 1
    }
    List.empty
  }
}
