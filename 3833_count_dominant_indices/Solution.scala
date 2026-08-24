// LeetCode 3833 - Count Dominant Indices
// https://leetcode.com/problems/count-dominant-indices/

object Solution {
  def dominantIndices(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var suf = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      if (nums(i).toLong * (n - i - 1) > suf) ans += 1
      suf += nums(i)
      i -= 1
    }
    ans
  }
}
