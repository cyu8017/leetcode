// LeetCode 1309 - Decrypt String From Alphabet To Integer Mapping
// https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

object Solution {
  def freqAlphabets(s: String): String = {
    val answer = new StringBuilder
    var i = s.length - 1
    while (i >= 0) {
      if (s(i) == '#') {
        answer.append(('a' + s.substring(i - 2, i).toInt - 1).toChar)
        i -= 3
      } else {
        answer.append(('a' + (s(i) - '0') - 1).toChar)
        i -= 1
      }
    }
    answer.reverse.toString
  }
}
