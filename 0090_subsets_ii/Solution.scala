// LeetCode 0090 - Subsets II
// https://leetcode.com/problems/subsets-ii/

object Solution {
  def subsetsWithDup(nums: Array[Int]): List[List[Int]] = {
    val sorted = nums.sorted
    val result = scala.collection.mutable.ListBuffer.empty[List[Int]]
    val path = scala.collection.mutable.ArrayBuffer.empty[Int]

    def backtrack(start: Int): Unit = {
      result += path.toList
      for (i <- start until sorted.length) {
        if (i == start || sorted(i) != sorted(i - 1)) {
          path += sorted(i)
          backtrack(i + 1)
          path.remove(path.length - 1)
        }
      }
    }

    backtrack(0)
    result.toList
  }
}
