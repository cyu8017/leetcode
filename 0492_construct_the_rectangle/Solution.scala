// LeetCode 0492 - Construct the Rectangle
// https://leetcode.com/problems/construct-the-rectangle/

object Solution {
  def constructRectangle(area: Int): Array[Int] = {
    val limit = math.sqrt(area).toInt
    var width = limit
    while (width > 0) {
      if (area % width == 0) return Array(area / width, width)
      width -= 1
    }
    Array(area, 1)
  }
}
