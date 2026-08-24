// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

object Solution {
  def colorRed(n: Int): Array[Array[Int]] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var i = 1
    while (i <= n) {
      ans += Array(i, 1)
      i += 1
    }
    i = n % 2 + 2
    while (i <= n) {
      var j = 2
      while (j <= 2 * (n - i) + 2) {
        ans += Array(i, j)
        j += 1
      }
      i += 2
    }
    ans.toArray
  }
}
