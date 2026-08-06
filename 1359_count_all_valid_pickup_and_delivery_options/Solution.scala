object Solution {
  def countOrders(n: Int): Int = {
    val mod = 1000000007L
    (1 to n).foldLeft(1L)((answer, i) => answer * i % mod * (2L * i - 1) % mod).toInt
  }
}
