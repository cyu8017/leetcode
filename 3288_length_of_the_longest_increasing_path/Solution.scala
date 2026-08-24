// LeetCode 3288 - Length of the Longest Increasing Path
// https://leetcode.com/problems/length-of-the-longest-increasing-path/

object Solution {
  private def lis(a: Array[Int]): Int = {
    val tails = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (x <- a) {
      var lo = 0
      var hi = tails.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (tails(mid) < x) lo = mid + 1
        else hi = mid
      }
      if (lo == tails.length) tails += x
      else tails(lo) = x
    }
    tails.length
  }

  def maxPathLength(coordinates: Array[Array[Int]], k: Int): Int = {
    val n = coordinates.length
    val arr = Array.tabulate(n)(i => Array(coordinates(i)(0), coordinates(i)(1), i))
    scala.util.Sorting.stableSort(arr, (a: Array[Int], b: Array[Int]) =>
      if (a(0) == b(0)) a(1) > b(1) else a(0) < b(0)
    )
    val kx = coordinates(k)(0)
    val ky = coordinates(k)(1)
    val left = scala.collection.mutable.ArrayBuffer.empty[Int]
    val right = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (p <- arr) {
      if (p(0) < kx && p(1) < ky) left += p(1)
      if (p(0) > kx && p(1) > ky) right += p(1)
    }
    lis(left.toArray) + 1 + lis(right.toArray)
  }
}
