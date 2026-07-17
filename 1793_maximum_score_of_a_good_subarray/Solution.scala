// LeetCode 1793 - Maximum Score of a Good Subarray
// https://leetcode.com/problems/maximum-score-of-a-good-subarray/

object Solution {
  def maximumScore(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    var ans = 0L
    for (i <- 0 to n) {
      while (stack.nonEmpty && (i == n || nums(i) < nums(stack.last))) {
        val mid = stack.remove(stack.length - 1)
        val left = if (stack.nonEmpty) stack.last + 1 else 0
        val right = i - 1
        if (left <= k && k <= right) {
          ans = math.max(ans, nums(mid).toLong * (right - left + 1))
        }
      }
      stack += i
    }
    ans.toInt
  }
}
