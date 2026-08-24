// LeetCode 2282 - Number of People That Can Be Seen in a Grid
// https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

object Solution {
  def seePeople(heights: Array[Array[Int]]): Array[Array[Int]] = {
    val m = heights.length
    val n = heights(0).length
    val ans = Array.ofDim[Int](m, n)
    var i = 0
    while (i < m) {
      val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
      var j = n - 1
      while (j >= 0) {
        var cnt = 0
        while (stack.nonEmpty && heights(i)(stack.last) < heights(i)(j)) {
          stack.remove(stack.length - 1)
          cnt += 1
        }
        if (stack.nonEmpty) cnt += 1
        ans(i)(j) += cnt
        while (stack.nonEmpty && heights(i)(stack.last) == heights(i)(j)) stack.remove(stack.length - 1)
        stack += j
        j -= 1
      }
      i += 1
    }
    var j = 0
    while (j < n) {
      val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
      i = m - 1
      while (i >= 0) {
        var cnt = 0
        while (stack.nonEmpty && heights(stack.last)(j) < heights(i)(j)) {
          stack.remove(stack.length - 1)
          cnt += 1
        }
        if (stack.nonEmpty) cnt += 1
        ans(i)(j) += cnt
        while (stack.nonEmpty && heights(stack.last)(j) == heights(i)(j)) stack.remove(stack.length - 1)
        stack += i
        i -= 1
      }
      j += 1
    }
    ans
  }
}
