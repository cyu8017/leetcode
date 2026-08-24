// LeetCode 2498 - Frog Jump II
// https://leetcode.com/problems/frog-jump-ii/

object Solution {
  def maxJump(stones: Array[Int]): Int = {
    var ans = stones(1) - stones(0)
    var i = 2
    while (i < stones.length) {
      val diff = stones(i) - stones(i - 2)
      if (diff > ans) ans = diff
      i += 1
    }
    ans
  }
}
