// LeetCode 0258 - Add Digits
// https://leetcode.com/problems/add-digits/

object Solution {
  def addDigits(num: Int): Int =
    if (num == 0) 0 else 1 + (num - 1) % 9
}
