// LeetCode 0448 - Find All Numbers Disappeared in an Array
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

object Solution {
  def findDisappearedNumbers(nums: Array[Int]): List[Int] = {
    for (number <- nums) {
      val index = math.abs(number) - 1
      if (nums(index) > 0) {
        nums(index) = -nums(index)
      }
    }
    nums.zipWithIndex.collect { case (value, index) if value > 0 => index + 1 }.toList
  }
}
