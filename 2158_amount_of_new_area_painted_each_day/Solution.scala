// LeetCode 2158 - Amount of New Area Painted Each Day
// https://leetcode.com/problems/amount-of-new-area-painted-each-day/

object Solution {
  def amountPainted(paint: Array[Array[Int]]): Array[Int] = {
    val ans = Array.fill(paint.length)(0)
    val line = Array.fill(50001)(0)
    var i = 0
    while (i < paint.length) {
      val start = paint(i)(0)
      val end = paint(i)(1)
      var j = start
      while (j < end) {
        if (line(j) == 0) {
          ans(i) += 1
          line(j) = end
          j += 1
        } else {
          val next = line(j)
          line(j) = math.max(end, next)
          j = next
        }
      }
      i += 1
    }
    ans
  }
}
