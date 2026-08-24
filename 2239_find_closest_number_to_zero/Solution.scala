// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

object Solution {
  def findClosestNumber(nums: Array[Int]): Int = {
    var ans = nums(0)
    for (x <- nums) {
      if (math.abs(x) < math.abs(ans) || (math.abs(x) == math.abs(ans) && x > ans)) ans = x
    }
    ans
  }
}
