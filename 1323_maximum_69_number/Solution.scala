// LeetCode 1323 - Maximum 69 Number
// https://leetcode.com/problems/maximum-69-number/

object Solution {
  def maximum69Number(num: Int): Int =
    num.toString.replaceFirst("6", "9").toInt
}
