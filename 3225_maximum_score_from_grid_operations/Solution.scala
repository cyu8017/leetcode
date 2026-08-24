// LeetCode 3225 - Maximum Score From Grid Operations
// https://leetcode.com/problems/maximum-score-from-grid-operations/

object Solution {
  def maximumScore(grid: Array[Array[Int]]): Long = {
    val n = grid.length
    val prefix = Array.ofDim[Long](n, n + 1)
    var j = 0
    while (j < n) {
      var i = 0
      while (i < n) {
        prefix(j)(i + 1) = prefix(j)(i) + grid(i)(j)
        i += 1
      }
      j += 1
    }
    var prevPick = new Array[Long](n + 1)
    var prevSkip = new Array[Long](n + 1)
    j = 1
    while (j < n) {
      val currPick = new Array[Long](n + 1)
      val currSkip = new Array[Long](n + 1)
      var curr = 0
      while (curr <= n) {
        var prev = 0
        while (prev <= n) {
          if (curr > prev) {
            val score = prefix(j - 1)(curr) - prefix(j - 1)(prev)
            currPick(curr) = math.max(currPick(curr), prevSkip(prev) + score)
            currSkip(curr) = math.max(currSkip(curr), prevSkip(prev) + score)
          } else {
            val score = prefix(j)(prev) - prefix(j)(curr)
            currPick(curr) = math.max(currPick(curr), prevPick(prev) + score)
            currSkip(curr) = math.max(currSkip(curr), prevPick(prev))
          }
          prev += 1
        }
        curr += 1
      }
      prevPick = currPick
      prevSkip = currSkip
      j += 1
    }
    var ans = Long.MinValue
    for (v <- prevPick) ans = math.max(ans, v)
    ans
  }
}
