// LeetCode 3008 - Find Beautiful Indices in the Given Array II
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/

object Solution {
  private def buildLPS(lps: Array[Int], pattern: String): Unit = {
    var l = 0
    var i = 1
    val sl = pattern.length
    lps(0) = 0
    while (i < sl) {
      if (pattern.charAt(i) == pattern.charAt(l)) {
        l += 1
        lps(i) = l
        i += 1
      } else if (l != 0) l = lps(l - 1)
      else { lps(i) = l; i += 1 }
    }
  }

  private def kmp(s: String, pat: String, lps: Array[Int], index: scala.collection.mutable.ArrayBuffer[Int]): Unit = {
    val sLen = s.length
    val patL = pat.length
    var i = 0
    var j = 0
    while (sLen - i >= patL - j) {
      if (s.charAt(i) == pat.charAt(j)) { i += 1; j += 1 }
      if (j == patL) {
        index += (i - patL)
        j = lps(j - 1)
      } else if (i < sLen && s.charAt(i) != pat.charAt(j)) {
        if (j != 0) j = lps(j - 1) else i += 1
      }
    }
  }

  def beautifulIndices(s: String, a: String, b: String, k: Int): List[Int] = {
    val lpsA = Array.ofDim[Int](a.length)
    val lpsB = Array.ofDim[Int](b.length)
    val aIndex = scala.collection.mutable.ArrayBuffer.empty[Int]
    val bIndex = scala.collection.mutable.ArrayBuffer.empty[Int]
    val result = scala.collection.mutable.ListBuffer.empty[Int]
    buildLPS(lpsA, a)
    buildLPS(lpsB, b)
    kmp(s, a, lpsA, aIndex)
    kmp(s, b, lpsB, bIndex)
    var i = 0
    var j = 0
    while (i < aIndex.length && j < bIndex.length) {
      if (aIndex(i) + k >= bIndex(j) && aIndex(i) - k <= bIndex(j)) {
        result += aIndex(i)
        i += 1
      } else if (aIndex(i) - k > bIndex(j)) j += 1
      else i += 1
    }
    result.toList
  }
}
