// LeetCode 2343 - Query Kth Smallest Trimmed Number
// https://leetcode.com/problems/query-kth-smallest-trimmed-number/

object Solution {
  def smallestTrimmedNumbers(nums: Array[String], queries: Array[Array[Int]]): Array[Int] = {
    val n = nums.length
    val m = queries.length
    val ans = Array.fill(m)(0)
    var qi = 0
    while (qi < m) {
      val k = queries(qi)(0)
      val trim = queries(qi)(1)
      val arr = Array.tabulate(n) { i =>
        val s = nums(i)
        (s.substring(s.length - trim), i)
      }
      scala.util.Sorting.stableSort(arr, (a: (String, Int), b: (String, Int)) => {
        val c = a._1.compareTo(b._1)
        if (c != 0) c < 0 else a._2 < b._2
      })
      ans(qi) = arr(k - 1)._2
      qi += 1
    }
    ans
  }
}
