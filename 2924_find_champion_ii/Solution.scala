// LeetCode 2924 - Find Champion II
// https://leetcode.com/problems/find-champion-ii/

object Solution {
  def findChampion(n: Int, edges: Array[Array[Int]]): Int = {
    val indeg = Array.fill(n)(0)
    edges.foreach(e => indeg(e(1)) += 1)
    var ans = -1
    for (i <- 0 until n if indeg(i) == 0) {
      if (ans != -1) return -1
      ans = i
    }
    ans
  }
}
