// LeetCode 1765 - Map of Highest Peak
// https://leetcode.com/problems/map-of-highest-peak/

object Solution {
  def highestPeak(isWater: Array[Array[Int]]): Array[Array[Int]] = {
    val m = isWater.length
    val n = isWater(0).length
    val dist = Array.fill(m, n)(-1)
    val queue = scala.collection.mutable.Queue.empty[(Int, Int)]
    for (i <- 0 until m; j <- 0 until n) {
      if (isWater(i)(j) == 1) {
        dist(i)(j) = 0
        queue.enqueue((i, j))
      }
    }
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    while (queue.nonEmpty) {
      val (i, j) = queue.dequeue()
      for ((di, dj) <- dirs) {
        val x = i + di
        val y = j + dj
        if (x >= 0 && x < m && y >= 0 && y < n && dist(x)(y) == -1) {
          dist(x)(y) = dist(i)(j) + 1
          queue.enqueue((x, y))
        }
      }
    }
    dist
  }
}
