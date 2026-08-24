// LeetCode 0810 - Chalkboard XOR Game
// https://leetcode.com/problems/chalkboard-xor-game/

object Solution {
  def xorGame(nums: Array[Int]): Boolean = {
    var x = 0
    nums.foreach(num => x ^= num)
    x == 0 || nums.length % 2 == 0
  }
}
