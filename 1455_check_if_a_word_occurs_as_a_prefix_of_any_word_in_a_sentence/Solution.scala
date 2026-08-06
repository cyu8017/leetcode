object Solution {
  def isPrefixOfWord(sentence: String, searchWord: String): Int = {
    val index = sentence.split(" ").indexWhere(_.startsWith(searchWord))
    if (index == -1) -1 else index + 1
  }
}
