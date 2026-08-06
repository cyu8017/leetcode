object Solution {
  def stringMatching(words: Array[String]): List[String] = words.filter(w => words.count(_.contains(w)) > 1).toList
}
