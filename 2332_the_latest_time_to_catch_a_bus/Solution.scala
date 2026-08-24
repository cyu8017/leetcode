// LeetCode 2332 - The Latest Time to Catch a Bus
// https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

object Solution {
  def latestTimeCatchTheBus(buses: Array[Int], passengers: Array[Int], capacity: Int): Int = {
    java.util.Arrays.sort(buses)
    java.util.Arrays.sort(passengers)
    var pos = 0
    var bi = 0
    while (bi < buses.length) {
      val bus = buses(bi)
      var cap = capacity
      while (cap > 0 && pos < passengers.length && passengers(pos) <= bus) {
        pos += 1
        cap -= 1
      }
      if (bi == buses.length - 1) {
        var cand = if (cap == 0) passengers(pos - 1) else bus
        val taken = scala.collection.mutable.HashSet.empty[Int]
        passengers.foreach(p => taken += p)
        while (taken.contains(cand)) cand -= 1
        return cand
      }
      bi += 1
    }
    -1
  }
}
