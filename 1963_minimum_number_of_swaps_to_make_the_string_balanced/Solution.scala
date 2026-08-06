// LeetCode 1963 - Minimum Number of Swaps to Make the String Balanced
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

object Solution {
  def minSwaps(s: String): Int = {
    var bal = 0
    var mx = 0
    for (ch <- s) {
      if (ch == '[') bal += 1
      else bal -= 1
      mx = math.min(mx, bal)
    }
    (-mx + 1) / 2
  }
}
