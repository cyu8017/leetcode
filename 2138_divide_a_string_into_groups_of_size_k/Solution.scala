// LeetCode 2138 - Divide a String Into Groups of Size k
// https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

object Solution {
  def divideString(s: String, k: Int, fill: Char): Array[String] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[String]
    var i = 0
    while (i < s.length) {
      if (i + k <= s.length) ans += s.substring(i, i + k)
      else {
        val chunk = new StringBuilder(s.substring(i))
        while (chunk.length < k) chunk.append(fill)
        ans += chunk.toString
      }
      i += k
    }
    ans.toArray
  }
}
