// LeetCode 2293 - Min Max Game
// https://leetcode.com/problems/min-max-game/

object Solution {
  def minMaxGame(nums: Array[Int]): Int = {
    var cur = nums
    while (cur.length > 1) {
      val next = new Array[Int](cur.length / 2)
      var i = 0
      while (i < next.length) {
        if (i % 2 == 0) next(i) = math.min(cur(2 * i), cur(2 * i + 1))
        else next(i) = math.max(cur(2 * i), cur(2 * i + 1))
        i += 1
      }
      cur = next
    }
    cur(0)
  }
}
