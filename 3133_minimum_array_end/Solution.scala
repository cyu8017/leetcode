// LeetCode 3133 - Minimum Array End
// https://leetcode.com/problems/minimum-array-end/

object Solution {
  def minEnd(n0: Int, x: Int): Long = {
    var n = n0 - 1
    var ans = x.toLong
    var i = 0
    while (i < 31) {
      if (((x >> i) & 1) == 0) {
        ans |= (n & 1).toLong << i
        n >>= 1
      }
      i += 1
    }
    ans |= n.toLong << 31
    ans
  }
}
