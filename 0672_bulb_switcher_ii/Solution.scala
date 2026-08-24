// LeetCode 0672 - Bulb Switcher II
// https://leetcode.com/problems/bulb-switcher-ii/

object Solution {
  def flipLights(n0: Int, presses: Int): Int = {
    val n = math.min(n0, 3)
    if (presses == 0) return 1
    val onePress = Array(2, 3, 4)
    val twoPress = Array(2, 4, 7)
    val manyPress = Array(2, 4, 8)
    if (presses == 1) return onePress(n - 1)
    if (presses == 2) return twoPress(n - 1)
    manyPress(n - 1)
  }
}
