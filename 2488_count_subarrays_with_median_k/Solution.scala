// LeetCode 2488 - Count Subarrays With Median K
// https://leetcode.com/problems/count-subarrays-with-median-k/

object Solution {
  def countSubarrays(nums: Array[Int], k: Int): Int = {
    var pos = 0
    var i = 0
    while (i < nums.length) {
      if (nums(i) == k) { pos = i; i = nums.length }
      else i += 1
    }
    val bal = scala.collection.mutable.Map[Int, Int](0 -> 1)
    var cur = 0
    i = pos - 1
    while (i >= 0) {
      cur += (if (nums(i) < k) -1 else 1)
      bal(cur) = bal.getOrElse(cur, 0) + 1
      i -= 1
    }
    var ans = bal.getOrElse(0, 0) + bal.getOrElse(1, 0)
    cur = 0
    i = pos + 1
    while (i < nums.length) {
      cur += (if (nums(i) < k) -1 else 1)
      ans += bal.getOrElse(-cur, 0) + bal.getOrElse(1 - cur, 0)
      i += 1
    }
    ans
  }
}
