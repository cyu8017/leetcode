// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

object Solution {
  def maxSubarrayLength(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    val st = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (i <- n - 1 to 0 by -1) {
      if (st.isEmpty || nums(i) > nums(st.last)) st += i
    }
    for (i <- 0 until n) {
      while (st.nonEmpty && nums(i) > nums(st.last)) {
        val j = st.remove(st.length - 1)
        if (j - i + 1 > ans) ans = j - i + 1
      }
    }
    ans
  }
}
