object Solution {
  def arrangeWords(text: String): String = {
    val result = text.toLowerCase.split(" ").sortBy(_.length).mkString(" ")
    result.head.toUpper + result.tail
  }
}
