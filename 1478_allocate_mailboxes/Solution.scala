object Solution {
  def minDistance(houses: Array[Int], k: Int): Int = {
    val sorted = houses.sorted
    val n = sorted.length
    val cost = Array.ofDim[Int](n, n)
    for (i <- 0 until n; j <- i until n) {
      val median = sorted((i + j) / 2)
      cost(i)(j) = (i to j).map(t => math.abs(sorted(t) - median)).sum
    }
    val inf = Long.MaxValue / 4
    var dp = Array.tabulate(n + 1)(i => if (i == 0) 0L else inf)
    for (_ <- 0 until k) {
      val next = Array.fill(n + 1)(inf)
      next(0) = 0L
      for (j <- 1 to n; i <- 0 until j) next(j) = math.min(next(j), dp(i) + cost(i)(j - 1))
      dp = next
    }
    dp(n).toInt
  }
}
