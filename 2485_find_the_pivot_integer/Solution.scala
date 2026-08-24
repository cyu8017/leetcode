// LeetCode 2485 - Find the Pivot Integer
// https://leetcode.com/problems/find-the-pivot-integer/

object Solution {
  def pivotInteger(n: Int): Int = {
    val total = n * (n + 1) / 2
    var sum = 0
    var x = 1
    while (x <= n) {
      sum += x
      if (sum == total - sum + x) return x
      x += 1
    }
    -1
  }
}
