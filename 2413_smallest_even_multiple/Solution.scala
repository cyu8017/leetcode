// LeetCode 2413 - Smallest Even Multiple
// https://leetcode.com/problems/smallest-even-multiple/

object Solution {
  def smallestEvenMultiple(n: Int): Int = if (n % 2 == 0) n else n * 2
}
