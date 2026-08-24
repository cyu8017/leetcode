// LeetCode 2056 - Number of Valid Move Combinations On Chessboard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

object Solution {
  private case class Move(dr: Int, dc: Int, steps: Int)

  def countCombinations(pieces: Array[String], positions: Array[Array[Int]]): Int = {
    val dirs = Map(
      "rook" -> Array((1, 0), (-1, 0), (0, 1), (0, -1)),
      "bishop" -> Array((1, 1), (1, -1), (-1, 1), (-1, -1)),
      "queen" -> Array((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
    )
    val n = pieces.length
    val allMoves = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Move])
    var i = 0
    while (i < n) {
      allMoves(i) += Move(0, 0, 0)
      val r = positions(i)(0)
      val c = positions(i)(1)
      dirs(pieces(i)).foreach { case (dr, dc) =>
        var nr = r + dr
        var nc = c + dc
        var step = 1
        while (nr >= 1 && nr <= 8 && nc >= 1 && nc <= 8) {
          allMoves(i) += Move(dr, dc, step)
          nr += dr
          nc += dc
          step += 1
        }
      }
      i += 1
    }
    val chosen = Array.ofDim[Move](n)
    var ans = 0
    def okCombo(end: Int): Boolean = {
      var maxT = 0
      var t0 = 0
      while (t0 <= end) { maxT = math.max(maxT, chosen(t0).steps); t0 += 1 }
      var t = 1
      while (t <= maxT) {
        val seen = scala.collection.mutable.HashSet.empty[Long]
        var pi = 0
        while (pi <= end) {
          val m = chosen(pi)
          val (pr, pc) =
            if (m.steps == 0) (positions(pi)(0), positions(pi)(1))
            else {
              val use = math.min(t, m.steps)
              (positions(pi)(0) + m.dr * use, positions(pi)(1) + m.dc * use)
            }
          val key = (pr.toLong << 32) ^ (pc.toLong & 0xffffffffL)
          if (!seen.add(key)) return false
          pi += 1
        }
        t += 1
      }
      true
    }
    def dfs(idx: Int): Unit = {
      if (idx == n) { ans += 1; return }
      allMoves(idx).foreach { m =>
        chosen(idx) = m
        if (okCombo(idx)) dfs(idx + 1)
      }
    }
    dfs(0)
    ans
  }
}
