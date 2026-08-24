// LeetCode 0731 - My Calendar II
// https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo() {
  private val booked = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
  private val overlaps = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]

  def book(startTime: Int, endTime: Int): Boolean = {
    for (o <- overlaps) {
      if (o(0) < endTime && startTime < o(1)) return false
    }
    for (b <- booked) {
      if (b(0) < endTime && startTime < b(1)) {
        overlaps += Array(math.max(b(0), startTime), math.min(b(1), endTime))
      }
    }
    booked += Array(startTime, endTime)
    true
  }
}
