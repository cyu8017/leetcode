// LeetCode 2648 - Generate Fibonacci Sequence
// https://leetcode.com/problems/generate-fibonacci-sequence/

object Solution {
  def fibGenerator(): () => Int = {
    val ab = Array(0, 1)
    () => {
      val v = ab(0)
      val na = ab(1)
      ab(1) = ab(0) + ab(1)
      ab(0) = na
      v
    }
  }
}
