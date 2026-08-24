// LeetCode 0909 - Snakes and Ladders
// https://leetcode.com/problems/snakes-and-ladders/

object Solution {
  def snakesAndLadders(board: Array[Array[Int]]): Int = {
    val n = board.length
    val target = n * n
    def pos(square: Int): (Int, Int) = {
      val s = square - 1
      val row = s / n
      val rem = s % n
      val r = n - 1 - row
      val c = if (row % 2 == 0) rem else n - 1 - rem
      (r, c)
    }
    val q = scala.collection.mutable.Queue[Int]()
    val seen = Array.ofDim[Boolean](target + 1)
    q.enqueue(1)
    seen(1) = true
    var moves = 0
    while (q.nonEmpty) {
      val sz = q.size
      var s = 0
      while (s < sz) {
        val cur = q.dequeue()
        if (cur == target) return moves
        val lim = math.min(cur + 6, target)
        var nxt = cur + 1
        while (nxt <= lim) {
          val (r, c) = pos(nxt)
          val dest = if (board(r)(c) != -1) board(r)(c) else nxt
          if (!seen(dest)) {
            seen(dest) = true
            q.enqueue(dest)
          }
          nxt += 1
        }
        s += 1
      }
      moves += 1
    }
    -1
  }
}
