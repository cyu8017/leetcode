// LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
// https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

object Solution {
  def minArrayLength(nums: Array[Int], k: Int): Int = {
    if (nums.isEmpty) return 0
    var ans = 1
    var prod = nums(0).toLong
    for (i <- 1 until nums.length) {
      if (prod <= k && nums(i) <= k && (nums(i) == 0 || prod <= k / nums(i))) {
        prod *= nums(i)
      } else {
        ans += 1
        prod = nums(i)
      }
    }
    ans
  }
}
