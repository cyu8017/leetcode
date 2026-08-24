// LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
// https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

object Solution {
  def minimumSeconds(land: List[List[String]]): Int = {
    val m = land.length
    val n = land.head.length
    val INF = 1 << 30
    val water = Array.fill(m, n)(INF)
    val wq = scala.collection.mutable.Queue.empty[(Int, Int)]
    var sx = 0
    var sy = 0
    var dx = 0
    var dy = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val cell = land(i)(j)
        if (cell == "*") {
          water(i)(j) = 0
          wq.enqueue((i, j))
        } else if (cell == "S") {
          sx = i
          sy = j
        } else if (cell == "D") {
          dx = i
          dy = j
        }
        j += 1
      }
      i += 1
    }
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    while (wq.nonEmpty) {
      val (x, y) = wq.dequeue()
      dirs.foreach { case (ddx, ddy) =>
        val ni = x + ddx
        val nj = y + ddy
        if (ni >= 0 && nj >= 0 && ni < m && nj < n) {
          val cell = land(ni)(nj)
          if (cell != "X" && cell != "D" && water(ni)(nj) > water(x)(y) + 1) {
            water(ni)(nj) = water(x)(y) + 1
            wq.enqueue((ni, nj))
          }
        }
      }
    }
    val dist = Array.fill(m, n)(-1)
    val q = scala.collection.mutable.Queue.empty[(Int, Int)]
    q.enqueue((sx, sy))
    dist(sx)(sy) = 0
    while (q.nonEmpty) {
      val (x, y) = q.dequeue()
      if (x == dx && y == dy) return dist(x)(y)
      dirs.foreach { case (ddx, ddy) =>
        val ni = x + ddx
        val nj = y + ddy
        if (ni >= 0 && nj >= 0 && ni < m && nj < n && dist(ni)(nj) == -1 && land(ni)(nj) != "X") {
          val nd = dist(x)(y) + 1
          if (land(ni)(nj) == "D" || nd < water(ni)(nj)) {
            dist(ni)(nj) = nd
            q.enqueue((ni, nj))
          }
        }
      }
    }
    -1
  }
}
