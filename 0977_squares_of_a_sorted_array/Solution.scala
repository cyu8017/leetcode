// LeetCode 0977 - Squares of a Sorted Array
// https://leetcode.com/problems/squares-of-a-sorted-array/

object Solution {
  def sortedSquares(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val ans = Array.ofDim[Int](n)
    var i = 0
    var j = n - 1
    var k = n - 1
    while (k >= 0) {
      if (math.abs(nums(i)) > math.abs(nums(j))) {
        ans(k) = nums(i) * nums(i)
        i += 1
      } else {
        ans(k) = nums(j) * nums(j)
        j -= 1
      }
      k -= 1
    }
    ans
  }
}
