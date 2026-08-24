// LeetCode 0868 - Binary Gap
// https://leetcode.com/problems/binary-gap/

object Solution {
  def binaryGap(n: Int): Int = {
    var num = n
    var last = -1
    var ans = 0
    var bit = 0
    while (num != 0) {
      if ((num & 1) == 1) {
        if (last != -1) ans = math.max(ans, bit - last)
        last = bit
      }
      num >>= 1
      bit += 1
    }
    ans
  }
}
