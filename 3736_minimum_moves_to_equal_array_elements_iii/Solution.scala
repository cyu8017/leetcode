// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

object Solution {
  def minMoves(nums: Array[Int]): Int = {
    var mx = 0
    var s = 0
    nums.foreach { x =>
      mx = math.max(mx, x)
      s += x
    }
    mx * nums.length - s
  }
}
