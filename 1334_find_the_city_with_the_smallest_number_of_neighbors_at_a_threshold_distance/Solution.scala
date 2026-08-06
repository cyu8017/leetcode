// LeetCode 1334 - Find the City With the Smallest Number of Neighbors at a Threshold Distance
// https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

object Solution {
  def findTheCity(n: Int, edges: Array[Array[Int]], distanceThreshold: Int): Int = {
    val inf = 1000000000000000L
    val dist = Array.fill(n, n)(inf)
    for (i <- 0 until n) dist(i)(i) = 0
    for (e <- edges) {
      dist(e(0))(e(1)) = e(2).toLong
      dist(e(1))(e(0)) = e(2).toLong
    }
    for (k <- 0 until n; i <- 0 until n; j <- 0 until n) {
      dist(i)(j) = math.min(dist(i)(j), dist(i)(k) + dist(k)(j))
    }
    var bestCity = 0
    var bestCount = Int.MaxValue
    for (city <- 0 until n) {
      val count = dist(city).count(_ <= distanceThreshold)
      if (count < bestCount || (count == bestCount && city > bestCity)) {
        bestCount = count
        bestCity = city
      }
    }
    bestCity
  }
}
