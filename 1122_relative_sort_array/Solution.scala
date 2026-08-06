// LeetCode 1122 - Relative Sort Array
// https://leetcode.com/problems/relative-sort-array/

object Solution {
  def relativeSortArray(arr1: Array[Int], arr2: Array[Int]): Array[Int] = {
    val order = arr2.zipWithIndex.toMap
    arr1.sortBy(x => (order.getOrElse(x, 1000 + x), x))
  }
}
