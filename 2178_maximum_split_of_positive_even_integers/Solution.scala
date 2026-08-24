// LeetCode 2178 - Maximum Split of Positive Even Integers
// https://leetcode.com/problems/maximum-split-of-positive-even-integers/

object Solution {
  def maximumEvenSplit(finalSum: Long): List[Long] = {
    if (finalSum % 2 != 0) return List.empty
    val ans = scala.collection.mutable.ArrayBuffer.empty[Long]
    var remain = finalSum
    var x = 2L
    while (x <= remain) {
      ans += x
      remain -= x
      x += 2
    }
    ans(ans.length - 1) = ans(ans.length - 1) + remain
    ans.toList
  }
}
