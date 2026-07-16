// LeetCode 0022 - Generate Parentheses
// https://leetcode.com/problems/generate-parentheses/

object Solution {
  def generateParenthesis(n: Int): List[String] = {
    val result = scala.collection.mutable.ListBuffer.empty[String]
    val path = scala.collection.mutable.ArrayBuffer.empty[Char]

    def backtrack(openCount: Int, closeCount: Int): Unit = {
      if (path.length == 2 * n) {
        result += path.mkString
        return
      }
      if (openCount < n) {
        path += '('
        backtrack(openCount + 1, closeCount)
        path.remove(path.length - 1)
      }
      if (closeCount < openCount) {
        path += ')'
        backtrack(openCount, closeCount + 1)
        path.remove(path.length - 1)
      }
    }

    backtrack(0, 0)
    result.toList
  }
}
