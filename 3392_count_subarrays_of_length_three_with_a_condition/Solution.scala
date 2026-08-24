// LeetCode 3392 - Count Subarrays of Length Three With a Condition
// https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

object Solution {
  def countSubarrays(nums: Array[Int]): Int = {
    var ans = 0
    var i = 0
    while (i + 2 < nums.length) {
      if (nums(i) * 2 + nums(i + 2) * 2 == nums(i + 1)) ans += 1
      i += 1
    }
    ans
  }
}
