// LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
// https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

object Solution {
  def maximumBeauty(nums: Array[Int], k: Int): Int = {
    val a = nums.sorted
    var ans = 0
    var left = 0
    var right = 0
    while (right < a.length) {
      while (a(right) - a(left) > 2 * k) left += 1
      ans = math.max(ans, right - left + 1)
      right += 1
    }
    ans
  }
}
