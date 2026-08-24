// LeetCode 0740 - Delete and Earn
// https://leetcode.com/problems/delete-and-earn/

object Solution {
  def deleteAndEarn(nums: Array[Int]): Int = {
    if (nums.isEmpty) return 0
    var maxNum = 0
    for (num <- nums) maxNum = math.max(maxNum, num)
    val points = Array.fill(maxNum + 1)(0)
    for (num <- nums) points(num) += num
    var take = 0
    var skip = 0
    for (value <- points) {
      val newTake = skip + value
      val newSkip = math.max(skip, take)
      take = newTake
      skip = newSkip
    }
    math.max(take, skip)
  }
}
