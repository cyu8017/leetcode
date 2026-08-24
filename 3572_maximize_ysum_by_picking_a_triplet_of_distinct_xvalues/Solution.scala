// LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
// https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

object Solution {
  def maxSumDistinctTriplet(x: Array[Int], y: Array[Int]): Int = {
    val n = x.length
    val arr = Array.ofDim[Int](n, 2)
    var i = 0
    while (i < n) { arr(i) = Array(x(i), y(i)); i += 1 }
    java.util.Arrays.sort(arr, (a: Array[Int], b: Array[Int]) => Integer.compare(b(1), a(1)))
    var ans = 0
    val vis = scala.collection.mutable.HashSet.empty[Int]
    i = 0
    while (i < n) {
      val a = arr(i)(0)
      val b = arr(i)(1)
      if (!vis.contains(a)) {
        vis.add(a)
        ans += b
        if (vis.size == 3) return ans
      }
      i += 1
    }
    -1
  }
}
