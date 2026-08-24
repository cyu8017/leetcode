// LeetCode 0932 - Beautiful Array
// https://leetcode.com/problems/beautiful-array/

object Solution {
  def beautifulArray(n: Int): Array[Int] = {
    if (n == 1) return Array(1)
    val left = beautifulArray((n + 1) / 2)
    val right = beautifulArray(n / 2)
    val ans = Array.ofDim[Int](n)
    var k = 0
    left.foreach { x => ans(k) = 2 * x - 1; k += 1 }
    right.foreach { x => ans(k) = 2 * x; k += 1 }
    ans
  }
}
