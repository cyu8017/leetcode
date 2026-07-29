// LeetCode 1066 - Campus Bikes II
// https://leetcode.com/problems/campus-bikes-ii/

object Solution {
  def assignBikes(workers: Array[Array[Int]], bikes: Array[Array[Int]]): Int = {
    val m = bikes.length
    val memo = scala.collection.mutable.Map.empty[(Int, Int), Int]

    def dp(i: Int, mask: Int): Int = {
      if (i == workers.length) return 0
      memo.getOrElseUpdate((i, mask), {
        var best = Int.MaxValue
        val wx = workers(i)(0)
        val wy = workers(i)(1)
        for (b <- 0 until m if (mask & (1 << b)) == 0) {
          val bx = bikes(b)(0)
          val by = bikes(b)(1)
          val dist = math.abs(wx - bx) + math.abs(wy - by)
          best = math.min(best, dist + dp(i + 1, mask | (1 << b)))
        }
        best
      })
    }

    dp(0, 0)
  }
}
