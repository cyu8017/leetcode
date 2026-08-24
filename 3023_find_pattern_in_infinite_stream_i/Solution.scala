// LeetCode 3023 - Find Pattern in Infinite Stream I
// https://leetcode.com/problems/find-pattern-in-infinite-stream-i/

class InfiniteStream(_bits: Array[Int]) {
  private val bits = _bits
  private var i = 0
  def next(): Int = { val v = bits(i); i += 1; v }
}

object Solution {
  def findPattern(stream: InfiniteStream, pattern: Array[Int]): Int = {
    var a = 0
    var b = 0
    val m = pattern.length
    val half = m >> 1
    val mask1 = (1 << half) - 1
    val mask2 = (1 << (m - half)) - 1
    var i = 0
    while (i < half) { a |= pattern(i) << (half - 1 - i); i += 1 }
    i = half
    while (i < m) { b |= pattern(i) << (m - 1 - i); i += 1 }
    var x = 0
    var y = 0
    i = 1
    while (true) {
      var v = stream.next()
      y = y << 1 | v
      v = (y >> (m - half)) & 1
      y &= mask2
      x = x << 1 | v
      x &= mask1
      if (i >= m && a == x && b == y) return i - m
      i += 1
    }
    -1
  }
}
