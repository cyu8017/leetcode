// LeetCode 2497 - Maximum Star Sum of a Graph
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

object Solution {
  def maxStarSum(vals: Array[Int], edges: Array[Array[Int]], k: Int): Int = {
    val n = vals.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    var ans = vals(0)
    var i = 0
    while (i < n) {
      val neigh = scala.collection.mutable.ArrayBuffer.empty[Int]
      g(i).foreach { v => if (vals(v) > 0) neigh += vals(v) }
      val arr = neigh.toArray
      scala.util.Sorting.quickSort(arr)
      var sum = vals(i)
      var j = arr.length - 1
      var taken = 0
      while (j >= 0 && taken < k) {
        sum += arr(j)
        taken += 1
        j -= 1
      }
      if (sum > ans) ans = sum
      i += 1
    }
    ans
  }
}
