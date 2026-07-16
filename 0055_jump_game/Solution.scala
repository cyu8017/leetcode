// LeetCode 0055 - Jump Game
// https://leetcode.com/problems/jump-game/

object Solution {
  def canJump(nums: Array[Int]): Boolean = {
    var farthest = 0

    nums.indices.foreach { i =>
      if (i > farthest) {
        return false
      }
      farthest = math.max(farthest, i + nums(i))
    }

    true
  }
}
