// LeetCode 0893 - Groups of Special-Equivalent Strings
// https://leetcode.com/problems/groups-of-special-equivalent-strings/

object Solution {
  def numSpecialEquivGroups(words: Array[String]): Int = {
    val groups = scala.collection.mutable.Set.empty[String]
    words.foreach { w =>
      val even = scala.collection.mutable.ArrayBuffer[Char]()
      val odd = scala.collection.mutable.ArrayBuffer[Char]()
      var i = 0
      while (i < w.length) {
        if (i % 2 == 0) even += w.charAt(i)
        else odd += w.charAt(i)
        i += 1
      }
      groups += even.sorted.mkString + "|" + odd.sorted.mkString
    }
    groups.size
  }
}
