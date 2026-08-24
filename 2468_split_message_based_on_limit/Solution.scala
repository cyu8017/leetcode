// LeetCode 2468 - Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/

object Solution {
  def splitMessage(message: String, limit: Int): Array[String] = {
    val n = message.length
    var parts = 1
    while (parts <= n) {
      val sbDigits = parts.toString.length
      var ok = true
      var idx = 0
      val res = scala.collection.mutable.ArrayBuffer.empty[String]
      var i = 1
      while (i <= parts && ok) {
        val tail = 3 + i.toString.length + sbDigits
        val cap = limit - tail
        if (cap <= 0 || idx >= n) ok = false
        else {
          var take = cap
          if (take > n - idx) take = n - idx
          res += message.substring(idx, idx + take) + "<" + i + "/" + parts + ">"
          idx += take
        }
        i += 1
      }
      if (ok && idx == n) return res.toArray
      parts += 1
    }
    Array.empty[String]
  }
}
