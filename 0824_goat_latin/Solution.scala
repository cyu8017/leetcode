// LeetCode 0824 - Goat Latin
// https://leetcode.com/problems/goat-latin/

object Solution {
  def toGoatLatin(sentence: String): String = {
    val vowels = Set('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    val words = sentence.split(" ")
    words.indices.map { i =>
      val word = words(i)
      val goat = new StringBuilder
      if (vowels.contains(word.charAt(0))) goat.append(word).append("ma")
      else goat.append(word.substring(1)).append(word.charAt(0)).append("ma")
      goat.append("a" * (i + 1))
      goat.toString
    }.mkString(" ")
  }
}
