// LeetCode 1307 - Verbal Arithmetic Puzzle
// https://leetcode.com/problems/verbal-arithmetic-puzzle/

object Solution {
  def isSolvable(words: Array[String], result: String): Boolean = {
    if (words.map(_.length).max > result.length) return false
    val chars = (words.mkString + result).toSet
    if (chars.size > 10) return false
    val leading = scala.collection.mutable.HashSet[Char]()
    for (word <- words if word.length > 1) leading += word(0)
    if (result.length > 1) leading += result(0)
    val value = scala.collection.mutable.HashMap[Char, Int]()
    val used = Array.ofDim[Boolean](10)
    val width = result.length

    def dfs(column: Int, row: Int, total: Int): Boolean = {
      if (column == width) return total == 0
      if (row < words.length) {
        if (column >= words(row).length) return dfs(column, row + 1, total)
        val ch = words(row)(words(row).length - 1 - column)
        if (value.contains(ch)) return dfs(column, row + 1, total + value(ch))
        for (digit <- 0 to 9) {
          if (!used(digit) && (digit != 0 || !leading.contains(ch))) {
            value(ch) = digit
            used(digit) = true
            if (dfs(column, row + 1, total + digit)) return true
            used(digit) = false
            value.remove(ch)
          }
        }
        return false
      }
      val ch = result(result.length - 1 - column)
      val digit = total % 10
      val carry = total / 10
      if (value.contains(ch)) return value(ch) == digit && dfs(column + 1, 0, carry)
      if (used(digit) || (digit == 0 && leading.contains(ch))) return false
      value(ch) = digit
      used(digit) = true
      val ok = dfs(column + 1, 0, carry)
      used(digit) = false
      value.remove(ch)
      ok
    }

    dfs(0, 0, 0)
  }
}
