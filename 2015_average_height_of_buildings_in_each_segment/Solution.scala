// LeetCode 2015 - Average Height of Buildings in Each Segment
// https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

object Solution {
  def averageHeightOfBuildings(buildings: Array[Array[Int]]): Array[Array[Int]] = {
    val events = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    buildings.foreach { b =>
      events += Array(b(0), 1, b(2))
      events += Array(b(1), -1, b(2))
    }
    val sorted = events.sortBy(e => (e(0), e(1)))
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var count = 0
    var sum = 0
    var prev = sorted(0)(0)
    sorted.foreach { e =>
      if (e(0) != prev && count > 0) {
        val avg = sum / count
        if (ans.nonEmpty && ans.last(1) == prev && ans.last(2) == avg) ans.last(1) = e(0)
        else ans += Array(prev, e(0), avg)
      }
      count += e(1)
      sum += e(1) * e(2)
      prev = e(0)
    }
    ans.toArray
  }
}
