// LeetCode 2103 - Rings and Rods
// https://leetcode.com/problems/rings-and-rods/

object Solution {
  def countPoints(rings: String): Int = {
    val mask = Array.fill(10)(0)
    var i = 0
    while (i < rings.length) {
      val c = rings.charAt(i)
      val r = rings.charAt(i + 1) - '0'
      val bit = if (c == 'R') 1 else if (c == 'G') 2 else 4
      mask(r) |= bit
      i += 2
    }
    mask.count(_ == 7)
  }
}
