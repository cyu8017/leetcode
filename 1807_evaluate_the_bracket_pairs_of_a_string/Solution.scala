// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

object Solution {
  def evaluate(s: String, knowledge: Array[Array[String]]): String = {
    val lookup = knowledge.map(p => p(0) -> p(1)).toMap
    val sb = new StringBuilder
    var i = 0
    while (i < s.length) {
      if (s(i) == '(') {
        val j = s.indexOf(')', i + 1)
        val key = s.substring(i + 1, j)
        sb.append(lookup.getOrElse(key, "?"))
        i = j + 1
      } else {
        sb.append(s(i))
        i += 1
      }
    }
    sb.toString
  }
}
