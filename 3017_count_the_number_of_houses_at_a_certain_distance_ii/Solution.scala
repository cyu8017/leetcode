// LeetCode 3017 - Count the Number of Houses at a Certain Distance II
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

object Solution {
  def countOfPairs(n: Int, x0: Int, y0: Int): Array[Long] = {
    var x = x0
    var y = y0
    if (x > y) { val t = x; x = y; y = t }
    val A = Array.ofDim[Long](n)
    var i = 1
    while (i <= n) {
      A(0) += 2
      A(math.min(i - 1, math.abs(i - y) + x).toInt) -= 1
      A(math.min(n - i, math.abs(i - x) + 1 + (n - y)).toInt) -= 1
      A(math.min(math.abs(i - x), math.abs(y - i) + 1).toInt) += 1
      A(math.min(math.abs(i - x) + 1, math.abs(y - i)).toInt) += 1
      val r = math.max(x - i, 0) + math.max(i - y, 0)
      A((r + (y - x) / 2).toInt) -= 1
      A((r + (y - x + 1) / 2).toInt) -= 1
      i += 1
    }
    i = 1
    while (i < n) { A(i) += A(i - 1); i += 1 }
    A
  }
}
