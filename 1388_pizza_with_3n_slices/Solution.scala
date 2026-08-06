object Solution {
  def maxSizeSlices(slices: Array[Int]): Int = {
    val k = slices.length / 3
    def line(a: Array[Int]): Int = { val dp = Array.fill(a.length + 2, k + 1)(0); for (i <- a.indices; j <- 1 to k) dp(i + 2)(j) = math.max(dp(i + 1)(j), dp(i)(j - 1) + a(i)); dp(a.length + 1)(k) }
    math.max(line(slices.dropRight(1)), line(slices.drop(1)))
  }
}
