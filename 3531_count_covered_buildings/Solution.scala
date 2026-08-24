// LeetCode 3531 - Count Covered Buildings
// https://leetcode.com/problems/count-covered-buildings/

object Solution {
  def countCoveredBuildings(n: Int, buildings: Array[Array[Int]]): Int = {
    val g1 = scala.collection.mutable.HashMap.empty[Int, java.util.ArrayList[Integer]]
    val g2 = scala.collection.mutable.HashMap.empty[Int, java.util.ArrayList[Integer]]
    for (b <- buildings) {
      if (!g1.contains(b(0))) g1(b(0)) = new java.util.ArrayList[Integer]()
      if (!g2.contains(b(1))) g2(b(1)) = new java.util.ArrayList[Integer]()
      g1(b(0)).add(b(1))
      g2(b(1)).add(b(0))
    }
    for (list <- g1.values) java.util.Collections.sort(list)
    for (list <- g2.values) java.util.Collections.sort(list)
    var ans = 0
    for (b <- buildings) {
      val x = b(0); val y = b(1)
      val l1 = g1(x)
      val l2 = g2(y)
      if (l2.get(0) < x && x < l2.get(l2.size() - 1) && l1.get(0) < y && y < l1.get(l1.size() - 1)) ans += 1
    }
    ans
  }
}
