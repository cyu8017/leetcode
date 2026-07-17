// LeetCode 1794 - Count Pairs of Equal Substrings With Minimum Difference
// https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/

object Solution {
  def countQuadruples(firstString: String, secondString: String): Long = {
    val first = Array.fill(26)(-1)
    val lastF = Array.fill(26)(-1)
    val lastS = Array.fill(26)(-1)
    for (i <- firstString.indices) {
      val c = firstString(i) - 'a'
      if (first(c) == -1) first(c) = i
      lastF(c) = i
    }
    for (i <- secondString.indices) {
      lastS(secondString(i) - 'a') = i
    }
    var best = Long.MaxValue
    for (c <- 0 until 26) {
      if (first(c) != -1 && lastS(c) != -1) {
        best = math.min(best, (lastF(c) - lastS(c)).toLong)
      }
    }
    if (best == Long.MaxValue) return 0L
    var ans = 0L
    for (c <- 0 until 26) {
      if (first(c) != -1 && lastS(c) != -1 && (lastF(c) - lastS(c)).toLong == best) {
        var iCount = 0L
        for (k <- first(c) to lastF(c)) {
          if (firstString(k) - 'a' == c) iCount += 1
        }
        var aCount = 0L
        for (k <- 0 to lastS(c)) {
          if (secondString(k) - 'a' == c) aCount += 1
        }
        ans += iCount * aCount
      }
    }
    ans
  }
}
