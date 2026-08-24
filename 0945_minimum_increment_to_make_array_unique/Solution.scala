// LeetCode 0945 - Minimum Increment to Make Array Unique
// https://leetcode.com/problems/minimum-increment-to-make-array-unique/

object Solution {
  def minIncrementForUnique(nums: Array[Int]): Int = {
    val arr = nums.sorted
    var ans = 0
    var i = 1
    while (i < arr.length) {
      if (arr(i) <= arr(i - 1)) {
        val need = arr(i - 1) + 1
        ans += need - arr(i)
        arr(i) = need
      }
      i += 1
    }
    ans
  }
}
