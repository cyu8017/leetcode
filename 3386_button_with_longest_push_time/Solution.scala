// LeetCode 3386 - Button with Longest Push Time
// https://leetcode.com/problems/button-with-longest-push-time/

object Solution {
  def buttonWithLongestTime(events: Array[Array[Int]]): Int = {
    var bestT = events(0)(1)
    var bestI = events(0)(0)
    var i = 1
    while (i < events.length) {
      val t = events(i)(1) - events(i - 1)(1)
      if (t > bestT || (t == bestT && events(i)(0) < bestI)) {
        bestT = t
        bestI = events(i)(0)
      }
      i += 1
    }
    bestI
  }
}
