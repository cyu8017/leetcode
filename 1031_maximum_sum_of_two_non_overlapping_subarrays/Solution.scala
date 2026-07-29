// LeetCode 1031 - Maximum Sum of Two Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

object Solution {
  def maxSumTwoNoOverlap(nums: Array[Int], firstLen: Int, secondLen: Int): Int = {
    val prefix = Array.ofDim[Int](nums.length + 1)
    for (i <- nums.indices) prefix(i + 1) = prefix(i) + nums(i)
    def best(a: Int, b: Int): Int = {
      var bestA = 0
      var ans = 0
      for (i <- (a + b) until prefix.length) {
        bestA = math.max(bestA, prefix(i - b) - prefix(i - b - a))
        ans = math.max(ans, bestA + prefix(i) - prefix(i - b))
      }
      ans
    }
    math.max(best(firstLen, secondLen), best(secondLen, firstLen))
  }
}
