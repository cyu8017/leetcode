// LeetCode 0587 - Erect the Fence
// https://leetcode.com/problems/erect-the-fence/

import scala.collection.mutable

object Solution {
  def outerTrees(trees: Array[Array[Int]]): Array[Array[Int]] = {
    val points = trees.sortBy(p => (p(0), p(1)))
    if (points.length <= 1) return points
    val lower = build(points)
    val reversed = points.reverse
    val upper = build(reversed)
    val seen = mutable.Set.empty[String]
    val unique = mutable.ArrayBuffer.empty[Array[Int]]
    var i = 0
    while (i + 1 < lower.size) { addUnique(unique, seen, lower(i)); i += 1 }
    i = 0
    while (i + 1 < upper.size) { addUnique(unique, seen, upper(i)); i += 1 }
    unique.toArray
  }

  private def build(ordered: Array[Array[Int]]): mutable.ArrayBuffer[Array[Int]] = {
    val hull = mutable.ArrayBuffer.empty[Array[Int]]
    ordered.foreach { point =>
      while (hull.size >= 2 && cross(hull(hull.size - 2), hull(hull.size - 1), point) < 0) {
        hull.remove(hull.size - 1)
      }
      hull += point
    }
    hull
  }

  private def cross(o: Array[Int], a: Array[Int], b: Array[Int]): Long =
    1L * (a(0) - o(0)) * (b(1) - o(1)) - 1L * (a(1) - o(1)) * (b(0) - o(0))

  private def addUnique(unique: mutable.ArrayBuffer[Array[Int]], seen: mutable.Set[String], point: Array[Int]): Unit = {
    val key = s"${point(0)},${point(1)}"
    if (seen.add(key)) unique += point
  }
}
