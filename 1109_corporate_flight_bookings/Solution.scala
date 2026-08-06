// LeetCode 1109 - Corporate Flight Bookings
// https://leetcode.com/problems/corporate-flight-bookings/

object Solution {
  def corpFlightBookings(bookings: Array[Array[Int]], n: Int): Array[Int] = {
    val diff = Array.fill(n + 1)(0)
    for (b <- bookings) {
      diff(b(0) - 1) += b(2)
      diff(b(1)) -= b(2)
    }
    val ans = Array.ofDim[Int](n)
    var cur = 0
    for (i <- 0 until n) {
      cur += diff(i)
      ans(i) = cur
    }
    ans
  }
}
