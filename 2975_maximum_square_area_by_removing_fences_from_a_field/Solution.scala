// LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

object Solution {
  private def gaps(fences: Array[Int], bound: Int): Set[Int] = {
    val list = scala.collection.mutable.ArrayBuffer[Int](1)
    for (f <- fences) list += f
    list += bound
    val sorted = list.sorted
    val gs = scala.collection.mutable.HashSet[Int]()
    var i = 0
    while (i < sorted.length) {
      var j = i + 1
      while (j < sorted.length) {
        gs += sorted(j) - sorted(i)
        j += 1
      }
      i += 1
    }
    gs.toSet
  }

  def maximizeSquareArea(m: Int, n: Int, hFences: Array[Int], vFences: Array[Int]): Int = {
    val mod = 1000000007
    val hg = gaps(hFences, m)
    val vg = gaps(vFences, n)
    var best = -1L
    for (g <- hg) if (vg.contains(g) && g > best) best = g
    if (best < 0) -1 else ((best * best) % mod).toInt
  }
}
