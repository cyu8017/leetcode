// LeetCode 2802 - Find The K-th Lucky Number
// https://leetcode.com/problems/find-the-k-th-lucky-number/

object Solution {
  def kthLuckyNumber(k0: Int): String = {
    var k = k0 + 1
    var bits = ""
    while (k > 1) {
      if (k % 2 == 0) bits = "4" + bits
      else bits = "7" + bits
      k /= 2
    }
    bits
  }
}
