// LeetCode 1931 - Painting a Grid With Three Different Colors
// https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

object Solution {
  def colorTheGrid(m: Int, n: Int): Int = {
    val MOD = 1000000007

    def validColumn(mask: Int): Boolean = {
      var prev = -1
      var x = mask
      for (_ <- 0 until m) {
        val c = x % 3
        if (c == prev) return false
        prev = c
        x /= 3
      }
      true
    }

    def getColors(mask: Int): Array[Int] = {
      val cols = Array.ofDim[Int](m)
      var x = mask
      for (i <- 0 until m) {
        cols(i) = x % 3
        x /= 3
      }
      cols
    }

    val states = (0 until math.pow(3, m).toInt).filter(validColumn).toArray
    val compat = states.map { a =>
      val ca = getColors(a)
      states.filter { b =>
        val cb = getColors(b)
        ca.indices.forall(i => ca(i) != cb(i))
      }.toArray
    }.zip(states).map { case (arr, s) => s -> arr }.toMap

    val memo = scala.collection.mutable.Map.empty[(Int, Int), Int]
    def dp(col: Int, prev: Int): Int = {
      if (col == n) return 1
      memo.getOrElseUpdate((col, prev), {
        var total = 0
        val curs = if (prev == -1) states else compat(prev)
        for (cur <- curs) total = (total + dp(col + 1, cur)) % MOD
        total
      })
    }
    dp(0, -1)
  }
}
