// LeetCode 3996 - Even Number of Knight Moves
// https://leetcode.com/problems/even-number-of-knight-moves/

object Solution {
  def canReach(start: Array[Int], target: Array[Int]): Boolean =
    ((start(0) + start(1)) % 2) == ((target(0) + target(1)) % 2)
}
