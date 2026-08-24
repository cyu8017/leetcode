// LeetCode 0605 - Can Place Flowers
// https://leetcode.com/problems/can-place-flowers/

object Solution {
  def canPlaceFlowers(flowerbed: Array[Int], n0: Int): Boolean = {
    var n = n0
    if (n == 0) return true
    var i = 0
    while (i < flowerbed.length) {
      if (flowerbed(i) != 1) {
        val leftEmpty = i == 0 || flowerbed(i - 1) == 0
        val rightEmpty = i == flowerbed.length - 1 || flowerbed(i + 1) == 0
        if (leftEmpty && rightEmpty) {
          flowerbed(i) = 1
          n -= 1
          if (n == 0) return true
        }
      }
      i += 1
    }
    false
  }
}
