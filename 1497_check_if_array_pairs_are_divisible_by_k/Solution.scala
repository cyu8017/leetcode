object Solution {
  def canArrange(arr: Array[Int], k: Int): Boolean = {
    val count = Array.fill(k)(0)
    for (value <- arr) count(((value % k) + k) % k) += 1
    if (count(0) % 2 != 0) return false
    for (remainder <- 1 to k / 2) {
      if (remainder == k - remainder) {
        if (count(remainder) % 2 != 0) return false
      } else if (count(remainder) != count(k - remainder)) return false
    }
    true
  }
}
