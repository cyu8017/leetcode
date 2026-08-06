object Solution {
  def ways(pizza: Array[String], k: Int): Int = {
    val mod = 1000000007L; val rows = pizza.length; val cols = pizza(0).length
    val apples = Array.fill(rows + 1, cols + 1)(0)
    for (r <- (rows - 1) to 0 by -1; c <- (cols - 1) to 0 by -1)
      apples(r)(c) = (if (pizza(r)(c) == 'A') 1 else 0) + apples(r + 1)(c) + apples(r)(c + 1) - apples(r + 1)(c + 1)
    var dp = Array.tabulate(rows, cols)((r, c) => if (apples(r)(c) > 0) 1L else 0L)
    for (_ <- 1 until k) {
      val next = Array.fill[Long](rows, cols)(0)
      for (r <- 0 until rows; c <- 0 until cols) {
        for (nr <- r + 1 until rows if apples(r)(c) > apples(nr)(c)) next(r)(c) = (next(r)(c) + dp(nr)(c)) % mod
        for (nc <- c + 1 until cols if apples(r)(c) > apples(r)(nc)) next(r)(c) = (next(r)(c) + dp(r)(nc)) % mod
      }
      dp = next
    }
    dp(0)(0).toInt
  }
}
