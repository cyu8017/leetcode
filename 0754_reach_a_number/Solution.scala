// LeetCode 0754 - Reach a Number
// https://leetcode.com/problems/reach-a-number/

object Solution {
  def reachNumber(target0: Int): Int = {
    val target = math.abs(target0)
    var steps = 0
    var total = 0
    while (total < target || (total - target) % 2 != 0) {
      steps += 1
      total += steps
    }
    steps
  }
}
