// LeetCode 1646 - Get Maximum in Generated Array
// https://leetcode.com/problems/get-maximum-in-generated-array/

object Solution {
  def getMaximumGenerated(n: Int): Int = {
    if (n < 2) return n
    val a = Array.fill(n + 1)(0)
    a(1) = 1
    for (i <- 2 to n) {
      a(i) = if (i % 2 == 0) a(i / 2) else a(i / 2) + a(i / 2 + 1)
    }
    a.max
  }
}
