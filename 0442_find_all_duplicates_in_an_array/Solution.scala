// LeetCode 0442 - Find All Duplicates in an Array
// https://leetcode.com/problems/find-all-duplicates-in-an-array/

object Solution {
  def findDuplicates(nums: Array[Int]): List[Int] = {
    val result = scala.collection.mutable.ListBuffer.empty[Int]
    for (number <- nums) {
      val index = math.abs(number) - 1
      if (nums(index) < 0) {
        result += math.abs(number)
      } else {
        nums(index) = -nums(index)
      }
    }
    result.toList
  }
}
