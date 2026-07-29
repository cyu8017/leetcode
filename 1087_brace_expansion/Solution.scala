// LeetCode 1087 - Brace Expansion
// https://leetcode.com/problems/brace-expansion/

object Solution {
  def expand(s: String): Array[String] = {
    val groups = scala.collection.mutable.ArrayBuffer.empty[Array[String]]
    var i = 0
    while (i < s.length) {
      if (s(i) == '{') {
        val j = s.indexOf('}', i)
        groups += s.substring(i + 1, j).split(",").sorted
        i = j + 1
      } else {
        groups += Array(s(i).toString)
        i += 1
      }
    }
    var ans = Array("")
    for (group <- groups) {
      ans = for (prefix <- ans; ch <- group) yield prefix + ch
    }
    ans
  }
}
