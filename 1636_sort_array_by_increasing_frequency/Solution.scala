// LeetCode 1636 - Sort Array by Increasing Frequency
// https://leetcode.com/problems/sort-array-by-increasing-frequency/

object Solution {
  def frequencySort(nums: Array[Int]): Array[Int] = {
    val count = nums.groupBy(identity).view.mapValues(_.length).toMap
    nums.sortBy(x => (count(x), -x))
  }
}
