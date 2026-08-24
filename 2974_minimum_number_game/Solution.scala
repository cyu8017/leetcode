// LeetCode 2974 - Minimum Number Game
// https://leetcode.com/problems/minimum-number-game/

object Solution {
  def numberGame(nums: Array[Int]): Array[Int] = {
    scala.util.Sorting.quickSort(nums)
    var i = 0
    while (i + 1 < nums.length) {
      val t = nums(i)
      nums(i) = nums(i + 1)
      nums(i + 1) = t
      i += 2
    }
    nums
  }
}
