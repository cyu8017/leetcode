// LeetCode 0040 - Combination Sum II
// https://leetcode.com/problems/combination-sum-ii/

object Solution {
  def combinationSum2(candidates: Array[Int], target: Int): List[List[Int]] = {
    val sorted = candidates.sorted
    val result = scala.collection.mutable.ListBuffer.empty[List[Int]]
    val path = scala.collection.mutable.ArrayBuffer.empty[Int]

    def backtrack(start: Int, remaining: Int): Unit = {
      if (remaining == 0) {
        result += path.toList
        return
      }
      if (remaining < 0) {
        return
      }

      for (i <- start until sorted.length) {
        if (i == start || sorted(i) != sorted(i - 1)) {
          path += sorted(i)
          backtrack(i + 1, remaining - sorted(i))
          path.remove(path.length - 1)
        }
      }
    }

    backtrack(0, target)
    result.toList
  }
}
