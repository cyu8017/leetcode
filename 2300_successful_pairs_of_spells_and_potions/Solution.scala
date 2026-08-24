// LeetCode 2300 - Successful Pairs of Spells and Potions
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

object Solution {
  def successfulPairs(spells: Array[Int], potions: Array[Int], success: Long): Array[Int] = {
    java.util.Arrays.sort(potions)
    val m = potions.length
    val ans = new Array[Int](spells.length)
    var i = 0
    while (i < spells.length) {
      var lo = 0
      var hi = m
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (spells(i).toLong * potions(mid) >= success) hi = mid
        else lo = mid + 1
      }
      ans(i) = m - lo
      i += 1
    }
    ans
  }
}
