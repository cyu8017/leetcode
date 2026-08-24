// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

object Solution {
  def sumRemoteness(grid: Array[Array[Int]]): Long = {
    val m = grid.length
    val n = grid(0).length
    val seen = Array.ofDim[Boolean](m, n)
    val dirs = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))
    var total = 0L
    for (i <- 0 until m; j <- 0 until n) if (grid(i)(j) != -1) total += grid(i)(j)
    var ans = 0L
    for (i <- 0 until m; j <- 0 until n) {
      if (grid(i)(j) != -1 && !seen(i)(j)) {
        val q = scala.collection.mutable.Queue(Array(i, j))
        seen(i)(j) = true
        var sum = 0L
        var cnt = 0
        while (q.nonEmpty) {
          val cur = q.dequeue()
          val x = cur(0)
          val y = cur(1)
          sum += grid(x)(y)
          cnt += 1
          dirs.foreach { d =>
            val ni = x + d(0)
            val nj = y + d(1)
            if (ni >= 0 && nj >= 0 && ni < m && nj < n && !seen(ni)(nj) && grid(ni)(nj) != -1) {
              seen(ni)(nj) = true
              q.enqueue(Array(ni, nj))
            }
          }
        }
        ans += (total - sum) * cnt
      }
    }
    ans
  }
}
