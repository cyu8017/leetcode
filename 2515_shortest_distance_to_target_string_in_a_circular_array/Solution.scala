// LeetCode 2515 - Shortest Distance to Target String in a Circular Array
// https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

object Solution {
  def closestTarget(words: Array[String], target: String, startIndex: Int): Int = {
    val n = words.length
    var best = -1
    var i = 0
    while (i < n) {
      if (words(i) == target) {
        var d = i - startIndex
        if (d < 0) d = -d
        if (n - d < d) d = n - d
        if (best < 0 || d < best) best = d
      }
      i += 1
    }
    best
  }
}
