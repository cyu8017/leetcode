// LeetCode 1042 - Flower Planting With No Adjacent
// https://leetcode.com/problems/flower-planting-with-no-adjacent/

object Solution {
  def gardenNoAdj(n: Int, paths: Array[Array[Int]]): Array[Int] = {
    val graph = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (p <- paths) {
      graph(p(0)) += p(1)
      graph(p(1)) += p(0)
    }
    val ans = Array.fill(n + 1)(0)
    for (garden <- 1 to n) {
      val used = graph(garden).map(ans).toSet
      ans(garden) = (1 to 4).find(!used.contains(_)).get
    }
    ans.slice(1, n + 1)
  }
}
