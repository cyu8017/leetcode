// LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

object Solution {
  val DIRS = Array(
    Array(1, 2), Array(1, -2), Array(-1, 2), Array(-1, -2),
    Array(2, 1), Array(2, -1), Array(-2, 1), Array(-2, -1)
  )

  def knightDist(x: Int, y: Int, pts: Array[Array[Int]]): Array[Int] = {
    val np = pts.length
    val ans = Array.fill(np)(-1)
    val vis = Array.ofDim[Boolean](50, 50)
    val q = scala.collection.mutable.Queue[Array[Int]]()
    q.enqueue(Array(x, y, 0))
    vis(x)(y) = true
    val need = scala.collection.mutable.HashMap.empty[Long, scala.collection.mutable.ArrayBuffer[Int]]
    var i = 0
    while (i < np) {
      val key = (pts(i)(0).toLong << 32) | (pts(i)(1) & 0xffffffffL)
      if (!need.contains(key)) need(key) = scala.collection.mutable.ArrayBuffer.empty[Int]
      need(key) += i
      i += 1
    }
    var found = 0
    while (q.nonEmpty && found < np) {
      val cur = q.dequeue()
      val key = (cur(0).toLong << 32) | (cur(1) & 0xffffffffL)
      need.get(key).foreach { idxs =>
        for (ii <- idxs if ans(ii) == -1) {
          ans(ii) = cur(2)
          found += 1
        }
      }
      for (d <- DIRS) {
        val nx = cur(0) + d(0)
        val ny = cur(1) + d(1)
        if (nx >= 0 && ny >= 0 && nx < 50 && ny < 50 && !vis(nx)(ny)) {
          vis(nx)(ny) = true
          q.enqueue(Array(nx, ny, cur(2) + 1))
        }
      }
    }
    ans
  }

  def maxMoves(kx: Int, ky: Int, positions: Array[Array[Int]]): Int = {
    val n = positions.length
    val pts = Array.ofDim[Int](n + 1, 2)
    pts(0)(0) = kx
    pts(0)(1) = ky
    var i = 0
    while (i < n) {
      pts(i + 1)(0) = positions(i)(0)
      pts(i + 1)(1) = positions(i)(1)
      i += 1
    }
    val dist = Array.ofDim[Int](n + 1).map(_ => null.asInstanceOf[Array[Int]])
    i = 0
    while (i <= n) {
      dist(i) = knightDist(pts(i)(0), pts(i)(1), pts)
      i += 1
    }
    val N = 1 << n
    val memo = Array.fill(N, n + 1)(-1)
    def dfs(mask: Int, cur: Int, turn: Int): Int = {
      if (mask == N - 1) return 0
      if (memo(mask)(cur) != -1) return memo(mask)(cur)
      var best = if (turn == 0) -(1 << 30) else (1 << 30)
      var ii = 0
      while (ii < n) {
        if ((mask & (1 << ii)) == 0) {
          val d = dist(cur)(ii + 1)
          val v = d + dfs(mask | (1 << ii), ii + 1, 1 - turn)
          if (turn == 0) { if (v > best) best = v }
          else if (v < best) best = v
        }
        ii += 1
      }
      memo(mask)(cur) = best
      best
    }
    dfs(0, 0, 0)
  }
}
