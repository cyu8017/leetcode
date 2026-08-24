// LeetCode 0806 - Number of Lines To Write String
// https://leetcode.com/problems/number-of-lines-to-write-string/

object Solution {
  def numberOfLines(widths: Array[Int], s: String): Array[Int] = {
    var lines = 1
    var width = 0
    s.foreach { ch =>
      val w = widths(ch - 'a')
      if (width + w > 100) {
        lines += 1
        width = w
      } else width += w
    }
    Array(lines, width)
  }
}
