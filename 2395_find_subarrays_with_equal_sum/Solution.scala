// LeetCode 2395 - Find Subarrays With Equal Sum
// https://leetcode.com/problems/find-subarrays-with-equal-sum/

object Solution {
  def findSubarrays(nums: Array[Int]): Boolean = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var i = 0
    while (i + 1 < nums.length) {
      val s = nums(i) + nums(i + 1)
      if (seen.contains(s)) return true
      seen += s
      i += 1
    }
    false
  }
}
