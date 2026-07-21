// LeetCode 1885 - Count Pairs in Two Arrays
// https://leetcode.com/problems/count-pairs-in-two-arrays/

object Solution {
  def countPairs(nums1: Array[Int], nums2: Array[Int]): Long = {
    val diff = nums1.zip(nums2).map { case (a, b) => a - b }.sorted
    var answer = 0L
    val n = diff.length
    for (i <- 0 until n) {
      val target = -diff(i)
      var lo = i + 1
      var hi = n
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (diff(mid) <= target) lo = mid + 1
        else hi = mid
      }
      answer += n - lo
    }
    answer
  }
}
