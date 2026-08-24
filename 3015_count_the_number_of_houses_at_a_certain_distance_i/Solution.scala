// LeetCode 3015 - Count the Number of Houses at a Certain Distance I
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

object Solution {
  def countOfPairs(n: Int, x0: Int, y0: Int): Array[Int] = {
    val ans = Array.ofDim[Int](n)
    val x = x0 - 1
    val y = y0 - 1
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        val a = j - i
        val b = math.abs(x - i) + math.abs(y - j) + 1
        val c = math.abs(x - j) + math.abs(y - i) + 1
        ans(math.min(a, math.min(b, c)) - 1) += 2
        j += 1
      }
      i += 1
    }
    ans
  }
}
