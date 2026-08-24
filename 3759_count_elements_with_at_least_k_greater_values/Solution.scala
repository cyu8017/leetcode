// LeetCode 3759 - Count Elements With At Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

object Solution {
  def countElements(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    if (k == 0) return n
    java.util.Arrays.sort(nums)
    var ans = 0
    var i = 0
    while (i < n - k) {
      if (nums(n - k) > nums(i)) ans += 1
      i += 1
    }
    ans
  }
}
