// LeetCode 0491 - Non-decreasing Subsequences
// https://leetcode.com/problems/non-decreasing-subsequences/

import scala.collection.mutable

object Solution {
  def findSubsequences(nums: Array[Int]): List[List[Int]] = {
    val result = mutable.Set.empty[List[Int]]
    backtrack(nums, 0, mutable.ArrayBuffer.empty[Int], result)
    result.toList.sorted
  }

  private def backtrack(
      nums: Array[Int],
      start: Int,
      path: mutable.ArrayBuffer[Int],
      result: mutable.Set[List[Int]],
  ): Unit = {
    if (path.length >= 2) result += path.toList
    val used = mutable.Set.empty[Int]
    for (index <- start until nums.length) {
      if (used.contains(nums(index))) ()
      else if (path.nonEmpty && nums(index) < path.last) ()
      else {
        used += nums(index)
        path += nums(index)
        backtrack(nums, index + 1, path, result)
        path.remove(path.length - 1)
      }
    }
  }
}
