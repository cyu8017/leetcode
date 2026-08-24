// LeetCode 2782 - Number of Unique Categories
// https://leetcode.com/problems/number-of-unique-categories/

object Solution {
  def numberOfCategories(n: Int, categoryHandler: Array[Int]): Int =
    categoryHandler.toSet.size
}
