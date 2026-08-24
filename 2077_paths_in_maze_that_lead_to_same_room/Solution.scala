// LeetCode 2077 - Paths in Maze That Lead to Same Room
// https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

object Solution {
  def numberOfPaths(n: Int, corridors: Array[Array[Int]]): Int = {
    val g = Array.fill(n + 1)(scala.collection.mutable.HashSet.empty[Int])
    corridors.foreach { e => g(e(0)) += e(1); g(e(1)) += e(0) }
    var ans = 0
    corridors.foreach { e =>
      val a = e(0)
      val b = e(1)
      g(a).foreach { c => if (g(b).contains(c)) ans += 1 }
    }
    ans / 3
  }
}
