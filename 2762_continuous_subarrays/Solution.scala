// LeetCode 2762 - Continuous Subarrays
// https://leetcode.com/problems/continuous-subarrays/

object Solution {
  def continuousSubarrays(nums: Array[Int]): Long = {
    var ans = 0L
    var left = 0
    val freq = scala.collection.mutable.TreeMap.empty[Int, Int]
    var right = 0
    while (right < nums.length) {
      freq(nums(right)) = freq.getOrElse(nums(right), 0) + 1
      while (freq.lastKey - freq.firstKey > 2) {
        val v = nums(left)
        left += 1
        val c = freq(v) - 1
        if (c == 0) freq.remove(v)
        else freq(v) = c
      }
      ans += right - left + 1
      right += 1
    }
    ans
  }
}
