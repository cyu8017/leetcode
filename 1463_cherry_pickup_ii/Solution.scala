object Solution {
  def cherryPickup(grid: Array[Array[Int]]): Int = {
    val n = grid(0).length
    var dp = Map((0, n - 1) -> (grid(0)(0) + (if (n > 1) grid(0)(n - 1) else 0)))
    for (r <- 1 until grid.length) {
      var next = Map.empty[(Int, Int), Int]
      for (((a, b), score) <- dp; na <- a - 1 to a + 1; nb <- b - 1 to b + 1
           if na >= 0 && na < n && nb >= 0 && nb < n) {
        val value = score + grid(r)(na) + (if (na != nb) grid(r)(nb) else 0)
        next = next.updated((na, nb), math.max(next.getOrElse((na, nb), -1), value))
      }
      dp = next
    }
    dp.values.max
  }
}
