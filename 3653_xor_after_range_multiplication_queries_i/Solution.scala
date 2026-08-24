// LeetCode 3653 - XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

object Solution {
  def xorAfterQueries(nums: Array[Int], queries: Array[Array[Int]]): Int = {
    val mod = 1000000007
    for (q <- queries) {
      val l = q(0)
      val r = q(1)
      val k = q(2)
      val v = q(3)
      var idx = l
      while (idx <= r) {
        nums(idx) = ((1L * nums(idx) * v) % mod).toInt
        idx += k
      }
    }
    var ans = 0
    for (x <- nums) ans ^= x
    ans
  }
}
