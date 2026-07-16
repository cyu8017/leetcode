// LeetCode 0017 - Letter Combinations of a Phone Number
// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

object Solution {
  private val mapping = Array(
    "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
  )

  def letterCombinations(digits: String): List[String] = {
    if (digits.isEmpty) {
      return List.empty
    }

    val result = scala.collection.mutable.ListBuffer.empty[String]
    val path = new StringBuilder

    def backtrack(index: Int): Unit = {
      if (index == digits.length) {
        result += path.toString
        return
      }
      mapping(digits(index) - '0').foreach { ch =>
        path.append(ch)
        backtrack(index + 1)
        path.deleteCharAt(path.length - 1)
      }
    }

    backtrack(0)
    result.toList
  }
}
