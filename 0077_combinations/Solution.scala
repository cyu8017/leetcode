// LeetCode 0077 - Combinations
// https://leetcode.com/problems/combinations/

object Solution {
  def combine(n: Int, k: Int): List[List[Int]] = {
    val result = scala.collection.mutable.ListBuffer.empty[List[Int]]
    val path = scala.collection.mutable.ListBuffer.empty[Int]

    def backtrack(start: Int): Unit = {
      if (path.length == k) {
        result += path.toList
        return
      }

      val remaining = k - path.length
      for (i <- start to (n - remaining + 1)) {
        path += i
        backtrack(i + 1)
        path.remove(path.length - 1)
      }
    }

    backtrack(1)
    result.toList
  }
}
