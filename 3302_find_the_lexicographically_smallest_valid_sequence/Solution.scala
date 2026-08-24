// LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

object Solution {
  private def canFinish(w1: String, w2: String, i: Int, j: Int, usedSkip: Boolean, right: Array[Int]): Boolean = {
    val m = w2.length
    if (j >= m) return true
    if (!usedSkip) {
      if (right(j) >= i) return true
      if (j + 1 <= m && right(j + 1) > i) return true
      if (right(j) > i) return true
      return false
    }
    right(j) >= i
  }

  def validSequence(word1: String, word2: String): Array[Int] = {
    val n = word1.length
    val m = word2.length
    val right = new Array[Int](m + 1)
    right(m) = n
    var j = m - 1
    var i = n - 1
    while (i >= 0 && j >= 0) {
      if (word1.charAt(i) == word2.charAt(j)) {
        right(j) = i
        j -= 1
      }
      i -= 1
    }
    while (j >= 0) {
      right(j) = -1
      j -= 1
    }
    val ans = new Array[Int](m)
    var usedSkip = false
    i = 0
    j = 0
    while (j < m) {
      var found = false
      while (i < n && !found) {
        if (word1.charAt(i) == word2.charAt(j)) {
          if (canFinish(word1, word2, i + 1, j + 1, usedSkip, right)) {
            ans(j) = i
            i += 1
            found = true
          } else i += 1
        } else if (!usedSkip) {
          if (canFinish(word1, word2, i + 1, j + 1, true, right)) {
            ans(j) = i
            i += 1
            usedSkip = true
            found = true
          } else i += 1
        } else i += 1
      }
      if (!found) return Array.emptyIntArray
      j += 1
    }
    ans
  }
}
