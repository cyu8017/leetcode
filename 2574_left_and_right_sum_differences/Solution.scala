// LeetCode 2574 - Left and Right Sum Differences
// https://leetcode.com/problems/left-and-right-sum-differences/

object Solution {
  def leftRightDifference(nums: Array[Int]): Array[Int] = {
    var total = 0
    nums.foreach(x => total += x)
    val ans = Array.fill(nums.length)(0)
    var left = 0
    var i = 0
    while (i < nums.length) {
      val right = total - left - nums(i)
      ans(i) = math.abs(left - right)
      left += nums(i)
      i += 1
    }
    ans
  }
}
