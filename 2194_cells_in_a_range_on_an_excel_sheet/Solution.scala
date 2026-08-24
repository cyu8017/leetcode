// LeetCode 2194 - Cells in a Range on an Excel Sheet
// https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

object Solution {
  def cellsInRange(s: String): List[String] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[String]
    var c = s.charAt(0)
    while (c <= s.charAt(3)) {
      var r = s.charAt(1)
      while (r <= s.charAt(4)) {
        ans += ("" + c + r)
        r = (r + 1).toChar
      }
      c = (c + 1).toChar
    }
    ans.toList
  }
}
