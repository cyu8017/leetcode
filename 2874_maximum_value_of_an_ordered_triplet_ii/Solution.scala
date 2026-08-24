// LeetCode 2874 - Maximum Value of an Ordered Triplet II
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

object Solution {
  def maximumTripletValue(nums: Array[Int]): Long = {
    var ans = 0L
    var maxI = 0L
    var maxDiff = 0L
    nums.foreach { v =>
      val value = v.toLong
      if (maxDiff * value > ans) ans = maxDiff * value
      if (maxI - value > maxDiff) maxDiff = maxI - value
      if (value > maxI) maxI = value
    }
    ans
  }
}
