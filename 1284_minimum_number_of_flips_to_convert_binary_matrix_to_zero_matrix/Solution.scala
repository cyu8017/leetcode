// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

object Solution {
  def minFlips(mat: Array[Array[Int]]): Int = {
    val m = mat.length
    val n = mat(0).length
    var start = 0
    for (r <- 0 until m; c <- 0 until n if mat(r)(c) == 1) start |= 1 << (r * n + c)
    val masks = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (r <- 0 until m; c <- 0 until n) {
      var mask = 0
      for ((dr, dc) <- Seq((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1))) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < m && nc >= 0 && nc < n) mask ^= 1 << (nr * n + nc)
      }
      masks += mask
    }
    val q = scala.collection.mutable.Queue((start, 0))
    val seen = scala.collection.mutable.Set(start)
    while (q.nonEmpty) {
      val (state, distance) = q.dequeue()
      if (state == 0) return distance
      for (mask <- masks) {
        val nxt = state ^ mask
        if (!seen.contains(nxt)) {
          seen += nxt
          q.enqueue((nxt, distance + 1))
        }
      }
    }
    -1
  }
}
