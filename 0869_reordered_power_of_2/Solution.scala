// LeetCode 0869 - Reordered Power of 2
// https://leetcode.com/problems/reordered-power-of-2/

object Solution {
  def reorderedPowerOf2(n: Int): Boolean = {
    def sig(x: Int): String = x.toString.sorted
    val target = sig(n)
    (0 until 31).exists(i => sig(1 << i) == target)
  }
}
