// LeetCode 1005 - Maximize Sum Of Array After K Negations
// https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

object Solution {
  def largestSumAfterKNegations(nums: Array[Int], k: Int): Int = {
    val arr = nums.sorted
    var remaining = k
    for (i <- arr.indices if remaining > 0 && arr(i) < 0) {
      arr(i) = -arr(i)
      remaining -= 1
    }
    if (remaining % 2 == 1) {
      java.util.Arrays.sort(arr)
      arr(0) = -arr(0)
    }
    arr.sum
  }
}
