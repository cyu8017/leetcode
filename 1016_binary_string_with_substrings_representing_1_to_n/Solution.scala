// LeetCode 1016 - Binary String With Substrings Representing 1 To N
// https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

object Solution {
  def queryString(s: String, n: Int): Boolean = {
    (n to (n / 2 + 1) by -1).forall(i => s.contains(i.toBinaryString))
  }
}
