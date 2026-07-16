// LeetCode 0531 - Lonely Pixel I
// https://leetcode.com/problems/lonely-pixel-i/

object Solution {
  def findLonelyPixel(picture: Array[Array[Char]]): Int = {
    val rows = picture.length
    val cols = picture(0).length
    val rowCounts = Array.fill(rows)(0)
    val colCounts = Array.fill(cols)(0)

    for (r <- 0 until rows; c <- 0 until cols if picture(r)(c) == 'B') {
      rowCounts(r) += 1
      colCounts(c) += 1
    }

    var lonely = 0
    for (r <- 0 until rows; c <- 0 until cols) {
      if (picture(r)(c) == 'B' && rowCounts(r) == 1 && colCounts(c) == 1) {
        lonely += 1
      }
    }
    lonely
  }
}
