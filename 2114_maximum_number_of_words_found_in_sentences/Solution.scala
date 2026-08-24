// LeetCode 2114 - Maximum Number of Words Found in Sentences
// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

object Solution {
  def mostWordsFound(sentences: Array[String]): Int = {
    var ans = 0
    sentences.foreach { s =>
      var c = 1
      var i = 0
      while (i < s.length) {
        if (s.charAt(i) == ' ') c += 1
        i += 1
      }
      ans = math.max(ans, c)
    }
    ans
  }
}
