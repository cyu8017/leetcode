// LeetCode 0648 - Replace Words
// https://leetcode.com/problems/replace-words/

object Solution {
  def replaceWords(dictionary: List[String], sentence: String): String = {
    val roots = dictionary.toSet
    val words = sentence.split(" ")
    val result = new StringBuilder
    var w = 0
    while (w < words.length) {
      val word = words(w)
      var replacement = word
      var i = 1
      var found = false
      while (i <= word.length && !found) {
        val prefix = word.substring(0, i)
        if (roots.contains(prefix)) {
          replacement = prefix
          found = true
        }
        i += 1
      }
      if (w > 0) result.append(' ')
      result.append(replacement)
      w += 1
    }
    result.toString
  }
}
