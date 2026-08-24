// LeetCode 3027 - Find the Number of Ways to Place People II
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

object Solution {
  def numberOfPairs(points: Array[Array[Int]]): Int = {
    scala.util.Sorting.stableSort(points, (a: Array[Int], b: Array[Int]) =>
      if (a(0) != b(0)) a(0) < b(0) else a(1) > b(1)
    )
    var ans = 0
    var i = 0
    while (i < points.length) {
      val y1 = points(i)(1)
      var maxY = Int.MinValue
      var j = i + 1
      while (j < points.length) {
        val y2 = points(j)(1)
        if (maxY < y2 && y2 <= y1) {
          maxY = y2
          ans += 1
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
