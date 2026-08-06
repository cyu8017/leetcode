// LeetCode 1508 - Range Sum of Sorted Subarray Sums
// https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

object Solution {
  def rangeSum(nums: Array[Int], n: Int, left: Int, right: Int): Int = {
    val values = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (i <- 0 until n) {
      var total = 0
      for (j <- i until n) {
        total += nums(j)
        values += total
      }
    }
    val sorted = values.sorted
    (sorted.slice(left - 1, right).map(_.toLong).sum % 1000000007L).toInt
  }
}
