// LeetCode 0729 - My Calendar I
// https://leetcode.com/problems/my-calendar-i/

class MyCalendar() {
  private val bookings = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]

  def book(startTime: Int, endTime: Int): Boolean = {
    for (b <- bookings) {
      if (b(0) < endTime && startTime < b(1)) return false
    }
    bookings += Array(startTime, endTime)
    true
  }
}
