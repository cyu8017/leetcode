// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

object Solution {
  def minimumSwap(s1: String, s2: String): Int = {
    var xy = 0
    var yx = 0
    for (i <- s1.indices) {
      if (s1(i) == 'x' && s2(i) == 'y') xy += 1
      else if (s1(i) == 'y' && s2(i) == 'x') yx += 1
    }
    if ((xy + yx) % 2 != 0) -1 else xy / 2 + yx / 2 + 2 * (xy % 2)
  }
}
