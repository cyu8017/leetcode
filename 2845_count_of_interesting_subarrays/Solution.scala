// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

object Solution {
  def countInterestingSubarrays(nums: Array[Int], modulo: Int, k: Int): Long = {
    val freq = scala.collection.mutable.Map(0 -> 1)
    var ans = 0L
    var pref = 0
    nums.foreach { v =>
      if (v % modulo == k) pref += 1
      var need = (pref - k) % modulo
      if (need < 0) need += modulo
      ans += freq.getOrElse(need, 0)
      val key = pref % modulo
      freq(key) = freq.getOrElse(key, 0) + 1
    }
    ans
  }
}
