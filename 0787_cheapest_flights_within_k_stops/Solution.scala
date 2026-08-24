// LeetCode 0787 - Cheapest Flights Within K Stops
// https://leetcode.com/problems/cheapest-flights-within-k-stops/

object Solution {
  def findCheapestPrice(n: Int, flights: Array[Array[Int]], src: Int, dst: Int, k: Int): Int = {
    val INF = Int.MaxValue / 4
    var dist = Array.fill(n)(INF)
    dist(src) = 0
    var i = 0
    while (i <= k) {
      val nxt = dist.clone()
      flights.foreach { f =>
        val u = f(0); val v = f(1); val price = f(2)
        if (dist(u) != INF && dist(u) + price < nxt(v)) nxt(v) = dist(u) + price
      }
      dist = nxt
      i += 1
    }
    if (dist(dst) == INF) -1 else dist(dst)
  }
}
