// LeetCode 2009 - Minimum Number of Operations to Make Array Continuous
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    val n = nums.length
    val uniq = nums.distinct.sorted
    var ans = n
    var j = 0
    var i = 0
    while (i < uniq.length) {
      while (j < uniq.length && uniq(j) - uniq(i) + 1 <= n) j += 1
      ans = math.min(ans, n - (j - i))
      i += 1
    }
    ans
  }
}
