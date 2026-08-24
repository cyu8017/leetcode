// LeetCode 3971 - Maximum Total Value
// https://leetcode.com/problems/maximum-total-value/

object Solution {
  def maximumTotalValue(value: Array[Int], decay: Array[Int], m: Long): Int = {
    val mod = 1000000007L
    if (countAtLeast(value, decay, 1) <= m) {
      var sum = 0L
      var i = 0
      while (i < value.length) {
        val terms = (value(i) - 1L) / decay(i) + 1
        sum = (sum + terms * value(i) - decay(i).toLong * terms * (terms - 1) / 2) % mod
        i += 1
      }
      return sum.toInt
    }
    var high = 0L
    for (v <- value) if (v > high) high = v
    var low = 1L
    while (low < high) {
      val mid = (low + high + 1) / 2
      if (countAtLeast(value, decay, mid) >= m) low = mid
      else high = mid - 1
    }
    val threshold = low
    var count = 0L
    var sum = 0L
    var i = 0
    while (i < value.length) {
      if (value(i) >= threshold) {
        val terms = (value(i) - threshold) / decay(i) + 1
        count += terms
        sum = (sum + (terms * value(i) - decay(i).toLong * terms * (terms - 1) / 2) % mod) % mod
      }
      i += 1
    }
    sum = (sum - ((count - m) % mod) * (threshold % mod)) % mod
    if (sum < 0) sum += mod
    sum.toInt
  }

  private def countAtLeast(value: Array[Int], decay: Array[Int], threshold: Long): Long = {
    var count = 0L
    var i = 0
    while (i < value.length) {
      if (value(i) >= threshold) count += (value(i) - threshold) / decay(i) + 1
      i += 1
    }
    count
  }
}
