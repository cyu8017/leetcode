// LeetCode 0593 - Valid Square
// https://leetcode.com/problems/valid-square/

object Solution {
  def validSquare(p1: Array[Int], p2: Array[Int], p3: Array[Int], p4: Array[Int]): Boolean = {
    val points = Array(p1, p2, p3, p4)
    val distances = Array.fill(6)(0)
    var idx = 0
    var i = 0
    while (i < 4) {
      var j = i + 1
      while (j < 4) {
        distances(idx) = distSq(points(i), points(j))
        idx += 1
        j += 1
      }
      i += 1
    }
    scala.util.Sorting.quickSort(distances)
    distances(0) > 0 && distances(0) == distances(1) && distances(1) == distances(2) &&
      distances(2) == distances(3) && distances(4) == distances(5) &&
      distances(4) == 2 * distances(0)
  }

  private def distSq(a: Array[Int], b: Array[Int]): Int = {
    val dx = a(0) - b(0)
    val dy = a(1) - b(1)
    dx * dx + dy * dy
  }
}
