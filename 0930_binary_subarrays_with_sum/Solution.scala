// LeetCode 0930 - Binary Subarrays With Sum
// https://leetcode.com/problems/binary-subarrays-with-sum/

object Solution {
  def numSubarraysWithSum(nums: Array[Int], goal: Int): Int = {
    val count = scala.collection.mutable.Map(0 -> 1)
    var prefix = 0
    var ans = 0
    nums.foreach { x =>
      prefix += x
      ans += count.getOrElse(prefix - goal, 0)
      count(prefix) = count.getOrElse(prefix, 0) + 1
    }
    ans
  }
}
