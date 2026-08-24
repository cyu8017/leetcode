// LeetCode 2588 - Count the Number of Beautiful Subarrays
// https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

object Solution {
  def beautifulSubarrays(nums: Array[Int]): Long = {
    val freq = scala.collection.mutable.Map(0 -> 1)
    var xorv = 0
    var ans = 0L
    nums.foreach { x =>
      xorv ^= x
      ans += freq.getOrElse(xorv, 0)
      freq(xorv) = freq.getOrElse(xorv, 0) + 1
    }
    ans
  }
}
