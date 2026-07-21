// LeetCode 1805 - Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/

object Solution {
  def numDifferentIntegers(word: String): Int = {
    val seen = scala.collection.mutable.Set.empty[String]
    var i = 0
    while (i < word.length) {
      if (word(i).isDigit) {
        var j = i
        while (j < word.length && word(j).isDigit) j += 1
        var start = i
        while (start < j - 1 && word(start) == '0') start += 1
        seen += word.substring(start, j)
        i = j
      } else i += 1
    }
    seen.size
  }
}
