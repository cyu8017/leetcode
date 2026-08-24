// LeetCode 0784 - Letter Case Permutation
// https://leetcode.com/problems/letter-case-permutation/

object Solution {
  def letterCasePermutation(s: String): List[String] = {
    var result = List("")
    s.foreach { ch =>
      if (ch.isLetter) {
        val lower = ch.toLower
        val upper = ch.toUpper
        result = result.flatMap(p => List(p + lower, p + upper))
      } else {
        result = result.map(_ + ch)
      }
    }
    result
  }
}
