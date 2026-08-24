// LeetCode 0650 - 2 Keys Keyboard
// https://leetcode.com/problems/2-keys-keyboard/

object Solution {
  def minSteps(n0: Int): Int = {
    var n = n0
    var steps = 0
    var factor = 2
    while (factor * factor <= n) {
      while (n % factor == 0) {
        steps += factor
        n /= factor
      }
      factor += 1
    }
    if (n > 1) steps += n
    steps
  }
}
