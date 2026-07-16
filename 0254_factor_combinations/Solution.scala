// LeetCode 0254 - Factor Combinations
// https://leetcode.com/problems/factor-combinations/

object Solution {
  def getFactors(n: Int): List[List[Int]] = {
    val result = scala.collection.mutable.ListBuffer.empty[List[Int]]
    val path = scala.collection.mutable.ArrayBuffer.empty[Int]

    def backtrack(remain: Int, start: Int): Unit = {
      if (start > remain) {
        if (path.length > 1) {
          result += path.toList
        }
        return
      }

      var factor = start
      while (factor * factor <= remain) {
        if (remain % factor == 0) {
          path += factor
          backtrack(remain / factor, factor)
          path.remove(path.length - 1)
        }
        factor += 1
      }

      if (path.nonEmpty) {
        path += remain
        if (path.length > 1) {
          result += path.toList
        }
        path.remove(path.length - 1)
      }
    }

    backtrack(n, 2)
    result.toList
  }
}
