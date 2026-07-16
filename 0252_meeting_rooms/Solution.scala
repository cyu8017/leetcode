// LeetCode 0252 - Meeting Rooms
// https://leetcode.com/problems/meeting-rooms/

object Solution {
  def canAttendMeetings(intervals: Array[Array[Int]]): Boolean = {
    val sorted = intervals.sortBy(_.head)
    for (index <- 1 until sorted.length) {
      if (sorted(index).head < sorted(index - 1)(1)) {
        return false
      }
    }
    true
  }
}
