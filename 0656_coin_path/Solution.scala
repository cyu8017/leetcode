// LeetCode 0656 - Coin Path
// https://leetcode.com/problems/coin-path/

import scala.collection.mutable

object Solution {
  def cheapestJump(coins: Array[Int], maxJump: Int): List[Int] = {
    val n = coins.length
    if (coins(n - 1) == -1) return List.empty
    val inf = Long.MaxValue / 4
    val cost = Array.fill(n)(inf)
    val nxt = Array.fill(n)(-1)
    cost(n - 1) = coins(n - 1)
    var i = n - 2
    while (i >= 0) {
      if (coins(i) != -1) {
        var jump = 1
        while (jump <= maxJump) {
          val j = i + jump
          if (j >= n) jump = maxJump + 1
          else {
            if (cost(j) != inf) {
              val candidate = coins(i) + cost(j)
              if (candidate < cost(i) || (candidate == cost(i) && (nxt(i) == -1 || j < nxt(i)))) {
                cost(i) = candidate
                nxt(i) = j
              }
            }
            jump += 1
          }
        }
      }
      i -= 1
    }
    if (cost(0) == inf) return List.empty
    val path = mutable.ArrayBuffer(1)
    i = 0
    while (i != n - 1) {
      i = nxt(i)
      path += i + 1
    }
    path.toList
  }
}
