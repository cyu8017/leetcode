// LeetCode 2366 - Minimum Replacements to Sort the Array
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

object Solution {
  def minimumReplacement(nums: Array[Int]): Long = {
    var ans = 0L
    val n = nums.length
    var prev = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      if (nums(i) <= prev) prev = nums(i)
      else {
        val parts = (nums(i) + prev - 1) / prev
        ans += parts - 1
        prev = nums(i) / parts
      }
      i -= 1
    }
    ans
  }
}
