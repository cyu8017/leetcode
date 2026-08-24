// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

object Solution {
  def colorTheArray(n: Int, queries: Array[Array[Int]]): Array[Int] = {
    val colors = new Array[Int](n)
    val ans = new Array[Int](queries.length)
    var same = 0
    var i = 0
    while (i < queries.length) {
      val idx = queries(i)(0)
      val color = queries(i)(1)
      if (colors(idx) != 0) {
        if (idx > 0 && colors(idx) == colors(idx - 1)) same -= 1
        if (idx + 1 < n && colors(idx) == colors(idx + 1)) same -= 1
      }
      colors(idx) = color
      if (idx > 0 && colors(idx) == colors(idx - 1)) same += 1
      if (idx + 1 < n && colors(idx) == colors(idx + 1)) same += 1
      ans(i) = same
      i += 1
    }
    ans
  }
}
