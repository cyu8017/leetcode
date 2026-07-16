// LeetCode 0533 - Lonely Pixel II
// https://leetcode.com/problems/lonely-pixel-ii/

object Solution {
  def findBlackPixel(picture: Array[Array[String]], target: Int): Int = {
    val rows = picture.length
    val cols = picture(0).length
    val rowStrings = picture.map(_.mkString)
    val rowCounts = Array.fill(rows)(0)
    val colCounts = Array.fill(cols)(0)

    for (r <- 0 until rows; c <- 0 until cols if picture(r)(c) == "B") {
      rowCounts(r) += 1
      colCounts(c) += 1
    }

    var lonely = 0
    for (r <- 0 until rows if rowCounts(r) == target; c <- 0 until cols) {
      if (picture(r)(c) == "B" && colCounts(c) == target) {
        val matches = (0 until rows).forall { i =>
          picture(i)(c) != "B" || rowStrings(r) == rowStrings(i)
        }
        if (matches) {
          lonely += 1
        }
      }
    }
    lonely
  }
}
