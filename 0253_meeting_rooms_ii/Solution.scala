// LeetCode 0253 - Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii/

object Solution {
  def minMeetingRooms(intervals: Array[Array[Int]]): Int = {
    val starts = intervals.map(_(0)).sorted.toArray
    val ends = intervals.map(_(1)).sorted.toArray
    var rooms = 0
    var maxRooms = 0
    var startIndex = 0
    var endIndex = 0

    while (startIndex < starts.length) {
      if (starts(startIndex) < ends(endIndex)) {
        rooms += 1
        maxRooms = math.max(maxRooms, rooms)
        startIndex += 1
      } else {
        rooms -= 1
        endIndex += 1
      }
    }

    maxRooms
  }
}
