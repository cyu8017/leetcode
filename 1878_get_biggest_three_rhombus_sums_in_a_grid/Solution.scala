// LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

import scala.collection.mutable

object Solution {
  def getBiggestThree(grid: Array[Array[Int]]): Array[Int] = {
    val m = grid.length
    val n = grid(0).length
    val s1 = Array.fill(m + 1, n + 2)(0)
    val s2 = Array.fill(m + 1, n + 2)(0)

    for (i <- 1 to m; j <- 1 to n) {
      val value = grid(i - 1)(j - 1)
      s1(i)(j) = s1(i - 1)(j - 1) + value
      s2(i)(j) = s2(i - 1)(j + 1) + value
    }

    val rhombusSums = mutable.Set.empty[Int]
    for (i <- 1 to m; j <- 1 to n) {
      val value = grid(i - 1)(j - 1)
      val limit = math.min(math.min(i - 1, m - i), math.min(j - 1, n - j))
      rhombusSums += value
      for (k <- 1 to limit) {
        val a = s1(i + k)(j) - s1(i)(j - k)
        val b = s1(i)(j + k) - s1(i - k)(j)
        val c = s2(i)(j - k) - s2(i - k)(j)
        val d = s2(i + k)(j) - s2(i)(j + k)
        rhombusSums += a + b + c + d - grid(i + k - 1)(j - 1) + grid(i - k - 1)(j - 1)
      }
    }
    rhombusSums.toArray.sorted.reverse.take(3)
  }
}
