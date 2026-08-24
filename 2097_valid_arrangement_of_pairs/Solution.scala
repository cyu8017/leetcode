// LeetCode 2097 - Valid Arrangement of Pairs
// https://leetcode.com/problems/valid-arrangement-of-pairs/

object Solution {
  def validArrangement(pairs: Array[Array[Int]]): Array[Array[Int]] = {
    val g = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    val indeg = scala.collection.mutable.Map.empty[Int, Int]
    val outdeg = scala.collection.mutable.Map.empty[Int, Int]
    pairs.foreach { p =>
      val u = p(0)
      val v = p(1)
      g.getOrElseUpdate(u, scala.collection.mutable.ArrayBuffer.empty[Int]) += v
      outdeg(u) = outdeg.getOrElse(u, 0) + 1
      indeg(v) = indeg.getOrElse(v, 0) + 1
    }
    var start = pairs(0)(0)
    outdeg.foreach { case (k, v) =>
      if (v - indeg.getOrElse(k, 0) == 1) start = k
    }
    val path = scala.collection.mutable.ArrayBuffer.empty[Int]
    def dfs(u: Int): Unit = {
      val nbrs = g.getOrElseUpdate(u, scala.collection.mutable.ArrayBuffer.empty[Int])
      while (nbrs.nonEmpty) {
        val v = nbrs.remove(nbrs.length - 1)
        dfs(v)
      }
      path += u
    }
    dfs(start)
    val rev = path.reverse
    Array.tabulate(rev.length - 1)(i => Array(rev(i), rev(i + 1)))
  }
}
