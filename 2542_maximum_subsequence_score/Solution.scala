// LeetCode 2542 - Maximum Subsequence Score
// https://leetcode.com/problems/maximum-subsequence-score/

object Solution {
  def maxScore(nums1: Array[Int], nums2: Array[Int], k: Int): Long = {
    val n = nums1.length
    val idx = (0 until n).toArray.sortBy(i => -nums2(i))
    val pq = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
    var sum = 0L
    var ans = 0L
    idx.foreach { i =>
      pq.enqueue(nums1(i))
      sum += nums1(i)
      if (pq.size > k) sum -= pq.dequeue()
      if (pq.size == k) {
        val cand = sum * nums2(i)
        if (cand > ans) ans = cand
      }
    }
    ans
  }
}
