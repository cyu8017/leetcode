// LeetCode 1094 - Car Pooling
// https://leetcode.com/problems/car-pooling/

object Solution {
  def carPooling(trips: Array[Array[Int]], capacity: Int): Boolean = {
    val diff = Array.fill(1001)(0)
    for (t <- trips) {
      diff(t(1)) += t(0)
      diff(t(2)) -= t(0)
    }
    var cur = 0
    for (x <- diff) {
      cur += x
      if (cur > capacity) return false
    }
    true
  }
}
