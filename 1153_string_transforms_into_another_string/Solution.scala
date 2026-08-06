// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

object Solution {
  def canConvert(str1: String, str2: String): Boolean = {
    if (str1 == str2) return true
    val mapping = scala.collection.mutable.Map.empty[Char, Char]
    for (i <- str1.indices) {
      val a = str1(i)
      val b = str2(i)
      if (mapping.contains(a) && mapping(a) != b) return false
      mapping(a) = b
    }
    str2.toSet.size < 26
  }
}
