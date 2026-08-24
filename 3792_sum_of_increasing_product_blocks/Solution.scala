// LeetCode 3792 - Sum Of Increasing Product Blocks
// https://leetcode.com/problems/sum-of-increasing-product-blocks/

object Solution {
  def sumOfBlocks(n: Int): Int = {
    val MOD = 1000000007
    var ans = 0
    var k = 1
    var i = 1
    while (i <= n) {
      var x = 1
      var j = k
      while (j < k + i) {
        x = ((x.toLong * j) % MOD).toInt
        j += 1
      }
      ans = (ans + x) % MOD
      k += i
      i += 1
    }
    ans
  }
}
