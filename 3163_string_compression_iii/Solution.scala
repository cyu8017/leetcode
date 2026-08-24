// LeetCode 3163 - String Compression III
// https://leetcode.com/problems/string-compression-iii/

object Solution {
  def compressedString(word: String): String = {
    val ans = new StringBuilder
    val n = word.length
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n && word.charAt(j) == word.charAt(i)) j += 1
      var k = j - i
      while (k > 0) {
        val x = math.min(9, k)
        ans.append(('0' + x).toChar)
        ans.append(word.charAt(i))
        k -= x
      }
      i = j
    }
    ans.toString
  }
}
