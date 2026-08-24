// LeetCode 0820 - Short Encoding of Words
// https://leetcode.com/problems/short-encoding-of-words/

object Solution {
  def minimumLengthEncoding(words: Array[String]): Int = {
    val good = scala.collection.mutable.Set(words: _*)
    words.foreach { word =>
      var i = 1
      while (i < word.length) {
        good.remove(word.substring(i))
        i += 1
      }
    }
    good.map(_.length + 1).sum
  }
}
