// LeetCode 2683 - Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

object Solution {
  def doesValidArrayExist(derived: Array[Int]): Boolean = {
    var x = 0
    var i = 0
    while (i < derived.length) {
      x ^= derived(i)
      i += 1
    }
    x == 0
  }
}
