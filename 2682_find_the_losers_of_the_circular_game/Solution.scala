// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

object Solution {
  def circularGameLosers(n: Int, k: Int): Array[Int] = {
    val seen = new Array[Boolean](n + 1)
    var cur = 1
    var step = 1
    while (!seen(cur)) {
      seen(cur) = true
      cur = (cur - 1 + step * k) % n + 1
      step += 1
    }
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 1
    while (i <= n) {
      if (!seen(i)) ans += i
      i += 1
    }
    ans.toArray
  }
}
