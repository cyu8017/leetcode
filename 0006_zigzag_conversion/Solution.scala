// LeetCode 0006 - Zigzag Conversion
// https://leetcode.com/problems/zigzag-conversion/

object Solution {
  def convert(s: String, numRows: Int): String = {
    if (numRows == 1 || numRows >= s.length) {
      return s
    }

    val rows = Array.fill(numRows)(new StringBuilder)
    var index = 0
    var step = 1

    s.foreach { ch =>
      rows(index).append(ch)
      if (index == 0) step = 1
      else if (index == numRows - 1) step = -1
      index += step
    }

    rows.map(_.toString()).mkString
  }
}
