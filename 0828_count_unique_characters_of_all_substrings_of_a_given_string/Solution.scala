// LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

object Solution {
  def uniqueLetterString(s: String): Int = {
    val n = s.length
    val last = scala.collection.mutable.Map.empty[Char, scala.collection.mutable.ListBuffer[Int]]
    s.foreach { ch => last.getOrElseUpdate(ch, scala.collection.mutable.ListBuffer(-1)) }
    var i = 0
    while (i < n) {
      last(s.charAt(i)) += i
      i += 1
    }
    last.values.foreach(_ += n)
    var ans = 0
    last.values.foreach { indices =>
      var k = 1
      while (k + 1 < indices.length) {
        ans += (indices(k) - indices(k - 1)) * (indices(k + 1) - indices(k))
        k += 1
      }
    }
    ans
  }
}
