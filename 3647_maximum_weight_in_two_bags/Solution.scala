// LeetCode 3647 - Maximum Weight in Two Bags
// https://leetcode.com/problems/maximum-weight-in-two-bags/

object Solution {
  def maxWeight(weights: Array[Int], w1: Int, w2: Int): Int = {
    val f = Array.ofDim[Int](w1 + 1, w2 + 1)
    for (x <- weights) {
      var j = w1
      while (j >= 0) {
        var k = w2
        while (k >= 0) {
          if (x <= j) f(j)(k) = math.max(f(j)(k), f(j - x)(k) + x)
          if (x <= k) f(j)(k) = math.max(f(j)(k), f(j)(k - x) + x)
          k -= 1
        }
        j -= 1
      }
    }
    f(w1)(w2)
  }
}
