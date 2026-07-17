// LeetCode 1743 - Restore the Array From Adjacent Pairs
// https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

import scala.collection.mutable

object Solution {
  def restoreArray(adjacentPairs: Array[Array[Int]]): Array[Int] = {
    val graph = mutable.Map.empty[Int, mutable.ListBuffer[Int]]
    for (pair <- adjacentPairs) {
      graph.getOrElseUpdate(pair(0), mutable.ListBuffer.empty[Int]) += pair(1)
      graph.getOrElseUpdate(pair(1), mutable.ListBuffer.empty[Int]) += pair(0)
    }
    var start = 0
    var found = false
    for (pair <- adjacentPairs if !found) {
      if (graph(pair(0)).size == 1) {
        start = pair(0)
        found = true
      } else if (graph(pair(1)).size == 1) {
        start = pair(1)
        found = true
      }
    }
    val n = graph.size
    val ans = new Array[Int](n)
    ans(0) = start
    var prev: Option[Int] = None
    for (i <- 1 until n) {
      val cur = ans(i - 1)
      val neighbors = graph(cur)
      ans(i) = if (!prev.contains(neighbors.head)) neighbors.head else neighbors(1)
      prev = Some(cur)
    }
    ans
  }
}
