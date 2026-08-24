// LeetCode 3925 - Concatenate Array With Reverse
// https://leetcode.com/problems/concatenate-array-with-reverse/

object Solution {
  def concatWithReverse(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val ans = new Array[Int](2 * n)
    var i = 0
    while (i < n) {
      ans(i) = nums(i)
      ans(i + n) = nums(n - i - 1)
      i += 1
    }
    ans
  }
}
