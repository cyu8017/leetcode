// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

object Solution {
  def maxSum(nums: Array[Int], m: Int, k: Int): Long = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var sum = 0L
    var ans = 0L
    for (i <- nums.indices) {
      freq(nums(i)) = freq.getOrElse(nums(i), 0) + 1
      sum += nums(i)
      if (i >= k) {
        val out = nums(i - k)
        sum -= out
        val c = freq(out) - 1
        if (c == 0) freq.remove(out) else freq(out) = c
      }
      if (i >= k - 1 && freq.size >= m) ans = math.max(ans, sum)
    }
    ans
  }
}
