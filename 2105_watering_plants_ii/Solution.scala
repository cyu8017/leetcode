// LeetCode 2105 - Watering Plants II
// https://leetcode.com/problems/watering-plants-ii/

object Solution {
  def minimumRefill(plants: Array[Int], capacityA: Int, capacityB: Int): Int = {
    var i = 0
    var j = plants.length - 1
    var a = capacityA
    var b = capacityB
    var ans = 0
    while (i < j) {
      if (a < plants(i)) { ans += 1; a = capacityA }
      a -= plants(i)
      i += 1
      if (b < plants(j)) { ans += 1; b = capacityB }
      b -= plants(j)
      j -= 1
    }
    if (i == j) {
      if (a >= b) { if (a < plants(i)) ans += 1 }
      else if (b < plants(i)) ans += 1
    }
    ans
  }
}
