// LeetCode 3210 - Find the Encrypted String
// https://leetcode.com/problems/find-the-encrypted-string/

object Solution {
  def getEncryptedString(s: String, k: Int): String = {
    val n = s.length
    val cs = new Array[Char](n)
    var i = 0
    while (i < n) {
      cs(i) = s.charAt((i + k) % n)
      i += 1
    }
    new String(cs)
  }
}
