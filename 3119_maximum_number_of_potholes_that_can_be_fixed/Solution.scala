// LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
// https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/

object Solution {
  def maxPotholes(road0: String, budget0: Int): Int = {
    val road = road0 + "."
    val n = road.length
    val cnt = new Array[Int](n)
    var k = 0
    var ans = 0
    var i = 0
    while (i < n) {
      val c = road.charAt(i)
      if (c == 'x') k += 1
      else if (k > 0) {
        cnt(k) += 1
        k = 0
      }
      i += 1
    }
    var budget = budget0
    k = n - 1
    while (k > 0 && budget > 0) {
      val t = math.min(budget / (k + 1), cnt(k))
      ans += t * k
      budget -= t * (k + 1)
      cnt(k - 1) += cnt(k) - t
      k -= 1
    }
    ans
  }
}
