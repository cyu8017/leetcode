// LeetCode 3167 - Better Compression of String
// https://leetcode.com/problems/better-compression-of-string/

object Solution {
  def betterCompression(compressed: String): String = {
    val cnt = new Array[Int](26)
    val n = compressed.length
    var i = 0
    while (i < n) {
      val c = compressed.charAt(i)
      var j = i + 1
      var x = 0
      var stop = false
      while (j < n && !stop) {
        val d = compressed.charAt(j)
        if (d < '0' || d > '9') stop = true
        else {
          x = x * 10 + (d - '0')
          j += 1
        }
      }
      cnt(c - 'a') += x
      i = j
    }
    val ans = new StringBuilder
    var c = 'a'
    while (c <= 'z') {
      if (cnt(c - 'a') > 0) {
        ans.append(c)
        ans.append(cnt(c - 'a'))
      }
      c = (c + 1).toChar
    }
    ans.toString
  }
}
