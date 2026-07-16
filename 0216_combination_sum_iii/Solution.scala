// LeetCode 0216 - Combination Sum III
// https://leetcode.com/problems/combination-sum-iii/

object Solution {
  def combinationSum3(k: Int, n: Int): List[List[Int]] = {
    val result = scala.collection.mutable.ListBuffer.empty[List[Int]]
    val path = scala.collection.mutable.ArrayBuffer.empty[Int]

    def backtrack(start: Int, remaining: Int): Unit = {
      if (path.length == k) {
        if (remaining == 0) {
          result += path.toList
        }
        return
      }
      if (remaining <= 0 || path.length >= k) {
        return
      }

      for (num <- start to 9 if num <= remaining) {
        path += num
        backtrack(num + 1, remaining - num)
        path.remove(path.length - 1)
      }
    }

    backtrack(1, n)
    result.toList
  }
}
