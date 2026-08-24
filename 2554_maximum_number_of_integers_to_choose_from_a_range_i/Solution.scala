// LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

object Solution {
  def maxCount(banned: Array[Int], n: Int, maxSum: Int): Int = {
    val ban = banned.toSet
    var ans = 0
    var sum = 0L
    var i = 1
    while (i <= n) {
      if (!ban.contains(i)) {
        if (sum + i > maxSum) return ans
        sum += i
        ans += 1
      }
      i += 1
    }
    ans
  }
}
