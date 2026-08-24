// LeetCode 0970 - Powerful Integers
// https://leetcode.com/problems/powerful-integers/

object Solution {
  def powerfulIntegers(x: Int, y: Int, bound: Int): List[Int] = {
    val ans = scala.collection.mutable.Set.empty[Int]
    var a = 1L
    var stopA = false
    while (a < bound && !stopA) {
      var b = 1L
      var stopB = false
      while (a + b <= bound && !stopB) {
        ans += (a + b).toInt
        if (y == 1) stopB = true
        else b *= y
      }
      if (x == 1) stopA = true
      else a *= x
    }
    ans.toList
  }
}
