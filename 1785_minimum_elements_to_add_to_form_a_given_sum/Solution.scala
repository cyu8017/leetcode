// LeetCode 1785 - Minimum Elements to Add to Form a Given Sum
// https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

object Solution {
  def minElements(nums: Array[Int], limit: Int, goal: Int): Int = {
    var sum = 0L
    for (num <- nums) {
      sum += num
    }
    val diff = math.abs(sum - goal)
    ((diff + limit - 1) / limit).toInt
  }
}
