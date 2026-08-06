// LeetCode 1523 - Count Odd Numbers in an Interval Range
// https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

object Solution {
  def countOdds(low: Int, high: Int): Int =
    (high + 1) / 2 - low / 2
}
