// LeetCode 3379 - Transformed Array
// https://leetcode.com/problems/transformed-array/

object Solution {
  def constructTransformedArray(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val ans = new Array[Int](n)
    var i = 0
    while (i < n) {
      val j = ((i + nums(i)) % n + n) % n
      ans(i) = nums(j)
      i += 1
    }
    ans
  }
}
