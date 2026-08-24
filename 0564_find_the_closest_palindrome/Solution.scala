// LeetCode 0564 - Find the Closest Palindrome
// https://leetcode.com/problems/find-the-closest-palindrome/

import scala.collection.mutable

object Solution {
  def nearestPalindromic(n: String): String = {
    val length = n.length
    val number = n.toLong
    val candidates = mutable.ArrayBuffer[Long]()
    candidates += pow10(length - 1) - 1
    candidates += pow10(length) + 1
    val prefix = n.substring(0, (length + 1) / 2).toLong
    var half = prefix - 1
    while (half <= prefix + 1) {
      candidates += makePalindrome(half, length)
      half += 1
    }
    var best = -1L
    var bestDiff = Long.MaxValue
    candidates.foreach { candidate =>
      if (candidate != number) {
        val diff = math.abs(candidate - number)
        if (diff < bestDiff || (diff == bestDiff && candidate < best)) {
          best = candidate
          bestDiff = diff
        }
      }
    }
    best.toString
  }

  private def makePalindrome(half: Long, length: Int): Long = {
    val text = half.toString
    val pal = new StringBuilder(text)
    if (length % 2 == 0) {
      var i = text.length - 1
      while (i >= 0) { pal.append(text.charAt(i)); i -= 1 }
    } else {
      var i = text.length - 2
      while (i >= 0) { pal.append(text.charAt(i)); i -= 1 }
    }
    pal.toString.toLong
  }

  private def pow10(exp: Int): Long = {
    var value = 1L
    var i = 0
    while (i < exp) { value *= 10; i += 1 }
    value
  }
}
