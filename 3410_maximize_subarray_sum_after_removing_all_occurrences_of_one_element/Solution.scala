// LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

object Solution {
  private def kadane(a: Seq[Int]): Long = {
    var best = -(1L << 62)
    var cur = 0L
    a.foreach { x =>
      cur += x
      if (cur > best) best = cur
      if (cur < 0) cur = 0
    }
    var allNeg = true
    var mx = a.head
    a.foreach { x =>
      if (x > mx) mx = x
      if (x >= 0) allNeg = false
    }
    if (allNeg) mx else best
  }

  def maxSubarraySum(nums: Array[Int]): Long = {
    var ans = kadane(nums)
    val uniq = scala.collection.mutable.Set.empty[Int]
    nums.foreach { x => if (x < 0) uniq += x }
    uniq.foreach { v =>
      val b = nums.filter(_ != v)
      if (b.nonEmpty) {
        val cand = kadane(b)
        if (cand > ans) ans = cand
      }
    }
    ans
  }
}
