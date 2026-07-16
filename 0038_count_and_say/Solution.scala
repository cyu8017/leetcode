// LeetCode 0038 - Count and Say
// https://leetcode.com/problems/count-and-say/

object Solution {
  def countAndSay(n: Int): String = {
    var term = "1"

    for (_ <- 1 until n) {
      val nextTerm = new StringBuilder
      var index = 0
      while (index < term.length) {
        var count = 1
        while (index + count < term.length && term(index + count) == term(index)) {
          count += 1
        }
        nextTerm.append(count)
        nextTerm.append(term(index))
        index += count
      }
      term = nextTerm.toString
    }

    term
  }
}
