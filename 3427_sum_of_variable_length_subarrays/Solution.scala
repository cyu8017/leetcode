// LeetCode 3427 - Sum of Variable Length Subarrays
// https://leetcode.com/problems/sum-of-variable-length-subarrays/

object Solution {
  def subarraySum(nums: Array[Int]): Int = {
    val n = nums.length
    val pref = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + nums(i)
      i += 1
    }
    var ans = 0
    i = 0
    while (i < n) {
      var start = i - nums(i)
      if (start < 0) start = 0
      ans += pref(i + 1) - pref(start)
      i += 1
    }
    ans
  }
}
