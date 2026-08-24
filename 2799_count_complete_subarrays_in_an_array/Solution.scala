// LeetCode 2799 - Count Complete Subarrays in an Array
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

object Solution {
  def countCompleteSubarrays(nums: Array[Int]): Int = {
    val need = nums.toSet.size
    var ans = 0
    val n = nums.length
    var i = 0
    while (i < n) {
      val seen = scala.collection.mutable.HashSet.empty[Int]
      var j = i
      var stop = false
      while (j < n && !stop) {
        seen += nums(j)
        if (seen.size == need) {
          ans += n - j
          stop = true
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
