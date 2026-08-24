// LeetCode 0634 - Find the Derangement of An Array
// https://leetcode.com/problems/find-the-derangement-of-an-array/

object Solution {
  def findDerangement(n: Int): Int = {
    val mod = 1000000007
    if (n == 1) return 0
    var prev2 = 0L
    var prev1 = 1L
    var size = 3
    while (size <= n) {
      val next = (size - 1) * (prev1 + prev2) % mod
      prev2 = prev1
      prev1 = next
      size += 1
    }
    prev1.toInt
  }
}
