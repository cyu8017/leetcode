// LeetCode 0282 - Expression Add Operators
// https://leetcode.com/problems/expression-add-operators/

object Solution {
  def addOperators(num: String, target: Int): List[String] = {
    val result = scala.collection.mutable.ListBuffer.empty[String]

    def backtrack(index: Int, path: String, value: Long, previous: Long): Unit = {
      if (index == num.length) {
        if (value == target) {
          result += path
        }
        return
      }
      var end = index
      var done = false
      while (end < num.length && !done) {
        if (end > index && num(index) == '0') {
          done = true
        } else {
          val currentStr = num.substring(index, end + 1)
          val current = currentStr.toLong
          if (index == 0) {
            backtrack(end + 1, currentStr, current, current)
          } else {
            backtrack(end + 1, path + "+" + currentStr, value + current, current)
            backtrack(end + 1, path + "-" + currentStr, value - current, -current)
            backtrack(
              end + 1,
              path + "*" + currentStr,
              value - previous + previous * current,
              previous * current,
            )
          }
          end += 1
        }
      }
    }

    backtrack(0, "", 0L, 0L)
    result.toList
  }
}
