// LeetCode 1725 - Number Of Rectangles That Can Form The Largest Square
// https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

object Solution {
  def countGoodRectangles(rectangles: Array[Array[Int]]): Int = {
    var best = 0
    var count = 0
    rectangles.foreach { rect =>
      val side = math.min(rect(0), rect(1))
      if (side > best) {
        best = side
        count = 1
      } else if (side == best) {
        count += 1
      }
    }
    count
  }
}
