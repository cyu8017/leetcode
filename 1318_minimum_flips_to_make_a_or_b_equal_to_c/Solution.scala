// LeetCode 1318 - Minimum Flips to Make a OR b Equal to c
// https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

object Solution {
  def minFlips(a: Int, b: Int, c: Int): Int = {
    var aa = a
    var bb = b
    var cc = c
    var flips = 0
    while (aa != 0 || bb != 0 || cc != 0) {
      val x = aa & 1
      val y = bb & 1
      val z = cc & 1
      flips += (if (z == 0) x + y else if (x == 0 && y == 0) 1 else 0)
      aa >>= 1
      bb >>= 1
      cc >>= 1
    }
    flips
  }
}
