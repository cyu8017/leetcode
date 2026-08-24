// LeetCode 2481 - Minimum Cuts to Divide a Circle
// https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

object Solution {
  def numberOfCuts(n: Int): Int = {
    if (n == 1) 0
    else if (n % 2 == 0) n / 2
    else n
  }
}
