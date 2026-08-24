// LeetCode 0809 - Expressive Words
// https://leetcode.com/problems/expressive-words/

object Solution {
  def expressiveWords(s: String, words: Array[String]): Int = {
    def groups(text: String): List[(Int, Int)] = {
      val result = scala.collection.mutable.ListBuffer.empty[(Int, Int)]
      var i = 0
      val n = text.length
      while (i < n) {
        var j = i
        while (j < n && text.charAt(j) == text.charAt(i)) j += 1
        result += ((text.charAt(i), j - i))
        i = j
      }
      result.toList
    }
    val target = groups(s)
    var ans = 0
    words.foreach { word =>
      val source = groups(word)
      if (source.length == target.length) {
        var ok = true
        var i = 0
        while (i < source.length && ok) {
          if (source(i)._1 != target(i)._1) ok = false
          else {
            val c1 = source(i)._2
            val c2 = target(i)._2
            if (c1 > c2 || (c1 != c2 && c2 < 3)) ok = false
          }
          i += 1
        }
        if (ok) ans += 1
      }
    }
    ans
  }
}
