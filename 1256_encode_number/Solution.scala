// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

object Solution {
  def encode(num: Int): String = {
    val s = Integer.toBinaryString(num + 1)
    if (s.length <= 1) "" else s.substring(1)
  }
}
