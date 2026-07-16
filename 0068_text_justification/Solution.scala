// LeetCode 0068 - Text Justification
// https://leetcode.com/problems/text-justification/

object Solution {
  def fullJustify(words: Array[String], maxWidth: Int): List[String] = {
    val result = scala.collection.mutable.ListBuffer.empty[String]
    var i = 0

    while (i < words.length) {
      val lineWords = scala.collection.mutable.ArrayBuffer.empty[String]
      var lineLen = 0

      while (i < words.length) {
        val word = words(i)
        val extra = if (lineWords.isEmpty) 0 else 1
        if (lineLen + word.length + extra > maxWidth) {
          break
        }
        lineWords += word
        lineLen += word.length + extra
        i += 1
      }

      if (i == words.length || lineWords.length == 1) {
        var line = lineWords.mkString(" ")
        line += " " * (maxWidth - line.length)
        result += line
      } else {
        val totalChars = lineWords.map(_.length).sum
        val totalSpaces = maxWidth - totalChars
        val gaps = lineWords.length - 1
        val space = totalSpaces / gaps
        val remainder = totalSpaces % gaps
        val line = new StringBuilder
        lineWords.init.zipWithIndex.foreach { case (word, j) =>
          line.append(word)
          line.append(" " * (space + (if (j < remainder) 1 else 0)))
        }
        line.append(lineWords.last)
        result += line.toString
      }
    }

    result.toList
  }
}
