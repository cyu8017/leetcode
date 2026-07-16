// LeetCode 0302 - Smallest Rectangle Enclosing Black Pixels
// https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

object Solution {
  def minArea(image: Array[Array[Char]], x: Int, y: Int): Int = {
    val rows = image.length
    val cols = image(0).length

    var left = 0
    var right = y
    while (left < right) {
      val mid = (left + right) / 2
      if (columnHasBlack(image, mid, rows)) {
        right = mid
      } else {
        left = mid + 1
      }
    }
    val leftBound = left

    left = y
    right = cols - 1
    while (left < right) {
      val mid = (left + right + 1) / 2
      if (columnHasBlack(image, mid, rows)) {
        left = mid
      } else {
        right = mid - 1
      }
    }
    val rightBound = left

    var top = 0
    var bottom = x
    while (top < bottom) {
      val mid = (top + bottom) / 2
      if (rowHasBlack(image, mid, cols)) {
        bottom = mid
      } else {
        top = mid + 1
      }
    }
    val topBound = top

    top = x
    bottom = rows - 1
    while (top < bottom) {
      val mid = (top + bottom + 1) / 2
      if (rowHasBlack(image, mid, cols)) {
        top = mid
      } else {
        bottom = mid - 1
      }
    }
    val bottomBound = top

    (rightBound - leftBound + 1) * (bottomBound - topBound + 1)
  }

  private def columnHasBlack(image: Array[Array[Char]], col: Int, rows: Int): Boolean = {
    var row = 0
    while (row < rows) {
      if (image(row)(col) == '1') {
        return true
      }
      row += 1
    }
    false
  }

  private def rowHasBlack(image: Array[Array[Char]], row: Int, cols: Int): Boolean = {
    var col = 0
    while (col < cols) {
      if (image(row)(col) == '1') {
        return true
      }
      col += 1
    }
    false
  }
}
