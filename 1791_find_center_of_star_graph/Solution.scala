// LeetCode 1791 - Find Center of Star Graph
// https://leetcode.com/problems/find-center-of-star-graph/

object Solution {
  def findCenter(edges: Array[Array[Int]]): Int = {
    val a = edges(0)(0)
    val b = edges(0)(1)
    val c = edges(1)(0)
    val d = edges(1)(1)
    if (a == c || a == d) a else b
  }
}
