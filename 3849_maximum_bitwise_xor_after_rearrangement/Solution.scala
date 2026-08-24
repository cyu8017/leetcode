// LeetCode 3849 - Maximum Bitwise Xor After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

object Solution {
  def maximumXor(s: String, t: String): String = {
    val cnt = new Array[Int](2)
    t.foreach { c => cnt(c - '0') += 1 }
    val ans = new Array[Char](s.length)
    var i = 0
    while (i < s.length) {
      val x = s.charAt(i) - '0'
      if (cnt(x ^ 1) > 0) {
        cnt(x ^ 1) -= 1
        ans(i) = '1'
      } else {
        cnt(x) -= 1
        ans(i) = '0'
      }
      i += 1
    }
    new String(ans)
  }
}
