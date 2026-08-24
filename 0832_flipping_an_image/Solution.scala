// LeetCode 0832 - Flipping an Image
// https://leetcode.com/problems/flipping-an-image/

object Solution {
  def flipAndInvertImage(image: Array[Array[Int]]): Array[Array[Int]] = {
    image.foreach { row =>
      var i = 0
      var j = row.length - 1
      while (i <= j) {
        val a = 1 - row(i)
        val b = 1 - row(j)
        row(i) = b
        row(j) = a
        i += 1
        j -= 1
      }
    }
    image
  }
}
