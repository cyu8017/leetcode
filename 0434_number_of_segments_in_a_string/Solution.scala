// LeetCode 0434 - Number of Segments in a String
// https://leetcode.com/problems/number-of-segments-in-a-string/

object Solution {
  def countSegments(s: String): Int = {
    var count = 0
    var inSegment = false
    for (char <- s) {
      if (char != ' ') {
        if (!inSegment) {
          count += 1
          inSegment = true
        }
      } else {
        inSegment = false
      }
    }
    count
  }
}
