object Solution {
  def kthFactor(n: Int, k: Int): Int = {
    var remaining = k
    for (factor <- 1 to n if n % factor == 0) {
      remaining -= 1
      if (remaining == 0) return factor
    }
    -1
  }
}
