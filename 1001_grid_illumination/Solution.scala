// LeetCode 1001 - Grid Illumination
// https://leetcode.com/problems/grid-illumination/

import scala.collection.mutable

object Solution {
  def gridIllumination(n: Int, lamps: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val rows = mutable.Map.empty[Int, Int].withDefaultValue(0)
    val cols = mutable.Map.empty[Int, Int].withDefaultValue(0)
    val diag1 = mutable.Map.empty[Int, Int].withDefaultValue(0)
    val diag2 = mutable.Map.empty[Int, Int].withDefaultValue(0)
    val lit = mutable.Set.empty[(Int, Int)]
    for (lamp <- lamps) {
      val r = lamp(0)
      val c = lamp(1)
      if (!lit.contains((r, c))) {
        lit.add((r, c))
        rows(r) += 1
        cols(c) += 1
        diag1(r - c) += 1
        diag2(r + c) += 1
      }
    }
    val ans = Array.ofDim[Int](queries.length)
    for (qi <- queries.indices) {
      val r = queries(qi)(0)
      val c = queries(qi)(1)
      ans(qi) = if (rows(r) > 0 || cols(c) > 0 || diag1(r - c) > 0 || diag2(r + c) > 0) 1 else 0
      for (i <- (r - 1) to (r + 1); j <- (c - 1) to (c + 1)) {
        if (lit.remove((i, j))) {
          rows(i) -= 1
          cols(j) -= 1
          diag1(i - j) -= 1
          diag2(i + j) -= 1
        }
      }
    }
    ans
  }
}
