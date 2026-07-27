// LeetCode 1632 - Rank Transform of a Matrix
// https://leetcode.com/problems/rank-transform-of-a-matrix/

import scala.collection.mutable

object Solution {
  def matrixRankTransform(matrix: Array[Array[Int]]): Array[Array[Int]] = {
    val m = matrix.length
    val n = matrix(0).length
    val groups = mutable.TreeMap.empty[Int, mutable.ArrayBuffer[(Int, Int)]]
    for (i <- 0 until m; j <- 0 until n) {
      groups.getOrElseUpdate(matrix(i)(j), mutable.ArrayBuffer.empty) += ((i, j))
    }
    val rank = Array.fill(m + n)(0)
    val ans = Array.ofDim[Int](m, n)
    for ((_, cells) <- groups) {
      val parent = mutable.Map.empty[Int, Int]
      def find(x: Int): Int = {
        if (!parent.contains(x)) parent(x) = x
        if (parent(x) != x) parent(x) = find(parent(x))
        parent(x)
      }
      for ((i, j) <- cells) {
        val a = find(i)
        val b = find(m + j)
        parent(a) = b
      }
      val best = mutable.Map.empty[Int, Int].withDefaultValue(0)
      for ((i, j) <- cells) {
        val root = find(i)
        best(root) = math.max(best(root), math.max(rank(i), rank(m + j)))
      }
      for ((i, j) <- cells) {
        val r = best(find(i)) + 1
        ans(i)(j) = r
      }
      for ((i, j) <- cells) {
        rank(i) = math.max(rank(i), ans(i)(j))
        rank(m + j) = math.max(rank(m + j), ans(i)(j))
      }
    }
    ans
  }
}
