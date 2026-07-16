// LeetCode 0217 - Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/

object Solution {
  def containsDuplicate(nums: Array[Int]): Boolean = {
    val seen = scala.collection.mutable.Set.empty[Int]
    nums.exists(num => !seen.add(num))
  }
}
