// LeetCode 0476 - Number Complement
// https://leetcode.com/problems/number-complement/

object Solution {
  def findComplement(num: Int): Int = {
    var mask = num
    mask |= mask >>> 1
    mask |= mask >>> 2
    mask |= mask >>> 4
    mask |= mask >>> 8
    mask |= mask >>> 16
    num ^ mask
  }
}
