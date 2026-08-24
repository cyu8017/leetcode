// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

object Solution {
  def sortBy(arr: Array[Int], fn: Int => Double): Array[Int] = {
    arr.sortBy(fn)
  }
}
