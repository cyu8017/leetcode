// LeetCode 0745 - Prefix and Suffix Search
// https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter(words: Array[String]) {
  private val lookup = scala.collection.mutable.HashMap.empty[String, Int]
  {
    var index = 0
    while (index < words.length) {
      val word = words(index)
      val size = word.length
      var i = 0
      while (i <= size) {
        var j = 0
        while (j <= size) {
          lookup(word.substring(0, i) + "#" + word.substring(j)) = index
          j += 1
        }
        i += 1
      }
      index += 1
    }
  }

  def f(pref: String, suff: String): Int = lookup.getOrElse(pref + "#" + suff, -1)
}
