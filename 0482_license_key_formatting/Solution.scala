// LeetCode 0482 - License Key Formatting
// https://leetcode.com/problems/license-key-formatting/

import scala.collection.mutable

object Solution {
  def licenseKeyFormatting(s: String, k: Int): String = {
    val chars = s.filter(_ != '-').toUpperCase.toCharArray
    if (chars.isEmpty) return ""
    val firstLen = if (chars.length % k == 0) k else chars.length % k
    val parts = mutable.ArrayBuffer(new String(chars, 0, firstLen))
    var index = firstLen
    while (index < chars.length) {
      parts += new String(chars, index, k)
      index += k
    }
    parts.mkString("-")
  }
}
