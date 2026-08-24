// LeetCode 0890 - Find and Replace Pattern
// https://leetcode.com/problems/find-and-replace-pattern/

object Solution {
  def findAndReplacePattern(words: Array[String], pattern: String): List[String] = {
    def normalize(s: String): Array[Int] = {
      val mapping = scala.collection.mutable.Map.empty[Char, Int]
      val out = Array.ofDim[Int](s.length)
      var i = 0
      while (i < s.length) {
        val ch = s.charAt(i)
        if (!mapping.contains(ch)) mapping(ch) = mapping.size
        out(i) = mapping(ch)
        i += 1
      }
      out
    }
    val target = normalize(pattern)
    words.filter(w => java.util.Arrays.equals(normalize(w), target)).toList
  }
}
