// LeetCode 0732 - My Calendar III
// https://leetcode.com/problems/my-calendar-iii/

class MyCalendarThree() {
  private val delta = scala.collection.mutable.TreeMap.empty[Int, Int]

  def book(startTime: Int, endTime: Int): Int = {
    delta(startTime) = delta.getOrElse(startTime, 0) + 1
    delta(endTime) = delta.getOrElse(endTime, 0) - 1
    var current = 0
    var best = 0
    for (change <- delta.values) {
      current += change
      best = math.max(best, current)
    }
    best
  }
}
