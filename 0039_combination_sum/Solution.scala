// LeetCode 0039 - Combination Sum
// https://leetcode.com/problems/combination-sum/

object Solution {
  def combinationSum(candidates: Array[Int], target: Int): List[List[Int]] = {
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

      for (i <- start until candidates.length) {
        path += candidates(i)
        backtrack(i, remaining - candidates(i))
        path.remove(path.length - 1)
      }
    }

    backtrack(0, target)
    result.toList
  }
}
