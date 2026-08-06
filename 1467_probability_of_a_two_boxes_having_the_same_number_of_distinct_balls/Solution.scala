object Solution {
  def getProbability(balls: Array[Int]): Double = {
    val half = balls.sum / 2
    val maxBall = balls.max
    val comb = Array.ofDim[Long](maxBall + 1, maxBall + 1)
    for (i <- 0 to maxBall) {
      comb(i)(0) = 1
      for (j <- 1 to i) comb(i)(j) = comb(i - 1)(j - 1) + comb(i - 1)(j)
    }
    var good = 0.0
    var total = 0.0
    def dfs(i: Int, left: Int, distinctDelta: Int, ways: Double): Unit = {
      if (i == balls.length) {
        if (left == half) {
          total += ways
          if (distinctDelta == 0) good += ways
        }
      } else {
        for (x <- 0 to balls(i) if left + x <= half) {
          val delta = (if (x > 0) 1 else 0) - (if (x < balls(i)) 1 else 0)
          dfs(i + 1, left + x, distinctDelta + delta, ways * comb(balls(i))(x))
        }
      }
    }
    dfs(0, 0, 0, 1.0)
    good / total
  }
}
