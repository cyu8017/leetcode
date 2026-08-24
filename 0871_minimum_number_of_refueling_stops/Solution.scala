// LeetCode 0871 - Minimum Number of Refueling Stops
// https://leetcode.com/problems/minimum-number-of-refueling-stops/

object Solution {
  def minRefuelStops(target: Int, startFuel: Int, stations: Array[Array[Int]]): Int = {
    val pq = scala.collection.mutable.PriorityQueue.empty[Int]
    val all = stations :+ Array(target, 0)
    var ans = 0
    var prev = 0
    var fuel = startFuel.toLong
    all.foreach { st =>
      val pos = st(0)
      val gas = st(1)
      fuel -= pos - prev
      while (pq.nonEmpty && fuel < 0) {
        fuel += pq.dequeue()
        ans += 1
      }
      if (fuel < 0) return -1
      pq.enqueue(gas)
      prev = pos
    }
    ans
  }
}
