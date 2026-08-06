// LeetCode 1526 - Minimum Number of Increments on Subarrays to Form a Target Array
// https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

object Solution {
  def minNumberOperations(target: Array[Int]): Int = {
    var ans = target(0)
    for (i <- 1 until target.length) ans += math.max(0, target(i) - target(i - 1))
    ans
  }
}
