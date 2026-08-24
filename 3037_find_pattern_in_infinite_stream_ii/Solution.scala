// LeetCode 3037 - Find Pattern in Infinite Stream II
// https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

class InfiniteStream(_bits: Array[Int]) {
  private val bits = _bits
  private var i = 0
  def next(): Int = { val v = bits(i); i += 1; v }
}

object Solution {
  private def getLPS(pattern: Array[Int]): Array[Int] = {
    val n = pattern.length
    val lps = Array.ofDim[Int](n)
    var j = 0
    var i = 1
    while (i < n) {
      while (j > 0 && pattern(j) != pattern(i)) j = lps(j - 1)
      if (pattern(i) == pattern(j)) {
        j += 1
        lps(i) = j
      }
      i += 1
    }
    lps
  }

  def findPattern(stream: InfiniteStream, pattern: Array[Int]): Int = {
    val lps = getLPS(pattern)
    var i = 0
    var j = 0
    var bit = 0
    var readNext = false
    while (true) {
      if (!readNext) {
        bit = stream.next()
        readNext = true
      }
      if (bit == pattern(j)) {
        i += 1
        readNext = false
        j += 1
        if (j == pattern.length) return i - j
      } else if (j > 0) {
        j = lps(j - 1)
      } else {
        i += 1
        readNext = false
      }
    }
    -1
  }
}
